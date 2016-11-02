# from django.shortcuts import render

from django.views.generic import TemplateView

import requests

from bs4 import BeautifulSoup

# Create your views here.


class PlayerView(TemplateView):
    template_name = "player.html"

    def get_context_data(self, player_url):
        context = super().get_context_data()
        page = requests.get("http://nfl.com/" + player_url)
        souper = BeautifulSoup(page.text, "html.parser")
        context["table"] = souper.find("table").contents
        return context


class IndexView(TemplateView):
    template_name = "index.html"

    def get_context_data(self):
        context = super().get_context_data()
        if self.request.GET:
            base_url = "http://www.nfl.com/players/search?category=name&filter={}&playerType=historical"
            data = requests.get(base_url.format(self.request.GET.get("player_name")))
            souper = BeautifulSoup(data.text, "html.parser")
            table = souper.find_all("table")[2]

            mysoup = table.find_all("a")

            print(mysoup)
            print("You pressed the button...")

            test_var = [(item.get("href"), item.get_text()) for item in mysoup]

            print("testbreak")
            print(test_var)
            context["test_var"] = test_var
        return context
