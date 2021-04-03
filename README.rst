Ashar Encryption and decryption
==========================
This project is for data encryption with password protection.

Installation
============

.. code::

    pip install ashar

Usage
=====
.. code:: python

    from ashar import ashar

    #For encryption
    p1=ashar("<PASSWORD>","<TEXT>").encode()
    print(p1)
    
    #To decrypt
    p2=ashar("<PASSWORD>","<ENCRYPTED_TEXT>").decode()
    print(p2)

.. begin changelog

Changelog
=========
0.5.3
-----
- Fix bugs.

0.5.0
-----
- First public release.

.. end changelog
