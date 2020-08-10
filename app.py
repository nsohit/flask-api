from flask import Flask, request
from flask_restful import Resource, Api
from flask_cors import CORS

#inisiai object flask
app = Flask(__name__)

#inisiasi object flask_restful
api = Api(app)

#inisiasi object flask_cors
CORS(app)

#membuat class Resource
identitas = {}

class MebuatResource(Resource):
	# metode get dan post
	def get(self):
		
		return identitas
	def post(self):
		nama = request.form["nama"]
		umur = request.form["umur"]
		identitas["nama"] = nama
		identitas["umur"] = umur
		response = {"msg" : "data berhasil dimasukan"}
		return response

#setup resourcenya
api.add_resource(MebuatResource,"/api", methods=["GET", "POST"])

if __name__ == "__main__":
	app.run(debug=True, port=5005)
