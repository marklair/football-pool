from django.contrib import admin
from .models import Season
from .models import Week
from .models import Team
from .models import Game
from .models import Pick

admin.site.register(Season)
admin.site.register(Week)
admin.site.register(Team)
admin.site.register(Game)
admin.site.register(Pick)