from django.db import models


class WeatherData(models.Model):
    """
    This model will create a table call WeatherData which will house
    all the rows of weather data by location.
    """

    namedate_id = models.CharField(max_length=255, primary_key=True)
    name = models.CharField(max_length=255)
    datetime = models.DateField()
    tempmax = models.FloatField()
    tempmin = models.FloatField()
    temp = models.FloatField()
    feelslikemax = models.FloatField()
    feelslikemin = models.FloatField()
    feelslike = models.FloatField()
    dew = models.FloatField()
    humidity = models.FloatField()
    precip = models.FloatField()
    precipprob = models.FloatField()
    precipcover = models.FloatField()
    preciptype = models.CharField(max_length=255)
    snow = models.FloatField()
    snowdepth = models.FloatField()
    windgust = models.FloatField()
    windspeed = models.FloatField()
    winddir = models.FloatField()
    sealevelpressure = models.FloatField()
    cloudcover = models.FloatField()
    visibility = models.FloatField()
    solarradiation = models.FloatField()
    solarenergy = models.FloatField()
    uvindex = models.FloatField()
    severerisk = models.CharField(max_length=255)
    sunrise = models.DateTimeField()
    sunset = models.DateTimeField()
    moonphase = models.FloatField()
    conditions = models.CharField(max_length=255)
    description = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    stations = models.CharField(max_length=255)
