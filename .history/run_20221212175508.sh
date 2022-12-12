iter="$1"

if [ -z "$iter" ]; then
    iter=1
fi

for i in $(eval echo "{0..$iter}"); do
    python3 main.py
done
