from flask import Blueprint, render_template

views=Blueprint(__name__,"views")

@views.route("/") #Esto será el index, si pongo /clima sería la pág clima
def home():
    return render_template("index.html",name="Sewax y Crawsectus") #Aquí cargamos el index.html y le pasamos como variable "name"
@views.route("/AudioDL")
def AudioDL():
    return render_template("AudioDL.html")