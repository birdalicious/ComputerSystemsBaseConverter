from baseconverter import convert
import random
import os

testcases = 400

cycles = 25000
includeOverflow = True
trickyinputs = True



overflowcomment = "overflow"
tobase10comment = "Into base 10"
frombase10comment = "From base 10"
frombaseatobcomment = "From base a to b"
noconversion = "No conversion"

overflowlines = []
tobase10lines = []
frombase10lines = []
frombaseatoblines = []
noconversionlines = []
trickyinputslist = []

testlist = []

for base in range(2,11):
	for newbase in range(2,11):
		for i in range(0,base):
			for j in range(0,base):
				for k in range(0,base):
					num = int(str(i)+str(j)+str(k))
					converted = convert(num,base,newbase)
					if converted < 1000:
						if base == newbase:
							line = noconversion
							line += ";" + str(num) + "," + str(base) + "," + str(newbase)
							line += ";" + str(converted) + ";" + str(cycles)
							noconversionlines.append(line)
						elif newbase == 10:
							line = tobase10comment
							line += ";" + str(num) + "," + str(base) + "," + str(newbase)
							line += ";" + str(converted) + ";" + str(cycles)
							tobase10lines.append(line)
						elif base == 10:
							line = frombase10comment
							line += ";" + str(num) + "," + str(base) + "," + str(newbase)
							line += ";" + str(converted) + ";" + str(cycles)
							frombase10lines.append(line)
						else:
							line = frombaseatobcomment
							line += ";" + str(num) + "," + str(base) + "," + str(newbase)
							line += ";" + str(converted) + ";" + str(cycles)
							frombaseatoblines.append(line)
					else:
						line = overflowcomment
						line += ";" + str(num) + "," + str(base) + "," + str(newbase)
						line += ";999;" + str(cycles)
						overflowlines.append(line)

if not os.path.isdir("batch"):		
	os.mkdir("batch")

f = open("batch/overflow.batch", "w")
for l in overflowlines:
	f.write(l + "\n")
f.close()
f = open("batch/tobase10.batch", "w")
for l in tobase10lines:
	f.write(l + "\n")
f.close()
f = open("batch/frombase10.batch", "w")
for l in frombase10lines:
	f.write(l + "\n")
f.close()
f = open("batch/frombaseatobaseb.batch", "w")
for l in frombaseatoblines:
	f.write(l + "\n")
f.close()
f = open("batch/noconversion.batch", "w")
for l in noconversionlines:
	f.write(l + "\n")
f.close()

f = open("batch/count.txt", "w")
f.write(overflowcomment + ": " + str(len(overflowlines)) + "\n")
f.write(tobase10comment + ": " + str(len(tobase10lines)) + "\n")
f.write(frombase10comment + ": " + str(len(frombase10lines)) + "\n")
f.write(frombaseatobcomment + ": " + str(len(frombaseatoblines)) + "\n")
f.write(noconversion + ": " + str(len(noconversionlines)) + "\n")
f.close()

f = open("batch/all.batch", "w")
for l in overflowlines:
	f.write(l + "\n")
for l in tobase10lines:
	f.write(l + "\n")
for l in frombase10lines:
	f.write(l + "\n")
for l in frombaseatoblines:
	f.write(l + "\n")
f.close()


if includeOverflow:
	per = testcases/4
else:
	per = testcases/3
per = int(per)

if includeOverflow:
	for x in range(1,per):
		testlist.append(overflowlines[random.randint(0,len(overflowlines)-1)])
for x in range(1,per):
	testlist.append(tobase10lines[random.randint(0,len(tobase10lines)-1)])
for x in range(1,per):
	testlist.append(frombase10lines[random.randint(0,len(frombase10lines)-1)])
for x in range(1,per):
	testlist.append(frombaseatoblines[random.randint(0,len(frombaseatoblines)-1)])

for x in range(1,per):
	num = random.randint(0,999)
	num = str(num)
	digit = int(num[random.randint(0,len(num)-1)])
	a = random.randint(0,digit)
	b = 10
	line = "tricky inputs;"
	line += num + "," + str(a) + "," + str(b) + ";" + "999" + ";" + str(cycles)
	trickyinputslist.append(line)

f = open("batch/trickyinputs.batch", "w")
for l in trickyinputslist:
	f.write(l + "\n")
f.close()

if trickyinputs:
	for i in trickyinputslist:
		testlist.append(i)

f = open("batch/testcases.batch", "w")
for l in testlist:
	f.write(l + "\n")
f.close()