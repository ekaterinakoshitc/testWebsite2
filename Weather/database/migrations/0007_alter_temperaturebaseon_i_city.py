# Generated by Django 4.1.7 on 2023-02-21 07:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("database", "0006_remove_temperaturebase_i_city_delete_tempbase_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="temperaturebaseon",
            name="i_city",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                to="database.citybase",
                verbose_name="Город",
            ),
        ),
    ]