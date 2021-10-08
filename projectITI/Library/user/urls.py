from django.urls import path
from user.views import *

urlpatterns = [
   path('loginform/', loginform, name='loginform'),
   path('home/', home , name='home'),
   path('admin/' , admin , name='admin'),
   path("details/<int:id>/",details,name = 'details'),
   path("borrow/<int:id>/", borrow, name='borrow'),
   path("adminuser/", adminuser, name='adminuser'),
   path("viewborrow/", viewborrow, name='viewborrow'),
   path("addbook/", addbook, name='addbook'),
   path("deletebook/<int:id>/", deletebook, name='deletebook'),
   path("updatebook/<int:id>/", updatebook, name='updatebook'),
   path("searchuser/", searchuser, name='searchuser'),
   path('returnBook/<int:id>/' , returnBook , name='returnBook'),
   path('getborrowedbook' , getBorrowedBook , name='getBorrowedBook'),
   path('yourprofile', updateUserProfile, name='yourprofile'),
   path('editprofile', updateAdminProfile, name='editprofile'),

]
