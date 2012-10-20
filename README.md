The Polybius Square Encipher/Decipher
=====================================

		
Description:
------------
A Polybius Square is a table that allows someone to translate letters into numbers. To give a small level of encryption, this table can be randomized and shared with the recipient. In order to fit the 26 letters of the alphabet into the 25 spots created by the table, the letters V and W are usually combined.
	
![Schema](http://boubakr92.files.wordpress.com/2012/09/square.png)
	
Each letter can be represented by a group of two numbers: that of his line and that of his column. So "A"=11, "E"=15, "U"=51 ...

Features:
---------
+ Encipher a plaintext
+ Decipher a ciphertext

Requirements:
-------------
+ Python 3.x

Installation:
-------------
Download the package and extract it, then:
```
$ cd package_directory
$ python setup.py build
$ sudo python setup.py install
```
Using pip:
```
$ pip install polybius
```

Usage:
------
The simple example for using Polybius Square:
```
>>> from polybius import Polybius
>>> myPolybius = Polybius()
>>> myPolybius.encipher("Boubakr")
12 35 51 12 11 31 43
>>> myPolybius.decipher("12 35 51 12 11 31 43")
BOUBAKR
```

Demo:
-----
```
$ cd package_directory
$ python3 main.py
```

More information:
-----------------
For more detailed (and up to date) instructions [see](http://polybius-square.sourceforge.net/).

Troubleshooting:
----------------
If you have any problem with The Polybius Square Encipher/Decipher don't hesitate to [contact me](http://boubakr92.wordpress.com/contact-us/).

License:
--------
Academic Free License (AFL)