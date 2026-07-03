# min= convert to days hrs min

total_min=474586
hours=total_min//60

days=hours//24

min_left=total_min-(days*24*60)

actual_hours=min_left//60

min_left=min_left-(actual_hours*60)

print("{} days {} hours {} min".format(days,actual_hours,min_left))