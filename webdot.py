from bottle import route, run, template, request, static_file, TEMPLATES
from dot import add_dot, save_dot, make_dot, remove_dot

@route('/')
def hello():
    return 'hello'
    
@route('/input')
def input():
    return template('input')
    
@route('/add', method='GET')
def add():
    src = request.GET.src
    dst = request.GET.dst
    g = add_dot(src, dst)
    make_dot(g)
    save_dot(g)
    return template('show', picture='result.png')
    
@route('/input2')
def input2():
    return template('input2')
    
@route('/remove', method='GET')
def remove():
    node = request.GET.node
    g = remove_dot(node)
    make_dot(g)
    save_dot(g)
    return template('show', picture='result.png')
    
@route('/show')
def show():
    return template('show', picture='result.png')
    
@route('/<picture>')
def serve_picture(picture):
    return static_file(picture, root='.')

TEMPLATES.clear()
run()