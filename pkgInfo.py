#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
# Copyright (c) 2023 Honda Research Institute Europe GmbH
#
# This file is part of common_sense_for_robots.
#
# common_sense_for_robots is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# common_sense_for_robots is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with common_sense_for_robots.  If not, see <https://www.gnu.org/licenses/>.
#
"""
Custom package settings
"""

sqLevel = "basic"

sqOptInRules = ["PY03", "PY04"]

sqOptOutRules = ["DOC03", "GEN07"]

sqOptOutDirs = [".venv/"]

copyright = """\
#
# Copyright (c) 2023 Honda Research Institute Europe GmbH
#
# This file is part of common_sense_for_robots.
#
# common_sense_for_robots is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# common_sense_for_robots is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with common_sense_for_robots.  If not, see <https://www.gnu.org/licenses/>.
#
"""

sqComments = {
    "DOC03": "examples included in scripts",
    "GEN07": "simple demo, no need for unit tests",
}

# EOF
