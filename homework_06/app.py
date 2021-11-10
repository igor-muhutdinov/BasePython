import os
from flask import Flask, render_template
from flask_migrate import Migrate
from models.database import db
from views.library import library_app

app = Flask(__name__)
SQLALCHEMY_DATABASE_URI = os.getenv("DB_CONN_URI",
                                    "postgresql+psycopg2://user:password@localhost:5432/library")
app.config.update(
    SQLALCHEMY_DATABASE_URI=SQLALCHEMY_DATABASE_URI,
    SQLALCHEMY_TRACK_MODIFICATIONS=False,
)

db.init_app(app)
migrate = Migrate(app, db)

app.register_blueprint(library_app, url_prefix="/library")


@app.route("/")
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run()
