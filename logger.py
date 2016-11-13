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


"""
5.1          class Logger:  this class constructs objects that can be used to log events at varying priority levels. 
from mylib import Logger

mylog = Logger('logfile.txt', priority='DEBUG',
               datetime=True, scriptname=True)

mylog.debug('will log if priority is DEBUG only')
mylog.info('will log if priority is INFO or DEBUG')
mylog.warning('will log if priority is INFO,DEBUG,WARNING')
mylog.error('will log if priority is INFO,DEBUG,WARNING,ERROR)
mylog.critical('will log in any case')

Logger produces an object that can flexibly append to a file specified in its constructor (use open(filename, 'a')).  Its behavior is modified by the three optional arguments (shown here with the defaults):  

priority='DEBUG' sets the "logging priority" which determines whether subsequent logging calls to debug(), info(), warning(), error() or critical() will be written.  These four priority levels are specified by the string arguments 'DEBUG', 'INFO', 'WARNING', 'ERROR' and 'CRITICAL'.  These levels are listed from the most exclusive to the least, so for example:
                                               i.   at priority='DEBUG', all five method calls will write to the log
                                              ii.   at priority='INFO', only info(), warning(), error() and critical() will write
                                             iii.   at priority='WARNING', only warning(), error() and critical() will write
                                            iv.   at priority='ERROR', only error() and critical() will write
                                             v.   at priority='CRITICAL', only critical() will write
The concept here is that we can fill our program with log messages at different levels of importance; during development of the script we'll want to log everything including debug messages, but once the script is in production we'll only want to log higher priority messages (perhaps just error() and critical() messages). 
datetime=True determines whether the date and time should be prepended to the log message.  A simple datetime string can be obtained from the time module
print time.ctime()      # Fri Oct 23 15:24:22 2015

filename=True determines whether the name of the script logging the messages should be prepended to the message.  This is obtained from the first element of sys.argv, and in fact should be separated from any path info:
filename = os.path.basename(sys.argv[0])

The os.path.basename() call would take ./test.py and return test.py.  
A full log message would look like this:
Fri Oct 23 15:24:22 2015  test.py  this is my log message

Exceptions:
If the file cannot be opened, raise an IOError exception with a custom message. 
If the 'priority' value is incorrect, raise a ValueError exception.
You can also choose to raise TypeError if the datetime or scriptname are not booleans. 
 
Tips for success:
Please avoid repeated code!  This means you may want to place some code inside a reusable function, such as a function that writes to the file.  Don't open and close the file multiple times in your code!  Think in terms of reusability and modularity. 
The priority levels should probably be converted to an integer scale so you can use numeric comparisons to determine logging level (instead of comparing strings). 
Class variables in my solution are:  priorities (a dict of priority names to integers 1-5); log_line_spacer (a string of 4 spaces used to separate elements of a log line)
"""
