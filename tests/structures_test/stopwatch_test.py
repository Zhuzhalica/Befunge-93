import os
import sys
import unittest

sys.path.append(os.getcwd())

from structures.stopwatch import Stopwatch


class Stopwatch_tests(unittest.TestCase):
    def test_correct_time_non_stop(self):
        sw = Stopwatch()
        sw.start()
        time1 = sw.time_per_second()
        time2 = sw.time_per_second()
        self.assertLess(time1, time2)

    def test_correct_time_stop(self):
        sw = Stopwatch()
        sw.start()
        sw.stop()
        time1 = sw.time_per_second()
        time2 = sw.time_per_second()
        self.assertEqual(time1, time2)

    def test_correct_time_non_stop_and_stop(self):
        sw = Stopwatch()
        sw.start()
        time1 = sw.time_per_second()
        sw.stop()
        time2 = sw.time_per_second()
        self.assertLess(time1, time2)

    def test_correct_time_without_start(self):
        sw = Stopwatch()
        time = sw.time_per_second()
        self.assertEqual(0, time)

    def test_correct_stop(self):
        sw = Stopwatch()
        sw.stop()
        time = sw.time_per_second()
        self.assertEqual(0, time)

    def test_correct_stop(self):
        sw = Stopwatch()
        sw.start()
        sw.stop()
        time = sw.time_per_second()
        sw2 = Stopwatch()
        sw2.stop()
        time2 = sw2.time_per_second()
        self.assertGreater(time, time2)

    def test_correct_break(self):
        sw = Stopwatch()
        sw2 = Stopwatch()
        sw.start()
        sw2.start()
        sw.timeout()
        for i in range(1000):
            pass
        sw.resume()
        sw.stop()
        sw2.stop()
        time = sw.time_per_second()
        time2 = sw2.time_per_second()
        self.assertLess(time, time2)
