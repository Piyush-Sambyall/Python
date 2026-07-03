# sec=147845769 convert to days , hours, min and sec




total_sec=147845769
total_min=total_sec//60
total_hour=total_min//60
total_days=total_hour//24

actual_hours=total_hour-(total_days*24)
actual_min=total_min-(total_hour*60)
actual_sec=total_sec-(total_min*60)

print("{} days {} hours {} minutes and {} sec".format(total_days,actual_hours,actual_min,actual_sec))

