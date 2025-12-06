"""
State management for your Drafter website.
"""

from dataclasses import dataclass


@dataclass
class State:
    energy_used: int
    count: int
