from django.urls import path
from .views import produtos_list, produtos_detail, vendas_list, vendas_detail, despesas_list, despesas_detail, metas_funcionario_list, metas_funcionario_detail

urlpatterns = [
    # Rotas para Produtos
    path('produtos/', produtos_list, name='produtos_list'),
    path('produtos/<int:produto_id>/', produtos_detail, name='produtos_detail'),

    # Rotas para Vendas
    path('vendas/', vendas_list, name='vendas_list'),
    path('vendas/<int:venda_id>/', vendas_detail, name='vendas_detail'),

    # Rotas para Despesas
    path('despesas/', despesas_list, name='despesas_list'),
    path('despesas/<int:despesa_id>/', despesas_detail, name='despesas_detail'),

    # Rotas para Metas dos Funcionários
    path('metas/', metas_funcionario_list, name='metas_funcionario_list'),
    path('metas/<int:meta_id>/', metas_funcionario_detail, name='metas_funcionario_detail'),
]