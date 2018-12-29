import matplotlib.pyplot as plt
import numpy as np
import re
import datetime

print('plotting pressure data from \'logfile\'')

#load the data, parse.
# datetime, altitude x2, pressure x2

logfile = open('./homelog', 'U')
print(logfile)

datetimes = []
pressures = []
for line in logfile:
	if not (re.match('#.*',line) or re.match('\s+',line)):
		#print(line)
		fields = line.split('\t')
		# yyyy-mm-dd hh24:mi:se.ms
		#print(fields[0])
		datetimes.append(datetime.datetime.strptime(fields[0].strip(), '%Y-%m-%d %H:%M:%S.%f'))
		data = fields[1].split(' ')
		pressures.append(data[3])
logfile.close()
#print(datetimes)
#print(pressures)

fig = plt.figure()  # an empty figure with no axes

# plot tpressure against time.  pyplot needs numpy arrays.
x = np.linspace(0, 2, 100)
plt.plot(datetimes, pressures, label='linear')
plt.xlabel('date')
plt.ylabel('pressure')
plt.title('Pressure timeseries')

plt.show()
