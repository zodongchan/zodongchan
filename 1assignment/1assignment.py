from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    data = {
        'title': '1일차 과제',
        'user': 'jongchan',
        'is_admin': True,
        'animal_list': ["사자","호랑이","코뿔소","하마","다람쥐","몽구스"]
    }

    return render_template('1assignment.html', data=data)

if __name__ == "__main__":
    app.run(debug=True)