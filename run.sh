if [ $# -ne 2 ]
then
	echo "請輸入足夠的參數!(2個)"
	exit
fi

mkdir $1
python crawler.py $1
python mix.py $1 $2
