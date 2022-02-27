#!/usr/bin/env python
# -*- coding: utf-8 -*-
from datetime import datetime
import re


class TimeChecker:
    __parser_expr = r'(?P<day>\w+):\s*(?P<start>\d+)-(?P<end>\d+)'

    def __init__(self, conf):
        self.__ls = []
        for it in re.finditer(self.__parser_expr, conf):
            self.__ls.append(it.groupdict())

    def check(self, date):
        day, time = date.strftime('%a %H%M').split(' ')
        it = next(filter(lambda a: a['day'] == day and a['start'] <= time <= a['end'], self.__ls), None)
        return bool(it)


if __name__ == '__main__':
    checker = TimeChecker('Mon: 1201-1400 Tue: 0900-1100 Fri: 0000-2400 Sun: 0000-0100')
    is_free = checker.check(datetime.now())
    print(is_free)

