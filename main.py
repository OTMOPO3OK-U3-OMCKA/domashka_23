from flask import Flask, request, jsonify
from data_reader import r_file
from flask_restx import Resource, Namespace, Api
from utils import dict_cmd



app = Flask(__name__)
n_s = Namespace("perform_query")
api = Api(app)
api.add_namespace(n_s)


@n_s.route("/")
class PerformQuery(Resource):
    def post(self):
        req = request.json
        try:
            cmd1 = dict_cmd[req["cmd1"]]
            cmd2 = dict_cmd[req["cmd2"]]
            result1 = cmd1(r_file(req["file_name"]), req["value1"])
            result2 = cmd2(result1, req["value2"])
            return jsonify(result2)
        except KeyError:
            return []



if __name__ == '__main__':
    app.run()


