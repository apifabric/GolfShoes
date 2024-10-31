import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { CartItemHomeComponent } from './home/CartItem-home.component';
import { CartItemNewComponent } from './new/CartItem-new.component';
import { CartItemDetailComponent } from './detail/CartItem-detail.component';

const routes: Routes = [
  {path: '', component: CartItemHomeComponent},
  { path: 'new', component: CartItemNewComponent },
  { path: ':id', component: CartItemDetailComponent,
    data: {
      oPermission: {
        permissionId: 'CartItem-detail-permissions'
      }
    }
  }
];

export const CARTITEM_MODULE_DECLARATIONS = [
    CartItemHomeComponent,
    CartItemNewComponent,
    CartItemDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class CartItemRoutingModule { }