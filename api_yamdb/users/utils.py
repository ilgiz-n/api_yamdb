import random
import string

from django.core.mail import send_mail

from users.models import CONFIRMATION_CODE_LENGTH


def send_mail_with_code(email, confirmation_code):
    send_mail(
        subject='Confirmation code for Yamdb',
        message=f'Confirmation code: {confirmation_code}',
        from_email='from@example.com',
        recipient_list=[email],
        fail_silently=False,
    )


def generate_confirmation_code():
    return ''.join(
        random.choices(
            string.digits,
            k=CONFIRMATION_CODE_LENGTH
        )
    )
