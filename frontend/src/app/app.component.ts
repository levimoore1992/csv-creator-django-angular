import {Component, OnInit} from '@angular/core';
import {FormBuilder, FormGroup, Validators} from '@angular/forms';
import {AppService} from './app.service';
import {FileSaverService} from 'ngx-filesaver';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  title = 'CVgenerator';
  CVGeneratorForm: FormGroup;

  constructor(private fb: FormBuilder,
              private service: AppService,
              private fileSaverService: FileSaverService) {}


  ngOnInit(): void {
            this.CVGeneratorForm = this.fb.group({
      name: ['', Validators.required],
      email: ['', Validators.required],
      summary: ['', Validators.required],
      'phone-number': [''],
      degree: [''],
      school: [''],
      skills: ['']
    });
  }

  submitForm() {

    const payload = {
      name: this.CVGeneratorForm.get('name').value,
      email: this.CVGeneratorForm.get('email').value,
      phone: this.CVGeneratorForm.get('phone-number').value,
      summary: this.CVGeneratorForm.get('summary').value,
      degree: this.CVGeneratorForm.get('degree').value,
      school: this.CVGeneratorForm.get('school').value,
      skills: this.CVGeneratorForm.get('skills').value,
    };

    this.service.sendCV(payload).subscribe(response => {
      this.fileSaverService.save(response.body, 'resume.pdf');

    });

  }
}
