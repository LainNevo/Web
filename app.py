from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def solana():
    return render_template('index.html')

@app.route('/solana_top')
def solana_top():
    return render_template("solana_top.html")

@app.route('/solana_closed')
def solana_closed():
    return render_template("solana_closed.html")


if __name__ == '__main__':
    app.run()
