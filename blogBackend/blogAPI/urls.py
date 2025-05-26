from django.urls import path
from .views import SignupView, LoginView, LogoutView, BlogCreateView, BlogListView, BlogDetailView, BlogUpdateDeleteView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', SignupView.as_view()),
    path('login/', LoginView.as_view(), name='token_obtain_pair'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('blogs/', BlogListView.as_view()),
    path('blogs/create/', BlogCreateView.as_view()),
    path('blogs/<int:id>/', BlogDetailView.as_view()),
    path('blogs/<int:id>/edit/', BlogUpdateDeleteView.as_view()),
]
