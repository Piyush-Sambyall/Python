# hrs=478569 convert to months days and hours

hours=478569
total_days=hours//24
total_months=total_days//30

actual_days=total_days-(total_months*30)

actual_hours=hours-(total_days*24)

print("{} months {} days and {} hours".format(total_months,actual_days,actual_hours))