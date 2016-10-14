from bottle import route, run

@route('/')
def main():
    test()
    return
    
def test():
    return 'hello'
    
run()