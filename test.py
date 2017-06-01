#!/usr/bin/python
# -*- coding: utf8 -*-


s = 'akdsakjhasjkdhkjashdaskjhfoopnnmioqouiew'*100000

for i in s:
    for j in s:
        s.count(j)
