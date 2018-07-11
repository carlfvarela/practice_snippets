#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 si et
import sys
import random


class Event:

    def __init__(self, date, location, num_pilots_n):

        self.date = date
        self.location = location
        self.num_pilots_n = int(num_pilots_n)

    def __str__(self):
        return str(self.__class__) + ": " + str(self.__dict__)

    @classmethod
    def from_input(cls):
        date = input('Date: ')

        location = input('Choose spot: \n \
                    teste1 (1)\n \
                    teste2 (2)\n\
                    teste3 (3)\n ')
        num_pilots_n = input('Choose number of pilots: \n \
                1 \n \
                2 \n \
                3 \n \
                4 \n ')

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
            num = random.randint(1, 50)
            #Pilot(num, first, last)
            # pilots.append(pilot.first)

            pilot_list.append(Pilot(num, first, last))
            print (pilot_list[0].__dict__)

            #pilots = dict(zip(pilot_list))

            i += 1
        print (pilot_list)


class Pilot:

    def __init__(self, num, first, last):
        self.num = int(num)
        self.first = first
        self.last = last


event1 = Event.from_input()
print("---------------------------")
print(event1.location)
print("---------------------------")
print("---------------------------")
event1.addPilot(event1.num_pilots_n)
print(event1)
