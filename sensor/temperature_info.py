from house_info import HouseInfo


class TemperatureData(HouseInfo):

    def _convert_data(self, data):
        recs = []
        for rec in data:
            rec.int(base=10).append(recs)
        return recs
