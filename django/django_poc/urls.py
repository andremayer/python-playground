from django.contrib import admin
from django.urls import path
from myapp.views import index, detail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('item/<int:item_id>/', detail),
]
