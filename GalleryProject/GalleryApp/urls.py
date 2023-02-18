from django.urls import path
from . import views


urlpatterns = [
    path('' , views.home_view , name = 'home' ),
    path('register/' , views.register_view , name = 'register' ),
    path('signout/' , views.signout_view , name = 'signout' ),
    path('gallery/' , views.gallery_view , name = 'gallery' ),
    path('addimage/' , views.addimage_view , name = 'addimage' ),
    path('category/<int:id>/' , views.category_view , name = 'category' ),

]