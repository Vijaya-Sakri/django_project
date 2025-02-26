"""SponsorsMedia URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('companies/', views.companies),
    path('company_details/',views.company_details),
    path('college_details/',views.college_details),
    path('colleges/',views.colleges),
    path('home/profile/college_event_details/<int:id>/',views.college_event_details),
    path('colleges/college_events/<int:id>/',views.college_events),
    path('colleges/college_events/<int:id>/',views.college_events),
    path('colleges/college_events/<int:id>/edit/<int:name>',views.edit_event_details),
    path('home/profile/college_events/<int:id>/',views.college_events),
    path('home/profile/college_events/<int:id>/edit/<int:name>/',views.edit_event_details),
    # path('colleges/college_events/<int:id>',views.college_events),
    # path('edit_college_details/<int:id>',views.edit_college_details),
    path('login/', views.login_user),
    path('signup/', views.signup),
    path('home/profile/<int:id>', views.profile),
    path('profile/logout', views.logout_user),
    path('logout/', views.logout_user),
    path('profile/<int:id>/', views.profile)
  
]
admin.site.index_title="Sponsors Media"
admin.site.site_header="Sponsors Media Admin"
admin.site.site_title = "Site title Sponsors Media"

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
