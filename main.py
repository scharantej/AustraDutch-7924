
from flask import Flask, render_template, request

# Flashcard data (replace with your own or connect to a database)
flashcards = {
    "Fair dinkum": "Echt waar",
    "She'll be right, mate": "Het komt wel goed, maat",
    "No worries": "Geen probleem",
    "Chuck a shrimp on the barbie": "Gooi een garnaal op de barbecue",
    "G'day": "Hallo"
}

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    saying = request.form['saying']
    translation = flashcards.get(saying, "Translation not found")
    return render_template('index.html', saying=saying, translation=translation)

if __name__ == '__main__':
    app.run()
