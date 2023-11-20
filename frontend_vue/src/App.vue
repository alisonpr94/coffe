<!-- src/App.vue -->
<template>
  <div id="app">
    <h1>Cafeteria App</h1>

    <h2>Produtos</h2>
    <ul>
      <li v-for="produto in produtos" :key="produto.id">{{ produto.nome }} - R${{ produto.preco }}</li>
    </ul>

    <h2>Vendas</h2>
    <ul>
      <li v-for="venda in vendas" :key="venda.id">{{ venda.total }} - {{ venda.data }}</li>
    </ul>
  </div>
</template>

<script>
export default {
  data() {
    return {
      produtos: [],
      vendas: [],
    };
  },
  mounted() {
    this.carregarProdutos();
    this.carregarVendas();
  },
  methods: {
    carregarProdutos() {
      // Carregue os produtos do backend
      this.$axios.get('http://localhost:8000/api/produtos/')
        .then(response => this.produtos = response.data)
        .catch(error => console.error('Erro ao buscar produtos:', error));
    },
    carregarVendas() {
      // Carregue as vendas do backend
      this.$axios.get('http://localhost:8000/api/vendas/')
        .then(response => this.vendas = response.data)
        .catch(error => console.error('Erro ao buscar vendas:', error));
    },
  },
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
