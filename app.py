from flask import Flask, render_template
 
app = Flask(_name_)
 
@app.route('/')
def index():
  titulo = "FErnando Daniel Murillo Viv"
  return render_template('index.html', titulo=titulo)
 
if __name__ == '__main__':
  app.run(host='0.0.0.0', debug=True, port=5000)