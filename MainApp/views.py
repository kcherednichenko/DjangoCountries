import json

from django.core.paginator import Paginator
from django.http import HttpResponseNotFound
from django.shortcuts import render


def home(request):
    return render(request, 'index.html')


def countries_list(request):
    context = {
        'alph': list("ABCDEFGHIJKLMNOPQRSTUVWXWY")
    }

    with open('country-by-languages2.json', 'r') as countries:
        data = json.load(countries)

        paginator = Paginator(data['countries'].copy(), 10)
        page_number = request.GET.get("page")
        page_obj = paginator.get_page(page_number)
        context["page_obj"] = page_obj

        return render(request, 'countries-list.html', context)


def country_page(request, country_id):

    with open('country-by-languages2.json', 'r') as countries:
        data = json.load(countries)
        for country in data['countries']:
            if country['id'] == country_id:
                return render(request, 'country-page.html', country)

    return HttpResponseNotFound(f"<text>Country with id = {country_id} not found</text>")


def countries_list_by_letters(request, first_letter):
    context = {
        'countries': [],
        'first_letter': first_letter.upper()
    }

    with open('country-by-languages2.json', 'r') as countries:
        data = json.load(countries)
        for country in data['countries']:
            if country['country'].upper().startswith(first_letter.upper()):
                context['countries'].append(country)

    return render(request, 'countries-list-by-letters.html', context)


def countries_list_by_languages(request, language):
    languages = dict()
    language = language.lower()

    with open('country-by-languages2.json', 'r') as countries:
        data = json.load(countries)
        for country in data['countries']:
            for language_ in country['languages']:
                languages[language_.lower()] = languages.get(language_.lower(), set()).union({country['country']})

    if language in languages.keys():
        context = {
            'countries': languages[language],
            'language': language
        }

        return render(request, 'countries-list-by-languages.html', context)

    else:
        return HttpResponseNotFound(f"<text>There is no country where people speak {language} language</text>")


def all_languages(request):
    languages = []

    with open('country-by-languages2.json', 'r') as countries:
        data = json.load(countries)
        for country in data['countries']:
            for language_ in country['languages']:
                languages.append(language_)

    paginator = Paginator(languages, 10)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    context = {"page_obj": page_obj}

    return render(request, 'all-languages.html', context)
