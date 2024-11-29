from django.contrib.syndication.views import Feed
from django.urls import reverse
from blog.models import MyPost


class LatestEntriesFeed(Feed):
    title = "Blog newest post"
    link = "/rss/feed"
    description = "Updated blogs in different categories"

    def items(self):
        return MyPost.objects.filter(status=True)

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.content[:120]