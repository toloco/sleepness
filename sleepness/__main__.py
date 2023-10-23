#!/usr/bin/env python3


import argparse
import math
import time
from datetime import datetime

import pyautogui
from tqdm import tqdm

pyautogui.FAILSAFE = False


def parse_args():
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--timer",
        type=int,
        default=0,
        help="Timer (in minutes), 0 means forever, default is forever.",
    )

    parser.add_argument(
        "--length",
        type=int,
        default=10,
        choices=range(1, 1000),
        metavar="[1-1000]",
        help="Lenght of movement (in secs), default is 10.",
    )

    parser.add_argument(
        "--wait",
        type=int,
        default=10,
        choices=range(10, 1000),
        metavar="[10-1000]",
        help="Waiting time between movements (in secs), default is 10.",
    )

    parser.set_defaults(feature=True)

    return parser.parse_args()


def nod(length: float):
    pos = pyautogui.position()

    SCREEN_SIZE = pyautogui.size()

    x = ((pos.x * 177) % (SCREEN_SIZE[0] * 0.8)) + SCREEN_SIZE[0] * 0.1
    y = math.pow(pos.y, 21) % (SCREEN_SIZE[1] * 0.8) + SCREEN_SIZE[1] * 0.1
    pyautogui.moveTo(x, y, duration=length, tween=pyautogui.easeInOutQuad)


def runner():
    args = parse_args()

    if args.timer <= 0:
        print(f"Run forever")
        while True:
            time.sleep(args.wait)
            nod(float(args.length))
            print(f"{datetime.now().time()} ping")

    iters = int((args.timer * 60) / (args.wait + args.length))
    for i in tqdm(
        iterable=range(iters),
        total=iters,
        colour="BLUE",
        leave=False,
        bar_format="{l_bar}{bar}",
    ):
        time.sleep(args.wait)
        nod(float(args.length))


def main():
    try:
        runner()
    except KeyboardInterrupt:
        pass
    exit(0)
