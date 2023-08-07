from aiogram import Router

from . import messages

router = Router()
router.include_routers(
    messages.router,
)
