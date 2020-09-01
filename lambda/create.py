from pprint import pprint
import boto3


class Movie:

    def __init__(self, title, year, plot, rating) -> None:
        self.title = title
        self.year = year
        self.info = dict(
            plot=plot,
            rating=rating)


def put_movie(table_name: str, movie: Movie):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.put_item(Item=movie.__dict__)
    return response


def handler(event, context):
    table_name = event['table']

    mov = Movie(event['movie_name'], event['movie_year'], event['movie_plot'], event['movie_rating'])

    movie_resp = put_movie(table_name, mov)

    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)
