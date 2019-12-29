from flask import render_template
from models.Materia import Materia
def routes(app):
    @app.route("/")
    def index():
        materias = Materia.query.all()
        return render_template("materias.html",materias=materias)