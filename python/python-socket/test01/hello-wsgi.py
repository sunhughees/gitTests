#!/usr/bin/env python


def app(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    return '<h1>Hello, %s!</h1>' % (environ['PATH_INFO'][1:] or 'World')

if __name__ == '__main__':
    from wsgiref.simple_server import make_server

    httpd = make_server('localhost', 8000, app)
    print "Serving HTTP on port 8000..."
    httpd.serve_forever()
