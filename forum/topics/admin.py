from django.contrib import admin
from .models import Topic, Message, Moder


class MessageInline(admin.StackedInline):
    model = Message
    extra = 2

class TopicAdmin(admin.ModelAdmin):
    list_display = ('name', 'date', 'state')
    inlines = [MessageInline, ]

admin.site.register(Topic, TopicAdmin)
admin.site.register(Message)
admin.site.register(Moder)

