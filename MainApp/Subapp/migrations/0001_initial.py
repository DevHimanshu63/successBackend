# Generated by Django 3.1.5 on 2022-09-10 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
