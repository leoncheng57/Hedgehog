from flask import Flask
import os.path

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Index</h1>'

if __name__ == '__main__':
    app.debug = True
    app.secret_key = '895uvq_09ta834_xna_2847vt3v9o3u8tw948t5e'
    app.run('0.0.0.0',
        8080 if os.path.isfile('./cloudy') else 8000)
