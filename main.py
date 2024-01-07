from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime

from bot import tweet


scheduler = BlockingScheduler()


@scheduler.scheduled_job("interval", minutes=40, next_run_time=datetime.now())
def post_tweet():
    tweet.run()


if __name__ == "__main__":
    # scheduler.start()
    tweet.run()
