# from django.core.mail import send_mail
import threading

from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.timezone import now

from Library_.settings import EMAIL_HOST_USER
from users.models import Token
from .service.utils import gen_unique_cod


class SendEmailAsync(threading.Thread):

    def __init__(self, sender=None,
                 receiver=None, subject=None,
                 body=None, message_type=None,
                 template_name=None):
        super(SendEmailAsync, self).__init__()
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.body = body
        self.message_type = message_type
        self.template_name = template_name

    def run(self) -> None:
        email = EmailMessage(
            subject=self.subject,
            from_email=self.sender,
            body=self.body,
            to=self.receiver
        )
        email.send()


class SendHtmlMessageAsync(threading.Thread):
    def __init__(self, sender=None, receiver=None, subject=None, html_content=None):
        super(SendHtmlMessageAsync, self).__init__()
        self.sender = sender
        self.receiver = receiver
        self.subject = subject
        self.html_content = html_content

    def run(self) -> None:
        email = EmailMessage(
            subject=self.subject,
            from_email=self.sender,
            body=self.html_content,
            to=self.receiver
        )
        email.content_subtype = "html"
        email.send()


def send_html_email_async(sender=None, receiver=None, subject=None, context=None, template_name=None):
    sender = EMAIL_HOST_USER
    html_data = render_to_string(template_name, context=context)
    email = SendHtmlMessageAsync(sender=sender, receiver=receiver, subject=subject, html_content=html_data)
    email.start()


def send_activation_link(user):
    token = gen_unique_cod()
    send_html_email_async(receiver=[user.email],
                          subject='Activation link',
                          template_name='mails/verification.html',
                          context={'token': token})
    Token(user=user, token=token, send_time=now()).save()

