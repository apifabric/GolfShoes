import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './Cart-card.component.html',
  styleUrls: ['./Cart-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.Cart-card]': 'true'
  }
})

export class CartCardComponent {


}