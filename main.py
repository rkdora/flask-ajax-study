from flask import Flask, render_template,jsonify

from models.models import LogContent

from models.database import db_session
from datetime import datetime

import time

app = Flask(__name__)


@app.route('/')
def hello_view():
    heading_1 = "Hello,World"
    all_log = LogContent.query.all()
    return render_template('hello.html', title='flask now!', heading_1=heading_1, all_log=all_log)

@app.route("/log",methods=["post"])
def log():

    log = time.time()
    content = LogContent(log,datetime.now())
    db_session.add(content)
    db_session.commit()

    all_log = LogContent.query.all()
    return jsonify({'result': 'ok', 'value': all_log[-1].log})

if __name__ == '__main__':
    app.run()
