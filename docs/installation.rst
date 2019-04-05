============
Installation
============

To create a new project based on Bartacus create it with composer and Symfony Flex:

.. code-block:: bash

    $ composer create-project bartacus/website-skeleton

It will install all necessary stuff for you. Due to missing flex recipes for now, you have to create most of the TypoScript and site configuration for yourself.

TYPO3 Database Installation
===========================

To install TYPO3 itself, a helpful command of the TYPO3 console is included:

.. code-block:: bash

    $ vendor/bin/typo3cms install:setup --site-setup-type='site'

Now you can login with your admin user.
