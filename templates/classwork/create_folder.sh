echo "which assignment is this: "
read assignment_num
directory="$assignment_num""_py"
# works if you run from root directory
mkdir "$directory"
#rsync used because cp does not work
rsync templates/classwork/* "$directory" --exclude "create_folder.sh"
exit
