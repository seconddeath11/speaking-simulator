from flask import Flask, render_template

from Task import Task
from Variant import Variant

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)


@app.route('/')
def index():
    num = app.config["NUM_OF_VARS"]
    return render_template('index.html', num=num)


@app.route('/var<num>/blank_')
def blank_(num):
    return render_template('blank_.html', num=num)


def compile_task(var_num, task_num):
    with open('static/variants/' + str(var_num) + "/" + str(task_num) + ".txt", encoding="utf8") as f:
        text = f.readlines()
    return {
        1: Task(task_num, text=text, prep_time=90, answer_time=90),
        2: Task(task_num, text=text, picture1=picture_path(var_num, 2), prep_time=90, answer_time=20),
        3: Task(task_num, audio=audio_path(var_num), prep_time=0, answer_time=270),
        4: Task(task_num, text=text[1:], picture1=picture_path(var_num, 4, 1),
                picture2=picture_path(var_num, 4, 2), prep_time=150, answer_time=180, project_name=text[0])
    }.get(task_num, 1)


def audio_path(var_num):
    return "variants/" + str(var_num) + "/" + "3.mp3"


def picture_path(var_num, task_num, pic_num=1):
    if task_num == 2:
        return "variants/" + str(var_num) + "/2.png"
    else:
        return "variants/" + str(var_num) + "/4_" + str(pic_num) + ".png"


def get_var(var_num):
    return Variant(var_num, compile_task(var_num, 1), compile_task(var_num, 2), compile_task(var_num, 3),
                   compile_task(var_num, 4))


@app.route('/var<int:var_num>/task<int:task_num>')
def var(var_num, task_num):
    variant = get_var(var_num)
    return render_template('var.html', task=variant.get_task(task_num), var=variant)


def get_next_page(prep, var_num, task, ans_time=None):
    st = "/var/" + str(var_num) + "/task"
    if prep == 1:
        return st + str(task) + ("/answer" if task != 2 else "/answer/1")
    else:
        if (task == 2) and (ans_time is not None) and (int(ans_time) < 4):
            return st + str(task) + ("/answer" if task != 2 else "/answer/" + str(int(ans_time) + 1))
        elif task == 2:
            return st + str(task + 1) + "/answer"
        elif task == 4:
            return "/"
        else:
            return st + str(task + 1) + "/prep"


if __name__ == '__main__':
    app.run(debug=True)
