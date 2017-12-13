from flask import Flask, redirect, render_template

app = Flask(__name__)

counts = 0


@app.route('/')
def request_counter():
    return render_template("index.html", count=counts)


@app.route('/request-counter')
def increment():
    global counts
    counts += 1
    return redirect('/')


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
