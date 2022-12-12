# Background
Blackjack without face cards.
Normally when you play blackjack, it is risky to hit when you have 12 or more points.

Since there are many cards that are worth 10 points, (10, Jack, Queen, and King), it is ill-advised to hit. Since there is a high chance you will bust trying to do so.

However, this strategy changes when there are no face cards in the deck.

* All cards in deck 2,3,4,5,6,7,8,9,10,A


# What to test?

When is it most ideal to hit? To stand?

`2, 3, 4, 5, 6 --- 7, 8, 9, 10, A`

Hypothesis:
My prediction is that you should hit when your points are at 15 or below. This is because at 15 points, you have a 50% chance of drawing a card that will yield higher points, or a Blackjack.


How to test this:
Simulate game situation when hand is at 2 through 20 points.

Per each point, test at least 1000 trials and record the outcomes.