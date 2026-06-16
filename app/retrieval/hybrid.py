from .dense import dense_search
from .sparse import sparse_search
from .rrf import reciprocal_rank_fusion
from .reranker import rerank


def hybrid_retrieve(
        query,
        top_k=5
):

    dense_results = dense_search(
        query,
        top_k=10
    )

    sparse_results = sparse_search(
        query,
        top_k=10
    )

    fused = reciprocal_rank_fusion(
        dense_results,
        sparse_results
    )

    reranked = rerank(
        query,
        fused[:10]
    )

    return reranked[:top_k]