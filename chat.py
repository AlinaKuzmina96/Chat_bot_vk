# -- coding: utf-8 --﻿
import vk_api, time
from Chat_bot_vk_2 import messageHandler

vk = vk_api.VkApi(token="0508fc8fa3c6b0ef98e56a11b7894ceeab39158b1a32fe21a744ac1660f1007c44f55bf4554098d3953a2")
vk._auth_token()

while True:
    try:
        messages = vk.method("messages.getConversations", {"offset": 0, "count": 200})
        if messages["count"] >= 1:
            id = messages["items"][0]["last_message"]["from_id"]
            body = messages["items"][0]["last_message"]["text"]
            messageHandler.create_answer(body, id)
            time.sleep(0.5)

    except Exception as E:
        time.sleep(1)