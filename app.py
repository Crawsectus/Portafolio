from flask import Flask,jsonify,request
from views import views #Importo el otro archivo

app=Flask(__name__) #La app como tal
app.register_blueprint(views,url_prefix="/") #registra las págs de views.py en la app

if __name__ == "__main__":
    app.run(debug=True) #corre la vaina