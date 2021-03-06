# -*- coding: utf-8 -*-

# Copyright 2010-2020 OpenStack Foundation
#
# Licensed under the Apache License, Version 2.0 (the "License"); you may
# not use this file except in compliance with the License. You may obtain
# a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
# WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
# License for the specific language governing permissions and limitations
# under the License.

from sushycli import base


class BaseParserMixIn(base.BaseParserMixIn):
    """Common bits and pieces of all `sushycli manager` commands.

    Does not implement any CLI command by its own.
    """
    MANAGER_ID_HELP = (
        'The canonical path to the Manager resource to interact with. It '
        'should include the root service, version and the unique resource '
        'path to a Manager. For example: /redfish/v1/Managers/BMC'
    )

    def add_parser_options(self, parser):

        parser = super(BaseParserMixIn, self).add_parser_options(parser)

        parser.add_argument(
            '--manager-id',
            help=self.MANAGER_ID_HELP)

        return parser


class BaseCommand(BaseParserMixIn, base.BaseCommand):
    """Common base for all sushycli manager status commands"""


class BaseLister(BaseParserMixIn, base.BaseLister):
    """Common base for all sushycli manager listing commands"""
