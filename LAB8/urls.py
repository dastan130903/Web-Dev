from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse
from django.shortcuts import redirect



def redirect_to_api(request):

    return redirect('/api/')

urlpatterns = [
    path('', redirect_to_api),    # или path('', home_view),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
]
