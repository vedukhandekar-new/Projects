from django.contrib import admin

# Register your models here.



from .models import User, Item, Match, Message, Review

admin.site.register(User)
admin.site.register(Item)
admin.site.register(Match)
admin.site.register(Message)
admin.site.register(Review)
