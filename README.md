# Local Binary Pattern

<a href="https://en.wikipedia.org/wiki/Local_binary_patterns">LBP</a>, Local Binary Pattern, is used in computer vision as a kind of feature.

### 簡易 LBP 實作，只做方形 3x3 大致上流程：

1. 將影像中的每個像素，與它周圍八個像素進行比較。
 
2. 周圍像素 <= 中心像素，則設置為 0；否則，設置為 1。
 
3. 獲得一組數列(當作2進制數列)，並轉為10進制數列，可視為灰階顏色。(數列的起始點可自訂義)
 
4. 計算 0-255 的直方圖，就得到影像的特徵向量。
 
5. 此特徵向量可以通過SVM來進行分類。


原圖：

<img src="https://github.com/CYT823/LocalBinaryPattern/blob/main/git_images/resource.png" width=200>

經過LBP計算後：

<img src="https://github.com/CYT823/LocalBinaryPattern/blob/main/git_images/result.png" width=200>

直方圖：

<img src="https://github.com/CYT823/LocalBinaryPattern/blob/main/git_images/histogram.png" width=200>
