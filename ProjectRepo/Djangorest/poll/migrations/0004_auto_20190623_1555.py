# Generated by Django 2.2 on 2019-06-23 10:25

from django.db import migrations, models
import poll.models


class Migration(migrations.Migration):

    dependencies = [
        ('poll', '0003_auto_20190623_1541'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testmodel',
            name='AssetId',
            field=models.CharField(default=poll.models.TestModel.create_assetcode, editable=False, max_length=14, unique=True),
        ),
    ]
