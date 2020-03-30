from flask import Flask, json, Response
from adam_joke_scraper import scrape
app = Flask(__name__)

@app.route('/', methods=['GET'])
def home_get():
    joke = scrape()
    return json.jsonify({'joke': joke})


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)