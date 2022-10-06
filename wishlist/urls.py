from django.urls import path
from wishlist.views import show_wishlist, show_wishlist_ajax, create_wishlist_json, show_xml, show_json, show_json_by_id, register, login_user, logout_user

app_name = 'wishlist'

urlpatterns = [
    path('', show_wishlist, name='show_wishlist'),
    path('ajax/', show_wishlist_ajax, name="show_wishtlist_ajax"),
    path('ajax/submit/', create_wishlist_json, name="create_wishlist_json"),
    path('xml/', show_xml, name='show_xml'),
    path('json/', show_json, name='show_json'),
    path('json/<int:id>', show_json_by_id, name='show_json_by_id'),
    path('register/', register, name='register'),
    path('login/', login_user, name='login'),
    path('logout/', logout_user, name='logout'),
]