from services.llm import call_llm


def generate_fix_node(state):

    incident = state["incident"]
    diagnosis = state["diagnosis"]

    prompt = f"""
You are a DevOps automation engine.

Incident:
{incident}

Diagnosis:
{diagnosis}

Generate:
1. Terraform fix (if needed)
2. Bash fix
3. Explanation
"""

    fix = call_llm(prompt)

    return {
        "fix": fix
    }