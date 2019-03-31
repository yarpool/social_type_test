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
                        return "Дюма"
                    else:
                        return "Наполеон"
                else:
                    if intr > extr:
                        return "Габен"
                    else:
                        return "Жуков"
            else:
                if e > l:
                    if intr > extr:
                        return "Есенин"
                    else:
                        return "Гексли"
                else:
                    if intr > extr:
                        return "Бальзак"
                    else:
                        return "Дон Кихот"
        else:
            if sense > ittr:
                if e > l:
                    if intr > extr:
                        return "Драйзер"
                    else:
                        return "Гюго"
                else:
                    if intr > extr:
                        return "Максим Горький"
                    else:
                        return "Штирлиц"
            else:
                if e > l:
                    if intr > extr:
                        return "Джек Лондон"
                    else:
                        return "Гамлет"
                else:
                    if intr > extr:
                        return "Достоевский"
                    else:
                        return "Робеспьер"
