from bottle import route, run, template, request, static_file
from dot import add_dot

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
    ret = add_dot(src, dst)
    return static_file('result.png', root='.')

run()