from typing import TypedDict

from langgraph.graph import StateGraph, END

from agents.diagnose import diagnose_node
from agents.generate_fix import generate_fix_node


class IncidentState(TypedDict):
    incident: str
    diagnosis: str
    fix: str


def build_graph():

    workflow = StateGraph(IncidentState)

    workflow.add_node(
        "diagnose",
        diagnose_node
    )

    workflow.add_node(
        "generate_fix",
        generate_fix_node
    )

    workflow.set_entry_point("diagnose")

    workflow.add_edge(
        "diagnose",
        "generate_fix"
    )

    workflow.add_edge(
        "generate_fix",
        END
    )

    return workflow.compile()