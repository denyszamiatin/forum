from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.http.response import HttpResponse, Http404
from django.shortcuts import render, redirect

from .forms import TopicForm
from .models import Topic, Moder


def index(request):
    return render(request, "index.html", {
        'topics': Topic.objects.all()
    })


def add(request):
    if request.method == 'POST':
        add_form = TopicForm(request.POST)
        if add_form.is_valid():
            user = User.objects.get(id=1)
            moder = Moder.objects.get(id=1)
            Topic.objects.create(
                name=request.POST['name'],
                author=user,
                moder=moder
            )
            return redirect('/topics/index')
    else:
        add_form = TopicForm()
    return render(request, 'add.html', {
        'add_form': add_form,
    })

def detail(request, id):
    try:
        return render(request, 'detail.html', {
            'topic': Topic.objects.get(id=int(id))
        })
    except ObjectDoesNotExist:
        raise Http404