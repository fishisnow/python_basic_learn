import datetime

dtstr = str(raw_input("Enter the daytime:(20151201)"))
dt = datetime.datetime.strptime(dtstr, "%Y%m%d")
print dt
another_datetime = datetime.datetime.strptime(dtstr[:4] + '0101', "%Y%m%d")
print int((dt-another_datetime).days+1)
