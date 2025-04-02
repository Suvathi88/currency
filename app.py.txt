from flask import Flask, render_template, request
from forex_python.converter import CurrencyRates

app = Flask(__name__)
currency_rates = CurrencyRates()

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        amount = float(request.form["amount"])
        from_currency = request.form["from_currency"]
        to_currency = request.form["to_currency"]

        # Convert currency
        try:
            converted_amount = currency_rates.convert(from_currency, to_currency, amount)
            return render_template("index.html", converted_amount=converted_amount, amount=amount, from_currency=from_currency, to_currency=to_currency)
        except Exception as e:
            return render_template("index.html", error="Error in conversion. Please check the input.")

    return render_template("index.html", converted_amount=None)

if __name__ == "__main__":
    app.run(debug=True)
