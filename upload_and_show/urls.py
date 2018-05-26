"""upload_and_show URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.views.generic import TemplateView, RedirectView

from upload import views as upload_views
from show import views as show_views
from login import views as login_views

from face_reg_test import views as face_reg_views

from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    url(r'^admin/', admin.site.urls),
	url(r'show/',show_views.show),
	url(r'^upload/',upload_views.upload),
	url(r'^guide_upload/',upload_views.guide_upload),
	url(r'^get_next/',show_views.get_next, name="get_next"),
   # url(r'^get_all/',Set_views.get_all, name="get_all"),
    #url(r'^submit_set/',Set_views.submit_set, name="submit_set"),
	url(r'^error_answer/',show_views.error_answer,name="error_answer"),
	#url(r'^makeSet/',Set_views.makeSet),
	url(r'^register/',login_views.nregister),
	url(r'^face_reg_test/',face_reg_views.index,name="face_reg_index"),
	url(r'^upload_snap_test/',face_reg_views.upload_snap,name="upload_snap_test"),
	url(r'^get_feeling_test/',face_reg_views.get_feeling,name="get_feeling_test"),
	url(r'^upload_snap/',show_views.upload_snap,name="upload_snap"),
	url(r'^get_feeling/',show_views.get_feeling,name="get_feeling"),
	url(r'^index/', TemplateView.as_view(template_name='index.html'), name='index'),

] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
