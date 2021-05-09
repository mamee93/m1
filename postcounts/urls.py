from django.urls import path
from .views import countList,InsertCount,CoustomLoginView,RegisterPage
from django.contrib.auth.views import LogoutView

urlpatterns = [
   path('login', CoustomLoginView.as_view(), name='login'),
   path('register', RegisterPage.as_view(), name='register'),
   path('logout', LogoutView.as_view(next_page="login"), name='logout'),
   path('', countList.as_view(), name='count-List'),
   path('insert-Count/', InsertCount.as_view(), name='Insert-Count'),
]