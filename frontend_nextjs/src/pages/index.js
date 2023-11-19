// pages/index.js
import React, { useEffect, useState } from 'react';
import api from '../services/api';

function Home() {
  const [produtos, setProdutos] = useState([]);
  const [vendas, setVendas] = useState([]);

  useEffect(() => {
    carregarProdutos();
    carregarVendas();
  }, []);

  const carregarProdutos = async () => {
    try {
      const response = await api.get('produtos/');
      setProdutos(response.data);
    } catch (error) {
      console.error('Erro ao buscar produtos:', error);
    }
  };

  const carregarVendas = async () => {
    try {
      const response = await api.get('vendas/');
      setVendas(response.data);
    } catch (error) {
      console.error('Erro ao buscar vendas:', error);
    }
  };

  return (
    <div>
      <h1>Cafeteria App</h1>

      <h2>Produtos</h2>
      <ul>
        {produtos.map(produto => (
          <li key={produto.id}>{produto.nome} - R${produto.preco}</li>
        ))}
      </ul>

      <h2>Vendas</h2>
      <ul>
        {vendas.map(venda => (
          <li key={venda.id}>{venda.total} - {venda.data}</li>
        ))}
      </ul>
    </div>
  );
}

export default Home;
