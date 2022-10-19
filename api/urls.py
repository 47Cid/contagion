from django.urls import path

from . import views

urlpatterns = [
    path('', views.listUsers, name='list-users'),
    path('user/<int:user_id>/', views.userData, name='user-data'),
    path('add/user/', views.addUser, name='add-user'),
    path('add/travel-record/',
         views.addTravelRecord, name='add-travel-record'),
    path('add/infection-record/',
         views.addInfectionRecord, name='add-infection-record'),
    path('delete/user/<int:user_id>/', views.deleteUser, name='delete_user'),
    path('delete/travel-record/<int:travel_id>/',
         views.deleteTravelRecord, name='delete-infection-record'),
    path('delete/infection-record/<int:infection_id>/', views.deleteInfectionRecord,
         name='delete-infection-record'),
]
