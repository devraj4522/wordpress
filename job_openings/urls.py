from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


app_name = 'job_openings'


urlpatterns = [
    path('', (cache_page(60*60*24*7))(views.index), name="Blog Home"),
    path('admit-card/', views.admit_card, name="Admit_card"),
    path('latest-job/', views.latest_job, name="Latest_job"),
    path('result/', views.result, name="Result"),
    path('BingSiteAuth.xml', views.bingSiteMap, name='bingSiteMap'),
    path('contact/', views.contact, name="Contact"),
    path('Terms_and_conditions/', views.terms_and_conditions, name="Conditions"),
    path('Privacy-Policy/', views.privacy_policy, name="Privacy"),
    path('Disclaimer/', views.disclaimer, name="Disclaimer"),
    path('<slug:slug>/', (cache_page(60*60*24*7))(views.post_view), name="postView"),

]












