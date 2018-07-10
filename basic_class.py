#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: ts=4 sts=4 sw=4 si et


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
                    Aqua (1)\n \
                    Famões (2)\n\
                    Expo (3)\n ')
        num_pilots_n = input('Choose number of pilots: \n \
                1 \n \
                2 \n \
                3 \n \
                4 \n ')
        try:
            location in range(1, 3)

            if location == 1:
                location = "Aqua"
            elif location == 2:
                location = "Famões"
            elif location == 3:
                location == "Expo"
            else:
                location = None
                raise Exception
        except Exception:
            print("deu merda")

        finally:
            return cls(date, location, int(num_pilots_n))

    def addPilot(self, num_pilots_n):
        # i = 0
        # for i in range(0, num_pilots_n):
        #     i = i + 1
        #     pilots = []
        #     #print (num_pilots_n)
        #     pilots.append(Pilot(self, Pilot))

        # print (pilots)
        # print (i)
        first = input("First name: ")
        last = input("last name: ")
        print(type(num_pilots_n))
        i = 0
        pilots = []
        while i <= num_pilots_n:
            pilot = Pilot(first, last)
            pilots.append(pilot)
            i += 1

        print(pilot)

    # def registerPilot(self, num_pilots_n):
    #     i = 0
    #     for i in range(1, num_pilots_n):
    #         i = i + 1
    #         return Pilot.addPilot()


class Pilot:
    def __init__(self, first, last):
        self.first = first
        self.last = last

    @classmethod
    def pilot_input(clspilot):
        first = input("First name: ")
        last = input("last name: ")
        return cls(first, last)


event1 = Event.from_input()
print("---------------------------")
print(event1.location)
print("---------------------------")
print("---------------------------")
event1.addPilot(event1.num_pilots_n)
print(event1)
