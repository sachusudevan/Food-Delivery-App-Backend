from django.conf import settings
from django.urls import path, include
from django.conf.urls import url
from django.conf.urls.static import static
from . import views
from django.contrib.auth.decorators import login_required

from apps.products.views import CategoryView

app_name = "products"

urlpatterns = [

        url(r'^categories/', include([    

            path('list', CategoryView.as_view() , name="get_categories"),

        ])),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
