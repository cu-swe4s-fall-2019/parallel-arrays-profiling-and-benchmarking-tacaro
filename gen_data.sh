
for i in `seq 1 100`; do
    echo $RANDOM $RANDOM
done

(for i in `seq 1 100`; do
    echo "$RANDOM $RANDOM";
done )> data.txt
