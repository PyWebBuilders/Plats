from services.app import create_app


app = create_app("config")


if __name__ == "__main__":
    import config

    if config.DEBUG:
        if config.WSGI_MODE:
            from bframe.wsgi import WSGIProxy
            from wsgiref.simple_server import make_server
            with make_server(config.HOST, config.PORT, WSGIProxy(app)) as httpd:
                print("Serving on port http://%s:%s..." % (config.HOST,
                                                           config.PORT))
                httpd.serve_forever()
        else:
            app.run(config.HOST, config.PORT)

    if not config.DEBUG:
        from bframe.wsgi import WSGIProxy
        from gevent.monkey import patch_all
        patch_all()
        from gevent.pywsgi import WSGIServer
        server = WSGIServer((config.HOST, config.PORT),
                            WSGIProxy(app))
        print("Serving on port http://%s:%s..." % (config.HOST,
                                                   config.PORT))
        server.serve_forever()
