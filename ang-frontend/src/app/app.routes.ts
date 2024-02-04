import { Routes } from '@angular/router';
import { DashboardComponent } from './components/dashboard/dashboard.component';
import { AuthComponent } from './components/auth/auth.component';

export const routes: Routes = [
    { path: "dashboard", component: DashboardComponent},
    { path: "login", component: AuthComponent},
    { path: "", redirectTo: "/dashboard", pathMatch: "full"}
];
