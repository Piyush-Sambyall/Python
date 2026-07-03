a=99987
hours=a//60
days=hours//24
months=days//30
d_day=days-(months*30)
d_hours=hours-(days*24)
min=a-(hours*60)
print("{} months {} days {} hours {} minutes".format(months, d_day, d_hours, min))