from django.urls import path

from . import views


app_name = 'conversation'
urlpatterns = [
    path('', view=views.inbox, name='inbox'),
    path('<int:pk>/conversation/', view=views.detail, name='detail'),
    path('new/<int:item_pk>/', view=views.new_conversation, name='new')
]

