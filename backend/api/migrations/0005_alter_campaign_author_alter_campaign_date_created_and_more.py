# Generated by Django 5.0.7 on 2024-07-16 13:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_alter_campaign_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='campaign',
            name='author',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='date_created',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='description',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='headline',
            field=models.TextField(default=''),
        ),
        migrations.AlterField(
            model_name='campaign',
            name='title',
            field=models.TextField(default=''),
        ),
    ]
