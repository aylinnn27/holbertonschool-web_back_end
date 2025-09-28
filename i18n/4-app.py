from flask import Flask, render_template, request
from flask_babel import Babel, _

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']

babel = Babel(app)

@babel.localeselector
def get_locale():
    # Check if the URL contains ?locale=...
    locale = request.args.get('locale')
    if locale in app.config['BABEL_SUPPORTED_LOCALES']:
        return locale
    # fallback to default
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

@app.route('/')
def index():
    return render_template('4-index.html')

if __name__ == '__main__':
    app.run(debug=True)
