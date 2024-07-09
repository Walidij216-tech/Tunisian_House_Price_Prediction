#we have to import the python flask server witch is the back-end of our UI(User Interface) application
from  flask import Flask,request,jsonify # type: ignore
import util 
app=Flask(__name__)
#1er routine for the locations
@app.route('/get_location_names', methods=['GET'])
def get_location_names():
    response = jsonify({
        'locations': util.get_location_names()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response


@app.route('/predict_home_price',methods=['GET','POST'])
def predict_home_price():
    total_m2=float(request.form['total_m2'])
    location = request.form['location']
    bhk=int(request.form['bhk'])
    bath=int(request.form['bath'])

    response = jsonify({
        'estimated_price': util.get_estimated_price(location,total_m2,bhk,bath)
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
    
    

if __name__ == "__main__":
    print("Starting python Flask Server For Home Price Prediction...")
    util.load_saved_artifacts()
    app.run()