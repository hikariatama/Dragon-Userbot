from pyrogram import Client, filters
from .utils.utils import modules_help


@Client.on_message(filters.command('inf', ['.']) & filters.me)
def get_user_inf(client, message):
    user = message.reply_to_message.from_user.id
    user_info = client.get_users(user)
    if user_info.username == None:
        username = 'None'
    else:
        username = f'@{user_info.username}'
    user_info = (f'''|=<b>Username: {username}
|-Id: {user_info.id}
|-Bot: {user_info.is_bot}
|-Scam: {user_info.is_scam}
|-Name: {user_info.first_name}
|-Status: {user_info.status}
|-Deleted: {user_info.is_deleted}
</b>''')
    message.edit(user_info)



modules_help.update({'user_info': '''<b>Help for |User_info|\nUsage:</b>
<code>.inf </code>
<b>[Reply to any message from a user to find out information about him]</b>''', 'user_info module': '<b>• User_info</b>:<code> inf</code>\n'})

