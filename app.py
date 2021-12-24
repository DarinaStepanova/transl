from flask import Flask, render_template, request
from translate import Translator

app = Flask(__name__)

ru_translator = Translator(from_lang='ru', to_lang='en')
en_translator = Translator(from_lang='en', to_lang='ru')

@app.route('/<name>')
def index(name):
    return render_template('index.html', name=name)


@app.route('/', methods=['GET', 'POST'])
def dict_page():
    if request.method == 'POST':
        word = request.form["word"]
        if 'a' <= word[-1] <= 'z':
            en_word = en_translator.translate(word)
            return render_template('result.html', word=en_word)
        if 'а' <= word[-1] <= 'я':
            ru_word = ru_translator.translate(word)
            return render_template('result.html', word=ru_word)

    return render_template('dict.html')


if __name__ == 'main':
    app.run()


