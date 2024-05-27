def handle_response(message: str) -> str:
    p_message = message.lower()

    if p_message == "hello bewb":
        return "Hey there Bewber"
    
    if p_message == "!help":
        return "`Who knows, good luck.`"