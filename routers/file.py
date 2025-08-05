from fastapi import APIRouter

router = APIRouter(
    prefix='/file',
    tags=['files']
)

@router.post('/file')
def get_file():
    return {"message": "File received"}
