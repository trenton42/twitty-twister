#!/usr/bin/env python
"""

Copyright (c) 2008  Dustin Sallings <dustin@spy.net>
"""

import os
import sys

from twisted.internet import reactor, protocol, defer, task

from twittytwister import twitter

def gotEntry(msg):
    print "Got a entry from %s: %s" % (msg.sender_screen_name, msg.text)

twitter.Twitter(sys.argv[1], sys.argv[2]).direct_messages(gotEntry).addBoth(
    lambda x: reactor.stop())

reactor.run()
