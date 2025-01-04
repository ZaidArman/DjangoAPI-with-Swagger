from django.urls import path
from . import views

# Define the URL patterns for the Titanic app
urlpatterns = [
    # List and Create views
    path('passengers/', views.PassengerListCreateView.as_view(), name='passenger-list-create'),
    path('passengers/<int:pk>/', views.PassengerDetailView.as_view(), name='passenger-detail'),
    
    # Filtered views
    path('passengers/survived/', views.SurvivedPassengersView.as_view(), name='survived-passengers'),
    path('passengers/by-class/<int:pclass>/', views.PassengersByClassView.as_view(), name='passengers-by-class'),
    path('passengers/by-gender/<str:gender>/', views.PassengersByGenderView.as_view(), name='passengers-by-gender'),
    path('passengers/expensive-tickets/', views.ExpensiveTicketsView.as_view(), name='expensive-tickets'),
    path('passengers/family-travelers/', views.FamilyTravelersView.as_view(), name='family-travelers'),
]