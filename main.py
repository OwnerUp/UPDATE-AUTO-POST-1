# =========================================
# main.py
# =========================================

import os
import sys

ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

from telethon import TelegramClient

from config import (

    API_ID,
    API_HASH,
    PHONE,
    SESSION_NAME

)

# =========================================
# HANDLERS
# =========================================

from handlers.league_handler import (
    register_league_handler
)

from handlers.toss_handler import (
    register_toss_handler
)

from handlers.toss_pass import (
    register_toss_pass_handler
)

from handlers.delete_toss import (
    register_delete_toss_handler
)

from handlers.match_handler import (
    register_match_handler
)

from handlers.match_pass import (
    register_match_pass_handler
)

from handlers.delete_match import (
    register_delete_match_handler
)

from handlers.edit_toss import (
    register_edit_toss_handler
)

from handlers.edit_match import (
    register_edit_match_handler
)

from handlers.session_handler import (
    register_session_handler
)

from handlers.sball_handler import (
    register_sball_handler
)

from handlers.session_pass import (
    register_session_pass_handler
)

from handlers.sbpass_handler import (
    register_sbpass_handler
)

from handlers.session_loss import (
    register_session_loss_handler
)

from handlers.sbloss_handler import (
    register_sball_loss_handler
)

from handlers.entry_handler import (
    register_entry_handler
)

from handlers.inning_break_handler import register_inning_break_handler

from handlers.cashout_handler import register_cashout_handler

# =========================================
# CLIENT
# =========================================

client = TelegramClient(

    SESSION_NAME,

    API_ID,

    API_HASH
)

# =========================================
# REGISTER ALL
# =========================================

register_league_handler(client)

register_toss_handler(client)

register_toss_pass_handler(client)

register_match_handler(client)

register_match_pass_handler(client)

register_delete_toss_handler(client)

register_delete_match_handler(client)

register_edit_toss_handler(client)

register_edit_match_handler(client)

register_session_handler(client)

register_sball_handler(client)

register_session_pass_handler(client)

register_sbpass_handler(client)

register_session_loss_handler(client)

register_sball_loss_handler(client)

register_entry_handler(client)

register_inning_break_handler(client)

register_cashout_handler(client)

# =========================================
# START
# =========================================

async def main():

    await client.start(
        phone=PHONE
    )

    me = await client.get_me()

    print(
        f"✅ LOGGED IN: {me.first_name}"
    )

    print("🚀 PREMIUM MULTI BOT STARTED")

    await client.run_until_disconnected()


# =========================================
# RUN
# =========================================

if __name__ == "__main__":

    with client:

        client.loop.run_until_complete(
            main()
        )