import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { Book } from "./book";

@Injectable()
export class BookService {
    private createBook(res: any): Book {
        return new Book(
            res["id"],
            res["title"],
            res["author"],
            res["description"],
            res["genres"].split(",").map((genre: string) => genre.trim()).filter((genre: string) => genre.length > 0)
        )
    }

    async getBook(id: string): Promise<Book> {
        return new Promise<Book>((resolve, reject) => {
            this.http.get(`http://127.0.0.1:5000/books/${id}`, {headers: {"Access-Control-Allow-Origin": "*"}})
                .subscribe(
                    (data: any) => {
                        resolve(this.createBook(data));
                    },
                )
        });
    }

    async searchBooks(query: string): Promise<Book[]> {
        return new Promise<Book[]>((resolve, reject) => {
            this.http.get(`http://127.0.0.1:5000/books?q=${query}`, {headers: {"Access-Control-Allow-Origin": "*"}})
                .subscribe(
                    data => {
                        console.log(data);
                        
                        resolve((data as Array<any>).map(el => {
                            return this.createBook(el);
                        }));
                    },
                );
        });
    }

    async getRecommendations(read_books_ids: string[]): Promise<Book[]> {
        return new Promise<Book[]>((resolve, reject) => {
            this.http.post(`http://127.0.0.1:5000/recommendations`, 
                {"read_books": read_books_ids},
                {headers: { "Access-Control-Allow-Origin": "*"}}
            )
                .subscribe(
                    data => {
                        let books: Book[] = [];
                        (data as string[]).map(id => {
                            this.getBook(id).then(b => {
                                books.push(b);
                            });
                        });
                        resolve(books);
                    }
                );
        });
    }

    constructor(private http: HttpClient) { }
}