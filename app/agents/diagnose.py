from services.llm import call_llm


def diagnose_node(state):

    incident = state["incident"]

    prompt = f"""
You are a senior DevOps engineer.

Analyze this incident:

{incident}

Return:
- root cause
- affected system
- severity
"""

    diagnosis = call_llm(prompt)

    return {
        "diagnosis": diagnosis
    }