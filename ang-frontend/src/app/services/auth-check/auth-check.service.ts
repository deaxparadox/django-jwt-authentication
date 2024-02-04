import { Injectable, OnInit } from '@angular/core';
import { AuthService } from '../auth/auth.service';

@Injectable({
  providedIn: 'root'
})
export class AuthCheckService implements OnInit {

  constructor(
    private authService: AuthService
  ) { }

  
  ngOnInit(): void {
    this.authService.login()
  }
}
