import { HttpClient } from '@angular/common/http';
import { Component, OnInit } from '@angular/core';

@Component({
    selector: 'app-root',
    templateUrl: './app.component.html',
    styleUrls: ['./app.component.scss'],
})
export class AppComponent implements OnInit {
    title = 'orbrat-io';
    reminders: any[] = [];

    constructor(private httpClient: HttpClient) {}

    ngOnInit() {
        this.httpClient
            .get<any>('http://localhost:8080/api/v1/reminders')
            .subscribe((reminders) => {
                console.log(reminders);
                this.reminders = reminders.data;
            });
    }
}
