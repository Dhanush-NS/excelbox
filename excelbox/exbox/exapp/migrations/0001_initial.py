# Generated by Django 5.0.6 on 2024-12-17 11:30

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Totalsolutions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('application', models.CharField(max_length=255)),
                ('category', models.CharField(choices=[('hardware', 'Hardware'), ('software', 'Software'), ('service', 'Service'), ('all', 'All Categories')], default='all', max_length=50)),
                ('product_name', models.CharField(max_length=255)),
                ('make', models.CharField(max_length=255)),
                ('model', models.CharField(max_length=255)),
                ('specification', models.TextField()),
                ('uom', models.CharField(max_length=50)),
                ('buying_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('vendor', models.CharField(max_length=255)),
                ('quotation_received_month', models.CharField(max_length=50)),
                ('lead_time', models.CharField(max_length=50)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('list_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('discount', models.DecimalField(decimal_places=2, max_digits=5)),
                ('sales_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('sales_margin', models.DecimalField(decimal_places=2, max_digits=5)),
            ],
        ),
    ]
