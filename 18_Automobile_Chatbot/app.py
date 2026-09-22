
import os
from flask import Flask,render_template,request,session,jsonify
from dotenv import load_dotenv
from config import *
load_dotenv()
app=Flask(__name__);app.secret_key='change-me'
@app.get('/')
def home():
    return render_template('index.html',title=TITLE,welcome=WELCOME,bg=BG,primary=PRIMARY)
@app.post('/chat')
def chat():
    msg=request.json.get('message','')
    if DOMAIN.lower() not in msg.lower() and len(msg.split())>2:
        return jsonify(reply=f"Sorry, I only answer {DOMAIN} questions.")
    return jsonify(reply=f"Demo reply for {DOMAIN}: {msg}")
@app.post('/clear')
def clear():
    session.clear();return jsonify(ok=True)
if __name__=='__main__':
    app.run(host='0.0.0.0',port=int(os.getenv('PORT',5000)))
