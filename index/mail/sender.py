from threading import Thread as __th


class Sandman(__th):
    def __init__(self, **kwargs):
        from index import settings
        from django.core.mail import EmailMessage

        self.flat = kwargs.get('flat', False)

        self.template = kwargs.get('template')
        self.extension = str(kwargs.get('extension', 'html')).strip('.')
        self.using = kwargs.get('using')
        self.context = kwargs.get('context', {})

        self.body = kwargs.get('body', 'Mail from %s' % settings.DEFAULT_NAME)
        self.headers = kwargs.get('headers', {})
        self.request = kwargs.get('request')

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
            from os import sep
            from django.template import Template, loader

            self.headers['Content'] = 'text/html'
            self.context['body'] = self.body
            self.context['request'] = self.request
            self.message.content_subtype = 'html'

            compiled_name = "mail%(separator)s%(template)s.%(extension)s" % {
                'separator': sep,
                'template': self.template,
                'extension': self.extension,
            }

            template: Template = loader.get_template(
                compiled_name,
                self.using,
            )

            self.message.body = template.render(self.context)

        self.message.extra_headers = self.headers
        self.message.send(fail_silently)

    def run(self):
        self()
