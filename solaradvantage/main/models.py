from django.db import models


class WeatherData(models.Model):
    """
    This model will create a table call WeatherData which will house
    all the rows of weather data by location.
    """

    namedate_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    datetime = models.DateField()
    tempmax = models.CharField(max_length=255)
    tempmin = models.CharField(max_length=255)
    temp = models.CharField(max_length=255)
    feelslikemax = models.CharField(max_length=255)
    feelslikemin = models.CharField(max_length=255)
    feelslike = models.CharField(max_length=255)
    dew = models.CharField(max_length=255)
    humidity = models.CharField(max_length=255)
    precip = models.CharField(max_length=255)
    precipprob = models.CharField(max_length=255)
    precipcover = models.CharField(max_length=255)
    preciptype = models.CharField(max_length=255)
    snow = models.CharField(max_length=255)
    snowdepth = models.CharField(max_length=255)
    windgust = models.CharField(max_length=255)
    windspeed = models.CharField(max_length=255)
    winddir = models.CharField(max_length=255)
    sealevelpressure = models.CharField(max_length=255)
    cloudcover = models.CharField(max_length=255)
    visibility = models.CharField(max_length=255)
    solarradiation = models.CharField(max_length=255)
    solarenergy = models.CharField(max_length=255)
    uvindex = models.CharField(max_length=255)
    severerisk = models.CharField(max_length=255)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    moonphase = models.CharField(max_length=255)
    conditions = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    stations = models.CharField(max_length=255)
