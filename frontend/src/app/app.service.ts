import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class AppService {

  constructor(private http: HttpClient) { }

  sendCV(payload) {
    return this.http.post('http://localhost:80/api/cvgenerator', payload, {
      observe: 'response',
      responseType: 'blob'
    });
  }
}
