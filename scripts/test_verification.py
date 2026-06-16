from app.verification.verification_pipeline import (
    verify_answer
)

#Sample:

query = (
    "How many annual leave days do employees receive?"
)

contexts = [
    "Employees receive 20 days of annual leave."
]

#Run:

result = verify_answer(
    query,
    contexts
)

print(result)