import django.core.handlers.wsgi
from django.conf import settings
from django.utils.importlib import import_module
session_engine = import_module(settings.SESSION_ENGINE)

import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.wsgi
import tornado.websocket

import json

from django.contrib.auth.models import User
from source.tests.models import GlobalTesting
from source.tests.classes import GTValues
from source.tests.models import TestCaseInGT
from source.tests.views import pass_tcigt

class GTHandler(tornado.websocket.WebSocketHandler):

    def open(self, gt_id):
        # set self.gt_id for self.gtvalues

        session_key = self.get_cookie(settings.SESSION_COOKIE_NAME)
        session = session_engine.SessionStore(session_key)
        try:
            self.user_id = session["_auth_user_id"]
            self.user = User.objects.get(id=self.user_id)
        except (KeyError, User.DoesNotExist):
            self.close()
            return

        self.gt_id = gt_id
        scheduled = tornado.ioloop.PeriodicCallback(self.gtvalues, 500)
        scheduled.start()

    def on_message(self, message):
        tcigt_id = message.split('_')[-1]
        if 'get_tcigt' in message:
            print 'IM GOINT TO {0} WITH ID IS {1}'.format('get', tcigt_id)
        if 'bugreport_tcigt' in message:
            print 'IM GOINT TO {0} WITH ID IS {1}'.format('bugreport', tcigt_id)
        if 'pass_tcigt' in message:
            tcigt = TestCaseInGT.objects.get(id=tcigt_id)
            pass_tcigt(tcigt, self.user)
            self.write_message(json.dumps({'tcigt_status{0}'.format(tcigt.id): 'passed'}))
            print 'IM GOINT TO {0} WITH ID IS {1}'.format('pass', tcigt_id)
        if 'set_tcigt' in message:
            print 'IM GOINT TO {0} WITH ID IS {1}'.format('set', tcigt_id)

    def on_close(self):
        print 'connection closed'

    def gtvalues(self):
        gt = GlobalTesting.objects.get(id=self.gt_id)
        gtvalues_dict = GTValues(gt).as_dict()
        self.write_message(json.dumps(gtvalues_dict))


wsgi_app = tornado.wsgi.WSGIContainer(django.core.handlers.wsgi.WSGIHandler())
application = tornado.web.Application([
    (r'/get_gtvalues/(?P<gt_id>\d+)/', GTHandler),
    (r'/pass_case_in_gt/(?P<tcigt_id>\d+)/', GTHandler),
    ('.*', tornado.web.FallbackHandler, dict(fallback=wsgi_app)),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)

    main_loop = tornado.ioloop.IOLoop.instance()
    main_loop.start()
