安裝套件:
pip install -r requirements.txt

爬蟲分為兩部分:
1.依據分類爬每個歌手 ex.male/周杰倫.csv
2.合成分類內全部歌手 ex.male/* -> male/all.csv

先執行測試程式:
bash run.sh test test_all.csv
會有一個資料夾test，裡面有爬到的5個csv
還有一個test_all.csv，此為結果
此程式執行成功，表示一切OK，即可開始下面的程式

bash run.sh <要爬的分類> <輸出路徑>
分類有六種:male/female/group/JapanKorea/EUNA/else ***一定要是其中一個***
輸出路徑:輸出的csv檔名  ex.male_all.csv
