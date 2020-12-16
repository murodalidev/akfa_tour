from django.urls import path
from tour.views import (
    form_view,
    success_view
)

urlpatterns = [
    path('', form_view, name='form'),

    path('success/', success_view, name='success'),
]