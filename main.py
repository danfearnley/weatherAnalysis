from flask import Flask, render_template
import matplotlib.pyplot
import pandas as pd
import matplotlib
import numpy as np

if __name__ == "__main__":
    df = pd.read_csv("data_small/TG_STAID000001.txt", skiprows=20, parse_dates=["    DATE"])
    print(df.columns)
    columnHeaders = df.columns
    print(df[['STAID', '    DATE', '   TG', ' Q_TG']])

    # Simple stats
    print(df['   TG'].mean()) # return mean of temps
    averageTemp = df.loc[df['   TG'] != -9999]['   TG'].mean() # exclude all -9999 temps - no data for that day. Part in loc[] is the condition to apply.
                                                            # then only return the ['   TG'] column, and get average
    print(averageTemp / 10) # have to divide by 10, as data is multiplied by 10 for simplicity
    maxTemp = df.loc[df['   TG'] != -9999]['   TG'].max()
    print(maxTemp / 10)

    # Get certain cells
    print(df.loc[df["    DATE"] == "1860-01-05"]['   TG'].squeeze()) # squeeze removes the index from data
    print(df.loc[df['   TG'] == df['   TG'].max()]["    DATE"].squeeze()) # return date with max temp

    # Calculate a new column from existing column
    df["TG0"] = df['   TG'].mask(df['   TG'] == -9999, np.nan) # replaces all -9999 values with NaN. useful as wont calculate those values
    df["Celsius"] = df['TG0'] / 10 # create a new col with temp / 10 to give actual value
    print(df)

    ## Histogram - right click run in interactive window
    # histogram = df.loc[df['   TG'] != -9999]['   TG'].hist()
    # print(histogram)
    # matplotlib.pyplot(histogram)
    # matplotlib.pyplot.show()

    # Plotting
    print(df["Celsius"].hist())
    print(df.plot(x="    DATE", y="Celsius", figsize=(15,3)))

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/api/v1/<station>/<date>/")
def about(station, date):
    df = pd.read_csv("data_small/TG_STAID000001.txt", skiprows=20, parse_dates=["    DATE"])
    # temp = df.station(date)
    temp = 23
    return {"station": station,
            "date": date,
            "temperature": temp}


if __name__ == "__main__":
    app.run(debug=True)