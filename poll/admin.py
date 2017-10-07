from django.contrib import admin
from poll.models import Poll, PollChoice


class PollAdmin(admin.ModelAdmin):
    pass


class PollChoiceAdmin(admin.ModelAdmin):
    pass


admin.site.register(Poll, PollAdmin)
admin.site.register(PollChoice, PollChoiceAdmin)
