from flask import Flask, render_template, request

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


@app.route('/choice/<planet_name>')
def choice(planet_name):
    return f"""<!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="/static/css/style.css'" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Варианты выбора</title>
                  </head>
                  <body>
                    <h1>Мое предположение: {planet_name}</h1>
                    <p>Это планета близка к Земле;</p>
                      <div class="alert alert-secondary alert" role="alert">На планете была вода! </div>
                      <div class="alert alert-primary alert" role="alert">У планеты нет почвы </div>
                      <div class="alert alert-warning alert" role="alert">На планете нет кислорода </div>
                    
                  </body>
                </html>"""


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
                    <img src="/static/img/mars1.jpg" alt="Марс потерялся">
                    <p>Это марс.</p>
                  </body>
                </html>"""


@app.route('/rating/<nickname>/<int:level>/<float:rating>')
def rating(nickname, level, rating):
  return f'''
              <!doctype html>
                <html lang="ru">
                  <head>
                    <meta charset="utf-8">
                    <link rel="stylesheet" href="/static/css/style.css'" />
                    <link rel="stylesheet" 
                    href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css" 
                    integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1" 
                    crossorigin="anonymous">
                    <title>Результат отборас</title>
                  </head>
                  <body>
                    <h1>Результаты отбора</h1>
                    <p>Пренендента на участие в миссии {nickname}</p>
                      <div class="alert alert-primary alert" role="alert">Поздравляем! Ваш рейтинг после {level} этапа отбора составляет {rating} </div>
                      <div class="alert alert-warning alert" role="alert">Желаем удачи </div>
                      
                    
                  </body>
                </html>
              '''


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
                      <img src="/static/img/mars1.jpg" alt="Марс потерялся">
                      <div class="alert alert-warning alert" role="alert">'Человечество вырастает из детства.' </div>
                      <div class="alert alert-dark aler" role="alert">"Человечеству мала одна планета." </div>
                      <div class="alert alert-primary" role="alert">"Мы сделаем обитаемыми безжизненные пока планеты." </div>
                      <div class="alert alert-secondary alert" role="alert">"И начнем с Марса!" </div>
                      <div class="alert alert-danger" role="alert">"Присоединяйся!" </div>
                    </body>
                  </html>"""


@app.route('/carousel')
def carousel():
      return f'''<!doctype html>
                      <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          
                          <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
                          <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"
                          integrity="sha384-JZR6Spejh4U02d8jOt6vLEHfe/JQGiRRSQQxSfFWpi1MquVdAyjUar5+76PVCmYl" 
                          crossorigin="anonymous"></script>
                          
                          <link rel="stylesheet" href="/static/css/style.css" />
                          <title>Карусель</title>
                        </head>
                        <body>
                          <div id="Carousel" class="carousel slide" data-ride="carousel">
                            <div class="carousel-inner">
                              <div class="carousel-item active">
                                <img class="d-block w-50" src="/static/img/mars1.jpg" alt="mars1">
                              </div>
                              <div class="carousel-item">
                                <img class="d-block w-50" src="/static/img/mars2.jpg" alt="mars2">
                              </div>
                              <div class="carousel-item">
                                <img class="d-block w-50" src="/static/img/mars3.jpg" alt="mars3">
                              </div>
                              <div class="carousel-item">
                                <img class="d-block w-50" src="/static/img/mars4.jpg" alt="mars4">
                              </div>
                            </div>
                        </div>
                        </body>
                      </html>'''

@app.route('/form_sample', methods=['POST', 'GET'])
def form_sample():
    if request.method == 'GET':
        return f'''<!doctype html>
                        <html lang="en">
                          <head>
                            <meta charset="utf-8">
                            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                            <link rel="stylesheet"
                            href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                            integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                            crossorigin="anonymous">
                            <link rel="stylesheet" href="/static/css/style.css" />
                            <title>Анкетаы</title>
                          </head>
                          <body>
                            <h1 class="form_h1" >Анкета претендета на участие в миссии</h1>
                            <div>
                                <form class="login_form" method="post">
                                    <input type="text" class="form-control" id="name" aria-describedby="namelHelp" placeholder="Введите ваше имя" name="name">
                                    <input type="text" class="form-control" id="surname" aria-describedby="surnamelHelp" placeholder="Введите вашу фамилию" name="surname">
                                    <input type="email" class="form-control" id="email" aria-describedby="emailHelp" placeholder="Введите адрес почты" name="email">
                                    <input type="text" class="form-control" id="education" aria-describedby="educationHelp" placeholder="Какое у вас образование" name="education">
                                    <input type="password" class="form-control" id="password" placeholder="Введите пароль" name="password">
                                    <div class="form-group">
                                        <label for="classSelect">Ваша основная профессия</label>
                                        <select class="form-control" id="classSelect" name="class">
                                          <option>Инженер-исследователь</option>
                                          <option>Пилот</option>
                                          <option>Строитель</option>
                                          <option>Экзобиолог</option>
                                          <option>Врач</option>
                                          <option>инженер по терраформированию</option>
                                          <option>Кот</option>
                                          <option>Климатолог</option>
                                        </select>
                                    </div>
                                    <div class="form-group">
                                        <label for="form-check">Укажите пол</label>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="male" value="male" checked>
                                          <label class="form-check-label" for="male">
                                            Мужской
                                          </label>
                                        </div>
                                        <div class="form-check">
                                          <input class="form-check-input" type="radio" name="sex" id="female" value="female">
                                          <label class="form-check-label" for="female">
                                            Женский
                                          </label>
                                        </div>
                                    </div>
                                    <div class="form-group">
                                        <label for="about">Немного о себе</label>
                                        <textarea class="form-control" id="about" rows="3" name="about"></textarea>
                                    </div>
                                    <div class="form-group">
                                        <label for="photo">Приложите фотографию</label>
                                        <input type="file" class="form-control-file" id="photo" name="file">
                                    </div>

                                    <div class="form-group form-check">
                                        <input type="checkbox" class="form-check-input" id="acceptRules" name="accept">
                                        <label class="form-check-label" for="acceptRules">Готов быть добровольцем</label>
                                    </div>
                                    <button type="submit" class="btn btn-primary">Записаться</button>
                                </form>
                            </div>
                          </body>
                        </html>'''


@app.route('/loadphoto', methods=['POST', 'GET'])
def load_photo():
  if request.method == 'GET':
      return f'''<!doctype html>
                      <html lang="en">
                        <head>
                          <meta charset="utf-8">
                          <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
                          <link rel="stylesheet"
                          href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta1/dist/css/bootstrap.min.css"
                          integrity="sha384-giJF6kkoqNQ00vy+HMDP7azOuL0xtbfIcaT9wjKHr8RbDVddVHyTfAAsrekwKmP1"
                          crossorigin="anonymous">
                          <link rel="stylesheet" href="/static/css/style.css" />
                          <title>Загрузка фото</title>
                        </head>
                        <body>
                        <img src='/image.png')>
                          <form method="post" enctype="multipart/form-data">
                            <h1 class="form_h1" >Загрузка фото</h1>
                              <div class="form-group">
                                  <label for="photo">Приложите фотографию</label>
                                  <input type="file" class="form-control-file" id="photo" name="file">
                              </div>
                                  <button type="submit" class="btn btn-primary">Загрузить</button>
                          </form>
                        </body>
                      </html>'''
  elif request.method == 'POST':
      f = request.files['file']
      f.save("image.png")
      return "Форма отправлена"

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')