# Generated by Django 3.1.6 on 2021-05-02 06:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gellary', '0006_remove_imagealbum_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imagealbum',
            name='image10',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image2',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image3',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image4',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image5',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image6',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image7',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image8',
        ),
        migrations.RemoveField(
            model_name='imagealbum',
            name='image9',
        ),
        migrations.AddField(
            model_name='imagealbum',
            name='image',
            field=models.ImageField(default=1, upload_to=''),
            preserve_default=False,
        ),
    ]
