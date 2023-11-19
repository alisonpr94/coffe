from rest_framework import serializers
from .models import Produto, Venda, Despesa, MetaFuncionario

class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = '__all__'

class VendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Venda
        fields = '__all__'

class DespesaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Despesa
        fields = '__all__'

class MetaFuncionarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetaFuncionario
        fields = '__all__'