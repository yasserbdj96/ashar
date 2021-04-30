Ashar Encryption and decryption
==========================
This project is for data encryption with password protection.

.. image:: https://travis-ci.com/byRo0t96/ashar.svg?branch=main
.. image:: https://img.shields.io/github/issues/byRo0t96/ashar
.. image:: https://img.shields.io/github/forks/byRo0t96/ashar
.. image:: https://img.shields.io/github/stars/byRo0t96/ashar
.. image:: https://img.shields.io/badge/license-Apache--2.0-green.svg


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

1.0.0
-----
- Fix bugs.

0.5.5
-----
- Fix bugs.

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

.. image:: https://ko-fi.com/img/githubbutton_sm.svg
   :target: https://ko-fi.com/L3L34CEPV
