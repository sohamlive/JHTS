from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include('blog.urls')),
    url(r'^gallery/', inclue('gallery.urls'))
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', {'next_page': '/'}),
    url(r'^ckeditor/', include('ckeditor.urls')),
    url(r'^', include('pages.urls')),
)+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
