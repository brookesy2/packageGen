# packageGen
Create a package.xml from a directory.

To run:
python3 packageGen.py --path=SOME PATH

Limitations:
Doesn't do anything folder based, reports etc.

Also the org I did the describe on probably doesn't have all features enabled, so it may miss some things.

Files:

* folderHelper.py - Just stores the output from a describe.
* mappingHelper.py - Maps between folder names and xml names. Also contains suffix information and dir names
* packageGen.py - Main executable.
