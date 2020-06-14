from flask import Flask, request, render_template, redirect
from convert import Convert


app = Flask(__name__)
app.config["SECRET_KEY"] = "idgafkltsic"
c = Convert()


@app.route('/')
def show_index():
    """ SHow home route """
    return render_template('index.html')

@app.route("/convert")
def get_conversion():
    """ revice calues ot convert and update for conversion """
    ch_from = request.args["from"].upper()
    ch_to = request.args["to"].upper()
    amount = request.args["amount"]
    
    if c.all_true(ch_from, ch_to, amount):
        symbol =  c.get_currency_code(ch_to)
        amount = c.exchange(ch_from, ch_to, amount)
        return render_template("convert.html", amount=amount, symbol=symbol)

    else:
        return redirect("/")

      
                
            
    
        
        
    



