from django.db import models
from django.urls import reverse
# Create your models here.

class Category(models.Model):
	"""
	Model for category of items, Assuming there aren't any further subcategories
	"""
	name = models.CharField(max_length=50, help_text="Category that closely mathces your item")

	def __str__(self):
		"""
		String for representing model object
		"""
		return self.name

	def get_absolute_url(self):
		"""Return URL for categories
		"""
		return reverse('categories', args=[str(self.id)])

	class Meta:
		"""
		Meta Details about Category
		"""
		verbose_name_plural = 'Categories'


class Price(models.Model):
	"""
	Price as described the seller
	"""
	MRP=models.IntegerField(help_text="MRP or the rate per unit at which you want to sell")
	units = models.CharField(max_length=75, help_text="Rate per units (eg: 500 gms or 12 Nos")

	def __str__(self):
		"""
		Sting representing Rate in verbose
		"""
		return str(self.MRP) + ".Rs for " + self.units


class Item(models.Model):
	"""
	Model representing Items name and their discription
	"""
	name = models.CharField(max_length=75, help_text="Name of the item")
	discription = models.TextField(max_length=1200, help_text="Describe this item. Write something that tells about this item")
	how_to_use = models.TextField(max_length=1200)
	available_units = models.IntegerField(help_text="How many Nos or Kgs available?")
	price = models.ForeignKey('Price', on_delete=models.SET_NULL, null=True)
	category = models.ManyToManyField('Category')


	def __str__(self):
		"""
		String representing the model object
		"""
		return self.name

	def get_absolute_url(self):
		"""
		Returns the url to access this particular item
		"""
		return reverse('item-detail', args=[str(self.id)])

	def display_price(self):
		"""Return string of Price for this particular item in admin panel
		"""
		return self.price
	display_price.short_description = 'Price'		

	def display_category(self):
		"""
		Return String of the category. Needed this to display in admin panel
		"""
		return ', '.join([category.name for category in self.category.all()])
	display_category.short_description = 'Categories'
