from django.db import models
from pgvector.django import VectorField


class LangchainPgCollection(models.Model):
    uuid = models.UUIDField(primary_key=True)
    name = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)  # This field type is a guess.

    class Meta:
        managed = False
        db_table = 'langchain_pg_collection'


class LangchainPgEmbedding(models.Model):
    uuid = models.UUIDField(primary_key=True)
    collection = models.ForeignKey(LangchainPgCollection, models.DO_NOTHING, blank=True, null=True)
    embedding = VectorField(dimensions=1536)  # This field type is a guess.
    document = models.CharField(blank=True, null=True)
    cmetadata = models.TextField(blank=True, null=True)  # This field type is a guess.
    custom_id = models.CharField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'langchain_pg_embedding'
