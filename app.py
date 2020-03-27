import logging
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route('/', methods=['POST'])
def home_post():
    data = request.json()

    resp = None
    if data['type'] == 'REMOVED_FROM_SPACE':
        logging.info('Bot removed from space')
    else:
        resp_dict = format_response(data)
        resp = json.jsonify(resp_dict)

    print(data)
    return resp

def format_response(event):
    
    text = ""

    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        text = "Thanks for adding the OpEx Joke Teller AKA Keiths Competition to the Chat."
    elif event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'DM':
        text = "Lol who adds a bot to DM"
    elif event['type'] == 'MESSAGE':
        text = "OK... Calculating Funniest Joke Ever Created..."
    else:
        text = ""
    return {'text': text}

@app.route('/', methods=['GET'])
def home_get():
    return render_template("home.html")

if __name__ == '__main__':
    app.run(port=8080, debug=True)
