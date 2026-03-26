"""diff_engine.py — Compare current vs future FlowSets to produce change impact.

Generates the §5 Change Impact Summary matching DS-020 reference:
  - NEW: flow chains in future but not current
  - REMOVED: flow chains in current but not future
  - MODIFIED: flow chains in both but with different paths/interfaces
  - UNCHANGED: identical in both
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Literal

from .csv_parser import FlowChain, FlowSet


ChangeType = Literal["NEW", "REMOVED", "MODIFIED", "UNCHANGED"]


@dataclass
class FlowChange:
    """A single change between current and future flow chain states."""
    change_type: ChangeType
    flow_chain: str
    detail: str


@dataclass
class DiffResult:
    """Complete diff between two FlowSets."""
    changes: list[FlowChange]

    @property
    def new_count(self) -> int:
        return sum(1 for c in self.changes if c.change_type == "NEW")

    @property
    def removed_count(self) -> int:
        return sum(1 for c in self.changes if c.change_type == "REMOVED")

    @property
    def modified_count(self) -> int:
        return sum(1 for c in self.changes if c.change_type == "MODIFIED")

    @property
    def unchanged_count(self) -> int:
        return sum(1 for c in self.changes if c.change_type == "UNCHANGED")

    @property
    def summary_str(self) -> str:
        return (f"{self.new_count} new - {self.removed_count} removed - "
                f"{self.modified_count} modified - {self.unchanged_count} unchanged")


def _chain_signature(chain: FlowChain) -> str:
    """Produce a comparable signature from a chain's hops."""
    parts = []
    for h in chain.hops:
        parts.append(f"{h.source_system}|{h.target_system}|{h.interface_tech}")
    return "::".join(parts)


def diff_flows(current: FlowSet, future: FlowSet) -> DiffResult:
    """Diff current vs future flow sets by flow chain name and content."""
    cur_map: dict[str, FlowChain] = {c.name: c for c in current.chains}
    fut_map: dict[str, FlowChain] = {c.name: c for c in future.chains}

    all_names = sorted(set(cur_map.keys()) | set(fut_map.keys()))
    changes: list[FlowChange] = []

    for name in all_names:
        in_cur = name in cur_map
        in_fut = name in fut_map

        if in_fut and not in_cur:
            changes.append(FlowChange("NEW", name, "Added in future state"))
        elif in_cur and not in_fut:
            changes.append(FlowChange("REMOVED", name, "Not present in future state"))
        else:
            cur_sig = _chain_signature(cur_map[name])
            fut_sig = _chain_signature(fut_map[name])
            if cur_sig == fut_sig:
                changes.append(FlowChange("UNCHANGED", name, "No change"))
            else:
                changes.append(FlowChange("MODIFIED", name, "Path or interface changed"))

    # Sort: NEW first, then REMOVED, MODIFIED, UNCHANGED
    order = {"NEW": 0, "REMOVED": 1, "MODIFIED": 2, "UNCHANGED": 3}
    changes.sort(key=lambda c: (order[c.change_type], c.flow_chain))

    return DiffResult(changes=changes)
