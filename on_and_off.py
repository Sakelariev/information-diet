import os, sys
import schedule
import time
from datetime import datetime as dt
import no_distraction_gui2 as distraction



def setSchedule(self):
    schedule.every().day.at("20:40").do(distraction.turn_on)
    schedule.every().day.at("20:41").do(distraction.turn_off)
    while True:
        schedule.run_pending()
        time.sleep(1)
