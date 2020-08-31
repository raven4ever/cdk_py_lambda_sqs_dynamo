from pprint import pprint
import boto3


def put_movie(title, year, plot, rating, table_name):
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)

    response = table.put_item(
        Item={
            'year': year,
            'title': title,
            'info': {
                'plot': plot,
                'rating': rating
            }
        }
    )
    return response


def handler(event, context):
    table_name = event['table']
    movie_name = event['movie_name']
    movie_year = event['movie_year']
    movie_plot = event['movie_plot']
    movie_rating = event['movie_rating']

    movie_resp = put_movie(movie_name, movie_year, movie_plot, movie_rating, table_name)

    print("Put movie succeeded:")
    pprint(movie_resp, sort_dicts=False)
