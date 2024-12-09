from.views import *
from django.urls import path
from django.contrib.sitemaps.views import sitemap
from .sitemaps import ItemSitemap 
from .views import *

sitemaps={
    'item':ItemSitemap,
}

urlpatterns = [
    path('',ListBlog,name="list"),
    path('blog/<id>',DetailBlog,name="detail"),
    path('sitemap.xml',sitemap,{'sitemaps':sitemaps}),
    path('upload-csv/', UploadCSV.as_view(), name='upload-csv'),
     path('BulkUploadPerson',BulkUploadPerson.as_view(), name='BulkUploadPerson')
]
