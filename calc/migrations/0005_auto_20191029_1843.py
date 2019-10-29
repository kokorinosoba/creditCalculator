# Generated by Django 2.2.6 on 2019-10-29 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calc', '0004_auto_20191029_1829'),
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(default=None, max_length=30, unique=True)),
            ],
            options={
                'verbose_name': '学科',
                'verbose_name_plural': '学科',
            },
        ),
        migrations.AlterUniqueTogether(
            name='cource_subject',
            unique_together={('subject', 'cource')},
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cource', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calc.Cource')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='calc.Department')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'ユーザ',
                'verbose_name_plural': 'ユーザ',
            },
        ),
    ]