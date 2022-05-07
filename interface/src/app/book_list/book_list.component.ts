import { Component, EventEmitter, Input, Output } from "@angular/core";
import { Book } from "../book/book";

@Component({
    selector: "book-list",
    templateUrl: "./book_list.component.html",
    styleUrls: ["./book_list.component.scss"]
})
export class BookListComponent {
    @Input() books!: Book[];
    @Input() extended: boolean = true;
    @Input() readButtonEnabled: boolean = false;

    @Output() onBookSelected = new EventEmitter<Book>();
}