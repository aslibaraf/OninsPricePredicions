from flask import Flask,request,jsonify
import util
app=Flask(__name__)
@app.route("/hello")



def hello():
        return "Yes. Your conection is done for Farmer Project"

@app.route('/markletlist', methods=['GET'])
def markletlist():
    response = jsonify({
        'locations': util.markletlist()
    })
    response.headers.add('Access-Control-Allow-Origin', '*')

    return response
if __name__=="__main__":

    print("Wait. Starting the flask server for Farmer Modal Price predition")
    app.run()