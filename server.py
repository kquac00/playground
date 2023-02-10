
from flask import Flask, render_template
app = Flask(__name__)    

@app.route('/')
def initial():
    return "Enter playground Flask box option"

@app.route('/play')          
def play():
    return render_template('index.html')  

@app.route('/play/<int:number_box>')          
def play_box(number_box):
    return render_template('index1.html', repeat = number_box) 

@app.route('/play/<int:number_box>/<string:color>')
def box_color(number_box, color):
    return render_template("index2.html", repeat= number_box, color=color )

if __name__=="__main__":       
    app.run(debug=True)    