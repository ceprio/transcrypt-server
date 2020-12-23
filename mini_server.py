import os
from flask import Flask, render_template, send_from_directory
app = Flask(__name__)
import transcrypt


@app.route('/')
def index():
        return render_template('index.html')


@app.route('/favicon.ico')
def ico_file():
    return "None"


@app.route('/<filename>.html')
def html_files(filename=""):
    return render_template(f'{filename}.html')


@app.route('/jspy/<filename>.html')
def pyhtml_files(filename=""):
    target = f'"./__target__/{filename}.js"'
    return render_template('jspy_handler.html', target=target)


@app.route('/jspy/__target__/<path:path>.js')
def jspy_files(path):
    full_path = f"jspy/__target__/{path}.js"
    return send_from_directory(*os.path.split(full_path))


@app.route('/jspy/__target__/<path:path>.map')
def map_files(path):
    full_path = f"jspy/__target__/{path}.map"
    return send_from_directory(*os.path.split(full_path))


@app.route('/jspy/__target__/<path:path>.py')
def source_files(path):
    full_path = f"jspy/{path}.py"
    return send_from_directory(*os.path.split(full_path))


@app.route('/<path:path>.js')
def js_files(path):
    return app.send_static_file(f'js/{path}.js')


if __name__ == '__main__':
    app.debug = True
    app.run()
