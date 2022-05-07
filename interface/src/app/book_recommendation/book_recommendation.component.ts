import { Component, EventEmitter, Input, OnChanges, Output, SimpleChanges } from "@angular/core";
import { Book } from "../book/book";
import { BookService } from "../book/book.service";

@Component({
    selector: "book-recommendation",
    templateUrl: "./book_recommendation.component.html",
    styleUrls: ["./book_recommendation.component.scss"],
    providers: [BookService]
})
export class BookRecommendationComponent implements OnChanges {
    @Input() readBooks!: Book[];
    @Input() nReadBooks!: number;

    recommendations: Book[] = [];

    @Output() onFinished = new EventEmitter<void>();
    @Output() onRetry = new EventEmitter<void>();

    ngOnChanges(_changes: SimpleChanges): void {
        if (this.readBooks && this.readBooks.length == 3) {
            this.bookService.getRecommendations(this.readBooks.map(book => book.id)).then(books => {
                this.recommendations = books;
                this.onFinished.emit();
            });
        }
    }

    onRetryButtonClick() {
        this.onRetry.emit();
        this.recommendations = [];
    }

    constructor(private bookService: BookService) {}
}