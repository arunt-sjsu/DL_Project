import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {

  constructor(private httpClient:HttpClient) {
   }
   
   root_url = "http://127.0.0.1:5000"

   getImage() {
    return this.httpClient.get(
      this.root_url+'/api/get_images'
    );
    }

    pushUserImage(formData:any){
      console.log(formData)
      return this.httpClient.post(this.root_url+"/api/post_user_image",formData)
    }

    getModifiedImage(imgName:any){
      return this.httpClient.post(this.root_url+"/api/get_clothing",{"imageName":imgName})
    }
} 
