// src/app/app.component.ts
import { Component, OnInit } from '@angular/core';
import { DataService } from './data.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
})
export class AppComponent implements OnInit {
  produtos: any[] = [];
  vendas: any[] = [];

  constructor(private dataService: DataService) {}

  ngOnInit() {
    this.carregarProdutos();
    this.carregarVendas();
  }

  carregarProdutos() {
    this.dataService.getProdutos().subscribe(
      (data: any) => {
        this.produtos = data;
      },
      error => {
        console.error('Erro ao buscar produtos:', error);
      }
    );
  }

  carregarVendas() {
    this.dataService.getVendas().subscribe(
      (data: any) => {
        this.vendas = data;
      },
      error => {
        console.error('Erro ao buscar vendas:', error);
      }
    );
  }
}
