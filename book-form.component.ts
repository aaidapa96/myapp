import { Component } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-book-form',
  templateUrl: './book-form.component.html',
  styleUrls: ['./book-form.component.css']
})
export class BookFormComponent {
  book = {
    name: '',
    author: '',
    date: '',
    availability: false
  };

  constructor(private http: HttpClient) {}

  submitForm() {
    this.http.post('http://localhost:5000/api/add_book', this.book)
      .subscribe(response => {
        console.log(response);
        // Handle success or redirect
      }, error => {
        console.error(error);
        // Handle error
      });
  }
}
