import { Component } from '@angular/core';
import { Book } from './book/book';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.scss']
})
export class AppComponent {
  searchQuery = "";
  readBooks: Book[] = []
  nReadBooks = 0;
  isRecommendationDone = false;

  onSearch(query: string) {
    this.searchQuery = query;
  }

  onBookSelected(book: Book) {
    this.readBooks.push(book);
    this.nReadBooks++;
    this.searchQuery = "";
  }

  onFinishedRecommendation() {
    this.searchQuery = "";
    this.isRecommendationDone = true;
  }

  onRetryRecommendation() {
    this.readBooks = [];
    this.nReadBooks = 0;
    this.isRecommendationDone = false;
  }
}
