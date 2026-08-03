# =========================================
# emoji_engine.py
# =========================================

from telethon.tl.types import (

    MessageEntityBold,
    MessageEntityCustomEmoji

)

from emoji_maps import CHANNEL_EMOJIS

ALL_EMOJIS = {}
for emoji_map in CHANNEL_EMOJIS.values():
    ALL_EMOJIS.update(emoji_map)


# =========================================
# UTF16 INDEX
# =========================================

def utf16_index(string, pos):

    return len(

        string[:pos].encode(
            "utf-16-le"
        )

    ) // 2


# =========================================
# UTF16 LENGTH
# =========================================

def utf16_length(string):

    return len(

        string.encode(
            "utf-16-le"
        )

    ) // 2


# =========================================
# PREMIUM ENTITY ENGINE
# =========================================

def premium_entities(

    text,
    channel_name

):

    print("premium_entities CALLED")
    print(channel_name)
    print(text)

    entities = []


    # =====================================
    # FULL BOLD
    # =====================================

    entities.append(

        MessageEntityBold(

            offset=0,

            length=utf16_length(text)
        )
    )


    # =====================================
    # GET CHANNEL EMOJIS + KNOWN PREMIUM EMOJIS
    # =====================================

    emoji_map = {}
    emoji_map.update(ALL_EMOJIS)
    emoji_map.update(

        CHANNEL_EMOJIS.get(

            channel_name,

            {}
        )
    )


    # =====================================
    # LOOP EMOJIS
    # =====================================

    for emoji, document_id in emoji_map.items():

        current = 0

        while True:

            pos = text.find(

                emoji,

                current
            )

            if pos == -1:

                break


            entities.append(

                MessageEntityCustomEmoji(

                    offset=utf16_index(
                        text,
                        pos
                    ),

                    length=utf16_length(
                        emoji
                    ),

                    document_id=document_id
                )
            )

            current = pos + len(
                emoji
            )

    return entities


# =========================================
# PREMIUM TEXT REPLACE
# =========================================

def premium_replace(

    text,
    channel_name

):

    emoji_map = CHANNEL_EMOJIS.get(

        channel_name,

        {}
    )

    for emoji, emoji_id in emoji_map.items():

        premium_emoji = (

            f'<emoji id="{emoji_id}">{emoji}</emoji>'
        )

        text = text.replace(

            emoji,

            premium_emoji
        )

    return text


print("✅ EMOJI ENGINE LOADED")