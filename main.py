from flask import Flask, render_template
import pandas

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    # df = pandas.read_csv("")
    # temp = df.station(date)
    temp = 23
    return {"station": station,
            "date": date,
            "temperature": temp}


if __name__ == "__main__":
    app.run(debug=True)