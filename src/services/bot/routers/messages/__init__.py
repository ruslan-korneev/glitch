from aiogram import Router

from . import general

router = Router()
router.include_routers(
    general.router,
)
