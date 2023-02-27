from flask import Flask, render_template
from flask import request
from flask_wtf.csrf import CSRFProtect
from flask import make_response
from flask import flash
from collections import Counter
import json
import Actividad1_forms
import forms


app=Flask(__name__)

app.config['SECRET_KEY']="Esta es un clave encriptada"
csrf=CSRFProtect()

@app.errorhandler(404)
def no_encontrada(e):
    return render_template('404.html'),404

@app.before_request
def before_request():
    print("numero1")


@app.route("/calculoResitencias", methods=["GET","POST"])
def calculoResistencias():
    respuesta = ""
    tolerancia = "0"
    primerBanda = "9"
    segundaBanda = "9"
    Multiplicador = "9"
    colores = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'gray', 'white']
    colTolerancia = ['gold','silver']
    valorTolerancia=""
    
    if request.method=="POST":
        primerBanda = request.form.get('txtPrimer')
        segundaBanda = request.form.get('txtSegundo')
        Multiplicador = request.form.get('txtMultiplicador')
        tolerancia = request.form.get('btnTolerancia')
        respuesta = int(int(primerBanda + "" + segundaBanda) * (10 ** int(Multiplicador)))

    color1 = colores[int(primerBanda)]
    color2 = colores[int(segundaBanda)]
    color3 = colores[int(Multiplicador)]
    color4 = colTolerancia[int(tolerancia)]

    if color4 == "gold":
        valorTolerancia =5
    if color4 == "silver":
        valorTolerancia = 10

    maximo=respuesta+(respuesta*(valorTolerancia/100))
    minimo= respuesta-(respuesta*(valorTolerancia/100))
    valor_cookie=request.cookies.get("ultimo_Calculo")
    response=make_response(render_template("Actividad3.html", resultado = str(respuesta)+ "ohms " + str(valorTolerancia) +"%", color1 = color1, color2 = color2, color3= color3, color4 = color4, ultimoCalculo=valor_cookie,maximo=str(maximo),minimo=str(minimo)))
    response.set_cookie("ultimo_Calculo",(str(respuesta)+ "ohms" + str(valorTolerancia)))    
    return response

@app.route("/cookies",methods=["GET", "POST"])
def cookies():
    print("numero2")
    reg_user=forms.LoginForm(request.form)
    datos=""
    if request.method=="POST" and reg_user.validate():
        user=reg_user.username.data
        passw=reg_user.password.data
        datos=user+'@'+passw
        success_message="Bienvenido {}".format(user)
        flash(success_message)
        
    response=make_response(render_template("cookies.html",form=reg_user))  
    response.set_cookie("datos_user",datos)    
    return response

@app.after_request
def after_request(response):
    print("numero3")
    return response
    

@app.route("/saludo")
def saludo():
    valor_cookie=request.cookies.get("datos_user")
    nombre=valor_cookie.split("@")
    return render_template("saludo.html", nom=nombre[0])


@app.route("/formulario2",methods=["GET"])
def formulario2():
    return render_template("formulario2.html")

@app.route("/Alumnos",methods=["GET","POST"])
def Alumno():
    alum_form=forms.UserForm(request.form)
    mat=""
    nom=""
    if request.method=="POST" and alum_form.validate():
        mat=alum_form.matricula.data
        nom=alum_form.nombre.data
        #alum_form.apaterno.data
        #alum_form.amaterno.data
        #alum_form.email.data
        

    return render_template("Alumnos.html", form=alum_form, mat=mat,nom=nom)


    """Actividad2
    """
    
    
@app.route("/Actividad2",methods=["GET"])
def Actividad2():
    return render_template("Actividad2.html")

@app.route("/Recibir", methods=["POST"])
def Recibir():
    txtIngles = request.form.get('txtIngles').upper()
    txtEspañol = request.form.get('txtEspañol').upper()
# diccionario = {txtIngles:txtEspañol,txtEspañol:txtIngles}
# with open("diccionario.txt", "w") as archivo:
# json.dump(diccionario, archivo)
    
    with open("diccionario.txt","r") as archivo:
        diccionario_cargado = json.load(archivo)
        
    diccionario_cargado[txtIngles]=txtEspañol 
        
    with open("diccionario.txt","w") as archivo:
        json.dump(diccionario_cargado, archivo)
        
    with open("diccionario.txt","r") as archivo:
        diccionario_cargado = json.load(archivo)
        
    diccionario_cargado[txtEspañol]=txtIngles 
        
    with open("diccionario.txt","w") as archivo:
        json.dump(diccionario_cargado, archivo)
        
    return render_template("Actividad2.html", resultado ="")


@app.route("/mostrar", methods=["POST"])
def mostrar():
    txtFiltro = request.form.get('txtFiltro').upper()
    btnlenguaje= int(request.form.get('btnlenguaje'))
    
    
    
    with open("diccionario.txt","r") as archivo:
        diccionario = json.load(archivo)
    
    txtResultado =  (diccionario[txtFiltro])
    return render_template("Actividad2.html", resultado = str(txtResultado))

    """Actividad
    """
    
@app.route("/Actividad_formulario",methods=["GET"])
def Actividad_formulario():
    return render_template("Actividad_formulario.html")

@app.route("/Act1",methods=["GET","POST"])
def Act1():
    numero_form=Actividad1_forms.UserForm(request.form)
    if request.method=="POST":
        num=numero_form.matricula.data

    return render_template("Act1.html", form=numero_form, num=num)


@app.route("/GenerarCajas", methods=['GET', 'POST'])
def GenerarCajas():
    if  request.method == 'POST':
        cantidadCajas = int(request.form.get('txtcantidad'))
        return render_template('Actividad_formulario.html', cantidad = cantidadCajas)
    else:
        return render_template('Actividad_formulario.html', cantidad = 0)

@app.route("/generarResultado", methods=['POST'])
def generarResultado():
    cantidadCajas = int(request.form.get('cantidadIngresada'))
    listaNumeros = []
    
    for indice in range(1, int(cantidadCajas) + 1):
        valorNumerico = int(request.form.get('caja'+str(indice)))
        listaNumeros.append(valorNumerico)
    maximo = max(listaNumeros) 
    minimo = min(listaNumeros)
    promedio = sum(listaNumeros)/int(cantidadCajas) 
    contador = Counter(listaNumeros)
    return render_template('Actividad1_Res.html', maximo = str(maximo), minimo = str(minimo), promedio = str(promedio), contador = contador, lenCont = len(contador))



if __name__ =="__main__":
    csrf.init_app(app)
    app.run(debug=True,port=3000)