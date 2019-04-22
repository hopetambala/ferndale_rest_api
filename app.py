from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Resource, Api


import data_aggregation.main as dat

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})
api = Api(app)


@app.route('/')
def index():
    return "Hello, Ferndale!\nFor purchased: /dataz/purchased/<string:purchased>/\nFor lot# '/dataz/lot/<string:lot>'"

class AllMeterData(Resource):
    #df = data.df #DataFrame not used
    #df_json = data.df_json #JSON not used
    dataz = dat.df_dict
    def get(self):
        return {'dataz' : self.dataz }

class OneMeterData(Resource):
    dataz = dat.df_dict
    data = {}
    #print(records[0]['objectId'])
    #print(records[0])
  
    def get(self,purchased):
        for i in self.dataz:
            if i['purchased'] == str(purchased):
                self.data = i
                #print(self.data)
        return self.data

class SingleAllMeterData(Resource):
    #df = data.df #DataFrame not used
    #df_json = data.df_json #JSON not used
    dataz = dat.df_dict
    def get(self,lot):
        single_lot_data = []
        for i in self.dataz:
            if i['lot'] == str(lot):
                single_lot_data.append(i)
        return {'data': single_lot_data }



api.add_resource(AllMeterData, '/dataz/')
api.add_resource(OneMeterData, '/dataz/purchased/<string:purchased>/')
api.add_resource(SingleAllMeterData, '/dataz/lot/<string:lot>')


if __name__ == '__main__':
    app.run(debug=False)