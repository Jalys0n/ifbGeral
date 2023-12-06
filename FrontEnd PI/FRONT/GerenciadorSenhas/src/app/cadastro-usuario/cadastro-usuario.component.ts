import { Component, OnInit } from '@angular/core';
import { ApiService } from '../app.service';

@Component({
  selector: 'app-cadastro-usuario',
  templateUrl: './cadastro-usuario.component.html',
  styleUrls: ['./cadastro-usuario.component.css']
})
export class CadastroUsuarioComponent implements OnInit {
  assuntos: any[] = [];
  tiposUsuarios: any[] = [];

  constructor(private apiService: ApiService) {}

  ngOnInit(): void {
    console.log('ngOnInit foi chamado!');
    this.carregarAssuntos();
    this.carregarTiposUsuarios();
  }

  carregarAssuntos() {
    this.apiService.getAssuntos().subscribe(
      (data) => {
        this.assuntos = data;
        console.log('Assuntos carregados:', this.assuntos);
      },
      (error) => {
        console.error('Erro ao obter assuntos:', error);
      }
    );
  }

  carregarTiposUsuarios() {
    this.apiService.getTiposUsuarios().subscribe(
      (data) => {
        this.tiposUsuarios = data;
        console.log('Tipos de usuários carregados:', this.tiposUsuarios);
      },
      (error) => {
        console.error('Erro ao obter tipos de usuários:', error);
      }
    );
  }
}
