from django.utils.html import escape
from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.
class Kid(models.Model):
    kid_name=models.CharField(max_length=100)
    kid_age=models.IntegerField()
    parent_phone_number = models.CharField(max_length=12)
    parent_email_address=models.EmailField(max_length=100)

    def __str__(self):
        return self.kid_name

class Image(models.Model):
    class FoodGroup(models.TextChoices):
        FRUIT = 'fruit', _('Fruit')
        VEG = 'veg', _('Veg')
        GRAIN = 'grain', _('Grain')
        PROTEIN = 'protein', _('Protein')
        DAIRY = 'dairy', _('Dairy')
        CONFECTIONERY = 'confectionery', _('Confectionery')
        UNKNOWN = 'unknown', _('Unknown')
    
    kid= models.ForeignKey(Kid, on_delete=models.CASCADE)
    image_url = models.URLField(max_length=200)
    created_on = models.DateTimeField()
    updated_on = models.DateTimeField(auto_now=True)
    is_approved = models.BooleanField(default=True)
    approved_by= models.CharField(max_length=100)
    food_group= models.CharField(
        max_length=20,
        choices=FoodGroup.choices,
        default=FoodGroup.UNKNOWN,
    )

    def image_tag(self):
            return mark_safe('<img src="%s" width="150" height="150" />' % (self.image))

    image_tag.short_description = 'Image'
    image_tag.allow_tags = True
