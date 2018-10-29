from baseconverter import convert
import random
import os

testcases = 500

cycles = 5000
includeOverflow = True



overflowcomment = "overflow"
tobase10comment = "Into base 10"
frombase10comment = "From base 10"
frombaseatobcomment = "From base a to b"

overflowlines = []
tobase10lines = []
frombase10lines = []
frombaseatoblines = []

testlist = []

for base in range(2,11):
	for newbase in range(2,11):
		if base != newbase:
			for i in range(0,base):
				for j in range(0,base):
					for k in range(0,base):
						num = int(str(i)+str(j)+str(k))
						converted = convert(num,base,newbase)
						if converted < 1000:
							if newbase == 10:
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

f = open("batch/overflow.txt", "w")
for l in overflowlines:
	f.write(l + "\n")
f.close()
f = open("batch/tobase10.txt", "w")
for l in tobase10lines:
	f.write(l + "\n")
f.close()
f = open("batch/frombase10.txt", "w")
for l in frombase10lines:
	f.write(l + "\n")
f.close()
f = open("batch/frombaseatobaseb.txt", "w")
for l in frombaseatoblines:
	f.write(l + "\n")
f.close()

f = open("batch/count.txt", "w")
f.write(overflowcomment + ": " + str(len(overflowlines)) + "\n")
f.write(tobase10comment + ": " + str(len(tobase10lines)) + "\n")
f.write(frombase10comment + ": " + str(len(frombase10lines)) + "\n")
f.write(frombaseatobcomment + ": " + str(len(frombaseatoblines)) + "\n")
f.close()

f = open("batch/all.txt", "w")
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

f = open("batch/testcases.txt", "w")
for l in testlist:
	f.write(l + "\n")
f.close()