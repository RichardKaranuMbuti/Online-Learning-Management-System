from django.db import models
from django.urls import reverse
from django.utils.text import slugify
# Create your models here.
class DepartmentModel(models.Model):
	name = models.CharField(max_length=100)
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	code = models.CharField(max_length=50)
	description = models.TextField()

	def __str__(self):
		return (self.name + '-' + self.code).upper()

class UnitModel(models.Model):
	name = models.CharField(max_length=100)
	creator = models.CharField(max_length=50)
	image = models.ImageField(upload_to='units/')
	date_created = models.DateField(auto_now_add=True)
	date_updated = models.DateField(auto_now=True)
	rating = models.CharField(max_length=50)
	price = models.CharField(max_length=50)
	code = models.CharField(max_length=50)
	description = models.TextField()
	department = models.ForeignKey(DepartmentModel, on_delete=models.CASCADE)
	slug = models.SlugField(max_length=100)

	def get_absolute_url(self):
		return reverse("school:detail_unit", kwargs={"slug": self.slug})

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(UnitModel, self).save(*args, **kwargs)

	def __str__(self):
		return (self.name + '-' + self.code).upper()
