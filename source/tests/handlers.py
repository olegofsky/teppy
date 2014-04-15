import tornado.httpserver
import tornado.ioloop
import tornado.web
import tornado.websocket

import json

# from django.contrib.auth.models import User
from source.tests.models import GlobalTesting
from source.tests.classes import GTValues

class GTValuesHandler(tornado.websocket.WebSocketHandler):

    def open(self, gt_id):
        self.gt_id = gt_id
        scheduled = tornado.ioloop.PeriodicCallback(self.gtvalues, 500)
        scheduled.start()

    def on_message(self, message):
        print 'message recieved {0}'.format(message)

    def on_close(self):
        print 'connection closed'

    def gtvalues(self):
        gt = GlobalTesting.objects.get(id=self.gt_id)
        gtvalues_dict = GTValues(gt).as_dict()
        self.write_message(json.dumps(gtvalues_dict))

application = tornado.web.Application([
    (r'/get_gtvalues/(?P<gt_id>\d+)/', GTValuesHandler),
])

if __name__ == '__main__':
    http_server = tornado.httpserver.HTTPServer(application)
    http_server.listen(8888)

    main_loop = tornado.ioloop.IOLoop.instance()
    main_loop.start()
