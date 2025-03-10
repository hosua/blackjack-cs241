# Blackjack

This repository contains a series of scripts that automate games of Blackjack, saves them to `.json`, and uses matplotlib to graph the data to images for visualization.

## Dependencies

```
numpy 1.23.5
matplotlib 3.6.2
```

To install the necessary modules, run `pip install -r requirements.txt` before running the scripts.

## Usage

1. Run ``python3 optimal_standard.py 1000`` to generate 1000 trials of Blackjack data using standard optimal strategy on standard deck.

2. Run ``python3 unoptimal_nofaces.py 1000`` to generate 1000 trials of Blackjack data using standard optimal strategy on deck with no faces (The unoptimal strategy).

3. Run ``python3 optimal_nofaces.py 1000`` to generate 1000 trials of Blackjack data using our newly found optimized strategy on deck with no face cards.

3. Run ``python3 calc_busts.py 1000`` to generate 1000 trials of Blackjack data and generate statistics of the cards that the dealer drew throughout the game, and the times the dealer busted with said cards.

# Important Resources

[Blackjack Guide](https://www.kjartan.co.uk/games/blackjack.htm)

[Blackjack Chart](https://www.kjartan.co.uk/games/pix/cards/Blackjack%20full%20guide.pdf)
