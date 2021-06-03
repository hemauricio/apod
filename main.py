from flask import Flask, render_template
import json
import nasa

app = Flask("APOD")

@app.route("/", methods=["GET"])
def index():
    # return jsonify(nasa.apod())
    return render_template("apod.html", data=nasa.apod())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8080", debug=True, threaded=True)
