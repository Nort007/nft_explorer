def text_to_edit_selected_condition(nft_name, button, condition):
    return "NFT: {}\n" \
           "Short_condition: {}\n" \
           "Condition (your_price, current_price): {}".format(nft_name, button, condition)


def prepare_text_to_choose_option(choose):
    if choose == 'name':
        return "Insert nft name"
    else:
        return "Insert contract address"


def prepare_text_for_watchlist_menu():
    return '🗂 User watchlist:'
