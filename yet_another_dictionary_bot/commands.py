import urbandictionary as ud
from telegram import Bot, Update, ParseMode
from emoji import emojize

e_thumbs_up = emojize(':thumbsup:', use_aliases=True)
e_thumbs_down = emojize(':thumbsdown:', use_aliases=True)


def start(bot: Bot, update: Update):
    """Send Start / Help message to client.

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
    """
    reply = """*Yet Another Urban Dictionary Bot* 
     
[@yet_another_urban_dictionary_bot](https://t.me/yet_another_urban_dictionary_bot) | [GitHub](https://github.com/Nachtalb/yet_another_urban_dictionary_bot) 
 
*How to use me* 
Just send me any text and I try to find the definition in Urban Dictionary for you. Like this you don't have to 
extra open the another app and this whole slow process.
 
*Commands* 
- /help, /start: show this help message with information about the bot and it's usage. 
 
*My other bots*  
Please share this bot with your friends so that I ([the magician](https://github.com/Nachtalb/) behind this project)  
have enough motivation to continue and maintain this bot. 
 
Check out my other project\[s\]: 
- [@insta_looter_bot](https://t.me/insta_looter_bot) - Download images and videos from Instagram via 
Telegram
- [@reverse_image_search_bot](https://t.me/reverse_image_search_bot) - Reverse image search directly in  
Telegram

*Contributions* 
_Bug report / Feature request_ 
If you have found a bug or want a new feature, please make an issue here: [Nachtalb/yet_another_urban_dictionarybot](https://github.com/Nachtalb/yet_another_urban_dictionary_bot) 
 
_Code Contribution / Pull Requests_ 
Please use a line length of 120 characters and [Google Style Python Docstrings](http://sphinxcontrib-napoleon.readthedocs.io/en/latest/example_google.html).  
 
Thank you for using [@yet_another_urban_dictionary](https://t.me/yet_another_urban_dictionary_bot).
"""
    update.message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def define(bot: Bot, update: Update, args: list = None):
    """Search in dictionary

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
        args (:obj:`list`): List of sent arguments
    """
    word = update.message.text
    if args:
        word = ' '.join(args)

    definitions = ud.define(word)

    best = definitions[0]
    reply = """
*Definition for [{word}]*
    
{definition}

*Example*
    
{example}
    
*Votes*
{emoji_up} {upvotes} | {emoji_down} {downvotes}
""".format(
        word=best.word,
        definition=best.definition,
        example=best.example,
        upvotes=best.upvotes,
        downvotes=best.downvotes,
        emoji_up=e_thumbs_up,
        emoji_down=e_thumbs_down
    )
    reply = emojize(reply, use_aliases=True)
    update.message.reply_text(reply, parse_mode=ParseMode.MARKDOWN)


def unknown(bot: Bot, update: Update):
    """Send a error message to the client if the entered command did not work.

    Args:
        bot (:obj:`telegram.bot.Bot`): Telegram Api Bot Object.
        update (:obj:`telegram.update.Update`): Telegram Api Update Object
    """
    update.message.reply_text('Sorry, I didn\'t understand that command. Use /help for more information.')
