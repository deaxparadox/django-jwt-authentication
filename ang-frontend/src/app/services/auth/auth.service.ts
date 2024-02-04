import { HttpClient } from '@angular/common/http';
import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';

interface JWTToken {
  refresh: string;
  access: string;
}

@Injectable({
  providedIn: 'root'
})
export class AuthService {

  constructor(
    private httpService: HttpClient
  ) { }

  loginUrl = "http://localhost:8000/api/token/"
  refresh: string | undefined = undefined;
  access: string | undefined = undefined;
  authenticated: boolean = false;

  login() {
    this.httpService.post<JWTToken>(
      this.loginUrl,
      {"username": "admin", "password": "136900"},
      {
        "headers": {
          "Content-Type": "application/json",
        }
      }

    ).subscribe(
      e => {
        console.log(e);
        // sessionStorage.setItem("refresh", e.refresh);
        // sessionStorage.setItem("access", e.access);
        this.refresh = e.refresh;
        this.access = e.access;
        this.authenticated = true;
      }
    )
  }

}
