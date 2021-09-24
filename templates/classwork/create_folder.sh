mkdir ../../Knn
#rsync used because cp does not work
rsync ./* ../../Knn --exclude-from:"create_folder.sh"
exit
