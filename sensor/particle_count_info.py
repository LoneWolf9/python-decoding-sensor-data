from house_info import HouseInfo
from datetime import date


class ParticleData(HouseInfo):

    def _convert_data(self, data):
        recs = []
        for rec in data:
            recs.append(float(rec))
        return recs

    def get_data_by_area(self, rec_area=0):
        recs = super().get_data_by_area("particulate", rec_area)
        return self._convert_data(recs)

    def get_data_by_date(self, rec_date=date.today()):
        recs = super().get_data_by_date("particulate", rec_date)
        return self._convert_data(recs)

    def get_data_concentrations(self, data):
        particulate = {
            "good": 0,
            "moderate": 0,
            "bad": 0
        }

        for rec in data:
            if particulate <= 50.0:
                particulate{"good"}
            elif particulate == 50.0 & particulate <= 100.0:
                particulate{"moderate"}
            elif particulate > 100.0:
                particulate["bad"]

        return particulate
