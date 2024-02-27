from flask import Flask, render_template, request, url_for

app = Flask(__name__)


@app.route('/astronaut_selection', methods=['POST', 'GET'])
def form():
    if request.method == 'GET':
        return render_template('form.html')
    if request.method == 'POST':
        return 'Форма отправлена'


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')