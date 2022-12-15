# Blackjack

1. Run ``./run-optimal.sh 10`` to generate 10 sets of data using standard optimal strategy on standard deck.
2. Run ``./run-unoptimal-nofaces.sh 10`` to generate 10 sets of data using standard optimal strategy on deck with no faces (The unoptimal strategy).
3. Run ``./run-experiment-nofaces 10`` to generate 10 sets of data using our newly found optimized strategy on deck with no face cards.

Modify the `hard_hands` and `soft_hands` dicts in ``modified_experiment.py`` with our new hit threshholds that optimize the strategy of Blackjack given that there are no face cards in the game.
