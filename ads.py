from pyrogram.enums import ChatAction  
from pyrogram import Client, filters
import asyncio
from pyrogram.types import *
from pymongo import MongoClient
import requests
import random
from pyrogram.errors import (
    PeerIdInvalid,
    ChatWriteForbidden
)
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from pyrogram.errors import ChatAdminRequired, UserNotParticipant, ChatWriteForbidden
import os
import re


API_ID = "26271987"
API_HASH = "c13df74c80d672fbebc0ceaa40efc3f6"

MONGO_URL ="mongodb+srv://venturepvtme:INc7HJsa1gt9oZ33@lgcyalex855101.kgbzc.mongodb.net"

PHONE_NUMBER = "+918999917992"  


url = "https://t.me/+nQno_QM4iohlNWE1"
join_message = "Come to my VC"

client = Client(PHONE_NUMBER, API_ID, API_HASH, phone_number=PHONE_NUMBER)

# Dictionary to track user messages
user_message_count = {}

@client.on_message(
    filters.command("fazal", prefixes=["/", ".", "?", "-"])
    & ~filters.private)
async def start(client, message):
    await message.reply_text(f"**ᴜsᴇʀʙᴏᴛ ғᴏʀ ᴄʜᴀᴛᴛɪɴɢ ɪs ᴡᴏʀᴋɪɴɢ**")
    
@client.on_message(
 (
        filters.text
        | filters.sticker
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def fazalai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       fazaldb = MongoClient(MONGO_URL)
       fazal = fazaldb["FazalDB"]["fazal"] 
       is_fazal = fazal.find_one({"chat_id": message.chat.id})
       if not is_fazal:
           await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
           K = []  
           is_chat = chatai.find({"word": message.text})  
           k = chatai.find_one({"word": message.text})  

           if k:
                   for x in is_chat:
                       K.append(x['text'])
                       if K:  # Ensure K is not empty before using random.choice   
                           hey = random.choice(K)    
                           is_text = chatai.find_one({"text": hey})  
                           Yo = is_text['check']   
                           if Yo == "sticker":  
                               await message.reply_sticker(f"{hey}")   
                           else:
                               await message.reply_text(f"{hey}")
                       else:
                           print("I don't know how to respond yet! Teach me by replying to my messages.")

        
   if message.reply_to_message:  
       fazaldb = MongoClient(MONGO_URL)
       fazal = fazaldb["FazalDB"]["fazal"] 
       is_fazal = fazal.find_one({"chat_id": message.chat.id})    
       getme = await client.get_me()
       user_id = getme.id                             
       if message.reply_to_message.from_user.id == user_id: 
           if not is_fazal:                   
               await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})   

           if k:
                   for x in is_chat:
                       K.append(x['text'])
                       if K:  # Ensure K is not empty before using random.choice   
                           hey = random.choice(K)    
                           is_text = chatai.find_one({"text": hey})  
                           Yo = is_text['check']   
                           if Yo == "sticker":  
                               await message.reply_sticker(f"{hey}")   
                           else:
                               await message.reply_text(f"{hey}")
                       else:
                           print("I don't know how to respond yet! Teach me by replying to my messages.")


       if not message.reply_to_message.from_user.id == user_id:          
           if message.sticker:
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "id": message.sticker.file_unique_id})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.sticker.file_id, "check": "sticker", "id": message.sticker.file_unique_id})
           if message.text:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.text, "text": message.text})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.text, "text": message.text, "check": "none"})                                                                                                                                               

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & ~filters.private
    & ~filters.me
    & ~filters.bot,
)
async def fazalstickerai(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"]   

   if not message.reply_to_message:
       fazaldb = MongoClient(MONGO_URL)
       fazal = fazaldb["FazalDB"]["fazal"] 
       is_fazal = fazal.find_one({"chat_id": message.chat.id})
       if not is_fazal:
           await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})      
           k = chatai.find_one({"word": message.text})      
           if k:           
               for x in is_chat:
                   K.append(x['text'])
               hey = random.choice(K)
               is_text = chatai.find_one({"text": hey})
               Yo = is_text['check']
               if Yo == "text":
                   await message.reply_text(f"{hey}")
               if not Yo == "text":
                   await message.reply_sticker(f"{hey}")
   
   if message.reply_to_message:
       fazaldb = MongoClient(MONGO_URL)
       fazal = fazaldb["FazalDB"]["fazal"] 
       is_fazal = fazal.find_one({"chat_id": message.chat.id})
       getme = await client.get_me()
       user_id = getme.id
       if message.reply_to_message.from_user.id == user_id: 
           if not is_fazal:                    
               await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
               K = []  
               is_chat = chatai.find({"word": message.text})
               k = chatai.find_one({"word": message.text})      
               if k:           
                   for x in is_chat:
                       K.append(x['text'])
                   hey = random.choice(K)
                   is_text = chatai.find_one({"text": hey})
                   Yo = is_text['check']
                   if Yo == "text":
                       await message.reply_text(f"{hey}")
                   if not Yo == "text":
                       await message.reply_sticker(f"{hey}")
       if not message.reply_to_message.from_user.id == user_id:          
           if message.text:
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text})
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.text, "check": "text"})
           if message.sticker:                 
               is_chat = chatai.find_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id})                 
               if not is_chat:
                   chatai.insert_one({"word": message.reply_to_message.sticker.file_unique_id, "text": message.sticker.file_id, "check": "none"})    

