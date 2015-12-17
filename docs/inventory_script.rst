Inventory Script Subcommand
===========================

The tower-cli inventory script subcommand returns information about an
inventory in JSON format, consistent with Ansible standards for dynamic
inventory. It can be invoked by either the primary
key or another set of parameters that uniquely specifies the inventory.

For example, if the inventory was named ``QA_machines`` and had an primary
key of ``12``, either of the following commands would be valid:

.. code:: bash

    $ tower-cli inventory script --name="QA_machines"

or

.. code:: bash

    $ tower-cli inventory script 12

These commands will return text in JSON format.

Usage
-----

This command can be leveraged to feed dynamic inventory into Ansible locally
from Ansible Tower.

This can be implemented by feeding the command's output into Ansible through
the ```-i``` flag. However, an executable file is needed to act as a wrapper
in this usage. One possible option to do this is described below.

Manual Bash Wrapper Setup
~~~~~~~~~~~~~~~~~~~~~~~~~

Create a file named ```tower-inventory.sh`` with the following contents.

.. code:: bash

    #!/bin/bash

    tower-cli inventory script $TOWER_INVENTORY_ID

Save the file, and change its permissions to be executable.

.. code:: bash

    chmod +x tower-inventory.sh

While in the same directory, the following command will list the hosts via
Ansible in its command-line usage.

.. code:: bash

    TOWER_INVENTORY_ID=12 ansible -i tower-inventory.sh all --list-hosts

Assuming the inventory pk is 12, this will give a list of hosts in that
inventory.
