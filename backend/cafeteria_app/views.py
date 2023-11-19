from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Produto, Venda, Despesa, MetaFuncionario
from .serializers import ProdutoSerializer, VendaSerializer, DespesaSerializer, MetaFuncionarioSerializer

@api_view(['GET', 'POST'])
def produtos_list(request):
    if request.method == 'GET':
        produtos = Produto.objects.all()
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = ProdutoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def produtos_detail(request, produto_id):
    produto = get_object_or_404(Produto, pk=produto_id)

    if request.method == 'GET':
        serializer = ProdutoSerializer(produto)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ProdutoSerializer(produto, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        produto.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Views semelhantes para Vendas, Despesas e MetasFuncionario

@api_view(['GET', 'POST'])
def vendas_list(request):
    ...

@api_view(['GET', 'PUT', 'DELETE'])
def vendas_detail(request, venda_id):
    ...

@api_view(['GET', 'POST'])
def despesas_list(request):
    ...

@api_view(['GET', 'PUT', 'DELETE'])
def despesas_detail(request, despesa_id):
    ...

@api_view(['GET', 'POST'])
def metas_funcionario_list(request):
    ...

@api_view(['GET', 'PUT', 'DELETE'])
def metas_funcionario_detail(request, meta_id):
    ...