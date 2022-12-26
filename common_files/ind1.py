#!/usr/bin/env python3
# -*- coding: utf-8 -*-


if __name__ == '__main__':

    s = int(input())
    if s==1:
        print(f"Я купил {s} карандаш" )
    elif 1<s<5:
        print(f"Я купил {s} карандаша")
    elif 5<s<11:
        print(f"я купил {s} карандашей")
    elif s==0:
        print(f"я купил {s} карандашей")
