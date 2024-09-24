from fastcrud import FastCRUD
from ..models.category import Category
from ..schemas.category import CategoryCreate, CategoryRead, CategoryUpdate, CategoryDelete

CRUDCategory = FastCRUD[Category, CategoryCreate, CategoryUpdate, CategoryRead, CategoryDelete]
crud_category = CRUDCategory(Category)