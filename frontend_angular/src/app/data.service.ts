// src/app/data.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class DataService {
  private apiUrl = 'http://localhost:8000/api/';

  constructor(private http: HttpClient) {}

  getProdutos(): Observable<any> {
    return this.http.get(this.apiUrl + 'produtos/');
  }

  getVendas(): Observable<any> {
    return this.http.get(this.apiUrl + 'vendas/');
  }
}
