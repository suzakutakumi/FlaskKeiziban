# -*- coding: utf-8 -*-

from flask import *
import json

app=Flask(__name__)

chats=[]

# /にGETでリクエストが送られたら、Indexを実行する
@app.route("/")
def Index():
    return render_template('index.html')

# /chatにGETでリクエストが送られたら、SendChatsを実行する
@app.route("/chat", methods=['GET'])
def SendChats():
    # 辞書型のリストchatsをdateを基準にソート
    sorted_chats=sorted(chats,key=lambda x:x['date'])
    # 辞書型をJSONに変換して、送る準備
    response = jsonify(chats)
    # ステータスを200(正常終了)にする
    response.status_code = 200
    return response

# /chatにPOSTでリクエストが送られたら、ReciveChatを実行する
@app.route("/chat", methods=['POST'])
def ReciveChat():
    req=request.get_data()
    print(req)
    jsonData=json.loads(req)
    chats.append(jsonData)
    return Response(status=200)

if __name__=="__main__":
    app.run(debug=True)
