# Generated by Django 4.0 on 2021-12-21 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_topic_title'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='title',
        ),
        migrations.AddField(
            model_name='topic',
            name='name',
            field=models.CharField(default='default title', max_length=256, verbose_name='Наименование'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='position',
            name='article',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.article', verbose_name='Тематики статьи'),
        ),
        migrations.AlterField(
            model_name='position',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='positions', to='articles.topic', verbose_name='Раздел'),
        ),
    ]
