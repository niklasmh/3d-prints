Get-ChildItem "." -Filter *.scad | 
Foreach-Object {
  openscad -o "molds/$($_.BaseName).stl" $_.Name
  rm $_.Name
}
