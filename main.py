from flask import Flask, render_template
import pandas

app = Flask(__name__)
df = pandas.read_csv("dictionary.csv")

@app.route("/")
def home():
    return render_template("home.html")


@app.route("/api/v2/<word>")
def api(word):
    definition = df.loc[df["word"] == word]['definition'].squeeze()
    result_dictionary = {"word": word, "definition": definition}
    return result_dictionary


app.run(debug=True, port=5001)