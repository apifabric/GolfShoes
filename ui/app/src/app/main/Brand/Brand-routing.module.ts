import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { BrandHomeComponent } from './home/Brand-home.component';
import { BrandNewComponent } from './new/Brand-new.component';
import { BrandDetailComponent } from './detail/Brand-detail.component';

const routes: Routes = [
  {path: '', component: BrandHomeComponent},
  { path: 'new', component: BrandNewComponent },
  { path: ':id', component: BrandDetailComponent,
    data: {
      oPermission: {
        permissionId: 'Brand-detail-permissions'
      }
    }
  },{
    path: ':brand_id/Product', loadChildren: () => import('../Product/Product.module').then(m => m.ProductModule),
    data: {
        oPermission: {
            permissionId: 'Product-detail-permissions'
        }
    }
}
];

export const BRAND_MODULE_DECLARATIONS = [
    BrandHomeComponent,
    BrandNewComponent,
    BrandDetailComponent 
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class BrandRoutingModule { }