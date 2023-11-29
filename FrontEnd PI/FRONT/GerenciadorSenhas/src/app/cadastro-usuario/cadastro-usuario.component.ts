import { Component } from '@angular/core';
import {HttpClient} from '@angular/common/http';
import { UsuarioService } from './usuarioService';

@Component({
  selector: 'app-cadastro-usuario',
  templateUrl: './cadastro-usuario.component.html',
  styleUrls: ['./cadastro-usuario.component.css']
})
export class CadastroUsuarioComponent {
  constructor(private http: HttpClient) { }
  
  cadastrarUsuario(){
    const dados = {
      cpf : '06061997132',
      nomeUsuario : 'José',
      assunto: 'Trancar matrícula',
      comunidade: 'Externa',
      preferencia: 'preferenciasim'
    };
    this.http.post('http://127.0.0.1:5000/cadastro', dados).subscribe(
      (response)=>{
        console.log(response)
      }, 
      (error)=>{
        console.log(error)
      }
    )
  }
}
