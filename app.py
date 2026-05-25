from flask import Flask

app = Flask(__name__)

@app.route("/")
def table():
    number = 5
    result = ""

    for i in range(1, 11):
        result += f"{number} x {i} = {number * i}<br>"

    return f"""
    <h1>Multiplication Table App</h1>
    <h2>Table of {number}</h2>
    {result}
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
