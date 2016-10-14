from bottle import route, run, template, request, static_file
from dot import add_dot, save_dot, make_dot

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
    

@route('/input2')
def input2():
    return template('input2')
    
@route('/remove', method='GET')
def remove():
    node = request.GET.node
    
@route('/show')
def show():
    make_dot(g)
    save_dot(g)
    return static_file('result.png', '.')
    
run()