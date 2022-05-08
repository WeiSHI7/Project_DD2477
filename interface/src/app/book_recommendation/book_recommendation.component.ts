import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from "@angular/core";
import { Book } from "../book/book";
import { BookService } from "../book/book.service";

@Component({
    selector: "book-recommendation",
    templateUrl: "./book_recommendation.component.html",
    styleUrls: ["./book_recommendation.component.scss"],
    providers: [BookService]
})
export class BookRecommendationComponent {
    @Input() readBooks!: Book[];
    @Input() nReadBooks!: number;

    recommendations: Book[] = [];

    @Output() onFinished = new EventEmitter<void>();
    @Output() onRetry = new EventEmitter<void>();

    onRecommendButtonClick() {
        this.bookService.getRecommendations(this.readBooks.map(book => book.id)).then(books => {
            this.recommendations = books;
            this.onFinished.emit();
        });
    }

    onRetryButtonClick() {
        this.onRetry.emit();
        this.recommendations = [];
    }

    constructor(private bookService: BookService) {}
}