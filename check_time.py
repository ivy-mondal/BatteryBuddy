import random
import time
from datetime import datetime
from charge_reminder import charge_reminder


def check_time():
    while True:
        try:
            current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            battery_level = charge_reminder()

            if battery_level is not None:
                with open("battery_log.txt", "a") as log_file:
                    log_file.write(f"\n[{current_time}] Battery level {battery_level}%")

            check_interval = random.uniform(11 * 3600, 12 * 3600)
            time.sleep(check_interval)

        except Exception:
            time.sleep(300)


if __name__ == "__main__":
    print("Battery Buddy Test Started! Press Ctrl+C to stop")
    check_time()
