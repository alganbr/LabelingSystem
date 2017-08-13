for D in `find . -type d -maxdepth 1`
do
    rm -rf ./${D}/migrations
done