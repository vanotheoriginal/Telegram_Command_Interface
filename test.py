


message = '.delete_quote 1 This is newer quote'
quote = message.split(".delete_quote ", maxsplit=1)[1].split(' ', maxsplit=1)
quote_id, new_quote = quote
print(quote_id, ', ', new_quote)