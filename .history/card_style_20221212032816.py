def make_card(card):
    look = []
    rank = card.get_rank()
    suit = card.get_suit()
    look.append("┌─────────┐")
    look.append("|{}       |")
    look.append("|    .    |")
    look.append("|   / \   |")
    look.append("|  (_ _)  |")
    look.append("|    |    |")
    look.append("|       {}|")
    look.append("└─────────┘")

    covered = []
    covered.append("┌─────────┐")
    covered.append("|\ ~ ~ ~ /|")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("|/ ~ ~ ~ \|")
    covered.append("└─────────┘")

    if suit == "C" and rank == "Covered":
        return covered

    rank_len = len(rank)
    if rank_len == 1:
        x = ("|", rank, "        |")
        look[1] = "".join(x)
        x = ("|       ", rank, " |")
        look[6] = "".join(x)

    if rank_len == 2:
        x = ("|", rank, "       |")
        look[1] = "".join(x)
        x = ("|       ", rank, "|")
        look[6] = "".join(x)

    if rank_len > 2:
        x = ("|", rank[:1], "        |")
        look[1] = "".join(x)
        x = ("|       ", rank[:1], " |")
        look[6] = "".join(x)

    if suit == "Diamonds":
        look[2] = "|    ^    |"
        look[3] = "|   / \   |"
        look[4] = "|   \ /   |"
        look[5] = "|    .    |"

    if suit == "Clubs":
        look[2] = "|    _    |"
        look[3] = "|   ( )   |"
        look[4] = "|  (_'_)  |"
        look[5] = "|    |    |"

    if suit == "Hearts":
        look[2] = "|   _ _   |"
        look[3] = "|  ( v )  |"
        look[4] = "|   \ /   |"
        look[5] = "|    .    |"
    
        
    return look

def make_cover(card):

    covered = []
    covered.append("┌─────────┐")
    covered.append("|\ ~ ~ ~ /|")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("| }}}:{{{ |")
    covered.append("|/ ~ ~ ~ \|")
    covered.append("└─────────┘")

    return look
    
