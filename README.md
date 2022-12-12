# Blackjack


### Tester functions

```python
run(trials: int) -> dict
""" 
Runs games for a number of trials
"""

auto_play(hit_thresh: int) -> int
"""
Plays a single game, only hits if score is below hit_thresh
Returns 0 if loss, 1 if draw, and 2 if win
"""

init_stats_dict() -> dict
"""
Initializes dictionary containing the results of the trials.
---types---
thresh: int (0 through 20 inclusive)
freq: int
format: {
	thresh : {'loss': freq, 'draw': freq, 'win': freq }
	thresh : {'loss': freq, 'draw': freq, 'win': freq }
	thresh : {'loss': freq, 'draw': freq, 'win': freq }
		.
		.
		.
}
"""

def print_stats_dict(d: dict):
"""
Print the statistics dictionary
"""

```
