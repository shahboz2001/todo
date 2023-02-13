from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', hamma_todo),
    path('kundalik_edit/<int:son>/', kundalik_edit),
    path('kundalik_ochir/<int:son>/', kundalik_ochir),
]
