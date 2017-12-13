from flask import Flask, redirect, render_template, request
import data_handler

app = Flask(__name__)
filename = "/request_counts.txt"


@app.route('/')
def request_counter():
    counts = data_handler.read_file(filename)
    return render_template("index.html", count=sum(counts.values()))


@app.route('/request-counter')
def increment():
    counts = data_handler.read_file(filename)
    counts[request.method] += 1
    data_handler.write_file(filename, counts)
    return redirect('/')


@app.route('/statistics')
def stats():
    counts = data_handler.read_file(filename)
    return render_template("statistics.html", count=counts)


if __name__ == '__main__':
    app.run(
        port=5000,
        debug=True,
    )
