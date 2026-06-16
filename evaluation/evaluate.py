import json

from datasets import Dataset

from ragas import evaluate

from ragas.metrics import (
    faithfulness,
    answer_relevancy,
    context_precision,
)

from app.websearch.router import answer_query

with open("evaluation/golden_qa_set.json") as f:
    qa_pairs = json.load(f)

questions = []
answers = []
contexts = []
ground_truths = []

for row in qa_pairs:
    result = answer_query(row["question"])
    answer = result["answer"]["answer"]

    questions.append(row["question"])
    answers.append(answer)
    contexts.append([answer])
    ground_truths.append(row["ground_truth"])


dataset = Dataset.from_dict(
    {
        "question": questions,
        "answer": answers,
        "contexts": contexts,
        "ground_truths": ground_truths,
    }
)

results = evaluate(
    dataset,
    metrics=[
        faithfulness,
        answer_relevancy,
        context_precision,
    ],
)

