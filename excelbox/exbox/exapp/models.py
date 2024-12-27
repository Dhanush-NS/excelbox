from django.db import models
# from views import*
class Totalsolutions(models.Model):
    CATEGORY_CHOICES = [
        ('hardware', 'Hardware'),
        ('software', 'Software'),
        ('service', 'Service'),
        ('all', 'All Categories')
    ]

    application = models.CharField(max_length=255)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='all')
    product_name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    specification = models.TextField()
    uom = models.CharField(max_length=300)  # Unit of Measurement
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=255)
    quotation_received_month = models.CharField(max_length=50)
    lead_time = models.CharField(max_length=50)
    remarks = models.TextField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_margin = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_name

class Item(models.Model):
    sl_no = models.IntegerField()
    application = models.CharField(max_length=255)
    categories = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    specification = models.TextField()
    uom = models.CharField(max_length=50)
    buying_price = models.DecimalField(max_digits=10, decimal_places=2)
    vendor = models.CharField(max_length=255)
    quotation_received_date = models.DateField()
    lead_time = models.IntegerField()
    remarks = models.TextField(blank=True, null=True)
    list_price = models.DecimalField(max_digits=10, decimal_places=2)
    discount = models.DecimalField(max_digits=5, decimal_places=2)
    sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    sales_margin = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return self.product_name

