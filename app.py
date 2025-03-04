from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar CSRFProtect correctamente
csrf = CSRFProtect(app)

@app.route("/")
@app.route("/index")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
