from .abstract import ContinuousLimitGenerator
from shapely.geometry import Point, Polygon

import geopandas as gpd
gpd.io.file.fiona.drvsupport.supported_drivers['KML'] = 'rw'


class CoordinateLimitGenerator(ContinuousLimitGenerator[Point]):
    def __init__(self, kml_filepath: str, seed:int):
        polys = gpd.read_file(kml_filepath, driver='KML')
        self.polygon = polys.loc[0, 'geometry']
        ContinuousLimitGenerator.__init__(self,seed)

    def generateRandomOne(self):
        x1, y1, x2, y2 = self.polygon.bounds
        while True:
            p = Point(round(self.rand.uniform(x1, x2), 5), round(self.rand.uniform(y1,y2),5))
            if(p.within(self.polygon)):
                return {p.x, p.y}
        