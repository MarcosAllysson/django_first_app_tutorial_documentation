from django.urls import path
from . import views

# In case we have other apps on this django's project, we named this url routing
# And on the templates, we can point to it by: app_name:name_of_view
app_name = 'polls'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]

