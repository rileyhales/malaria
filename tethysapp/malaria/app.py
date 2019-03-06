from tethys_sdk.base import TethysAppBase, url_map_maker
from tethys_sdk.app_settings import CustomSetting


class Malaria(TethysAppBase):
    """
    Tethys app class for Malaria Spread Predictor.
    """

    name = 'Malaria Spread Predictor'
    index = 'malaria:home'
    icon = 'malaria/images/icon.gif'
    package = 'malaria'
    root_url = 'malaria'
    color = '#f53636'
    description = 'An app for forecasting malaria spread using dispersion models developed at John Hopkins University and using global datasets from NASA LDAS'
    tags = '&quot;Health&quot;, &quot;Malaria&quot;, &quot;Forecast&quot;, &quot;Prediction&quot;, &quot;LDAS&quot;'
    enable_feedback = False
    feedback_emails = []

    def url_maps(self):
        """
        Add controllers
        """
        UrlMap = url_map_maker(self.root_url)

        url_maps = (
            UrlMap(
                name='home',
                url='malaria',
                controller='malaria.controllers.home'
            ),
            UrlMap(
                name='customsettings',
                url='malaria/ajax/customsettings',
                controller='malaria.controllersAJAX.customsettings'
            ),
        )

        return url_maps

    def custom_settings(self):
        settings = (
            CustomSetting(
                name='datadirpath',
                type=CustomSetting.TYPE_STRING,
                description='Path to the DIRECTORY of netCDF data for this app. ex ~/Users/rileyhales/thredds/malaria',
                required=True,
            ),
            CustomSetting(
                name='threddsurl',
                type=CustomSetting.TYPE_STRING,
                description='URL of the thredds wms for this app\'s data. ex byu.edu/thredds/wms/',
                required=True,
            ),
        )
        return settings
