from flask import Flask, request, jsonify
from utils import aaaa
from flask_restx import Resource, Namespace, Api



app = Flask(__name__)
n_s = Namespace("perform_query")
api = Api(app)
api.add_namespace(n_s)


@n_s.route("/")
class PerformQuery(Resource):
    def post(self):
        p = request.json
        r = request.args.get("flav")
        return jsonify(p)



if __name__ == '__main__':
    app.run()


