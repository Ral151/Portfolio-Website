from flask import Flask, render_template
from livereload import Server
import time

app = Flask(__name__)

app.config["Global_Hero_Image"] = "https://my-portfolio-ger.s3.us-east-1.amazonaws.com/static/images/coolbackgrounds-particles-stellar.png"
app.config["Local_Hero_Image"] = "/static/images/coolbackgrounds-particles-stellar.png"
app.config["SMAKCBatch14_Logo"] = "https://my-portfolio-ger.s3.us-east-1.amazonaws.com/static/images/SMAKCYearbookBatch14.png"

@app.route("/")
def home():
    hero_image =  app.config["Global_Hero_Image"] or app.config["Local_Hero_Image"]
    yearbook_logo_image = app.config["SMAKCBatch14_Logo"]
    return render_template("index.html", hero_image = hero_image, yearbook_logo_image=yearbook_logo_image)

@app.route("/navbar")
def navbar():
    return render_template("navbar.html")

if __name__ == "__main__":
    app.debug = True

    server = Server(app.wsgi_app)
    server.watch('templates/**/*.html')   # watch templates
    server.watch('static/**/*')      # watch static files (css/js)
    server.serve(port=5000, host='127.0.0.1', debug=True)
