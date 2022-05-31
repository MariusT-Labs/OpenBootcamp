# Generated by Django 4.0.4 on 2022-05-30 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(help_text='Introduce el nombre del director', max_length=50)),
                ('apellido', models.CharField(help_text='Introduce el apellido del director', max_length=50)),
            ],
        ),
    ]
