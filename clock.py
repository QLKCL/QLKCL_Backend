#========================================
# Scheduler Jobs
#========================================
import pytz
from apscheduler.schedulers.background import BackgroundScheduler
from user_account.views import send_notification_is_last_test

scheduler = BackgroundScheduler()

vntz = pytz.timezone('Asia/Saigon')

scheduler.configure(timezone=vntz)

scheduler.add_job(send_notification_is_last_test, 'cron', hour=2, minute=5)
scheduler.start()