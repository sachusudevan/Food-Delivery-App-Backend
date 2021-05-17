
from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from . import settings
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


schema_view = get_schema_view(
    openapi.Info(
        title="Online Food Delivery API",
        default_version='v1',
        description="An api for Online Food Delivery Application",
        terms_of_service="",
        contact=openapi.Contact(email=""),
        license=openapi.License(name="Online Food Delivery License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)




urlpatterns = [
    path('admin/', admin.site.urls),

    # url('categorieslist', CategoryView.as_view()),

    url(r'^api/', include([

        url(r'^docs/', include([

            path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
            path("redoc", schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

        ])),
        url(r'^auth/', include([

            path('', include('apps.authentication.urls')),

        ])),
        

        url(r'^products/', include([

            url('', include('apps.products.urls')),

        ])),



        
    ])),

    
  
    
]



urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
