import os

from flask import Flask, request, jsonify,render_template, redirect
from werkzeug.utils import secure_filename
# from pdf2image import convert_from_path
import fitz
import google.generativeai as genai
from PIL import Image
import ast
import json
import sqlite3
import nltk

conn = sqlite3.connect("sqlite.db", check_same_thread=False)
conn.execute('CREATE TABLE IF NOT EXISTS users (name TEXT, email TEXT, password TEXT)') 
conn.execute('CREATE TABLE IF NOT EXISTS resume (id TEXT,name TEXT,email TEXT,phone TEXT,skills TEXT)') 


gemini_api_key = API_KEY;
genai.configure(api_key = gemini_api_key)

model = genai.GenerativeModel('gemini-pro-vision')

modeltext = genai.GenerativeModel('gemini-pro')

user = ()


app = Flask(__name__,static_url_path='/static')

@app.route("/home")
def home():
    return render_template("home.html")


@app.route("/")
def reLogin():
    return render_template("login.html")

@app.route("/register")
def reRegister():
    return render_template("register.html")

@app.route("/login",methods=["POST"])
def login():
    data = request.form
    email = data['email']
    password = data['password']
    with sqlite3.connect("sqlite.db") as users:
        data = users.cursor().execute("select * from users where email=? and password=?",(email,password))
        d = (data.fetchall())
        if(len(d)>0):
            global user
            user = d[0]
            return redirect('/home')
        else:
            return redirect("/")


@app.route("/register",methods=["POST"])
def register():
    data = (request.form)
    name = data['name']
    email = data['email']
    password = data['password']
    q = 'insert into users (name,email,password) values(?,?,?)'
    with sqlite3.connect("sqlite.db") as users: 
        cursor = users.cursor() 
        cursor.execute(q,(name,email,password))
        users.commit()
    return redirect("/")

@app.route("/profile")
def profile():
    print(user)
    return render_template("profile.html", user = user)

@app.route("/filter",methods=["GET"])
def filter():
    resumes = conn.execute("select * from resume;").fetchall()
    print(resumes)

    return render_template("filter.html",items=resumes)


@app.route("/filter",methods=["POST"])
def filtered():
    resumes = conn.execute("select * from resume;").fetchall()
    inp = request.form["job"]
    response = modeltext.generate_content([f"you are a hr for my company .. from this list select only eligible candidated for {inp} job role. list = {resumes} .. return only selected candidates in the same format array .. produce proper array format .. return [] if no one matches"])
    items = ast.literal_eval(response.text)

    return render_template("filter.html",items=items)


@app.route("/upload")
def upload():
    resumes = conn.execute("select * from resume;").fetchall()
    print(resumes)

    return render_template("upload.html",items=resumes)

def jsontoobj(text):
    text = (text[8:])
    text = (text[:-4])
    jsons = json.loads(text)
    print(jsons)
    return jsons




@app.route("/uploadresume",methods=["POST"])
def uploadresume():
    file = (request.files['resumes'])
    filename = secure_filename(file.filename) 
    file.save(filename)
    pdffile = "./"+filename
    doc = fitz.open(pdffile)
    page = doc.load_page(0)  # number of page
    pix = page.get_pixmap()
    output = "outfile.png"
    pix.save(output)
    doc.close()

    image = Image.open("./outfile.png")
    response = model.generate_content(["This is the image of a resume .. fetch the name as name, email as email, phone number as phone,skills as skills to json", image])

    obj = jsontoobj(response.text)

    name = obj['name']
    email=obj['email']
    phone = obj['phone']
    skills = obj['skills']

    query = f'insert into resume (name,email,phone,skills) values("{name}","{email}","{phone}","{skills}");'
    print(query)
    id = conn.cursor().execute(query)
    conn.commit()
    print(id)
    return redirect("/upload")


@app.route("/getjobs")
def getjobs():
    users = conn.execute("select * from resume;").fetchall()
    print(users)

    return "Hi"
