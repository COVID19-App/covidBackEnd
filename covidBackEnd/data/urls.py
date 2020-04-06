from django.conf.urls import url

from covidBackEnd.data.views import GetDataLast7Days, GetDataSummary, GetDataLocations, GetDataLocationsTrends

urlpatterns = [
    url(
        regex=r'^last7days/$',
        view=GetDataLast7Days.as_view(),
        name='API_last_7_days'
    ),
    url(
        regex=r'^summary/$',
        view=GetDataSummary.as_view(),
        name='API_summary'
    ),
    url(
        regex=r'^locations/$',
        view=GetDataLocations.as_view(),
        name='API_locations'
    ),
    url(
        regex=r'^locations/trends/$',
        view=GetDataLocationsTrends.as_view(),
        name='API_locations_trends'
    ),
]
