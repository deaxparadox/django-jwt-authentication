import { Component, OnInit } from '@angular/core';
import { AuthService } from '../../services/auth/auth.service';
import { HttpClient, HttpClientModule, provideHttpClient, withFetch } from '@angular/common/http';

@Component({
  selector: 'app-navbar',
  standalone: true,
  imports: [],
  providers: [
    // HttpClientModule
  ],
  templateUrl: './navbar.component.html',
  styleUrl: './navbar.component.scss'
})
export class NavbarComponent implements OnInit {
  constructor(
    private authService: AuthService
  ){}

  ngOnInit(): void {
    // this.authService.login();
  }
}
