from django.contrib import admin
from django.urls import path
from pdf_extraction_app.views import upload_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', upload_pdf, name='home'), 
    path('upload/', upload_pdf, name='upload_pdf'),
]
