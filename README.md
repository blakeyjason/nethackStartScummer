# nethackStartScummer
Psst - wanna cheat and start with a good wizard in nethack?

This script uses Expect to do the dirty work.  You might need to install it with:

sudo pip3 install pexpect

This script will run nethack over and over until the character that is generated has items matching the defined list.  It then saves the character, and lets you know.  By default, it tries to create a neutral human wizard with:

1. A scroll of identify
2. A spellbook of charm monster
3. A magic marker


It's a bit rough, but does work.  On my old laptop, it takes about a second per try.

You can set your character preferences in the configuration section inside the script.


Tested on Nethack version 3.6.1, Python 3.7.5



NOTE: If your list of wanted items gets long, it can take many, MANY iterations before you get your character.

Thanks,
jason
