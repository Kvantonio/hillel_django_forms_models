from django.urls import path

from . import views

app_name = 'polls'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('triangle/', views.hypotenuse_form, name='triangle'),
    path('person/', views.auth_modelform, name='person'),
    path(
        'person/<int:id>/',
        views.output_personal_data_modelform,
        name='person_res'
        ),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('<int:pk>/results/', views.ResultsView.as_view(), name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]
