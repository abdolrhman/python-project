from fastcrud import FastCRUD
from ..models.product import Product
from ..schemas.product import ProductCreate, ProductRead, ProductUpdate, ProductDelete

CRUDProduct = FastCRUD[Product, ProductCreate, ProductUpdate, ProductRead, ProductDelete]
crud_product = CRUDProduct(Product)