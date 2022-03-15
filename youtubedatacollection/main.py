from curses import meta
from flask import Flask, render_template, request, send_from_directory
from flask import Markup
import os
from youtube_easy_api.easy_wrapper import *
from flask import Flask,render_template,request,redirect
from urllib.parse import urlparse
from pytube import extract

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
        url_data = urlparse(f"{names}")
        wa = (url_data.query[2::])
        return redirect(f"/users/{wa}")

#Defining repo function for returning data
@app.route('/users/<wa>')
def users(wa):

    easy_wrapper = YoutubeEasyWrapper()
    easy_wrapper.initialize(api_key="j")
    metadata = easy_wrapper.get_metadata(video_id=wa)
    print(metadata['statistics'])
    b =(metadata['title']) 
    a = (metadata['statistics']['commentCount'])
    f = (metadata['description'])
    c = (metadata['statistics']['likeCount'])
    v = (metadata['statistics']['viewCount'])
    return render_template("return.html", likes = Markup(f'<b>Title Of Video: </b>{b}<br><b>Description: </b>{f}<br><b>Amount of likes: </b>{c}<br><b>Amount of comments: </b>{a}<br><b>Amount of views: </b>{v}<br><br><iframe src="https://www.youtube.com/embed/{wa}" width="853" height="480" frameborder="0" allowfullscreen></iframe>')
)

#Running Flask
if __name__ == "__main__":
    app.run(debug=True)