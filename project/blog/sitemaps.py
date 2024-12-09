from django.contrib.sitemaps import Sitemap
from .models import Item

class ItemSitemap(Sitemap):
    def items(self):
        return Item.objects.all()
    def lastmod(self, obj): 
        return obj.lastedit_date