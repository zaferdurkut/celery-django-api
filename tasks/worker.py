from celery import Celery
from dotenv import load_dotenv
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(dotenv_path=BASE_DIR)



app = Celery(
  broker=os.getenv('CELERY_BROKER_URL'), 
  include=('tasks',))
app.conf.beat_schedule = {
  'refresh': {
    'task': 'refresh',
    'schedule': float(os.getenv('NEWSPAPER_SCHEDULE')),
    'args': (os.getenv('NEWSPAPER_URLS').split(','),)
  },
}