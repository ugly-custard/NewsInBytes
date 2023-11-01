from flask import Flask, render_template, request, redirect, jsonify
from flask_cors import CORS
import json
from utils.summary import Summarizer


app = Flask(__name__)
app.secret_key="This_secret_key"
POSTS_PER_PAGE=5
    
@app.route("/",methods=['GET','POST'])
def home():
    return redirect("/news_feed/1")

@app.route("/home",methods=['GET','POST'])
def summary():
    return render_template("index.html")

@app.route("/RD",methods=['GET','POST'])
def RD():
    data_in_flask = request.get_json()
    print("Summarizing...")
    summary=s.generate_abstractive_summary(data_in_flask)
    print("Summary: ", summary)
    data={
        'data': f"{summary}"
    }
    return jsonify(data)

@app.route("/news_feed/<int:page_num>", methods=['GET', 'POST'])
def news_feed(page_num):
    with open('summarized_news.json', 'r') as fp:
        posts_data = json.load(fp)
        #page_num = request.args.get('page', 1, type=int)
        
        start_idx = (page_num - 1) * POSTS_PER_PAGE
        end_idx = start_idx + POSTS_PER_PAGE

        news = posts_data[start_idx:end_idx]
        
        if request.method == 'GET':
            return render_template(
                'news_feed.html',
                news=news,
                page_num=page_num,
                POSTS_PER_PAGE=POSTS_PER_PAGE
            )
        elif request.method == 'POST':
            return jsonify(news)


if __name__ == "__main__":
    s = Summarizer()
    app.run(debug=True)
    CORS(app)    
