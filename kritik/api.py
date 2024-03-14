from rest_framework import routers
from kritikApp import views as kritikApp_views

router = routers.DefaultRouter()
router.register(r'user', kritikApp_views.UserViewSet)
router.register(r'establishment', kritikApp_views.EstablishmentViewSet)
router.register(r'review', kritikApp_views.ReviewViewSet)