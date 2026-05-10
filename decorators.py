from datetime import datetime

def log_action(func):
    def wrapper(*args, **kwargs):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(f"  [LOG {timestamp}] {func.__name__} called")
        return func(*args, **kwargs)
    return wrapper
