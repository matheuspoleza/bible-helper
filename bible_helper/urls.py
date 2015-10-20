from django.conf.urls import include, url
from django.contrib import admin
from rest_framework import routers
from bible import views as bible_views
from theme import views as theme_views

router = routers.DefaultRouter()
router.register(r'verses', bible_views.VerseViewSet)
router.register(r'themes', theme_views.ThemeViewSet)
router.register(r'books', bible_views.BookViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^admin/', include(admin.site.urls)),
]