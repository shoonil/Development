from django import urls
from django.urls import path, include
from .views import MembershipViewSet
from rest_framework.routers import DefaultRouter
from . import views

router=DefaultRouter()
router.register('members', MembershipViewSet, basename='members')

urlpatterns = [
    # path('', include(router.urls)),
    path('',views.index, name='index'),
    # path('members/', MembershipList.as_view()),
    # path('members/<int:id>/', MembershipDetails.as_view())
    # path('members/', members_list),
    # path('members/<int:pk>/', members_details),

]
