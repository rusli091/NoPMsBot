#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) Shrimadhav U K
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.

# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.


from pyrogram import (
    Client
)
from pyrogram.raw.types import UpdateReadChannelInbox
from bot import (
    AUTH_CHANNEL
)
from bot.bot import Bot


@Bot.on_raw_update()
async def on_read_inbox(client: Bot, update, users, chats):
    if isinstance(update, UpdateReadChannelInbox):
        if update.channel_id == AUTH_CHANNEL:
            try:
                message = await client.get_messages(
                    chat_id=AUTH_CHANNEL,
                    message_ids=update.max_id
                )
                if message:
                    await message.react("👀")
            except Exception as e:
                # Log the exception for debugging
                client.LOGGER.exception(e)
