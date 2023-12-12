import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.css'
})

export class AppComponent {
  title = 'frontendApp';
  file: File | null = null; // Variable to store file
  encUrl: string | null = null;
  decUrl: string | null = null;
  downloadLink: string | null = null;

  async handleImageUpload() {
    const formData = new FormData();
    if (this.file) {
      formData.append('image', this.file);
    }

    const request = await fetch("http://10.9.0.4:5000/imageUpload", {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: formData,
    });
    const response = await request.json();
    console.log("image upload");
  }
  

  async encDecImage() {
    this.encUrl = ''; // Reset imageUrl
    this.decUrl = '';


    const formData = new FormData();
    if (this.file) {
      formData.append('image', this.file);
    }
    const request = await fetch("http://10.9.0.4:5000/encDecImage", {
      method: "POST",
      mode: "cors",
      cache: "no-cache",
      credentials: "same-origin",
      redirect: "follow",
      referrerPolicy: "no-referrer",
      body: formData,
    });
    const response = await request.blob();
    console.log("image encrypted");

    const reader = new FileReader();
    reader.readAsDataURL(response);
    reader.onloadend = () => {
      console.log(reader.result);
      this.encUrl = "http://10.9.0.4:5000/static/encrypted_image.png";
      this.decUrl = "http://10.9.0.4:5000/static/decrypted_image.png"
    };
  }

  onChange(event: any) {
    const file: File = event.target.files[0];

    if (file) {
      // this.status = "initial";
      this.file = file;
    }
  }
}
