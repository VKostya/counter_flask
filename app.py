from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://flask:flask@db:5432/counterdb"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)


class Counter(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    client_info = db.Column(db.String, nullable=True)


@app.route("/")
def home():
    user_agent = request.headers.get("User-Agent")
    counter_record = Counter(client_info=user_agent)

    db.session.add(counter_record)
    db.session.commit()

    return jsonify(
        {
            "id": counter_record.id,
            "timestamp": counter_record.timestamp,
            "client_info": counter_record.client_info,
        }
    )


@app.route("/count", methods=["GET"])
def get_count():
    count = Counter.query.count()
    return jsonify({"count": count})


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
