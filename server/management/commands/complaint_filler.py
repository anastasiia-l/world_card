from server.models import Complaint
import requests
from bs4 import BeautifulSoup
from django.core.management.base import BaseCommand


class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        for i in range(1, 217):

            url = 'https://www.eurolab.ua/symptoms/' + str(i) + '/'
            html_page = requests.get(url)

            soup = BeautifulSoup(html_page.text.encode("utf-8"))
            symptom_div = soup.findAll('div',
                                       {'class': 'symptom-desc symptom-desc_light'})
            if symptom_div:
                diagnosis = symptom_div[0].text \
                    if len(symptom_div[0].text) < 1000 else symptom_div[0].text[0:1000]
                medic_specialty = symptom_div[len(symptom_div) - 1].text
                symptom = soup.find('h2', {'class': 'symptom-header'}).text

                complaint = Complaint.objects.create(name=symptom,
                                                     diagnosis=diagnosis,
                                                     medic_specialty=medic_specialty)
                complaint.save()
