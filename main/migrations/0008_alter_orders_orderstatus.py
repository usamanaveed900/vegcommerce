# Generated by Django 3.2.4 on 2021-07-12 08:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_alter_orders_customerid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orders',
            name='orderStatus',
            field=models.CharField(choices=[('Pending', 'Pending'), ('Processed', 'Processed'), ('Completed', 'Completed'), ('Cancel', 'Cancel')], default='Pending', max_length=50),
        ),
    ]
