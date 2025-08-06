from fastapi import APIRouter
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi import Request

router = APIRouter(
    prefix="/templates",
    tags=["Templates"]
)

templates = Jinja2Templates(directory="templates")

@router.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})

@router.get("/products/{product_id}", response_class=HTMLResponse)
def get_product(product_id: str, request: Request):
    # Sample product data - in a real app, this would come from a database
    product_data = {
        "product_id": product_id,
        "product_name": f"Product {product_id}",
        "product_description": f"This is a sample product with ID {product_id}",
        "price": 99.99,
        "stock": 50
    }
    
    return templates.TemplateResponse(
        "product.html", 
        {"request": request, **product_data}
    ) 