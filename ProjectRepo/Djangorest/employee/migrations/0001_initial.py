# Generated by Django 2.2 on 2019-06-17 13:59

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('designation', models.CharField(max_length=20)),
                ('salary', models.IntegerField(blank=True, null=True)),
                ('user', models.OneToOneField(on_delete='models.CASCADE', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ('-salary',),
            },
        ),
    ]
