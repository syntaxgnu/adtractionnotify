''' Simple pushbullet notificator'''
import logging
from pushbullet import Pushbullet

class Notificator():
    ''' The class that handles the pushing '''
    def __init__(self, api_key):
        ''' Initialize pushbullet '''
        self.pushbullet = Pushbullet(api_key)
        self.logging = logging.getLogger('Notificator')
        self.logging.setLevel(level=logging.DEBUG)

    def send_notification(self, title, body):
        ''' Send notification with given title & body '''
        ret_data = self.pushbullet.push_note(title, body)
        self.logging.debug('API return data: %s', str(ret_data))
