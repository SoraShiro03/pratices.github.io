from django.urls.conf import path
from . import views

urlpatterns = [
   path('', views.list_view, name='list'),
   path('<int:year>/<int:month>/<int:day>/<slug:anime_list>/', views.list_detail, name='list_detail'),
   path('tag/<slug:tag_slug>', views.list_view, name='list_by_tag'),
]
