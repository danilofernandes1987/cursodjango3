# Generated by Django 3.0.6 on 2020-05-16 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_teste'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='categories',
            field=models.CharField(choices=[('TC', 'Tecnologia'), ('CR', 'Curiosidades'), ('GR', 'Geral')], default='GR', max_length=2),
        ),
    ]