from flask_restful import Resource, reqparse
from trace_route_db import get_result
from trace_route_thread import start_task
from restaurants import get_restaurants_by_location, get_restaurants_by_coordinate


class Root(Resource):
    def get(self):
        return {'status': 'ok'}


class TraceRouteRequest(Resource):
    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('target')
        args = parser.parse_args()
        task_id = start_task(args['target'])
        return {
            'status': 'ok',
            'task_id': task_id
        }


class TraceRouteResult(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('task_id')
        args = parser.parse_args()
        return get_result(args['task_id'])


class RestaurantRequest(Resource):
    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('location')
        parser.add_argument('latitude')
        parser.add_argument('longitude')
        args = parser.parse_args()
        if 'location' in args:
            return get_restaurants_by_location(args['location'])
        if 'latitude' in args and 'longitude' in args:
            return get_restaurants_by_coordinate(args['latitude'], args['longitude'])
        return {}


