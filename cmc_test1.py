#!/usr/bin/env python
# -*- coding: utf-8 -*-
import configparser
from datetime import datetime


# This should be the class that runs all the things and those methods will be integrated to that class.
class TestFreeDrinkTime():
    def __init__(self):
        # read free drink times from the sample config file
        config = configparser.ConfigParser()
        config.read('sample_config.cfg')
        self.FREE_TIMES_STR = config['free_drink_times']['FREE_TIMES_STR']

        print('FREE_TIMES_STR:', self.FREE_TIMES_STR)

        self.free_times_dict = self.parse_free_times(self.FREE_TIMES_STR)


    def parse_free_times(self, free_times_str):
        # One date and time in string is 15 chars long.
        free_times_str_list = [free_times_str[i: i + 15] for i in range(0, len(free_times_str), 15)]

        free_times_dict = {}
        for item in free_times_str_list:
            interval_day = item[:3]
            interval_hour_start = item[5:9]
            interval_hour_end = item[10:14]

            free_times_dict[interval_day.upper()] = [interval_hour_start, interval_hour_end]

        return free_times_dict


    def test_free_drink_time(self, now_str):
        current_weekday = now_str[:3]
        current_hour = now_str[4:]

        try:
            free_time_range = self.free_times_dict[current_weekday.upper()]
            return (current_hour >= free_time_range[0]) and (current_hour <= free_time_range[1])
        except:
            return False


if __name__ == "__main__":
    app = TestFreeDrinkTime()

    now = datetime.now()
    now_str = now.strftime('%a:%H%M')

    # the main action is here
    is_now_free = app.test_free_drink_time(now_str)

    print('now is a free time?:', is_now_free)




