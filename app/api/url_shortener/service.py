from app.constants.emojis import emojis


def filtered_emojis():
    emojis_list = emojis.get("emojis", [])
    excluded_categories = ["Symbols", "Flags"]
    return [
        emoji.get("emoji", "")
        for emoji in emojis_list
        if emoji.get("category", "") not in excluded_categories
        and len(emoji.get("code", [])) == 1
    ]
