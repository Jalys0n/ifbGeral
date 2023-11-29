// usuario.service.ts
import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';

@Injectable({
  providedIn: 'root'
})
export class UsuarioService {

  constructor(private http: HttpClient) { }

  cadastrarUsuario(dados: any): Observable<any> {
    const url = 'http://127.0.0.1:5000/cadastro';
    
    // Realize uma solicitação POST para a URL com os dados fornecidos
    return this.http.post(url, dados);
  }
}
