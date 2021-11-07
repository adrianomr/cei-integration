from dataclasses import dataclass
import json
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models.fields import BigIntegerField


@dataclass
class UserTransactionsDto():
    id: int
    transactions: list

    def dumps(self):
        return '{ "id": ' + str(self.id) + ', "transactions": ' + \
            json.dumps([ob.__dict__ for ob in self.transactions],
                       cls=DjangoJSONEncoder) + '}'
