from django.contrib import admin
from django.urls import path
from surprise import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # 🔐 ROOT = LOGIN
    path('', views.login_view, name='login'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout_view, name='logout'),

    # 💗 SURPRISE FLOW
    path('home/', views.home, name='home'),
    path('birthday/', views.birthday, name='birthday'),
    path('ready/', views.ready, name='ready'),
    path('message/', views.message, name='message'),
    path('gallery/', views.gallery, name='gallery'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
