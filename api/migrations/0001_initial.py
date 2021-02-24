# Generated by Django 2.2.19 on 2021-02-24 00:25

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=20, unique=True, verbose_name='タイトル')),
                ('price', models.IntegerField(blank=True, null=True, verbose_name='価格')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='登録日時')),
            ],
            options={
                'verbose_name': '本',
                'verbose_name_plural': '本',
                'db_table': 'book',
                'ordering': ['created_at'],
            },
        ),
    ]
