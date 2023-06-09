# Generated by Django 4.2.2 on 2023-06-09 10:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_event_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='date',
            field=models.DateField(verbose_name='Дата события'),
        ),
        migrations.AlterField(
            model_name='event',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='end_date',
            field=models.DateTimeField(verbose_name='Окончание'),
        ),
        migrations.AlterField(
            model_name='event',
            name='start_date',
            field=models.DateTimeField(verbose_name='Начало'),
        ),
        migrations.AlterField(
            model_name='event',
            name='template',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.PROTECT, to='core.eventtemplate', verbose_name='Набор эмоций'),
        ),
        migrations.AlterField(
            model_name='event',
            name='title',
            field=models.CharField(max_length=50, verbose_name='Название'),
        ),
        migrations.AlterField(
            model_name='vote',
            name='event',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.event'),
        ),
    ]