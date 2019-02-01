from threading import Thread as __th


class Sandman(__th):
    def __init__(self, **kwargs):
        from index import settings
        from django.core.mail import EmailMessage

        self.flat = kwargs.get('flat', False)
        self.template = kwargs.get('template', 'default')
        self.object = kwargs.get('object', object())

        mail_to = kwargs.get('mail_to', settings.EMAIL_HOST_USER)
        self.message = EmailMessage(
            from_email=kwargs.get('from_email', settings.EMAIL_HOST_USER),
            to=mail_to if 'str' != type(mail_to).__name__ else (mail_to,),
            subject=kwargs.get('subject', 'Mail from %s' % settings.DEFAULT_NAME),
            headers=kwargs.get('headers', {}),

            cc=kwargs.get('cc'),
            bcc=kwargs.get('bcc'),
            reply_to=kwargs.get('reply_to'),
            connection=kwargs.get('connection'),
            attachments=kwargs.get('attachments'),
        )

        if self.flat:
            self.message.body = kwargs.get('body', 'Mail from %s' % settings.DEFAULT_NAME)
        else:
            self.message.body = "a"

        super().__init__()

    def __call__(self, fail_silently=False):
        self.message.send(fail_silently)

    def run(self):
        self()
