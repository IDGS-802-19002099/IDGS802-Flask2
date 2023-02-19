from flask import Flask, render_template
from flask import request
from collections import Counter

import Actividad1_forms

app=Flask(__name__)

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
    app.run(debug=True,port=3000)