import os
import time
import requests
from dotenv import load_dotenv
from django.conf import settings
from celery import shared_task

load_dotenv()


@shared_task
def send_telegram_notification(payment_id, quantity, student_username, phone_number):
    time.sleep(5)
    token = settings.TELEGRAM_BOT_TOKEN
    method = 'sendMessage'
    message_text = f"New Order: {payment_id}\n Amount: {quantity}\n" \
                   f"Student: {student_username}\n tel: {phone_number}"

    response = requests.post(
        url=f'https://api.telegram.org/bot{token}/{method}',
        data={'chat_id': os.getenv('CHAT_ID', ''), 'text': message_text}
    ).json()