@client.on_message(
    (
        filters.text
        | filters.sticker
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
@client.on_message(
    (filters.text | filters.sticker) & filters.private & ~filters.me & ~filters.bot
)


@client.on_message(
    (filters.text | filters.sticker) & filters.private & ~filters.me & ~filters.bot
)
async def fazalprivate(client: Client, message: Message):
    global user_message_count

    chatdb = MongoClient(MONGO_URL)
    chatai = chatdb["Word"]["WordDb"]

    user_id = message.from_user.id

    # Track the number of DMs from the user
    if user_id not in user_message_count:
        user_message_count[user_id] = 1
    else:
        user_message_count[user_id] += 1

    if not message.reply_to_message:
        await client.send_chat_action(message.chat.id, ChatAction.TYPING)
        K = []  
        is_chat = chatai.find({"word": message.text})  

        for x in is_chat:
            K.append(x['text'])

        if K:
            hey = random.choice(K)
            is_text = chatai.find_one({"text": hey})
            Yo = is_text['check']

            if Yo == "sticker":
                await message.reply_sticker(f"{hey}")
            else:
                await message.reply_text(f"{hey}")

    if message.reply_to_message:
        getme = await client.get_me()
        bot_id = getme.id

        if message.reply_to_message.from_user.id == bot_id:
            await client.send_chat_action(message.chat.id, ChatAction.TYPING)
            K = []
            is_chat = chatai.find({"word": message.text})  

            for x in is_chat:
                K.append(x['text'])

            if K:
                hey = random.choice(K)
                is_text = chatai.find_one({"text": hey})
                Yo = is_text['check']

                if Yo == "sticker":
                    await message.reply_sticker(f"{hey}")
                else:
                    await message.reply_text(f"{hey}")

    # If user has sent 2 messages, send join link
    if user_message_count[user_id] == 2:
        
        await message.reply_text(f'[{join_message}]({url})')

@client.on_message(
 (
        filters.sticker
        | filters.text
    )
    & filters.private
    & ~filters.me
    & ~filters.bot,
)
async def fazalprivatesticker(client: Client, message: Message):

   chatdb = MongoClient(MONGO_URL)
   chatai = chatdb["Word"]["WordDb"] 
   if not message.reply_to_message:
       await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
       K = []  
       is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
       for x in is_chat:
           K.append(x['text'])
       hey = random.choice(K)
       is_text = chatai.find_one({"text": hey})
       Yo = is_text['check']
       if Yo == "text":
           await message.reply_text(f"{hey}")
       if not Yo == "text":
           await message.reply_sticker(f"{hey}")
   if message.reply_to_message:            
       getme = await client.get_me()
       user_id = getme.id       
       if message.reply_to_message.from_user.id == user_id:                    
           await client.send_chat_action(message.chat.id, ChatAction.TYPING) 
           K = []  
           is_chat = chatai.find({"word": message.sticker.file_unique_id})                 
           for x in is_chat:
               K.append(x['text'])
           hey = random.choice(K)
           is_text = chatai.find_one({"text": hey})
           Yo = is_text['check']
           if Yo == "text":
               await message.reply_text(f"{hey}")
           if not Yo == "text":
               await message.reply_sticker(f"{hey}")
               

client.run()
