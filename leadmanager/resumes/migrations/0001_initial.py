# Generated by Django 2.2.1 on 2019-05-29 18:44

from django.conf import settings
import django.contrib.postgres.fields
import django.contrib.postgres.fields.jsonb
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('label', models.CharField(blank=True, max_length=10, null=True)),
                ('email', models.EmailField(max_length=100, null=True, unique=True)),
                ('phone', models.CharField(blank=True, max_length=17, null=True, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('degree', models.CharField(blank=True, max_length=25, null=True)),
                ('website', models.TextField(blank=True, null=True, validators=[django.core.validators.URLValidator()])),
                ('summary', models.CharField(blank=True, max_length=500, null=True)),
                ('highlights', models.CharField(blank=True, max_length=500, null=True)),
                ('address', models.CharField(blank=True, max_length=100, null=True)),
                ('postal_code', models.CharField(blank=True, max_length=500, null=True)),
                ('city', models.CharField(blank=True, max_length=20, null=True)),
                ('country_code', models.CharField(blank=True, max_length=20, null=True)),
                ('region', models.CharField(blank=True, max_length=10, null=True)),
                ('profiles', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, null=True, size=None)),
                ('work', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, null=True, size=None)),
                ('education', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, null=True, size=None)),
                ('skills', django.contrib.postgres.fields.ArrayField(base_field=django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True), blank=True, null=True, size=None)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='resumes', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
