export class Book {
    id: string;
    title: string;
    author: string;
    description: string;
    genres: string[];

    constructor(id: string, title: string, author: string, description: string, genres: string[]) {
        this.id = id;
        this.title = title;
        this.author = author;
        this.description = description;
        this.genres = genres;
    }
}