from fastapi import APIRouter

router = APIRouter(
    prefix="/index",
    tags=["index"]
)


@router.get('/index')
def get_index():
    pass


@router.post('/index')
def post_index():
    pass
