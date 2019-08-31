import os
from flask import Flask, request, redirect, url_for,jsonify
from werkzeug.utils import secure_filename
import requests
import json


def BotPath(desc):
   addedbook = Book(title=desc)
#    session.add(addedbook)
#    session.commit()
   return addedbook



app = Flask(__name__)
@app.route("/")
@app.route("/botApi", methods = ['GET', 'POST'])
def bootFunction():
   if request.method == 'GET':
       return get_books()
   elif request.method == 'POST':
      print("received data....................")
      print(request, type(request), dir(request))
      input_json = request.get_json()
      
      print(input_json)
    #   input_json = "return data"
      print(type(input_json))
      print(input_json.values)
      print(input_json.keys)
      for item in input_json.items():
       #    print(type(item), item[0], item[1])
          ticketId =  item[0]
          description =  item[1]
          print(ticketId, description)
      for k in input_json.keys():
          print(k)
          print(input_json.get(k))
    #   json1_data = json.loads(input_json)
    #   print(json1_data)
      return json.dumps(input_json)

    #    ticketId = request.args.get('ticketId', '')
    #    desc = request.args.get('desc', '')
       
    #    return BotPath(desc,ticketId)
	   
@app.route('/home',methods=['GET'])#route() decorator to tell flask what url should trigger our application
def test123():
    #return '''<html><h2>OK</h2></html>'''
    return jsonify({'msg':'Welcome to training'});	   
	   
if __name__=='__main__':
	app.run(host='127.0.0.1',port=8099, threaded=True)  #10.76.132.251