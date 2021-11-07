from cei.ceiintegrationproducer import CeiIntegrationProducer
from cei.ceiservice import CeiService
from cei.models import User
import concurrent.futures
from cei.user_dto_adapter import parse
import asyncio


class FetchUsersTransactions:

    def execute():
        users = User.objects.all()
        for user in users:
            asyncio.run(FetchUsersTransactions.fetchUserTransaction(user))

    async def fetchUserTransaction(user:User):
        with concurrent.futures.ThreadPoolExecutor() as pool:
            print("fetchData")
            result = await CeiService.fetchData(user.username, user.password)
            print('custom thread pool', result)
            userTransactions = parse(user, result)
            print("---------------- User Transactions ----------------")
            print(userTransactions.dumps())
            CeiIntegrationProducer.sendMessage(userTransactions.dumps())
