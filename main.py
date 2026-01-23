#
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    titulo = "IDGS-802-Flask"
    lista = ["Huan", "Mario", "Pedro"]
    return render_template("index.html", titulo=titulo, lista=lista)


@app.route("/formulario")
def form():  # El nombre que quieras
    return render_template("formularios.html")


@app.route("/reportes")
def report():  # El nombre que quieras
    return render_template("reportes.html")


@app.route("/hola")
def hola():  # El nombre que quieras
    return "Hola desde /hola"


@app.route("/user/<string:user>")  # Rutas con parametros
def user(user):
    return f"Hola {user}"  # Se usa la f para dar formato a la variable


@app.route("/numero/<int:n>")
def number(n):
    return (
        f"Este es el numero: {n}"  # Se puede usar el .format(variable) en vez de la f
    )


@app.route("/float/<float:num1>/<float:num2>")
def decimal(num1, num2):
    return f"Este es el numero: {num1 + num2}"


@app.route("/user/<int:id>/<string:username>")
def credenciales(id, username):
    return f"ID: {id} nombre: {username}"


@app.route("/default/")
@app.route("/default/<string:param>")
def func(param="juan"):
    return f"<h1>Hola {param}</h1>"


@app.route("/operas")
def operas():
    return """
<form>
<label for="name"> Name: </label>
<input type="text" id="name" name="name" required>
<label for="name"> Apaterno: </label>
<input type="text" id="name" name="name" required>
</form>

        """

@app.route("/operasBas", methods =["GET","POST"])
def operas1():
    n1=0
    n2=0
    res =0
    if request.method == "POST":
        n1 = request.form.get("n1")
        n2 = request.form.get("n2")
        res = float(n1)+float(n2)
    return render_template("operasBas.html",n1=n1,n2=n2,res=res)

@app.route("/alumnos")
def alumnos():
        return render_template("alumnos.html")
    
@app.route("/distancia", methods =["GET","POST"])
def distancia():
    x1 = 0
    y1=0
    x2 = 0
    y2=0
    res = 0
    if request.method == "POST":
        x1 = request.form.get("x1")
        y1= request.form.get("y1")
        x2 = request.form.get("x2")
        y2= request.form.get("y2")
        res = (pow(float(x2)- float(x1),2) + pow(float(y2)- float(y1),2))** (0.5) 
    return render_template("distancia.html",x1=x1,y1=y1,x2=x2,y2=y2,res=res)

@app.route("/resultado", methods=["GET", "POST"])
def resultado():
    n1 = request.form.get("n1")
    n2 = request.form.get("n2")
    opera = request.form.get("opera")
    if opera == "+":
        return f"La suma es: {float(n1) + float(n2) }"
    if opera == "-":
        return f"La resta es: {float(n1) - float(n2) }"
    if opera == "*":
        return f"La multiplicacion es: {float(n1) * float(n2) }"
    if opera == "/":
        return f"La division es: {float(n1) / float(n2)}"


if __name__ == "__main__":
    app.run(debug=True)  # Para que se actualicen los cambios se pone en true
