#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: Carlton Joseph
"""
import asyncio
import websockets

async def hello():
    async with websockets.connect('ws://localhost:8765') as websocket:

        name = input("What's your name? ")
        await websocket.send(name)
        print("> {}".format(name))

        greeting = await websocket.recv()
        print("< {}".format(greeting))


def main():
    """
    Description
    """
    asyncio.get_event_loop().run_until_complete(hello())

if __name__ == "__main__":
    main()
