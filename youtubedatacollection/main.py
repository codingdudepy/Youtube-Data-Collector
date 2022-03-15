from curses import meta
from flask import Flask, render_template, request, send_from_directory
from flask import Markup
import os
from youtube_easy_api.easy_wrapper import *
from flask import Flask,render_template,request,redirect

app = Flask(__name__)
#Defining favicon (Still in development of fixing server issues with heroku displaying corrrect info)
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static', 'images'),
                               'wa.ico', mimetype='image/png') 

#Defining home page(form.html)
@app.route('/')
def form():
    return render_template('index.html')

@app.route('/return', methods = ['POST', 'GET'])
def repo():
    if request.method == 'POST':
        names = request.form['name']
        return redirect(f"/users/{names}")

#Defining repo function for returning data
@app.route('/users/<names>')
def users(names):

    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key="xxxxxxxx")
    metadata = easy_wrapper.get_metadata(video_id=names)
    print(metadata['statistics'])
    b =(metadata['title']) 
    a = (metadata['statistics']['commentCount'])
    f = (metadata['description'])
    c = (metadata['statistics']['likeCount'])
    v = (metadata['statistics']['viewCount'])
    return render_template("return.html", likes = Markup(f'<b>Title Of Video: </b>{b}<br><b>Description: </b>{f}<br><b>Amount of likes: </b>{c}<br><b>Amount of comments: </b>{a}<br><b>Amount of views: </b>{v}')
)

#Running Flask
if __name__ == "__main__":
    app.run(debug=True)