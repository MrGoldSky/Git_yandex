from flask import Flask

app = Flask(__name__)


@app.route('/')
def first():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/index')
def second():
    return "<h1>И на Марсе будут яблони цвести!</h1>"


@app.route('/promotion')
def promotion():
    countdown_list = ['Человечество вырастает из детства.',
                          "Человечеству мала одна планета.",
                          "Мы сделаем обитаемыми безжизненные пока планеты.",
                          "И начнем с Марса!",
                          "Присоединяйся!"]
    return '</br></b>'.join(countdown_list)


@app.route('/image_mars')
def image_mars():
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <title>Привет, Марс</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марса</h1>
                    <img src="/static/img/mars.jpg" alt="Марс потерялся">
                    <p>Это марс.</p>
                  </body>
                </html>"""
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')