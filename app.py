from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method=="POST":
        stock_trig=request.form.get('stock_trig')
        print(stock_trig)
        return render_template("index.html",stock=stock_trig)
    return render_template("index.html")


if __name__=="__main__":
    app.run(debug=True)