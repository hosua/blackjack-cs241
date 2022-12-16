iter="$1"
trials="$2"

if [ -z "$iter" ]; then
    iter=1
fi
if [ -z "$trials" ]; then
    trials=1000
fi

for i in $(eval echo "{1..$iter}"); do
    python3 optimal_standard.py "$trials"
done
