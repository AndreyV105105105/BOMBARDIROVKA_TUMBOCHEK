from flask import Flask, request, render_template
from database import DatabaseManager
from image import create_image

app = Flask(__name__)

dm = DatabaseManager()
dm.connect()
dm.create_tables()

@app.route('/')
def index():
    name, age, profession = "Jerry", 24, 'Programmer'
    template_context = dict(name=name, age=age, profession=profession)
    return render_template('index.html', **template_context)


@app.route('/reg_run', methods=['POST', 'GET'])
def reg_run():
    a = request.form['email']
    create_image(a)

    return render_template('index.html', href=a)


if __name__ == "__main__":
    app.run(host='0.0.0.0',
        port=5000,
        threaded=True)
