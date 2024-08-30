from flask import Flask, redirect, render_template, request
from db_helpers import get_birthdays, add_birthday, update_birthday, delete_birthday

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

@app.after_request
def after_request(response):
    """Ensure responses aren't cached"""
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


@app.route("/", methods=["GET", "POST"])
def index():
    # Handle the main page and form submission
    if request.method == "POST":
        id = request.form.get("id")
        name = request.form.get("name")
        month = request.form.get("month")
        day = request.form.get("day")
        year = request.form.get("year")

        if id:
            # Update the existing entry
            update_birthday(id, name, month, day, year)
        else:
            # Add new entry
            add_birthday(name, month, day, year)

    # Display the entries
    birthdays = get_birthdays()
    return render_template("index.html", birthdays=birthdays)


@app.route("/delete", methods=["POST"])
def delete():
    # Delete relevant entry
    id = request.form.get("id")
    if id:
        delete_birthday(id)
    return redirect("/")


@app.route("/edit", methods=["GET"])
def edit():
    # Handle edit logic
    id = request.args.get("id")
    name = request.args.get("name")
    month = request.args.get("month")
    day = request.args.get("day")
    year = request.args.get("year")

    # Display updated entries
    birthdays = get_birthdays()
    return render_template("index.html", birthdays=birthdays, id=id, name=name, month=month, day=day, year=year)


if __name__ == "__main__":
    app.run()
