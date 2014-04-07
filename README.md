xchat-autoghost 0.1.0
======
There are a few scripts that claim to serve this purpose already around, but in my experience, none of them worked as soon as they ran into little problems. Thus, I decided to roll my own.

Attention: Currently, this script is inly tested on FreeNode and Mozilla servers. Unfortunately, NickServ and server messages are different from server to server, so there is no reliable way to make it work everywhere. If you notice that a particular function is not working, please message me with the relevant line, or commit it yourself!

Licensed GPLv2, so have fun.

David Reis, Apr 2014

USAGE
======
Copy autoghost.py into your xchat configuration directory. (System-dependent; on Linux, it's ~/.xchat2.) Rest _should_ work automatically, provided that you set your desired nick and password correctly for the server in question.

HISTORY
======
0.1.0

- initial upload to github

TODO
======
- _Maybe_ find a better way to make this interoperable. Unlikely, though.

BUGS
======
- Surprisingly, at the moment none are known.
