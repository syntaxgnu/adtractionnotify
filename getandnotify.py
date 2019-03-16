''' Get provision and notify user '''
import configparser
import logging
import notificator
import provisiongetter

class GetAndNotify():
    ''' The class that ties provisiongetter and notificator together '''
    def __init__(self):
        ''' Initialize the Notificator '''

        config = configparser.ConfigParser()
        config.read('adtractionnotify.cfg')
        API_KEY = config['Notifier']['api_key']
        self.USERNAME = config['Notifier']['username']
        self.PASSWORD = config['Notifier']['password']

        self.notif = notificator.Notificator(API_KEY)
        logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')
        self.logging = logging.getLogger('GetAndNotify')
        self.logging.setLevel(level=logging.DEBUG)


    def get_and_notify(self):
        ''' Get provision and send notification with pushbullet '''
        with provisiongetter.ProvisionGetter(self.USERNAME, self.PASSWORD) as provision_getter:
            provision = provision_getter.get_provision()
            if provision != '0.00':
                self.logging.debug('Sending provision notification')
                self.notif.send_notification('Provision yesterday',
                                             'Yesterday\'s provision was ' + str(provision))

if __name__ == '__main__':
    GAN = GetAndNotify()
    GAN.get_and_notify()
