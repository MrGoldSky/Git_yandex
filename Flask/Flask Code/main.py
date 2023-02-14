from flask import Flask, render_template

app = Flask(__name__)

@app.route('/<title>')
@app.route('/index<title>')
def index(title):
    param = {}
    param['title'] = f"{title}"
    return render_template('index.html', **param)

@app.route("/training/<prof>")
def traning(prof):
    param = {}
    param['simulator'] = {prof}
    param['profi'] = "no"
    return render_template('index.html', **param)

@app.route('/')
def first():
    return "<h1>Миссия Колонизация Марса</h1>"


@app.route('/list_prof/<listy>')
def list_prof(listy):
    param = {}
    param['list'] = {listy}
    param['simulator'] = "no"
    param['profi'] = ["Программист", "Инжиенер", "Врачь", "Повар", "Клоун", "Зоолог", "Кот", "Кошечка"]
    return render_template('index.html', **param)


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
                    <link rel="stylesheet" href="/static/css/style.css'" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Привет, Марс</title>
                  </head>
                  <body>
                    <h1>Жди нас, Марса</h1>
                    <img src="/static/img/mars.jpg" alt="Марс потерялся">
                    <p>Это марс.</p>
                  </body>
                </html>"""


@app.route('/promotion_image')
def promotion_image():
  return """<!doctype html>
                  <html lang="ru">
                    <head>
                      <meta charset="utf-8">
                      <link rel="stylesheet" href="/static/css/style.css">
                      <link rel="stylesheet" 
                      href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                      integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                      crossorigin="anonymous">
                      <title>Привет, Марс</title>
                    </head>
                    <body>
                      <h1>Жди нас, Марс</h1>
                      </br>
                      <img src="/static/img/mars.jpg" alt="Марс потерялся">
                      <div class="alert alert-warning alert" role="alert">'Человечество вырастает из детства.' </div>
                      <div class="alert alert-dark aler" role="alert">"Человечеству мала одна планета." </div>
                      <div class="alert alert-primary" role="alert">"Мы сделаем обитаемыми безжизненные пока планеты." </div>
                      <div class="alert alert-secondary alert" role="alert">"И начнем с Марса!" </div>
                      <div class="alert alert-danger" role="alert">"Присоединяйся!" </div>
                    </body>
                  </html>"""
    
if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')