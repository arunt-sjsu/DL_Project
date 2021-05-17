import { Component, OnInit } from '@angular/core';
import { ApiService } from '../api.service';
import { FormGroup, FormControl, Validators} from '@angular/forms';

@Component({
  selector: 'app-gallery',
  templateUrl: './gallery.component.html',
  styleUrls: ['./gallery.component.css']
})

export class GalleryComponent implements OnInit {
  images:any;
  fileName:any;
  file:any;
  imageSrc:any;
  resultantImage:any;

  myForm = new FormGroup({
    file: new FormControl('', [Validators.required]),
    fileSource: new FormControl('', [Validators.required])
  });

  constructor(private apiService: ApiService) {
      this.resultantImage = {url:""}
   }

  ngOnInit(): void {
    this.apiService.getImage().subscribe((resp: any) => {
      this.images = resp.ImageBytes;
    });
  }
  
  get f(){
    return this.myForm.controls;
  }
   
  onFileChange(event:any) {
    const reader = new FileReader();
    console.log(event)
    if(event.target.files && event.target.files.length) {
      const [file] = event.target.files;
      reader.readAsDataURL(file);
    
      reader.onload = () => {
   
        this.imageSrc = reader.result as string;
     
        this.myForm.patchValue({
          fileSource: reader.result
        });
   
      };
   
    }
  }

  submitFile() {
    console.log("calling")
    this.apiService.pushUserImage(this.myForm.value).subscribe((resp:any) => {
      console.log(resp);
    });
  }

  getModifiedImage(img:any){
    this.apiService.getModifiedImage(img).subscribe((resp:any) => {
      this.resultantImage = resp.ImageBytes;
    });
  }
}
