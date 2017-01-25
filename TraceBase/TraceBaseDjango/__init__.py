from django.db import models
# Custom Floatfield to Real datatype PostgreSQL.


class RealField(models.FloatField):

    description = "A field with the Real datatype"

    def db_type(self, connection):
        return []
