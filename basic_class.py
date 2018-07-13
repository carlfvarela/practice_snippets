#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 si et
import sys
import time
import os
import random


class Event:

    pilot_list = []

    freqList = {'R1': 1111, 'R2': 2222, 'R3': 3333, 'R4': 44444}

    def __init__(self, date, location, num_pilots_n):

        self.date = date
        self.location = location
        self.num_pilots_n = int(num_pilots_n)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def eventLocation(self):
        return '{}'.format(self.location)

    @classmethod
    def from_input(cls):
        date = input('Date: ')

        location = input('Choose spot: \n \
                    teste1 (1)\n \
                    teste2 (2)\n\
                    teste3 (3)\n ')
        num_pilots_n = input('Choose number of pilots: ')

        try:
            location in range(1, 3)
            if location == 1:
                location = "teste1"
            elif location == 2:
                location = "teste2"
            elif location == 3:
                location = "teste3"
            else:
                location = None
                raise Exception
        except Exception:
            print("deu merda")

        finally:
            return cls(date, location, int(num_pilots_n))

    def addPilot(self, num_pilots_n):
        i = 1
        while i <= num_pilots_n:
            num = i
            print("Pilot nº %s" % i)
            print("Enter first name")
            first = sys.stdin.readline()
            print("ĺast")
            last = sys.stdin.readline()
            print("---------------------------")
            self.pilot_list.append(Pilot(num, first.rstrip('\n'), last.rstrip('\n')))
            i += 1
            print ("Pilot registered sucessfully")
            print("---------------------------")
            time.sleep(2)

    def getPilotList(self):
        print ("Registered pilots")
        for i in self.pilot_list:
            print (i.__str__())

    def setFreqList(self):
        return self.freqList.pop(random.choice(self.freqList.items()))

        # return random.sample(self.freqList)


class Pilot():

    def __init__(self, num, first, last):
        self.num = int(num)
        self.first = first
        self.last = last

    def __str__(self):
        return '{} - {} {}'.format(self.num, self.first, self.last)

    def getName(self):
        return '{} {}'.format(self.first, self.last)

    def getNum(self):
        return self.num


event1 = Event.from_input()
print("---------------------------")
print(event1.location)
print("---------------------------")
print("---------------------------")
event1.addPilot(event1.num_pilots_n)
print (event1.getPilotList())
event1.setFreqList()
#print (event1.freqList)
