import { Component, OnInit } from '@angular/core';
import { NavbarComponent } from '../navbar/navbar.component';
import { AuthService } from '../../services/auth/auth.service';
import { time } from 'console';

interface Timer {
  timer: NodeJS.Timeout;
  setTimer(): void;
  clearTimer(): void;
}

@Component({
  selector: 'app-dashboard',
  standalone: true,
  imports: [
    NavbarComponent
  ],
  templateUrl: './dashboard.component.html',
  styleUrl: './dashboard.component.scss'
})
export class DashboardComponent implements OnInit{
  constructor(
    private authService: AuthService
  ){}

  authenticated: boolean = false
  ngOnInit(): void {
    this.authService.login();
  }


  timer: NodeJS.Timeout | undefined;
  setTimer() {
    this.timer = setInterval(
      () => {
        if ((this.authService.authenticated) && (this.authenticated)) { 
          this.clearTimer();
          console.log(this.authenticated, this.authService.authenticated);
        }
        this.authenticated = this.authService.authenticated
      }, 1000
    )
  }
  clearTimer() {
    console.log(this.authenticated)
    clearInterval(this.timer);
  }
}
