from cei.user_transactions_dto import UserTransactionsDto
from cei.models import User


def parse(user: User, transactions:list) -> UserTransactionsDto:
    userTransactions = UserTransactionsDto(id=user.id, transactions=transactions)
    return userTransactions
