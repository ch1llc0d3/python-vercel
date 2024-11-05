from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseRedirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('blog/', include('blog.urls')),
    path("", lambda request: HttpResponseRedirect("blog/")),  # Redirect root URL to /blog/
]
