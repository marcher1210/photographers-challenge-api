from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    Response
)
from werkzeug import MultiDict
from .generator import *
from .exceptions import *

import sys, inspect

def route(path : str, method : str, args: MultiDict):
    try:
        #Find method from endpoint
        function_name = "%s_%s" % (method, path.replace('/', '_'))
        function = getattr(sys.modules[__name__], function_name, None)
        
        if not function:
            raise MethodNotFound(path, method)
        
        #Validate and fill parameters
        params = {}
        for p in inspect.signature(function).parameters.values():
            if not p.name in args:
                if p.default==inspect.Parameter.empty:
                    #Required parameter
                    raise MissingParameter(p.name, p.annotation)
                else:
                    #Optional parameter
                    continue
            strvalue = args[p.name]

            #try instatiating / casting the value
            try:
                if p.annotation in [date, time]:
                    value = p.annotation.fromisoformat(strvalue)
                else:
                    value = p.annotation(strvalue)
            except (TypeError, ValueError):
                raise ParameterCasting(p.name, p.annotation, strvalue)

            params[p.name] = value
        result = function(**params)
        return jsonify(result)
    except PhotoChallengeException as e:
        resp = jsonify({"error": {
            "message": e.error_message()
        }})
        return resp, e.status_code()