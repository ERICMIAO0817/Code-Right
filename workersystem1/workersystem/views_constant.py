import hashlib
from workersystem.settings import EMAIL_HOST_USER
from django.core.mail import message, send_mail
from django.template import loader

MALE = 0
FAMALE = 1


def hax_str(source):
    return hashlib.new('sha512', source.encode('utf-8')).hexdigest()


def send_email(username, recive, token):
    subject = '你好,%s' % username
    message = 'Hello'
    recipient_list = [recive]
    data = {
        'username': username,
        'active_url': 'http://localhost:8000/user/active/?u_token={}'.format(token)
    }
    html_message = loader.get_template('active.html').render(data)
    send_mail(subject=subject, message=message, from_email=EMAIL_HOST_USER, recipient_list=recipient_list,
              html_message=html_message)


def get_join(join1, join2, join3, join4):
    return (join1 + join2 + join3 + join4) / 4


def get_conclude(A, B, C):
    return A / (A + B + C)
