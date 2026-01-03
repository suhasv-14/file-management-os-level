from flask import Flask, render_template, request
from backend.manager.file_manager import FileManager

app = Flask(__name__)
fm = FileManager()

@app.route("/", methods=["GET", "POST"])
def index():
    message = ""

    if request.method == "POST":
        action = request.form.get("action")

        if action == "create_dir":
            fm.create_directory(request.form["path"], request.form["name"])
            message = "Directory created"

        elif action == "create_file":
            fm.create_file(request.form["path"], request.form["name"], request.form["size"])
            message = "File created"

        elif action == "access_file":
            message = fm.access_file(request.form["name"])

        elif action == "delete_file":
            fm.delete_file(request.form["name"])
            message = "File deleted"

        elif action == "rename_file":
            fm.rename_file(request.form["old_name"], request.form["new_name"])
            message = "File renamed"

    return render_template(
        "index.html",
        tree=fm.get_tree(),
        cache=fm.get_cache(),
        logs=fm.get_logs(),
        message=message
    )

if __name__ == "__main__":
    app.run(debug=True)
