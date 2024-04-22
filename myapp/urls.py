from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
urlpatterns = [
    path('',views.home,name="home-page"),
    path('articles/',views.main,name="articles-list"),
    path('articles/create/',views.create_article,name="create-article"),
    path('articles/<int:id>/',views.article_detail,name="article-detail"),

] 
