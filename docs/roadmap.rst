.. image:: _static/openl2m_logo.png

===============
Roadmap / To Do
===============

Planned improvements:
---------------------

* all planned improvements have been implemented!

Features Being Considered
-------------------------

Here are some other features we are considering implementing (*in no particular order!*)

* change user model, from standard user mode with separate profile table, to a new user class that has it all :-)

* support for Arista device via the eApi.

* Single-Sign-On (SSO) via SAML, and possibly OAUTH for authorization (switch group membership)
  with as primary SSO compatibility target Shiboleth SAML SSO. We plan to use the Python Social Auth library.

* IP v6 support, both for switch snmp access, and other informational tables.

* Tagged/Trunked ports tagged vlan management (we can do the untagged vlan now)

* hide change/submit buttons until form has changes (vlan, ifalias, etc.)

* make vendor support dynamic (i.e. discover at runtime what vendors are supported)

* test support for AES-192 and up. This will require Net-SNMP v5.8 (which is available on CentOS 8, Unbuntu 2020-LTS, and later)
