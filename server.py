from flask import Flask, render_template

app = Flask(__name__)

# Have the root route render a template with a checkerboard on it
@app.route('/')
def route_one():
    return render_template("index.html", row=8, column=8, color1="black", color2="red")

# Have another route accept a single parameter (i.e. "/<x>") and render a checkerboard with x many rows, with alternating colors
@app.route('/<int:x>')
def row(x):
    return render_template("index.html", row=x, column=8, color1="black", color2="red")

# Have another route accept 2 parameters (i.e. "/<x>/<y>") and render a checkerboard with x rows and y columns, with alternating colors
@app.route('/<int:x>/<int:y>')
def column(x,y):
    return render_template("index.html", row=x, column=y, color1="black", color2="red")

"""Have another route accept 4 parameters (i.e. "/<x>/<y>/<color1>/<color2>") and render
a checkerboard with x rows and y columns, with alternating colors, color1 and color2"""

@app.route('/<int:x>/<int:y>/<string:one>/<string:two>')
def column_row_two(x,y,one,two):
    return render_template("index.html", row=x, column=y, color1=one, color2=two)


if __name__ == "__main__":
    app.run(debug=True, host="localhost", port=5001)

