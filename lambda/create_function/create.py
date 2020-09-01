from pprint import pprint
import boto3
import json
from utils.movie import Movie


def put_movie(movie: Movie):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table('movies_table')

    response = table.put_item(Item=movie.__dict__)
    return response


def print_result(response):
    print("Put result:")
    pprint(response, sort_dicts=False)


def handler(event, context):
    initMode = event['initMode']

    if initMode:
        with open('initial.json') as json_file:
            movie_json = json.load(json_file)

        for item in movie_json['movies']:
            resp = put_movie(Movie(item))
            print_result(resp)
    else:
        mov = Movie.from_data(event['movie_name'], event['movie_year'], event['movie_plot'], event['movie_rating'])
        movie_resp = put_movie(mov)
        print_result(movie_resp)
