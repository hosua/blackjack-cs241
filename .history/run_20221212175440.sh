iter="$1"

for i in $(eval echo "{0..$iter}"); do
    python3 main.py
done
