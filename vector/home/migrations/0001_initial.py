# Generated by Django 5.0.1 on 2024-01-24 15:06

import pgvector.django
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LangchainPgCollection',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'langchain_pg_collection',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='LangchainPgEmbedding',
            fields=[
                ('uuid', models.UUIDField(primary_key=True, serialize=False)),
                ('embedding', pgvector.django.VectorField(dimensions=1536)),
                ('document', models.CharField(blank=True, null=True)),
                ('cmetadata', models.TextField(blank=True, null=True)),
                ('custom_id', models.CharField(blank=True, null=True)),
            ],
            options={
                'db_table': 'langchain_pg_embedding',
                'managed': False,
            },
        ),
    ]
