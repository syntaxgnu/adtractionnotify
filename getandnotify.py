import logging
import notificator
import provisiongetter

class GetAndNotify():
    def __init__(self):
        self.notif = notificator.Notificator()
        logging.basicConfig(format=' %(asctime)s - %(levelname)s - %(message)s')
        self.logging = logging.getLogger('GetAndNotify')
        self.logging.setLevel(level=logging.DEBUG)


    def get_and_notify(self):
        ''' Get provision and send notification with pushbullet '''
        with provisiongetter.ProvisionGetter() as pg:
            provision = pg.get_provision()
            if provision != '0.00':
                self.logging.debug('Sending provision notification')
                self.notif.send_notification('Provision yesterday', 'Yesterday\'s provision was ' + str(provision))

if __name__ == '__main__':
    gan = GetAndNotify()
    gan.get_and_notify()