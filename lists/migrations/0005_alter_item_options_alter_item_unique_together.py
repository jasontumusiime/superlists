# Generated by Django 5.0.2 on 2024-03-19 10:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0004_alter_item_list'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='item',
            options={'ordering': ('id',)},
        ),
        migrations.AlterUniqueTogether(
            name='item',
            unique_together={('list', 'text')},
        ),
    ]
