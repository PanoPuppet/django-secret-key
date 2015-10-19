""" Return a secret key for Django

SECURITY WARNING: keep the secret key used in production secret!
https://gist.github.com/ndarville/3452907
Make this unique, and don't share it with anybody.
"""

class DjangoSecretKey(object):

    def __init__(self, secret_file):
        try:
            self.secret_key = open(secret_file).read().strip()

            if len(self.secret_key) == 0:
                raise IOError
        except IOError:
            try:
                import random

                self.secret_key = ''.join([random.SystemRandom().choice('abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)') for i in range(50)])

                secret = open(secret_file, 'w')
                secret.write(self.secret_key)
                secret.close()
            except IOError:
                Exception('Please create a {0} file with random characters to generate your secret key!'.format(secret_file))

    def __str__(self):
        return self.secret_key

