from fastapi import APIRouter, Depends

from ...services.youtube import download
from ...schemas.link import LinkSchema

router = APIRouter(
    prefix="/index",
    tags=["index"]
)


@router.get('/')
async def get_index(link_param: LinkSchema = Depends()):
    url = link_param.link
    return download(url)


@router.post('/')
def post_index():
    return 'This does nothing for now.'
