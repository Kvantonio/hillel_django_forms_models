from bs4 import BeautifulSoup as bs

from celery import shared_task

from django.core.mail import send_mail

import requests

from .models import Creator, Quote


@shared_task
def scrap():
    rec = requests.get('https://quotes.toscrape.com')
    j = 0
    while j < 5:

        soup = bs(rec.content, features="html.parser")
        data = soup.findAll('div', {"class": "quote"})

        for i in data:
            quote = i.find('span', {"class": "text"}).text
            author = i.find('small', {"class": "author"}).text

            if not Quote.objects.filter(quote=quote):
                # проверяем нет ли такого автора в базе
                au, temp = Creator.objects.get_or_create(name=author)
                Quote.objects.create(quote=quote, creator=au)
                j += 1

            if j >= 5:
                break
        # ищем сслку на след. страницу
        find_link = soup.find('li', {'class': 'next'})
        if not find_link:
            # проверяем что это последняя цитата
            last_quote = data[-1].find('span', {"class": "text"}).text
            if Quote.objects.filter(quote=last_quote):
                send_mail(
                    'All quotes add in DB',
                    'All done',
                    'email@ex.com',
                    ['email_admin@ex.com'],
                )
                break
            break

        link = find_link.a.get('href')  # если нашли ссылку то берем ее
        rec = requests.get('https://quotes.toscrape.com' + link)
