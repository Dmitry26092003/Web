from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home\\homePage.html', {'PageName': ['Главная страница']})


def contact(request):
    return render(request, 'home\\basic.html',
                  {'values': ['Создатели:',
                              'Балахонский Дмитрий',
                              'Тел: 8(937)445-59-70',
                              'Email: Bal.Dima2003@yandex.ru',
                              'VK: https://vk.com/id174417882',
                              'Космынин Даниил',
                              'Тел: 8(937)915-25-08',
                              'Наша группа в вк:',
                              'https://vk.com/pythongame'],
                   'PageName': ['Контакты']})
