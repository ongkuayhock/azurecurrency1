import requests

from flask import Flask, jsonify, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    print("Currency converting1")
    return render_template("jsoncurrency1index.html")


@app.route("/convert", methods=["POST"])
def convert():

    print("Currency converting2")

    # Query for currency exchange rate
    fmcurrency = request.form.get("fmcurrency")  
    tocurrency = request.form.get("tocurrency")   

    print(f"Testing in Post function python from {fmcurrency} To {tocurrency}")

#    res = requests.get("https://api.fixer.io/latest", params={
#        "base": "USD", "symbols": currency})
    res = requests.get("https://api.exchangeratesapi.io/latest?base=" + fmcurrency+"&symbols=" + tocurrency)

    print (f"result from api is{res}")

    # Make sure request succeeded
    if res.status_code != 200:
        return jsonify({"success": False})

    # Make sure currency is in response
    data = res.json()
    print (f"API reesult is {data}")
    if tocurrency not in data["rates"]:
        return jsonify({"success": False})

    return jsonify({"success": True, "rate": data["rates"][tocurrency]})


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)



