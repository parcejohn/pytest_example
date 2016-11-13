#!/usr/bin/env python

"""
    @uthor: John Gallo
    Logger library Tests (py.test)
"""

import os
import pytest
import time
import re


from logger import Logger

class TestLogger(object):

    logfile = 'test.log'
    expected_priorities = ['INFO', 'DEBUG', 'CRITICAL', 'WARNING', 'ERROR']
    unexpected_priorities = ['BAD', 'unknown', 3]

    def setup_class(self):
        open(self.logfile, 'a').close()
        self.logobj = Logger(self.logfile)


    def teardown_class(self):
        # Comment out line and use pass
        # if you want to see the test log file
        # pass
        os.remove(self.logfile)
        


    def test_set_priority(self):
        # Expected output
        for priority in self.expected_priorities:
            self.logobj.set_priority(priority)
            assert priority in self.expected_priorities

        # Unexpected output
        # for priority in self.unexpected_priorities:
        #     self.logobj.set_priority(priority)
        #     assert priority in self.expected_priorities


    def test_set_datetime(self):
        assert self.logobj.set_datetime(False) == ''
        assert self.logobj.set_datetime(True) == time.ctime()

        # Unexpected output
        # assert self.logobj.set_datetime(3)
        # assert self.logobj.set_datetime()


    def test_set_scriptname(self):
        assert self.logobj.set_scriptname(False) == ''
        assert str(self.logobj.set_scriptname(True))


    def test_check_type_bool(self):
        assert self.logobj.check_type_bool(True) == True
        assert self.logobj.check_type_bool(False) == False

        # Unexpected output
        # assert self.logobj.check_type_bool('test') == True


    def test_write_log(self):
        self.logobj.write_log('test_write_log')
        assert re.search('test_write_log', open(self.logfile).read())

        # Unexpected output
        # self.logobj.write_log()
        # assert re.search(True, open(self.logfile).read()) 


    def test_debug(self):
        self.logobj.set_priority('DEBUG')
        self.logobj.debug('test_debug')
        assert re.search('test_debug', open(self.logfile).read())

        # Unexpected output
        # self.logobj.set_priority('CRITICAL')
        # self.logobj.debug('test_debug_with_critical_priority')
        # assert re.search('test_debug_with_critical_priority', open(self.logfile).read())


    def test_info(self):
        self.logobj.set_priority('INFO')
        self.logobj.info('test_info')
        assert re.search('test_info', open(self.logfile).read())

        # Unexpected output
        # self.logobj.set_priority('CRITICAL')
        # self.logobj.info('test_info_with_critical_priority')
        # assert re.search('test_info_with_critical_priority', open(self.logfile).read())


    def test_warning(self):
        self.logobj.set_priority('WARNING')
        self.logobj.warning('test_warning')
        assert re.search('test_warning', open(self.logfile).read())

        # Unexpected output
        # self.logobj.set_priority('CRITICAL')
        # self.logobj.warning('test_warning_with_critical_priority')
        # assert re.search('test_warning_with_critical_priority', open(self.logfile).read())


    def test_error(self):
        self.logobj.set_priority('ERROR')
        self.logobj.error('test_error')
        assert re.search('test_error', open(self.logfile).read())

        # Unexpected output
        # self.logobj.set_priority('CRITICAL')
        # self.logobj.error('test_error_with_critical_priority')
        # assert re.search('test_error_with_critical_priority', open(self.logfile).read())


    def test_critical(self):
        self.logobj.set_priority('CRITICAL')
        self.logobj.critical('test_critical')
        assert re.search('test_critical', open(self.logfile).read())
