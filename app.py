from logging import error
from flask import Flask, request
from flask_restful import Resource, Api, reqparse
import json

app = Flask(__name__)
api = Api(app)

null = None


class Home(Resource):
    def get(self):
        home = open("home.json", "r")
        jsonHome = json.load(home)
        return {"home": jsonHome}


class about(Resource):
    def get(self):
        about = open("about.json", "r")
        data = json.load(about)
        return data


class contact(Resource):
    def get(self):
        contact = open("contact.json", "r")
        data = json.load(contact)
        return data


class singlepodcast(Resource):
    def get(self):
        singlepodcast = open("single-podcast.json", "r")
        data = json.load(singlepodcast)
        return data


api.add_resource(Home, '/home/')
api.add_resource(about, '/about/')
api.add_resource(contact, '/contact/')
api.add_resource(singlepodcast, '/singlepodcast/')


@app.errorhandler(404)
def page_not_found(e):
    return {"error": "file not found"}, 404


if __name__ == '__main__':
    app.run(debug=True, port=5005)
