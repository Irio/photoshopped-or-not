folder=psed-reddit
for file in $folder/*.png
do
  outfile=$folder/`basename $file .png`.jpg
  echo convert -verbose "'$file'" "'$outfile'"
done > script.txt
gm batch -echo on -feedback on script.txt
