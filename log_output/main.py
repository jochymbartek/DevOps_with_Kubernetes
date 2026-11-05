import uuid
import time
from datetime import datetime, timezone

random_string = str(uuid.uuid4())

while True:
    timestamp = datetime.now(timezone.utc)
    print(f"{timestamp.isoformat()}: {random_string}", flush=True)
    time.sleep(5)