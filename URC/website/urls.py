from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='index'),
    path('team/', views.team, name='team'),
    path('blog/', views.blog, name='blog'),
    path('blog/<int:blog_id>', views.blog_details, name='detailed-blog'),
    path('contact/', views.contact, name='contact'),
    path('gallery/', views.gallery, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)