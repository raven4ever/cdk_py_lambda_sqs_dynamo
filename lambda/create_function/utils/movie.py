class Movie(object):
    def __init__(self, d: dict):
        self.__dict__ = d

    @classmethod
    def from_data(cls, title, year, plot, rating):
        data_as_dict = {
            'title': title,
            'year': year,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
        return cls(data_as_dict)
