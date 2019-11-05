from flask import Flask, render_template,jsonify

from models.models import OnegaiContent

from models.database import db_session
from datetime import datetime

import time

app = Flask(__name__)


@app.route('/')
def hello_view():
    heading_1 = "Hello,World"
    all_onegai = OnegaiContent.query.all()
    return render_template('hello.html', title='flask now!', heading_1=heading_1, all_onegai=all_onegai)

@app.route("/log",methods=["post"])
def log():
    all_onegai = OnegaiContent.query.all()
    # title = time.time()
    # body =time.time()
    # content = OnegaiContent(title,body,datetime.now())
    # db_session.add(content)
    # db_session.commit()
    return jsonify({'result': 'ok', 'value': all_onegai[-1].title})

if __name__ == '__main__':
    app.run()
