from app.agents.orchestrator import (
    run_agentic_retrieval
)
query = """
What health benefits do employees receive
and how much annual leave do they get?
"""
result = run_agentic_retrieval(
    query
)
print("\nSUBQUESTIONS\n")

for q in result["subquestions"]:

    print("-", q)

    print("\nCONTEXTS\n")

for c in result["contexts"]:

    print(c)

