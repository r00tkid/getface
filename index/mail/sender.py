from django.core.mail import EmailMessage
from index import settings


def send_mail(message, to, **kwargs):
    print(">>>> Start sending <<<<")
    return EmailMessage(
        subject="Ti pidor",
        body=message,
        from_email=settings.EMAIL_HOST_USER,
        to=to,
        headers=kwargs,
    )
