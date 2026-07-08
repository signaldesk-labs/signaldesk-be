from tortoise import fields
from tortoise.models import Model

class User(Model):
    id = fields.IntField(pk=True)
    email = fields.CharField(max_length=255, unique=True)
    password_hash = fields.CharField(max_length=255)

class RefreshToken(Model):
    id = fields.IntField(pk=True)
    user = fields.ForeignKeyField("models.User", related_name="refresh_tokens")
    token_hash = fields.CharField(max_length=255)
    revoked_at = fields.DatetimeField(null=True)
