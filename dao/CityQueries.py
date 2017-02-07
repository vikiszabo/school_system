from model.City import City


class CityQueries():
    @classmethod
    def getCityByName(cls, name):
        return City.get(city_name=name)