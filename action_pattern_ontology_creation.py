#!/usr/bin/env python
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
Set up a TBox for action patterns and populate it
"""

import json
import os
import types

import owlready2 as o2
import uuid


def create_base_onto(iri: str, onto_file: str) -> None:
    onto = o2.get_ontology(iri)
    with onto:

        class Action(o2.Thing):
            comment = [
                "Corresponds best to a process in BFO.",
                (
                    "A transformation pattern that describes an action "
                    "and the things involved."
                ),
            ]

        class Object(o2.Thing):
            comment = [
                "Comprises objects, agents, and tools.",
                "Corresponds to an object in BFO.",
            ]

        class State(o2.Thing):
            comment = [
                "Reification of an object's state.",
                "Corresponds best to a quality in BFO.",
            ]

        class Location(o2.Thing):
            comment = ["Corresponds to a spatial region in BFO."]

        class Time(o2.Thing):
            comment = ["Corresponds to a temporal region in BFO."]

        class spatial_relation(o2.ObjectProperty):
            domain = [Object]
            range = [Object]

        class has_agent(o2.ObjectProperty):
            comment = [
                (
                    "Relates objects to an action pattern, "
                    "which serve as the agent executing the action."
                )
            ]
            domain = [Action]
            range = [Object]

        class has_object(o2.ObjectProperty):
            comment = [
                (
                    "Relates objects to an action pattern, which are affected "
                    "by the action, i.e., they are the objects."
                )
            ]
            domain = [Action]
            range = [Object]

        class has_tool(o2.ObjectProperty):
            comment = ["Relates objects to an action pattern, which serve as tools."]
            domain = [Action]
            range = [Object]

        class has_location(o2.ObjectProperty):
            domain = [Action]
            range = [Location]

        class has_time(o2.ObjectProperty):
            domain = [Action]
            range = [Time]

        class has_state(o2.ObjectProperty):
            domain = [Object]
            range = [State]

        class transforms_to(o2.ObjectProperty):
            domain = [Object]
            range = [Object]

        Action.is_a.extend(
            [
                has_agent.min(1, Object),
                has_object.min(1, Object),
                has_tool.min(0, Object),
                has_location.exactly(1, Location),
                has_time.exactly(1, Time),
            ]
        )
        Object.is_a.append(has_state.min(1, State))
        Object.is_a.append(spatial_relation.some(Object))

    onto.save(file=onto_file)


def populate_onto(iri: str, onto_file: str, input_file: str) -> None:
    # NOTE: assumes data in the form [[action, actor, object, tool], ...]
    # NOTE: word sense disambiguation not supported yet
    with open(input_file) as f:
        data = json.load(f)

    onto = o2.get_ontology(iri).load()
    with onto:
        for ap in data:
            apc = [e.replace(" ", "_").capitalize() for e in ap]
            general_acti = (
                types.new_class(apc[0], (getattr(onto, "Action"),))
                if onto[apc[0]] is None
                else onto[apc[0]]
            )
            acti = types.new_class(apc[0] + "_" + str(uuid.uuid4()), (general_acti,))
            agen = (
                types.new_class(apc[1], (getattr(onto, "Object"),))
                if onto[apc[1]] is None
                else onto[apc[1]]
            )
            obje = (
                types.new_class(apc[2], (getattr(onto, "Object"),))
                if onto[apc[2]] is None
                else onto[apc[2]]
            )
            tool = (
                types.new_class(apc[3], (getattr(onto, "Object"),))
                if onto[apc[3]] is None
                else onto[apc[3]]
            )
            getattr(acti, "has_agent").append(agen)
            getattr(acti, "has_object").append(obje)
            getattr(acti, "has_tool").append(tool)
    onto.save(file=onto_file)


def safe_delete(filename: str) -> None:
    try:
        os.remove(filename)
    except OSError:
        pass


if __name__ == "__main__":
    iri = "http://example.org/action-patterns.owl"
    onto_file = "action-patterns.owl"
    input_file = "action_patterns_example.json"
    safe_delete(onto_file)
    create_base_onto(iri, onto_file)
    populate_onto(iri, onto_file, input_file)
