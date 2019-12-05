import smopy
import io

import matplotlib.pyplot as plt
plt.switch_backend('Agg')


from shapely.geometry import Point, Polygon
from flask import send_file, make_response

overview_fn = "html/maps/map_{:02d}_overview.png"
local_fn =    "html/maps/map_{:02d}_zoom.png"

localMapRadius=0.005


def getMap(y1, x1, y2, x2):
    map = smopy.Map((y1, x1, y2, x2), tileserver="http://tile.basemaps.cartocdn.com/rastertiles/voyager/{z}/{x}/{y}@2x.png", tilesize=512, maxtiles=16)
    return map

def getOverviewMapResponse(x,y, x1, y1, x2, y2):
    p = Point(x,y)
    return getMapResponse(p, x1, y1, x2, y2)

def getLocalMapResponse(x,y):
    p = Point(x,y)

    x1 = p.x - localMapRadius
    y1 = p.y - localMapRadius/2
    x2 = p.x + localMapRadius
    y2 = p.y + localMapRadius/2

    return getMapResponse(p, x1, y1, x2, y2)

def getMapResponse(p, x1, y1, x2, y2):
    map = getMap(y1, x1, y2, x2)

    #Plot
    ax = map.show_mpl(figsize=(5,5), dpi=300)
    x, y = map.to_pixels(p.y, p.x)
    ax.plot(x, y, 'or', ms=5, mew=1, alpha=0.35)

    f = ax.figure

    buf = io.BytesIO()
    plt.savefig(buf, format='png')
    plt.close(f)
    plt.close()
    response = make_response(buf.getvalue())
    response.content_type='image/png'
    return response
    
