# Generated by Django 3.1.5 on 2022-09-20 04:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Subapp', '0005_team'),
    ]

    operations = [
        migrations.AddField(
            model_name='team',
            name='MemberImg',
            field=models.ImageField(default='', upload_to='static/img'),
        ),
    ]
