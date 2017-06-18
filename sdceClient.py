#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import asyncio
import websockets

file = '/home/carltonj2000/cj/cj_CoursesCodeHelp/cj2017CoursesCodeHelp/selfDrivingCarTerm2/CarND-Extended-Kalman-Filter-Project/build/tele.txt'
data = []

async def hello():
    async with websockets.connect('ws://localhost:4567') as websocket:
        with open(file) as f:
            lines = f.readlines()

        for line in lines:
            await websocket.send("42" + line.strip())
            #print("> {}".format(line))

            greeting = await websocket.recv()
            #print("< {}".format(greeting))


def main():
    """
    Description
    """
    asyncio.get_event_loop().run_until_complete(hello())

if __name__ == "__main__":
    main()
