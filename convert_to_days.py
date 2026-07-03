given_min=15896 #convert to days, hours and minutes

hours=given_min//60
d_days=hours//24

d_hours=hours-(d_days*24)
d_min=given_min-(hours*60)
print(d_days, d_hours, d_min)

