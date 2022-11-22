from django.db import models


# Create your models here.
class BusinessModel(models.Model):
    """Main data model class of the app."""

    name = models.CharField(name='name', max_length=80, verbose_name="Name")
    location = models.TextField(name='location', verbose_name="Location")

    class Meta:
        """Meta info of the class."""

        verbose_name = 'Business Data'
        verbose_name_plural = 'Businesses Data'
    
    def __str__(self) -> str:
        """Represent default string."""
        return self.name
