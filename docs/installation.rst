============
Installation
============

To create a new project based on Bartacus create it with composer:

.. code-block:: bash

    composer create-project bartacus/bartacus-standard

It will install all necessary stuff for you.

TYPO3 Database Installation
===========================

To install TYPO3 itself, a helpful command of the TYPO3 console is
included:

.. code-block:: bash

    vendor/bin/typo3cms install:setup --site-setup-type='site'
    vendor/bin/typo3cms database:import < .misc/install.sql

Now you can login with your admin user.
