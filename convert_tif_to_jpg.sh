folder=non-psed
for file in $folder/*.TIF
do
  outfile=$folder/`basename $file .TIF`.jpg
  echo convert -verbose "'$file'" "'$outfile'"
done > script.txt
gm batch -echo on -feedback on script.txt
