from flask import Flask, render_template
from flask import request
from collections import Counter

import json

import Actividad1_forms

app=Flask(__name__)

@app.route("/Actividad2",methods=["GET"])
def Actividad2():
    return render_template("Actividad2.html")

@app.route("/Recibir", methods=["POST"])
def Recibir():
    txtIngles = request.form.get('txtIngles').upper()
    txtEspañol = request.form.get('txtEspañol').upper()
    
    
   # diccionario = {txtIngles:txtEspañol,txtEspañol:txtIngles}
    
   # with open("diccionario.txt", "w") as archivo:
   #     json.dump(diccionario, archivo)
    
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


if __name__ =="__main__":
    app.run(debug=True,port=3000)