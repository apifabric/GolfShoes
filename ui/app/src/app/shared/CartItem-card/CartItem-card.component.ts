import { Component, ViewEncapsulation } from '@angular/core';

@Component({
  selector: 'transactions-card',
  templateUrl: './CartItem-card.component.html',
  styleUrls: ['./CartItem-card.component.scss'],
  encapsulation: ViewEncapsulation.None,
  host: {
    '[class.CartItem-card]': 'true'
  }
})

export class CartItemCardComponent {


}