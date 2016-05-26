from Card import Card
class DealCard:

    def __init__(self):
        return

    def dealCard(self, house):
        drawCard = house.pop()
        card = Card()
        card.determineCardType(drawCard)
        print(card.face, card.suit, card.value)