####Flask server creation#########
from flask import Flask, render_template, url_for, request, redirect
import csv

app = Flask(__name__)
print(__name__)


####create routes##############


@app.route("/")
def my_home():
    return render_template("index.html")


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


def write_to_file(data):
    with open("database.txt", mode="a") as database:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        file = database.write(f"\n {email}, {subject}, {message}")


def write_to_csv(data):
    with open("database.csv", mode="a", newline="") as database2:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(
            database2,
            delimiter=",",
            quotechar="'",
            quoting=csv.QUOTE_MINIMAL,
        )
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=["POST", "GET"])
def submit_form():
    if request.method == "POST":
        data = request.form.to_dict()
        write_to_csv(data)
        return redirect("./thankyou.html")
    else:
        return "somthing went wrong. Try again!"


# don't need a route for favicon
# @app.route("/favicon.ico")
# def blog():
#     return "<p>these are my thoughts on blogs</p>"

# End ofcreate routes##############
# End of Flask server creation#####
