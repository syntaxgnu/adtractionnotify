import logging
from pushbullet import Pushbullet

API_KEY = '<API_KEY>'

class Notificator():
    def __init__(self):
        self.pb = Pushbullet(API_KEY)
        self.logging = logging.getLogger('Notificator')
        self.logging.setLevel(level=logging.DEBUG)

    def send_notification(self, title, body):
        ret_data = self.pb.push_note(title, body)
        self.logging.debug('API return data: ' +str(ret_data))
