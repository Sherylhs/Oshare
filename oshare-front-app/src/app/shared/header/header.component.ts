import { Router } from '@angular/router';
import { Component, OnInit } from '@angular/core';

@Component({
  selector: 'app-header',
  templateUrl: './header.component.html',
  styleUrls: ['./header.component.css']
})
export class HeaderComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit(): void {
  }
  Logout(){
    localStorage.removeItem('userToken');
    localStorage.removeItem('userId');
    location.reload();
    //this.router.navigate(['/login']);
  }

  checkLoginStatus(){
    return localStorage.getItem('userToken') != null;
  }
}
