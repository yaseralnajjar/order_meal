# Generated by Django 2.2 on 2019-05-20 15:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal_list', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price_order',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, to='meal_list.Meal', verbose_name='سعر الوجبة'),
        ),
    ]
