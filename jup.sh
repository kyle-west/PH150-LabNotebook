if [ "$1" == "convert" ]; then
   for ipynb in *.ipynb; do
      jupyter nbconvert --to html "$ipynb"
   done;
fi