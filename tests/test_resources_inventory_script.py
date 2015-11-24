# Copyright 2015, Red Hat, Inc.
# Alan Rominger <arominger@ansible.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import tower_cli
from tower_cli.api import client

from tests.compat import unittest


class UpdateTests(unittest.TestCase):
    """A set of tests for inventory script retrevial
    tower-cli inventory script inventory_id
    """
    def setUp(self):
        self.inventory = tower_cli.get_resource('inventory')

    def test_lookup_pk(self):
        """Test retrevial of an inventory script output by its pk
        """
        result_dict = {'all': {'hosts': []}}
        with client.test_mode as t:
            t.register_json('/inventories/12/script/',
                            result_dict, method='GET')
            result = self.inventory.script(pk=12)
            assert result == result_dict

    def test_lookup_name(self):
        """Test retrevial of an inventory script output by its name
        """
        result_dict = {'all': {'hosts': []}}
        with client.test_mode as t:
            t.register_json('/inventories/12/script/',
                            result_dict, method='GET')
            t.register_json(
                '/inventories/', {'count': 1, 'results': [{'id': 12}]},
                method='GET')
            result = self.inventory.script(name='foobar_inventory')
            assert result == result_dict
