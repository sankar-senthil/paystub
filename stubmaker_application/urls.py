from django.conf.urls import url
from stubmaker_application import views

urlpatterns = [
    url(r'home',views.Stub().home,name = "Home"),
    url(r'Preview',views.Stub().preview,name = "Preview"),
    ]
