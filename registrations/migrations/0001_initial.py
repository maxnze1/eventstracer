# Generated by Django 2.0.13 on 2020-01-14 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Invitation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=150)),
                ('message', models.TextField(max_length=2000)),
                ('source', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='SMERegistration',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('circuit', models.CharField(choices=[('eko_cake_fair', 'Eko Cake Fair'), ('skin_facial', 'Skin and Facial Beauty Fair')], max_length=20)),
                ('company_name', models.CharField(max_length=30)),
                ('type_of_business', models.CharField(choices=[('LL', 'Limited Liability'), ('RB', 'Registered Business Name'), ('P', 'Partnership'), ('U', 'Unregistered')], max_length=200)),
                ('company_address', models.CharField(max_length=100)),
                ('company_sector', models.CharField(max_length=20)),
                ('years_business', models.CharField(choices=[('L1', 'Less Than 1 Years'), ('1-3', '1-3 Years'), ('3-5', '3-5 Years'), ('O5', 'Over 5 Years')], max_length=20)),
                ('contact_person', models.CharField(max_length=20)),
                ('company_person_designation', models.CharField(blank=True, max_length=20, null=True)),
                ('phone_number', models.CharField(max_length=20)),
                ('description', models.TextField(blank=True, max_length=500, null=True)),
                ('email', models.EmailField(max_length=50)),
                ('website', models.CharField(blank=True, max_length=250, null=True)),
                ('date_incorporation', models.CharField(blank=True, choices=[('L1', 'Less Than 1 Years'), ('1-3', '1-3 Years'), ('3-5', '3-5 Years'), ('O5', 'Over 5 Years')], max_length=200, null=True)),
                ('contact_person2', models.CharField(blank=True, max_length=20, null=True)),
                ('employed_person', models.CharField(choices=[('L5', '0-5 Persons'), ('5-10', '5-10 Persons'), ('M10', 'More than 10 Persons')], max_length=20)),
                ('annual_revenue', models.CharField(choices=[('0-5', 'N0-N5M'), ('5-10', 'N5M-N10M'), ('10-15', 'N10M-N15M'), ('15-30', 'N15M-N30M'), ('M30', 'More than N30M')], max_length=200)),
                ('business_projection', models.TextField(blank=True, max_length=500, null=True)),
                ('challenges', models.TextField(blank=True, max_length=500, null=True)),
                ('outlets', models.CharField(blank=True, max_length=500, null=True)),
                ('improve_business', models.TextField(blank=True, max_length=500, null=True)),
                ('payment', models.CharField(blank=True, choices=[('S', 'Success'), ('F', 'Failed'), ('U', 'Unknown')], max_length=10, null=True)),
                ('payment_reference', models.CharField(blank=True, max_length=15, null=True)),
                ('pdf', models.FileField(blank=True, null=True, upload_to='documents')),
                ('invite', models.BooleanField(default=False)),
                ('photo', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('supporting_document', models.FileField(blank=True, null=True, upload_to='documents')),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='SMEScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('limited_liability', models.IntegerField()),
                ('registered_business_name', models.IntegerField()),
                ('partnership', models.IntegerField()),
                ('unregistered', models.IntegerField()),
                ('NYB_less_than_1_year', models.IntegerField()),
                ('NYB_1_to_3_year', models.IntegerField()),
                ('NYB_3_to_5_year', models.IntegerField()),
                ('NYB_over_5_year', models.IntegerField()),
                ('email', models.IntegerField()),
                ('website', models.IntegerField()),
                ('rc_number', models.IntegerField()),
                ('DOI_less_than_1_year', models.IntegerField()),
                ('DOI_1_to_3_year', models.IntegerField()),
                ('DOI_3_to_5_year', models.IntegerField()),
                ('DOI_over_5_year', models.IntegerField()),
                ('NPE_0_to_5_persons', models.IntegerField()),
                ('NPE_5_to_10_persons', models.IntegerField()),
                ('NPE_more_than_10_persons', models.IntegerField()),
                ('AR_0_to_5M', models.IntegerField()),
                ('AR_5_to_10M', models.IntegerField()),
                ('AR_10_to_15M', models.IntegerField()),
                ('AR_15_to_30M', models.IntegerField()),
                ('AR_30_to_50M', models.IntegerField()),
                ('AR_more_than_50M', models.IntegerField()),
                ('pass_mark', models.IntegerField()),
            ],
        ),
    ]
