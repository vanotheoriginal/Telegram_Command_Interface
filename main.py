from pyrogram import Client, filters
from sqlite import __sqlite_select_all, __sqlite_select_last, __sqlite_insert, __sqlite_update, __sqlite_delete_quote

app = Client("my_account")

@app.on_message(filters.command(['save_quote', 'print_last', 'print_all', 'delete_quote', 'quote_db', 'edit_quote'], prefixes='.') & filters.me & filters.private)
def my_handler(_, message):

    try:
        if message.command[0] == 'save_quote':

            message_text = message.text.split(".save_quote ", maxsplit=1)[1]
            __sqlite_insert(message_text)
            app.send_message('me', 'Saved successfully.')


        elif message.command[0] == 'print_last':

            res = __sqlite_select_last()
            app.send_message('me', res)


        elif message.command[0] == 'print_all':

            res = __sqlite_select_all()
            app.send_message('me', res)


        elif message.command[0] == 'delete_quote':

            quote_id = message.text.split(".delete_quote ", maxsplit=1)[1]
            __sqlite_delete_quote(quote_id)
            app.send_message('me', 'Deleted successfully.')


        elif message.command[0] == 'quote_db':

            res = __sqlite_select_all(2)
            app.send_message('me', res)


        elif message.command[0] == 'edit_quote':

            quote = message.text.split(".edit_quote ", maxsplit=1)[1].split(' ', maxsplit=1)
            quote_id, new_quote = quote
            __sqlite_update(new_quote, quote_id)
            app.send_message('me', 'Updated successfully.')


    # except IndexError:
    #     app.send_message('me', 'Quote field empty.')
    except Exception as e:
        app.send_message('me', f'Exception: {e}')

app.run()