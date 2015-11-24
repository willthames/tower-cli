# Copyright 2015, Ansible, Inc.
# Luke Sneeringer <lsneeringer@ansible.com>
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

import click

from tower_cli import models, resources
from tower_cli.utils import types, debug
from tower_cli.api import client
from tower_cli.conf import settings


class Resource(models.Resource):
    cli_help = 'Manage inventory within Ansible Tower.'
    endpoint = '/inventories/'
    identity = ('organization', 'name')

    name = models.Field(unique=True)
    description = models.Field(required=False, display=False)
    organization = models.Field(type=types.Related('organization'))
    variables = models.Field(required=False, display=False, yaml_vars=True)

    @resources.command
    @click.option('--hostvars', required=False, type=int,
                  help='Set to 1 to include host variables')
    def script(self, pk=None, format='json', **kwargs):
        """Return the script output for an inventory."""

        # set runtime value of format setting
        settings.format = format

        # pull out dictionary of values to pass in request
        payload = dict(
            (k, kwargs[k]) for k in ['hostvars'] if k in kwargs
        )

        # if primary key not given, look up via the standard get routine
        if not pk:
            get_resp = self.get(**kwargs)
            pk = get_resp['id']

        # make the request to /inventories/pk/script/
        debug.log('Getting script for inventory.', header='details')
        script_url = '%s%d/script/' % (self.endpoint, pk)
        r = client.get(script_url, params=payload)
        resp = r.json()

        return resp
