from django.db import models


STR_FORMAT = "%Y-%m-%d"


class User(models.Model):
    username = models.CharField(max_length=200)
    infection_probability = models.FloatField(default=0)
    creation_date = models.DateTimeField('added on')

    def __str__(self):
        return "username: %s, infection_probability: %s" % (
            self.username,
            self.infection_probability)


class Location(models.Model):
    name = models.CharField(max_length=200)
    infection_factor = models.FloatField(default=0)

    def __str__(self):
        return "%s %f" % (self.name, self.infection_factor)


class TravelRecord(models.Model):
    location = models.ForeignKey(Location, on_delete=models.CASCADE, default=0)
    arrived_at = models.DateTimeField('arrival time', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "%s %s %s" % (
            self.location.name, self.user.username,
            self.arrived_at.strftime(STR_FORMAT))


class InfectionRecord(models.Model):
    infected_at = models.DateTimeField('infected at', default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=0)

    def __str__(self):
        return "%s" % (self.infected_at.strftime(STR_FORMAT))
