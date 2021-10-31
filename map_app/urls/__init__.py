from django.urls import path, include

app_name = 'map_app'
urlpatterns = [
    path('customer/', include('map_app.urls.api_urls')),
]