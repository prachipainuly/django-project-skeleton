from django.db import models


class Sample(models.Model):
    """This class represents the sample model."""
    user_id = models.CharField(max_length=255, blank=False, unique=True)
    name = models.CharField(max_length=255, blank=False, unique=True)

    class Meta:
        app_label = "app"

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}_{}_{}_{}".format(self.user_id, self.name)
