from app.websearch.router import (
    answer_query
)



query = (
    "Latest developments in AI regulation"
)



result = answer_query(
    query
)

print(result)