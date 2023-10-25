from flask import Flask, request
from Translator import MarianMT_Translator
import json

app = Flask(__name__)

@app.route('/')
def index():
    return "Translate module. Use /translate/ or /available_languages/ to use the API."

@app.route('/translate/', methods=['POST'])
def translate():
    content_type = request.headers.get('Content-Type')
    if (content_type == 'application/json'):
        data = json.loads(request.data)
        
        Lo = MarianMT_Translator()
        Lo.loadModel(data['src_lan'], data['tar_lan'])
        trad = dict()
        trad["translate"] = Lo.translate(data['text'])
        
        return trad
    else:
        return 'Content-Type not supported!', 400

@app.route('/available_languages/', methods=['GET'])
def availableLanguages():
    lan = ["en", "fr", "ru", "ar", "pl"]
    return lan, 200

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=80)