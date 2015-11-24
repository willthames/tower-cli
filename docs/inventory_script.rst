Inventory Script Subcommand
===========================

The inventory script subcommand returns the output of dynamic inventory
scripts in JSON format by default. It can be invoked by either the primary
key or another set of parameters that uniquely specifies the inventory.

For example, if the inventory was named "QA_machines" and had an primary
key of 12, either of the following commands would be valid:

.. code:: bash

    $ tower-cli inventory script --name="QA_machines"

    $ tower-cli inventory script 12

These commands will return text in JSON format.

Example Usage
-------------

As a part of bash scripting (or some other automated workflow), this
command can be leveraged to feed dynamic inventory into Ansible locally
from Ansible Tower.

Tower-cli will can act as a stand-in for a script that dynamically defines
inventory. For example, consider the following file named `tower-inventory.sh`.

.. code:: bash

    #!/bin/bash

    tower-cli inventory script $TOWER_INVENTORY_ID --hostvars=1

While in the same directory, the following command will list the hosts via
Ansible in its command-line usage.

.. code:: bash

    TOWER_INVENTORY_ID=12 ansible -i tower-inventory.sh all --list-hosts

Assuming the inventory pk is 12, this will give a list of hosts in that
inventory.
