from flask import Flask , render_template , send_file 

import os
app = Flask(__name__)

#PRIMERA FUNCION
@app.route('/')
def index():
    return  render_template('index.html')      

#PONE LA IMAGEN EN LA PRIMERA FUNCION
@app.route('/media/<path:filename>')
def media_file(filename):
    file_path = os.path.join('images', filename)
    return send_file(file_path)  
   
#PONE MUSICA??????
@app.route('/audio/<path:filename>')
def audio_file(filename):
    file_path = os.path.join('audio', filename)
    return send_file(file_path)  
   
#segunda funcion MUESTRA SEGUNDO HTML
@app.route('comic/pruebados')
def pruebaDOS():
    return  render_template('pruebaDOS.html')

@app.route('/pruebatres')
def pruebatres():
    return  render_template('pruebatres.html')    

@app.route('/pruebacuatro')
def pruebacuatro():
    return  render_template('pruebacuatro.html') 

@app.route('/pruebacinco')
def pruebacinco():
    return  render_template('pruebacinco.html') 

@app.route('/pruebaseis')
def pruebaseis():
    return  render_template('pruebaseis.html') 


@app.route('/pruebasiete')
def pruebasiete():
    return  render_template('pruebasiete.html') 

@app.route('/pruebasietealfa')
def pruebasietealfa():
    return  render_template('pruebasietealfa.html') 

@app.route('/pruebabonusmarx')
def pruebabonusmarx():
    return  render_template('pruebabonusmarx.html')  

@app.route('/pruebaocho')
def pruebaocho():
    return  render_template('pruebaocho.html') 

@app.route('/pruebaochobeta')
def pruebaochobeta():
    return  render_template('pruebaochobeta.html') 

@app.route('/pruebaochobetauno')
def pruebaochobetauno():
    return  render_template('pruebaochobetauno.html') 

@app.route('/pruebabonusancap')
def pruebabonusancap():
    return  render_template('pruebabonusancap.html') 

@app.route('/pruebaochobetados')
def pruebaochobetados():
    return  render_template('pruebaochobetados.html')    

 
