from flask import render_template
from flask import request
from app import app


@app.route('/', methods=['POST', 'GET'])
@app.route('/index', methods=['POST', 'GET'])
def index():
    if request.method == 'GET':
        return render_template("main.html")
    elif request.method == 'POST':
        rational = 0
        unrational = 0
        sense = 0
        ittr = 0
        l = 0
        e = 0
        intr = 0
        extr = 0
        if request.form['q1'] == 'rational':
            rational += 1
        elif request.form['q1'] == 'unrational':
            unrational += 1
        if request.form['q2'] == 'rational':
            rational += 1
        elif request.form['q2'] == 'unrational':
            unrational += 1
        if request.form['q3'] == 'rational':
            rational += 1
        elif request.form['q3'] == 'unrational':
            unrational += 1
        if request.form['q4'] == 'rational':
            rational += 1
        elif request.form['q4'] == 'unrational':
            unrational += 1
        if request.form['q5'] == 'rational':
            rational += 1
        elif request.form['q5'] == 'unrational':
            unrational += 1
        if request.form['q6'] == 'sense':
            sense += 1
        elif request.form['q6'] == 'ittr':
            ittr += 1
        if request.form['q7'] == 'sense':
            sense += 1
        elif request.form['q7'] == 'ittr':
            ittr += 1
        if request.form['q8'] == 'sense':
            sense += 1
        elif request.form['q8'] == 'ittr':
            ittr += 1
        if request.form['q9'] == 'sense':
            sense += 1
        elif request.form['q9'] == 'ittr':
            ittr += 1
        if request.form['q10'] == 'sense':
            sense += 1
        elif request.form['q10'] == 'ittr':
            ittr += 1
        if request.form['q11'] == 'e':
            e += 1
        elif request.form['q11'] == 'l':
            l += 1
        if request.form['q12'] == 'e':
            e += 1
        elif request.form['q12'] == 'l':
            l += 1
        if request.form['q13'] == 'e':
            e += 1
        elif request.form['q13'] == 'l':
            l += 1
        if request.form['q14'] == 'e':
            e += 1
        elif request.form['q14'] == 'l':
            l += 1
        if request.form['q15'] == 'e':
            e += 1
        elif request.form['q15'] == 'l':
            l += 1
        if request.form['q16'] == 'extr':
            extr += 1
        elif request.form['q16'] == 'intr':
            intr += 1
        if request.form['q17'] == 'extr':
            extr += 1
        elif request.form['q17'] == 'intr':
            intr += 1
        if request.form['q18'] == 'extr':
            extr += 1
        elif request.form['q18'] == 'intr':
            intr += 1
        if request.form['q19'] == 'extr':
            extr += 1
        elif request.form['q19'] == 'intr':
            intr += 1
        if request.form['q20'] == 'extr':
            extr += 1
        elif request.form['q20'] == 'intr':
            intr += 1
        # return rational,unrational,sense,ittr,l,e,intr,extr
        if unrational > rational:
            if sense > ittr:
                if e > l:
                    if intr > extr:
                        return render_template("1.html", social_type="Дюма", head="Дюма (Посредник)", image='image1.jpg')
                    else:
                        return render_template("2.html", social_type="Наполеон", head="Наполеон (Политик)", image='image2.jpg')
                else:
                    if intr > extr:
                        return render_template("3.html", social_type="Габен", head="Габен (Мастер)", image='image3.jpg')
                    else:
                        return render_template("4.html", social_type="Жуков", head="Жуков (Маршал)", image='image4.jpg')
            else:
                if e > l:
                    if intr > extr:
                        return render_template("5.html", social_type="Есенин", head="Есенин (Лирик)", image='image5.jpg')
                    else:
                        return render_template("6.html", social_type="Гексли", head="Гексли (Советчик)", image='image6.jpg')
                else:
                    if intr > extr:
                        return render_template("7.html", social_type="Бальзак", head="Бальзак (Критик)", image='image7.jpg')
                    else:
                        return render_template("8.html", social_type="Дон Кихот", head="Дон Кихот (Искатель)", image='image8.jpg')
        else:
            if sense > ittr:
                if e > l:
                    if intr > extr:
                        return render_template("9.html", social_type="Драйзер", head="Драйзер (Хранитель)", image='image9.jpg')
                    else:
                        return render_template("10.html", social_type="Гюго", head="Гюго (Энтузиаст)", image='image10.jpg')
                else:
                    if intr > extr:
                        return render_template("11.html", social_type="Максим Горький", head="Максим Горький (Инспектор)", image='image11.jpg')
                    else:
                        return render_template("12.html", social_type="Штирлиц", head="Штирлиц (Администратор)", image='image12.jpg')
            else:
                if e > l:
                    if intr > extr:
                        return render_template("13.html", social_type="Джек Лондон", head="Джек Лондон (Предприниматель)", image='image13.jpg')
                    else:
                        return render_template("14.html", social_type="Гамлет", head="Гамлет (Наставник)", image='image14.jpg')
                else:
                    if intr > extr:
                        return render_template("15.html", social_type="Достоевский", head="Достоевский (Гуманист)", image='image15.jpg')
                    else:
                        return render_template("16.html", social_type="Робеспьер", head="Робеспьер (Аналитик)", image='image16.jpg')
