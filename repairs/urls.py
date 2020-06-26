''' repairs URL Configuration '''

from django.contrib import admin
from django.conf import settings
from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', LogoutView.as_view(), {'next_page': '/login/'}),
]
urlpatterns += [
    path('', include('reports.urls'))
]
urlpatterns += [
    path('sticker/', include('sticker.urls'))
]
if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
    path('__debug__/', include(debug_toolbar.urls)),
]