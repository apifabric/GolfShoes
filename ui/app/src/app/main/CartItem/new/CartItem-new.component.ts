import { Component, Injector, ViewChild } from '@angular/core';
import { NavigationService, OFormComponent } from 'ontimize-web-ngx';

@Component({
  selector: 'CartItem-new',
  templateUrl: './CartItem-new.component.html',
  styleUrls: ['./CartItem-new.component.scss']
})
export class CartItemNewComponent {
  @ViewChild("CartItemForm") form: OFormComponent;
  onInsertMode() {
    const default_values = {}
    this.form.setFieldValues(default_values);
  }
  constructor(protected injector: Injector) {
    this.injector.get(NavigationService).initialize();
  }
}