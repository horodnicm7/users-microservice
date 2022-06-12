from fastapi import APIRouter


router = APIRouter(
    prefix='/users'
)


@router.get('/{user_id}')
async def get_user_by_id(user_id: int):
    pass


@router.get('/')
async def get_users(user_id: int, name: str):
    pass


@router.post('/')
async def create_user():
    pass


@router.put('/{user_id}')
async def update_user(user_id: int):
    pass


@router.delete('/{user_id}')
async def delete_user(user_id: int):
    pass
