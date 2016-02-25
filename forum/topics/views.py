import datetime
import logging

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.mail import send_mail
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic.list import ListView
from django.contrib.messages import info

from .forms import MessageFormset
from .forms import TopicForm, MessageForm, MessageEditForm
from .models import Topic, Moder, Message
from django.dispatch import Signal, receiver


my_signal = Signal(providing_args=['x'])
logger = logging.getLogger(__name__)

@receiver(my_signal)
def f(sender, **kwargs):
    print ("AAA", kwargs['x'])


@receiver(my_signal)
def g(sender, **kwargs):
    print("BBB", kwargs['x'])


@login_required
def index(request):
    my_signal.send("A", x='123')
    logger.info("My message")
    send_mail('AAA', 'MMMM', 'a@a.org', ['b@b.org'])
    return render(request, "index.html", {
        'topics': Topic.objects.all(),
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
            info(request, "Topic successfully added")
            return redirect('/topics/index')
    else:
        add_form = TopicForm()
    return render(request, 'add.html', {
        'add_form': add_form,
    })


def detail(request, id):
    topic = get_object_or_404(Topic, id=int(id))
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            message = form.save(commit=False)
            message.author = User.objects.get(id=1)
            message.topic = topic
            message.save()
            return redirect('/topics/index')
    else:
        form = MessageForm()
    return render(request, 'detail.html', {
        'topic': topic,
        'form': form
    })

def edit(request, id):
    message = Message.objects.get(id=int(id))
    if request.method == 'POST':
        form = MessageEditForm(request.POST, instance=message)
        form.save()
    else:
        form = MessageEditForm(instance=message)
    return render(request, 'edit.html', {
        'form': form,
    })


class DateMixin:
    def get_date(self):
        return datetime.datetime.today()


class IndexView(DateMixin, ListView):
    permission_required = 'topics.add_topic'
    template_name = 'index.html'
    model = Topic
    paginate_by = 1

