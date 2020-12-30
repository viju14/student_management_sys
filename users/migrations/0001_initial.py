# Generated by Django 3.1.4 on 2020-12-29 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email_address')),
                ('is_student', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='CustomUserProfile',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('bio', models.TextField(blank=True, default='')),
                ('preferred_name', models.CharField(max_length=100, null=True)),
                ('avatar_url', models.CharField(max_length=255, null=True)),
                ('discord_name', models.CharField(max_length=100, null=True)),
                ('github_username', models.CharField(max_length=100)),
                ('codepen_username', models.CharField(max_length=100, null=True)),
                ('fcc_profile_url', models.CharField(max_length=255, null=True)),
                ('customuser', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.customuser')),
                ('current_level', models.IntegerField(choices=[(1, 'Level One'), (2, 'Level Two')], default=1)),
                ('phone', models.CharField(max_length=50, null=True)),
                ('timezone', models.CharField(max_length=50, null=True)),
            ],
        ),
    ]
