from django.conf.urls import include
from django.urls import path, re_path
from rest_framework.routers import DefaultRouter
from ramailo.views.company import CompanyDetailView, CompanyView

from ramailo.views import health

class OptionalSlashRouter(DefaultRouter):
    def __init__(self):
        super(DefaultRouter, self).__init__()
        self.trailing_slash = "/?"


router = OptionalSlashRouter()

utils_paths = [
    re_path('^', include(router.urls)),
    path('health/', health, name='health'),
]

api_paths = [
    path('companies/', CompanyView.as_view(), name='company'),
    path('companies/<uuid:company_id>', CompanyDetailView.as_view(), name='company_details'),
    path('user/:id/profile', UserProfileApi, name='user_profile'),
    path('user/me', UserMyProfileApi, name='user_profile'),
    path('user/:id/account', UserAccountApi, name='user_profile'),
]

urlpatterns = utils_paths + api_paths
