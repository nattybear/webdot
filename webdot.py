from bottle import route, run, template, request

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
    return src, dst
    
run()