import vk_api
import random
from vk_api.utils import get_random_id
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from config import TOKEN, GROUP_ID

CHANCE = 50

vk_session = vk_api.VkApi(token=TOKEN)
longpoll = VkBotLongPoll(vk_session, GROUP_ID)
vk = vk_session.get_api()


def send_message(chat_id, text):
    vk_session.method(
        "messages.send",
        {"chat_id": chat_id, "message": text, "random_id": get_random_id()},
    )


def get_user_name(user_id):
    return vk.users.get(user_ids=user_id)[0]["first_name"]


def main():
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
            chat_id = event.chat_id
            user_id = event.message.get("from_id")

            user_name = get_user_name(user_id)
            answers = ["я пока добрый", f"{user_name}, ПОШЕЛ ТЫ"]

            if CHANCE >= random.random() * 100:
                send_message(chat_id, random.choice(answers))


if __name__ == "__main__":
    main()
