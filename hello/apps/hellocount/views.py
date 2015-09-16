from django.shortcuts import render
from hellocount.models import Visit

def say_hello(request):
    user_agent = request.META['HTTP_USER_AGENT']
    Visit.objects.create(user_agent=user_agent)
    return render(request, 'say_hello.html', {
        'count': Visit.objects.count(),
        'user_agent': user_agent
    })
