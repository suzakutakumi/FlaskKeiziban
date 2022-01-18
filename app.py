from flask import *
import json

app=Flask(__name__)

chats=[]

@app.route("/chat", methods=['GET'])
def SendChats():
    response = jsonify(chats)
    response.status_code = 200
    return response

@app.route("/chat", methods=['POST'])
def ReciveChat():
    req=request.get_data()
    print(req)
    jsonData=json.loads(req)
    chats.append(jsonData)
    return Response(status=200)

if __name__=="__main__":
    app.run()