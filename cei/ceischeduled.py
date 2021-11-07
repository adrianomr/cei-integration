from datetime import datetime

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.interval import IntervalTrigger


from cei.fetch_users_transactions import FetchUsersTransactions


class CeiScheduled:
    scheduler = BlockingScheduler()

    @scheduler.scheduled_job(IntervalTrigger(hours=12))
    def train_model():
        print('Cei integration is running: %s' % datetime.now())
        FetchUsersTransactions.execute()

    def start(self):
        FetchUsersTransactions.execute()
        self.scheduler.start()
