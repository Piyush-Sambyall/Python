# hrs=1025003 month days hrs

total_hours=1025003

days=total_hours//24

months=days//30

hours_left=total_hours-(months*30*24)

actual_days=hours_left//24

hours_left=hours_left-(actual_days*24)

print("{} months {} days {} hours".format(months,actual_days,hours_left))