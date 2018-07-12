#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 si et
import sys


class Event:

    pilot_list = []

    def __init__(self, date, location, num_pilots_n):

        self.date = date
        self.location = location
        self.num_pilots_n = int(num_pilots_n)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    def eventLocation(self):
        return '{} {}'.format(self.first, self.last)

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
                location == "teste3"
            else:
                location = None
                raise Exception
        except Exception:
            print("deu merda")
        finally:
            return cls(date, location, int(num_pilots_n))

    def addPilot(self, num_pilots_n):
        i = 1
        pilot_list = []
        while i <= num_pilots_n:
            print("Pilot nº %s" % i)
            print("Enter first name")
            first = sys.stdin.readline()
            print("ĺast")
            last = sys.stdin.readline()
            print("---------------------------")

            num = i
            self.pilot_list.append(Pilot(num, first.rstrip('\n'), last.rstrip('\n')))
            print ("Pilot registered sucessfully")
            i += 1

    def getPilotList(self):
        print ("Registered pilots")
        for i in self.pilot_list:
            print (i.__str__())


class Pilot():

    def __init__(self, num, first, last):
        self.num = int(num)
        self.first = first
        self.last = last

    def __str__(self):
        return '{} - {} {}'.format(self.num, self.first, self.last)

    def getName(self):
        return '{} {}'.format(self.first, self.last)


event1 = Event.from_input()
print("---------------------------")
print(event1.location)
print("---------------------------")
print("---------------------------")
event1.addPilot(event1.num_pilots_n)
print (event1.getPilotList())
