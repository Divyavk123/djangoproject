# Generated by Django 2.2.6 on 2019-10-17 05:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('food', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='abc',
            name='img',
            field=models.ImageField(default='sample.jpj', upload_to='clicks'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='abc',
            name='date',
            field=models.DateField(auto_now_add=True),
        ),
    ]