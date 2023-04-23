from django.urls import path
from . import views

urlpatterns = [
        path("" ,views.Tax_page , name = "Tax_page" ),
        path("<int:price>",views.calculate_price , name = 'total_price'),
        path("taxrate" , views.Tax_value , name = 'Tax_value' )

    ]