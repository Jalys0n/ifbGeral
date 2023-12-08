import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root',
})
export class ApiService {
  private apiUrl = 'http://localhost:5000';

  constructor(private http: HttpClient) {}

  //retornar os assuntos
  getAssuntos(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/obter-atendimentos`);
  }
  // retornar os tipos de usuários
  getTiposUsuarios(): Observable<any[]> {
    return this.http.get<any[]>(`${this.apiUrl}/tipo-usuario`);
  }
}
