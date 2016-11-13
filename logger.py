#!/usr/bin/python

"""
    @uthor: John Gallo
    Logger library
"""

import time
import os
import sys


class Logger(object):
    """ Logger objects that can be used to log events at varying priority levels """

    priorities = {'CRITICAL': 1, 'ERROR': 2,
                  'WARNING': 3, 'INFO': 4, 'DEBUG': 5}
    log_line_spacer = 4

    def __init__(self, logfile, priority='CRITICAL', datetime=True, scriptname=True):
        """ Initialize Logger object """

        self.logfile = logfile
        self.priority = self.set_priority(priority)
        self.datetime = self.set_datetime(datetime)
        self.scriptname = self.set_scriptname(scriptname)

    def set_priority(self, priority):
        """ Set Logger instance priority """
        try:
            self.priority = Logger.priorities[priority]
            return Logger.priorities[priority]

        except Exception as e:
            raise ValueError('Priority must be one of: {}'.format(
                sorted(Logger.priorities, key=Logger.priorities.get)))

    def set_datetime(self, datetime):
        if self.check_type_bool(datetime):
            self.priority = time.ctime()
            return time.ctime()
        else:
            return ''

    def set_scriptname(self, scriptname):
        if self.check_type_bool(scriptname):
            self.scriptname = os.path.basename(sys.argv[0])
            return os.path.basename(sys.argv[0])
        else:
            return ''

    def check_type_bool(self, var):
        """ Check if var is of type Bool """
        if isinstance(var, bool):
            return var
        else:
            raise TypeError('"{}" must be of type bool'.format(var))

    def write_log(self, logevent):
        """ Write log to disk """
        try:
            with open(self.logfile, 'a') as fh:
                fh.write("{0}{3}{1}{3}{2}\n".format(
                    self.datetime, self.scriptname, logevent, ' ' * Logger.log_line_spacer))
        except IOError as e:
            raise IOError('Cannot open file: {}'.format(e))

    def debug(self, logevent):
        if self.priority == 5:
            self.write_log(logevent)

    def info(self, logevent):
        if self.priority >= 4:
            self.write_log(logevent)

    def warning(self, logevent):
        if self.priority >= 3:
            self.write_log(logevent)

    def error(self, logevent):
        if self.priority >= 2:
            self.write_log(logevent)

    def critical(self, logevent):
        if self.priority >= 1:
            self.write_log(logevent)
