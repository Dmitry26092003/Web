from django.shortcuts import render


# Create your views here.

def index(request):
    return render(request, 'home\\homePage.html', {'PageName': ['Главная страница']})


def contact(request):
    return render(request, 'home\\basic.html',
                  {'values': ['<h2>Создатели ПО/Игр:</h2>',
                              '<h4>Балахонский Дмитрий</h4>',
                              '<h6>Тел: </h6><p>8(937)445-59-70</p>',
                              '<h6>Email: </h6><a href="mailto:Bal.Dima2003@yandex.ru"><p>Bal.Dima2003@yandex.ru</p></a>',
                              '<h6>VK: </h6><a href="https://vk.com/id174417882"><p>https://vk.com/id174417882</p></a>',
                              '<h4>Космынин Даниил</h4>',
                              '<h6>Тел: </h6><p>8(937)915-25-08</p>',
                              '<h2>Наша группа в вк:</h2>',
                              '<a href="https://vk.com/pythongame"><p>https://vk.com/pythongame</p></a>'],
                   'PageName': ['Контакты']})
# можно 55