#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 si et

import sys


class Event:
    def __init__(self, date, location, num_pilots_n):

        self.date = date
        self.location = location
        self.num_pilots_n = num_pilots_n

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    @classmethod
    def from_input(cls):
        date = input('Date: ')

        location = str(input('Choose spot: \n \
                    test1 (1)\n \
                    test2 (2)\n\
                    test3 (3)\n '))
        num_pilots_n = input('Choose number of pilots: \n \
                1 \n \
                2 \n \
                3 \n \
                4 \n ')
        try:
            location in range(1, 3)

            if location == 1:
                location = "test1"
            elif location == 2:
                location = "test2"
            elif location == 3:
                location == "test3"
            else:
                location = None
                raise Exception
        except Exception:
            print("deu merda")

        finally:
            return cls(date, location, num_pilots_n)

    def addPilot():
        first = input("First name: ")
        last = input("last name: ")
        return Pilot.newPilot(first, last)


class Pilot:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    # @classmethod
    # def pilot_input(clspilot):
    #     first = input("First name: ")
    #     last = input("last name: ")
    #     return cls(first, last)

    def newPilot():

        print(num_pilots_n)
        i = 0
        pilots = []
        while i <= num_pilots_n:
            print (num_pilots_n)
            pilot = Pilot(first, last)
            pilots.append(pilot)
            i += 1
            print(pilot)


event1 = Event.from_input()
print ("---------------------------")
print (event1.location)
print ("---------------------------")
print ("---------------------------")

event1.addPilot
