from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

parent_splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=2000,
        chunk_overlap=200
    )
)

child_splitter = (
    RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )
)

def create_chunks(text):

    parents = parent_splitter.split_text(text)

    output = []

    for parent_idx,parent in enumerate(parents):

        children = child_splitter.split_text(
            parent
        )

        for child_idx,child in enumerate(children):

            output.append(
                {
                    "parent_id": parent_idx,
                    "child_id": child_idx,
                    "text": child,
                    "parent_text": parent
                }
            )

    return output

