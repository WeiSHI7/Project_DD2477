import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from "@angular/core";
import { Book } from "../book/book";
import { BookService } from "../book/book.service";

@Component({ 
    selector: "book-search",
    templateUrl: "./book_search.component.html",
    styleUrls: ["./book_search.component.scss"],
    providers: [BookService]
})
export class BookSearchComponent implements OnChanges {
    @Input() query!: string;

    searchResults: Book[] = [];

    @Output() onBookSelected = new EventEmitter<Book>();

    ngOnChanges(_changes: SimpleChanges): void {
        this.searchResults = [];
        if (this.query && this.query.length > 0) {
            this.bookService.searchBooks(this.query).then(books => {
                this.searchResults = books;
            });
        }
    }

    constructor(private bookService: BookService) { }
}