from django.shortcuts import render
from home.models import LangchainPgEmbedding
from .embedding import get_embedding
from pgvector.django import L2Distance, CosineDistance


def index(request):
    if request.method == 'POST':
        text = request.POST.get('input-text')
        embedding = get_embedding(text)
        document = LangchainPgEmbedding.objects.order_by(L2Distance('embedding', embedding)).first()
        context = {"text": text, 'most_similar': document} 
        return render(request, 'result.html', context)
    embeddings = LangchainPgEmbedding.objects.all()
    context = {"embeddings": embeddings} 
    return render(request, 'index.html', context)
