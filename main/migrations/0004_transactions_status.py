# Generated by Django 3.2.4 on 2021-06-04 04:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_countingunit_unit'),
    ]

    operations = [
        migrations.AddField(
            model_name='transactions',
            name='status',
            field=models.CharField(choices=[('Enable', 'Enable'), ('Disable', 'Disable')], default='Enable', max_length=50),
        ),
    ]
