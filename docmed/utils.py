import os.path
from datetime import datetime


def get_timestamp_upload_to(instance, filename: str) -> str:
    current_time = datetime.now()
    base_name, ext = os.path.splitext(filename)
    new_filename = f'{current_time.strftime("%Y%m%d_%H%M%S")}{ext}'
    return os.path.join(f'{instance.__class__.__name__.casefold()}/', new_filename)
