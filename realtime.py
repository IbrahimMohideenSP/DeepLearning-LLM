from datetime import datetime

def get_datetime_context():
    now = datetime.now()
    return f"Current Date and Time: {now.strftime('%Y-%m-%d %H:%M:%S')}"