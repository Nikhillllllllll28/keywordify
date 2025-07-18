from flask import Flask, render_template, request
from rake_spacy import Rake
import spacy

app = Flask(__name__)
nlp = spacy.load("en_core_web_sm")
# rake = Rake(nlp=nlp)
rake = Rake(nlp=nlp, min_length=1, max_length=1)

@app.route("/", methods=["GET", "POST"])
def index():
    keywords = []
    text_input = ""
    if request.method == "POST":
        text_input = request.form.get("text", "")
        if text_input:
            keywords = rake.apply(text_input)
    return render_template("index.html", keywords=keywords, text=text_input)

if __name__ == "__main__":
    app.run(debug=True)
