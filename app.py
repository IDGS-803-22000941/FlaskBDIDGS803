from flask import Flask, render_template, request, redirect, url_for, flash
from flask_wtf.csrf import CSRFProtect
from config import DevelopmentConfig
from models import db, Alumnos
import forms

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

# Inicializar CSRFProtect correctamente
csrf = CSRFProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'),404

@app.route("/")
@app.route("/index")
def index():
    create_form=forms.UserForm2(request.form)
    alumno=Alumnos.query.all() #selecte * from alumnos
    return render_template("index.html", form=create_form, alumnos=alumno)


@app.route('/detalles', methods=['GET', 'POST'])
def detalles():
    create_form = forms.UserForm2(request.form)
    if request.method == 'GET':
        id = request.args.get('id')
        alum1 = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        nombre = alum1.nombre
        apaterno = alum1.apaterno
        email = alum1.email
        return render_template('detalles.html', id=id, nombre=nombre, apaterno=apaterno, email=email)
    

@app.route('/Alumnos1', methods=['GET', 'POST'])
def Alumnos1():
    create_form = forms.UserForm2(request.form)
    if request.method == 'POST':
        alum=Alumnos(nombre=create_form.nombre.data,
            apaterno=create_form.apaterno.data,
            email=create_form.email.data)
        db.session.add(alum)
        db.session.commit()
        return redirect(url_for('index.html'))
    return render_template('Alumnos1.html', form=create_form )



if __name__ == '__main__':
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(debug=True)
