
from django.contrib import admin
from django.urls import include, path
from django.urls import path,include
from django.contrbi.staticfils.urlis import staticfiles_urlpaterns

urlpatterns = [
    path('', include('members.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns = [
    path('', include('members.urls')),
    path ('admin/',admin.site.url),
]


urlpatterns += staticfiles_urlpaterns()


urlpatterns =[
    path('',includ('members.urls')),
]
