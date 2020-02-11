#!/usr/bin/python
import random;
import string;

file1 = open("foo.txt", "w+");
randStr = "";
for i in range(0, 10):
	randStr += random.choice(string.ascii_lowercase);
print randStr;
randStr += '\n';
file1.write(randStr);
file1.close();

file2 = open("bar.txt", "w+");
randStr = "";
for i in range(0, 10):
	randStr += random.choice(string.ascii_lowercase);
print randStr;
randStr += '\n';
file2.write(randStr);
file2.close();

file3 = open("zap.txt", "w+");
randStr = "";
for i in range(0, 10):
	randStr += random.choice(string.ascii_lowercase);
print randStr;
randStr += '\n';
file3.write(randStr);
file3.close();

randNum1 = random.randint(1, 42);
randNum2 = random.randint(1, 42);
print randNum1;
print randNum2;

print randNum1 * randNum2;
