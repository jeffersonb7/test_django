# Generated by Django 4.0 on 2022-08-25 00:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('musica', '0003_musica_file_arquivo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='musica',
            name='file_arquivo',
            field=models.FileField(upload_to='test/'),
        ),
    ]