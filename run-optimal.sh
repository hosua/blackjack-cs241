iter="$1"

if [ -z "$iter" ]; then
    iter=0
fi

for i in $(eval echo "{0..$iter}"); do
    python3 optimal_strat.py
done
