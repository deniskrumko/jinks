Jira Issues + Links = Jinks
===========================

.. image:: https://img.shields.io/pypi/v/jinks.svg
    :target: https://pypi.org/project/jinks/
    :alt: PyPI version

.. image:: https://img.shields.io/pypi/pyversions/jinks.svg
    :target: https://pypi.org/project/jinks/
    :alt: Python versions

.. image:: https://img.shields.io/pypi/l/jinks.svg
    :target: https://raw.githubusercontent.com/deniskrumko/jinks/master/LICENSE
    :alt: License


Command line interface for opening links to JIRA-related things

PROJECT IN DEVELOPMENT! NO USAGE YET!
=====================================

Do you need it?
^^^^^^^^^^^^^^^

This script allows to quickly open different links, such as JIRA, K8S and
other.

P.S. This CLI is needed only to HomeCredit Marketplace fellows ;)

That's how output will look like:

.. code-block:: bash

    MRPL-3199

    1  ADMIN     https://admin-jinks-3199.homecred.it
    2  FRONT     https://market-jinks-3199.homecred.it
    3  API       https://api-jinks-3199.homecred.it
    4  JIRA      https://jira.homecred.it/browse/MRPL-3199
    5  K8S       https://k8s.homecred.it/#!/overview?namespace=MRPL-3199

Then you press number on keyboard, and link opens in a browser. Voila!

Installation
^^^^^^^^^^^^
.. code-block:: bash

    pip3 install jinks

How to use
^^^^^^^^^^

For example, your project code in Jira is *JINK*

.. code-block:: bash

    jinks 1234  # links for JINK-1234 issue
