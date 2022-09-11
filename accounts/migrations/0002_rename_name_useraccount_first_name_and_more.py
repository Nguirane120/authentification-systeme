# Generated by Django 4.1.1 on 2022-09-11 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='useraccount',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='useraccount',
            name='last_name',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='useraccount',
            name='email',
            field=models.EmailField(max_length=255, unique=True),
        ),
    ]
