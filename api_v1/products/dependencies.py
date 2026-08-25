from fastapi import Depends, HTTPException, Path
from sqlalchemy.ext.asyncio import AsyncSession
from starlette import status
from typing import Annotated

from core.models import db_helper, Product
from . import crud


# ================  Функция зависимости для получения товара по id ============================
async def product_by_id(product_id: Annotated[int, Path],
                        session: AsyncSession = Depends(db_helper.scope_session_dependency), ) -> Product:

    product = await crud.get_product(session=session, product_id=product_id)
    if product is not None:
        return product

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Product by {product_id} not found"
    )
