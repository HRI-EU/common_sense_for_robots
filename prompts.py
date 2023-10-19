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
Snippets for generating prompts
"""

from typing import List


PROMPT_CANDIDATES = """\
Choose only from the following candidates: {candidates}.
"""


# Extracting tools

PROMPT_EXTRACT_TOOLS = """\
In your response, I want you to answer with nothing but a list \
of suitable comma-separated words sorted by relevance.
Which tool can I use to {action} {object}?
"""

PROMPT_EXTRACT_TOOLS_DEMASKING = """\
A [MASK] is a great tool to {action} {object}.
"""


def prompt_tools(
    action: str, object_: str, candidates: List[str] = None, demasking: bool = False
) -> str:
    if demasking:
        prompt = PROMPT_EXTRACT_TOOLS_DEMASKING.format(action=action, object=object_)
    else:
        prompt = PROMPT_EXTRACT_TOOLS.format(action=action, object=object_)
    if candidates:
        prompt += PROMPT_CANDIDATES.format(candidates=", ".join(candidates))
    return prompt


# Extracting object states

PROMPT_EXTRACT_STATES = """\
In your response, I want you to answer with nothing but a list \
of suitable comma-separated words sorted by relevance.
What is the state of a {object} {temporal_relation} it is {action} with a {tool}?
Consider only adjectives that are relevant for the action '{action}'.
"""

PROMPT_EXTRACT_STATES_DEMASKING = """\
{temporal_relation} being {action} with a {tool} a {object} is [MASK].
"""


def prompt_states(
    action: str,
    object_: str,
    tool: str,
    temporal_relation: str,
    demasking: bool = False,
) -> str:
    assert temporal_relation in ("before", "after")
    if demasking:
        prompt = PROMPT_EXTRACT_STATES_DEMASKING.format(
            action=action,
            object=object_,
            tool=tool,
            temporal_relation=temporal_relation.capitalize(),
        )
    else:
        prompt = PROMPT_EXTRACT_STATES.format(
            action=action,
            object=object_,
            tool=tool,
            temporal_relation=temporal_relation,
        )
    return prompt


# Extracting spatial relations

PROMPT_EXTRACT_SPATIAL_RELATIONS = """\
In your response, I want you to answer with nothing but a list \
of suitable comma-separated words sorted by relevance.
After having {action} the {object}, where is the {object} located \
relative to the {tool}?
Choose only from the following candidates: in, on, near, outside, off.
"""

PROMPT_EXTRACT_SPATIAL_RELATIONS_DEMASKING = """\
After having {action} the {object}, the {object} is located [MASK] the {tool}.
"""


def prompt_spatial_relations(
    action: str, object_: str, tool: str, demasking: bool = False
) -> str:
    if demasking:
        prompt = PROMPT_EXTRACT_SPATIAL_RELATIONS_DEMASKING.format(
            action=action, object=object_, tool=tool
        )
    else:
        prompt = PROMPT_EXTRACT_SPATIAL_RELATIONS.format(
            action=action, object=object_, tool=tool
        )
    return prompt


# Extracting entire action patterns

PROMPT_EXTRACT_ACTION_PATTERNS_PT1 = """\
Please respond with nothing but lists of the form '(action, agent, object, tool)'. 
An action pattern is defined by an action, i.e., a verb, an agent \
who executes the action, an object, which is modified, and optionally a tool. 
Generate {amount} action patterns for the domain of interest '{domain_of_interest}'.
"""

PROMPT_EXTRACT_ACTION_PATTERNS_PT2 = """\
Thereby, consider the following restrictions: 
Use only {options} as {element}.
"""


def prompt_action_patterns(
    amount: int,
    domain_of_interest: str,
    restriction: List[str] = None,
    element: str = None,
) -> str:
    prompt = PROMPT_EXTRACT_ACTION_PATTERNS_PT1.format(
        amount=str(amount), domain_of_interest=domain_of_interest
    )
    if restriction:
        prompt += PROMPT_EXTRACT_ACTION_PATTERNS_PT2.format(
            options=" or ".join(restriction), element=element
        )
    return prompt


if __name__ == "__main__":
    print("Example prompt for extracting tools:")
    print(prompt_tools(action="cut", object_="bread"))
    print("Using demasking:")
    print(prompt_tools(action="cut", object_="bread", demasking=True))

    print("Example prompt for extracting object states:")
    print(
        prompt_states(
            action="cut", object_="bread", tool="knife", temporal_relation="after"
        )
    )
    print("Using demasking:")
    print(
        prompt_states(
            action="cut",
            object_="bread",
            tool="knife",
            temporal_relation="after",
            demasking=True,
        )
    )

    print("Example prompt for extracting spatial relations:")
    print(prompt_spatial_relations(action="cut", object_="bread", tool="knife"))
    print("Using demasking:")
    print(
        prompt_spatial_relations(
            action="cut", object_="bread", tool="knife", demasking=True
        )
    )

    print("Example prompt for extracting entire action patterns:")
    print(
        prompt_action_patterns(
            amount=100,
            domain_of_interest="kitchen",
            restriction=["chef"],
            element="agent",
        )
    )
