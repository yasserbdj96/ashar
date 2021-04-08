Ashar Encryption and decryption
==========================
This project is for data encryption with password protection.

.. image:: https://travis-ci.com/byRo0t96/ashar.svg?branch=main

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
0.5.4
-----
- Static encryption.
- Fix bugs.

0.5.3
-----
- Fix bugs.

0.5.0
-----
- First public release.

.. end changelog

.. image:: https://raw.githubusercontent.com/byRo0t96/byRo0t96/main/images/Ro0t-96_v.3.1.png
    :width: 100px
    :align: center
