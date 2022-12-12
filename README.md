# Blackjack


### Tester functions

```python
run(trials: int) -> dict
```
* Runs games for a number of trials

```python
def run_with_modified_deck(trials: int, ranks: list[str], frequencies: list[int]) -> dict:
```

* Runs games for a number of trials, with the removal of frequencies[i] # cards of rank[i], with i
being the index of the lists. Note that `len(ranks) must == len(frequencies)`.

---

```python
auto_play(hit_thresh: int) -> int
```
* Plays a single game, only hits if score is below hit_thresh
Returns 0 if loss, 1 if draw, and 2 if win

```python
init_stats_dict() -> dict
```
* Initializes dictionary containing the results of the trials.

---

Statistics dictionary structure:
```
key: int (2 through 20 inclusive)
val: dict({'loss': 0, 'draw': 0, 'win': 0})

stats_dict = {
	2 : {'loss': freq, 'draw': freq, 'win': freq }
	3 : {'loss': freq, 'draw': freq, 'win': freq }
	4 : {'loss': freq, 'draw': freq, 'win': freq }
		.
		.
	20 : {'loss': freq, 'draw': freq, 'win': freq }
}
```
```python
def print_stats_dict(d: dict):
```
* Print the statistics dictionary

