# Generated by Django 3.2.3 on 2021-06-06 22:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0002_productreview'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='productreview',
            options={'ordering': ('-created_at',), 'verbose_name': 'Review', 'verbose_name_plural': 'Product Reviews'},
        ),
        migrations.RenameField(
            model_name='productreview',
            old_name='starts',
            new_name='stars',
        ),
    ]
