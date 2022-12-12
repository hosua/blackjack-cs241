iter="$1"
num_trials="$2"

if [ -z "$num_trials" ]; then
	num_trials=1000
fi

if [ -z "$iter" ]; then
    iter=0
fi

for i in $(eval echo "{0..$iter}"); do
    python3 main.py "$num_trials"
done
