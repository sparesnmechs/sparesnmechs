"""config URL Configuration.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))

"""
from django.conf.urls import url
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),

    # Clients
    url(r'^spare_dealer', include('snm.clients.urls', namespace='spare_dealer')
        ),
    url(r'^mechanic', include('snm.clients.urls', namespace='mechanic')),
    url(r'^car_owner', include('snm.clients.urls', namespace='car_owner')),

    # Spareparts
    url(r'^spare_part', include('snm.spareparts.urls', namespace='spare_part')
        ),
    url(r'^spare_part_category', include(
        'snm.spareparts.urls', namespace='spare_part_category')),
    url(r'^spare_part_sub_category', include(
        'snm.spareparts.urls', namespace='spare_part_sub_category')),

    url(r'^speciality', include('snm.spareparts.urls', namespace='speciality')
        ),
    url(r'^car_make', include('snm.spareparts.urls', namespace='car_make')),
    url(r'^car_model', include('snm.spareparts.urls', namespace='car_model')),
]
