from utils.Movies import load_nodes
from django.shortcuts import render, redirect
from dal import autocomplete
from .models import Node
from .forms import UserInputForm
from bs4 import BeautifulSoup
from utils.Graph import *
from utils.Movies import *


def home(request):
    if request.method == "POST":
        print("Post request!")
        print(request.POST.get)
        form = UserInputForm(request.POST)
        print(form.errors)
        print(form.is_valid())
        form_soup = BeautifulSoup(form.__str__(), 'lxml')
        selected_soup = form_soup.find_all('option', selected=True)
        print(selected_soup)
        for soup in selected_soup:
            print(soup.text)
        nodes = [soup.text for soup in selected_soup]
        print("Redirecting!")
        union_colors_results, energy_spread_results = gen_recommendations(
            nodes)
        print(union_colors_results)
        print(energy_spread_results)
        return render(request, "cinewise/result.html",
                      {"union_colors_results": union_colors_results, "energy_spread_results": energy_spread_results})
    else:
        form = UserInputForm()
        print(form)
        return render(request, 'Cinewise/index.html', {'form': form})


class NodeAutocomplete(autocomplete.Select2QuerySetView):
    def get_queryset(self):
        qs = Node.objects.all()
        if self.q:
            qs = qs.filter(name__icontains=self.q)
        return qs
