from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    redirect
)
from werkzeug import MultiDict
from .generator import *
from .exceptions import *

import sys, inspect
from random import randrange

def redirect_with_seed():
    seed = randrange(sys.maxsize)
    url = request.url
    if "localhost" not in url and "127.0.0.1" not in url:
        url = url.replace('http://', 'https://', 1)
    return redirect(url+"&seed="+str(seed))

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
                    if(method == "GET" and p.name=="seed"):
                        return redirect_with_seed()
                    raise MissingParameter(p.name, p.annotation)
                else:
                    #Optional parameter
                    continue
            strvalue = args[p.name]

            #try instatiating / casting the value
            try:
                if p.annotation in [list,dict]:
                    if type(args[p.name]) in [list,dict]:
                        value = args[p.name]
                    else:
                        value = args.getlist(p.name)
                elif p.annotation in [date, time]:
                    value = p.annotation.fromisoformat(strvalue)
                else:
                    value = p.annotation(strvalue)
            except (TypeError, ValueError):
                raise ParameterCasting(p.name, p.annotation, strvalue)

            params[p.name] = value
        result = function(**params)
        try:
            return jsonify(result)
        except (TypeError):
            return result
    except PhotoChallengeException as e:
        resp = jsonify({"error": {
            "message": e.error_message()
        }})
        return resp, e.status_code()