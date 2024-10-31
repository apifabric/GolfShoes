import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Brand-card.component.html',
  styleUrls: ['./Brand-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Brand-card]': 'true'
  }
})

export class BrandCardComponent {


}