from random import shuffle

class Card:

	def __init__(self, suit, value):
		self.suit = suit
		self.value = value

	def __repr__(self):
		return f"{self.value} of {self.suit}"

class Deck:

	suit = ('Hearts', 'Diamonds', 'Clubs', 'Spades')
	value = ('A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K')

	def __init__(self, numCards):
		self.cards = []
		self.numCards = numCards
		for i in self.suit:
			for j in self.value:
				self.cards.append(Card(i, j))


	def __repr__(self):
		return f'Deck of {self.count()} cards'

	def count(self):
		return len(self.cards)

	def _deal(self, numCards):
		count = self.count()
		dealt = []

		for i in range(numCards):
			if count == 0:
				raise ValueError('All Cards Have Been Dealt')
			else:
				dealt.append(self.cards.pop())

		return dealt

	def deal_hand(self, size):
		return self._deal(size)

	def deal_card(self):
		return self._deal(1)[0]

	def shuffle(self):
		if self.count() < 52:
			raise ValueError('Only full decks can be shuffled')
		shuffle(self.cards)
		return self


deck = Deck(52)
deck.shuffle()
card = deck.deal_card()
print(card)
hand = deck.deal_hand(50)
card2 = deck.deal_card()
print(card2)
print(deck.cards)
deck.deal_card()