from flask import Flask, render_template
from flask_restful import Api
from flask_cors import CORS

import resources

app = Flask(__name__, static_url_path='/static')
CORS(app)
api = Api(app)


@app.route('/')
def show_index():
    return render_template("index.html")


@app.route('/traceroute')
def show_traceroute():
    return render_template("traceroute-graph.html")


@app.route('/restaurants')
def show_restaurants():
    return render_template("restaurants.html")


api.add_resource(resources.TraceRouteRequest, '/api/traceroute/request')
api.add_resource(resources.TraceRouteResult, '/api/traceroute/result')
api.add_resource(resources.RestaurantRequest, '/restaurants/request')
# api.add_resource(resources.TraceRouteResult, '/restaurants/result')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
