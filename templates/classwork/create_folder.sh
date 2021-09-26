# works if you run from root director
mkdir nn_Py
#rsync used because cp does not work
rsync templates/classwork/* nn_Py --exclude "create_folder.sh"
exit
