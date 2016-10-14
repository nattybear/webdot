from bottle import route, run, template

@route('/')
def hello():
    return 'hello'
    
@route('/input')
def input():
    return template('input')
    
run()