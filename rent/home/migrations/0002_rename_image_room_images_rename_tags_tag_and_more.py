# Generated by Django 4.1.7 on 2023-03-04 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Room_images',
        ),
        migrations.RenameModel(
            old_name='Tags',
            new_name='Tag',
        ),
        migrations.RenameField(
            model_name='room',
            old_name='room_thumdnail_image',
            new_name='room_image',
        ),
    ]