# Uncomment the imports before you add the code
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'djangoapp'
urlpatterns = [
    path(route='login', view=views.login_user, name='login'),
    path(route='logout', view=views.logout_request, name='logout'),
    path(route='registration', view=views.registration, name='registration'),
    path('get_cars', views.get_cars, name='get_cars'),
    path('get_dealers', views.get_dealerships, name='get_dealers'),
    path('get_dealers/<str:state>', views.get_dealerships,
         name='get_dealers_by_state'),
    path('dealer/<int:dealer_id>', views.get_dealer_details,
         name='dealer_details'),
    path('reviews/<int:dealer_id>', views.get_dealer_reviews,
         name='dealer_reviews'),
    path('add_review', views.add_review, name='add_review'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
