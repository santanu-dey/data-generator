import random
import math
import time
import datetime
import json

def rand_gaussin(mu, sigma, bottom, top):
    a = random.gauss(mu,sigma)
    while (bottom <= a <= top) == False:
        a = random.gauss(mu,sigma)
    return  math.floor(a)

def rand_gaussin_float(mu, sigma, bottom, top):
    a = random.gauss(mu,sigma)
    while (bottom <= a <= top) == False:
        a = random.gauss(mu,sigma)
    return  a

def rand_uniform(bottom, top):
    a = random.uniform(bottom,top)
    return  math.floor(a)


# time_stamp=datetime.datetime.now();
time_stamp = datetime.datetime(2016, 7, 30, 21, 20, 1);

# only for csv
with open("data.txt", "a") as myfile:
	myfile.write("ts"+","+"temperature" +","+ "pressure" +","+"pH"+","+"co2rate" )

for i in range(0, 3000):

	# number = rand_gaussin(1, 18, 0, 37);
	data_row = {}
	time_stamp = time_stamp + datetime.timedelta(minutes = 10)
	#data_row["time"] = time_stamp.strftime('%Y-%m-%d %H:%M:%S'); # for json
	data_row["time"] = time_stamp.strftime('%Y/%m/%d %I:%M:%S %p'); # for CSV
	#data_row["equipment"] = "Reactor1" # for json
	data_row["temperature"] = round(rand_gaussin_float(201, 2.68, 195, 211), 2); # reactor 1
	#data_row["temperature"] = round(rand_gaussin_float(201, 2.9, 195, 213), 2); # reacor 2
	data_row["pressure"] = round (rand_gaussin_float(2, 0.024, 2, 2.1), 3); # reactor 1
	#data_row["pressure"] = round (rand_gaussin_float(2, 0.027, 2, 2.3), 3); # reacor 2
	data_row["pH"] = round (rand_gaussin_float(9.5, 0.004, 9, 10), 4);
	data_row["CO2-emission-rate"] = round(rand_gaussin_float(0.025, 0.001, 0.021, 0.035), 6);

	with open("data.txt", "a") as myfile:
	    #myfile.write('\n'+json.dumps(data_row)) # For JSON
	    myfile.write('\n'+data_row["time"]+","+str(data_row["temperature"]) +","+str(data_row["pressure"]) +","+str(data_row["pH"]) +","+str(data_row["CO2-emission-rate"]) ) # For CSV
pass

