from flask import Flask, redirect, render_template, request

app = Flask(__name__)

counts = {
    'GET': 0,
    'POST': 0,
    'DELETE': 0,
    'PUT': 0,
}


@app.route('/')
def request_counter():
    return render_template("index.html", count=sum(counts.values()))


@app.route('/request-counter')
def increment():
    global counts
    counts[request.method] += 1
    return redirect('/')


@app.route('/statistics')
def stats():
    return render_template("statistics.html")


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
