import requests
from flask import Flask, render_template, request

app = Flask(__name__)

API_KEY = "r7Rd2jdaiOnbwGUPNTKMzGIRjkqtHGz3"
MOST_POPULAR_API_ENDPOINT = f"http://api.nytimes.com/svc/mostpopular/v2/mostviewed/all-sections/7.json?api-key={API_KEY}"

@app.route("/")
def index():
    response = requests.get(MOST_POPULAR_API_ENDPOINT)
    articles = response.json()["results"]
    return render_template("index.html", articles=articles)

@app.route("/article/<int:index>")
def article(index):
    response = requests.get(MOST_POPULAR_API_ENDPOINT)
    articles = response.json()["results"]
    article = articles[index]
    return render_template("article.html", article=article)

if __name__ == "__main__":
    app.run(debug=True, port=50000)



