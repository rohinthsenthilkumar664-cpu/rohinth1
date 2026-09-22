import os
from flask import Flask,render_template,request,jsonify,session
from dotenv import load_dotenv
from google import genai
from config import *
load_dotenv()
app=Flask(__name__);app.secret_key=os.getenv("SECRET_KEY","change-me")
client=genai.Client(api_key=os.getenv("GEMINI_API_KEY"))
@app.get("/")
def home():
 return render_template("index.html",cfg={"TITLE":TITLE,"WELCOME":WELCOME_MESSAGE,"BG":BG,"ACCENT":ACCENT})
@app.post("/chat")
def chat():
 m=request.json.get("message","");r=client.models.generate_content(model="gemini-2.5-flash-lite",contents=SYSTEM_PROMPT+"\nUser:"+m);return jsonify(reply=r.text)
@app.post("/clear")
def clear():session.clear();return jsonify(ok=True)
if __name__=="__main__":app.run(host="0.0.0.0",port=int(os.getenv("PORT",PORT)))
