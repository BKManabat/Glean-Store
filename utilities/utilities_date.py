from datetime import datetime
from pytz import timezone

def time_now():
  return datetime.now().astimezone(timezone("Asia/Manila"))