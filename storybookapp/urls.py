from django.urls import path
from . import views

app_name = 'storybookapp'

urlpatterns = [
    path('', views.story_list,name="story_list"),
    path('/<slug:category_slug>', views.story_list,name="story_category"),
    path('<int:id>/', views.story_detail,name="story_detail"),  
    path('search/', views.search_story,name="story_search")
] 