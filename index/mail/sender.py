from threading import Thread as __th


class Sandman(__th):
    from django.template.loader import get_template as __gt
    from django.template import Context as __ctx

    def __init__(self, **kwargs):
        from index import settings
        from django.core.mail import EmailMessage

        self.flat = kwargs.get('flat', False)
        self.template = kwargs.get('template')
        self.context = kwargs.get('context', {})
        self.body = kwargs.get('body', 'Mail from %s' % settings.DEFAULT_NAME)
        self.headers = kwargs.get('headers', {})

        mail_to = kwargs.get('mail_to', settings.EMAIL_HOST_USER)
        self.message = EmailMessage(
            from_email=kwargs.get('mail_from', settings.EMAIL_ADDRESSES.get('main')),
            to=mail_to if 'str' != type(mail_to).__name__ else (mail_to,),
            subject=kwargs.get('subject', 'Mail from %s' % settings.DEFAULT_NAME),
            headers=self.headers,

            cc=kwargs.get('cc'),
            bcc=kwargs.get('bcc'),
            reply_to=kwargs.get('reply_to'),
            connection=kwargs.get('connection'),
            attachments=kwargs.get('attachments'),
        )

        if self.flat or not self.template:
            self.headers['Content'] = 'text/plain'
            self.message.content_subtype = 'plain'
            self.message.body = kwargs.get('body', 'Mail from %s' % settings.DEFAULT_NAME)

        super().__init__()

    def __call__(self, fail_silently=False):
        if not self.flat and bool(self.template):
            self.headers['Content'] = 'text/html'
            self.context['body'] = self.body
            self.message.content_subtype = 'html'

            context = self.__ctx(self.context)
            template = self.__gt('mail/%s.html' % self.template)

            self.message.body = template.render(context)

        self.message.extra_headers = self.headers
        self.message.send(fail_silently)

    def run(self):
        self()
