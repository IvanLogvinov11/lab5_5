#!/usr/bin/env python3
# -*- coding: utf-8 -*-
if __name__ == '__main__':

    for b in range(11):
        for k in range(21):
            t = 100 - b - k
            if 10*b+5*k+0.5*t==100: print(b, k, t)