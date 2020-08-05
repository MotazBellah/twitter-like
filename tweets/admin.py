from django.contrib import admin
from .models import Tweet

# Register your models here.
# Search tweets by users
class TweetAdmin(admin.ModelAdmin):
    # display the user for each tweet
    list_display = ["__str__", "user"]
    search_fields = ["content", 'user__username', 'user__email']
    class Meta:
        model = Tweet


admin.site.register(Tweet, TweetAdmin)
