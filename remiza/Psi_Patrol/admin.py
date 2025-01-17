from django.contrib import admin
from.models import Firefighter
from.models import Firetruck
from.models import Squad
from.models import FirefighterInSquad

# Register your models here.

admin.site.register(Firefighter)
admin.site.register(Firetruck)
admin.site.register(Squad)
admin.site.register(FirefighterInSquad)