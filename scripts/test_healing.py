from app.self_healing.healing_loop import (
    self_healing_retrieve
)
query = (
    "employee vacation benefits"
)
result = self_healing_retrieve(
    query
)
print("\nHEALED")

print(
    result["healed"]
)

print(
    "\nRETRIES"
)

print(
    result["retries"]
)

print(
    "\nQUALITY"
)

print(
    result["quality"]
)
for chunk in result["results"]:

    print(
        "\n",
        chunk["text"]
    )