# Generated by Django 4.2.3 on 2024-02-27 14:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('giftapp', '0017_feedbacktable_review_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='MultipleFeedBackImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('f_image', models.FileField(upload_to='')),
                ('f_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='giftapp.feedbacktable')),
            ],
        ),
    ]
