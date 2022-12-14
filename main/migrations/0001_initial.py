# Generated by Django 3.2.4 on 2021-06-02 11:14

from django.conf import settings
from django.db import migrations, models
from django.db.models import fields
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    # sql = """CREATE VIEW v_Customer_Proceesed_Orders AS
    #         SELECT customerId_id, COUNT(id) AS processedorders FROM main_orders WHERE orderStatus='Pending' GROUP BY customerID_id;"""

    operations = [
        migrations.CreateModel(
            name='AboutUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Address', models.CharField(max_length=200)),
                ('Number', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=100)),
                ('lastName', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
                ('message', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='CountingUnit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='PrivacyPolicy',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='TermAndConditions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('text', models.TextField()),
                ('updated_date', models.DateTimeField(auto_now_add=True)),
                ('expire_date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Sub_Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sub_category_name', models.CharField(max_length=200)),
                ('CategoryID', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='subcategoryies', to='main.category')),
            ],
        ),
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('product_image', models.ImageField(upload_to='ProductImg')),
                ('selling_price', models.FloatField()),
                ('discount_percentage', models.PositiveIntegerField(default=1)),
                ('Sub_Category_ID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.sub_category')),
                ('countingUnit', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.countingunit')),
            ],
        ),
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Order_Date', models.DateTimeField(auto_now_add=True)),
                ('orderStatus', models.CharField(choices=[('Pending', 'Pending'), ('Completed', 'Completed'), ('Cancel', 'Cancel')], default='Pending', max_length=50)),
                ('customerID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('price', models.FloatField()),
                ('orderID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.orders')),
                ('productID', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main.products')),
            ],
        ),
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('address', models.TextField()),
                ('phone', models.CharField(max_length=15)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        # migrations.RunSQL(sql="""CREATE VIEW v_Customer_Proceesed_Orders AS
        #     SELECT customerId_id, COUNT(id) AS processedorders FROM main_orders WHERE orderStatus='Pending' GROUP BY customerID_id;""",), 
        # migrations.CreateModel(
        #     name='ExampleView',
        #     fields=[
        #         ('customerId_id', models.PositiveIntegerField()),
        #         ('processedorders', models.PositiveIntegerField()),
        #     ],
        # ),
        
    ]
