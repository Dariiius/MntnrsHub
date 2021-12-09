# Generated by Django 4.0 on 2021-12-09 14:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.CharField(blank=True, default='', max_length=255, null=True)),
                ('posted_on', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('posted', 'Posted'), ('archived', 'Archived')], default='posted', max_length=50)),
                ('visibility_status', models.CharField(choices=[('public', 'Public'), ('private', 'Private')], default='public', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='auth.user')),
            ],
        ),
    ]