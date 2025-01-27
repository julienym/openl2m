.. OpenL2M - Open Layer 2 Management documentation entry file, created by
   sphinx-quickstart on Mon Sep 16 08:48:33 2019.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

.. image:: _static/openl2m_logo.png

======================
What Is New In OpenL2M
======================

* v3.0 introduces a REST API. This allows for remotely making changes to devices without needing to know the underlying vendor.
  Read the API section of the documentation for more details.

* v2.4 upgrades the Django framework to v4.2 LTS

* v2.3 adds support for Juniper Junos devices.

* v2.2 adds support for Aruba AOS-CX switches.

* v2.1 implements command templates, a controlled method to give users variable input on commands.
  This gives tremendous flexibility in giving users in a controlled fashion more visibility into the device.
  See the Configuration section for more.

* v2.0 implements a new plug-in API for add-on device drivers.
  This makes is easy to add support for any kind of network device,
  whether the interface is SSH, REST, NetConf, or other methods.
  See more in the development section below.


:doc:`Please read the release notes for more details on each release. <releases/index>`