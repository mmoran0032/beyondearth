beyondearth
===========

Getting mods to work with Civ:BE

Since I develop and game on Linux, many mods obtained through Steam and other
sources don't work since they were developed on Windows machines (for the most
part). As such, a case-sensitive file system will have problems with something
written for a case-insensitive file system.

It looks like Aspyr, during the port to Linux, ensured that any mod files would
be all lowercase, hopefully getting around a lot of the problems. Unfortunately,
some modders used regular casing within the MOD.modinfo file, which doesn't work
with Aspyr's scheme.

As such, I'm writing this to convert those files to hopefully work (with a
backup of the original file, just to be sure!)
