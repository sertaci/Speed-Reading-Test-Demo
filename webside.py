from flask import Flask, render_template, request
from speechCore import from_mic

app = Flask(__name__, template_folder="template")

@app.route('/')
def home():
    return render_template('speech.html')

@app.route('/start_recognition', methods=['POST'])
def start_recognition():
    readText = str(from_mic().text)

    print(readText)
    return str(len(readText.split(" ")))


if __name__ == '__main__':
    app.run(debug=True)    