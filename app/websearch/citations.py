def extract_sources(
        results
):
    citations = []
    for item in results:
        url = item.get(
            "url"
        )
        if url:
            citations.append(
                url
            )



    return citations