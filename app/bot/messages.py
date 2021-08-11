import typing as t

from aiogram import types

from app.constants import Message
from app.database.models import Link
from app.database.models import User


async def get_random_link_message(
    user: User, mailing: bool = False
) -> t.Tuple[str, t.Optional[types.InlineKeyboardMarkup]]:
    if link := await Link.get_random_by_owner(user):
        markup = types.InlineKeyboardMarkup()
        markup.insert(
            types.InlineKeyboardButton(Message.READ, callback_data=f"read_{link.id}")
        )
        if mailing:
            return Message.F_URL_MAILING.format(link.url), markup
        return Message.F_URL.format(link.url), markup
    else:
        if mailing:
            return Message.NOTHING_TO_SEND_MAILING, None
        return Message.NOTHING_TO_SEND, None
