import numpy as np  #NumPyを組み込み、npという名前でNumpPyの関数を使う
import matplotlib.pyplot as plt

root =  "d:\\data\\data\\" #ファイルを保存したディレクトリ名を入れる
path =  root+"data20230505-20200120.txt"    #ファイル名を入れる(要修正)
pathgraph =root+"coronapos.pdf"   #pdf形式でグラフを保存する場所(要修正)
with open(path) as fileobj:           #ファイルを開いて、fileobjという名前にする
    dlist =  fileobj.readlines()

datalist = dlist[::-1]          #古い日付から新しい日付の順にに入れ替え
data = [ int(s) for s in  datalist] #文字データを数字データに変換
print(data)

plt.plot(data)
plt.xlabel("from 20200124 to 20220703")
plt.title("Coronavirus positives in Tokyo ")
plt.savefig(pathgraph)   #pdf形式でグラフを保存
plt.show()

import numpy as np  #NumPyを組み込み、npという名前でNumpPyの関数を使う
import matplotlib.pyplot as plt     

pathdir =root     #データファイルの保存先、要修正
path = pathdir + "data20230505-20200120.txt"  #データファイル名

with open(path) as fileobj:           #ファイルを開いて、fileobjという名前にする
    dlist =  fileobj.readlines()

datalist = dlist[::-1]          #古い日付から新しい日付の順にに入れ替え
datanp = [ int(s) for s in  datalist]  #文字データを数値に変換
datalen=len(datanp)
print("Data length=",datalen)

plt.style.use('default')             #描画スタイルは通常の形
fig, ax = plt.subplots()
fig.suptitle("COVID-19 positive in Tokyo", fontsize = 16)
ax.plot(datanp, label = "Reported")     #描画用データ作成(表示しないがここで図を作成)

ax.legend()
ax.set_xlabel("days")             
ax.set_ylabel("COVID-19 positive / day")            

plt.savefig(pathdir+"Fig1.pdf")   #図の保存
plt.savefig(pathdir+"Fig1.png")   #図の保存
plt.show()                       #図を表示する

#　×をクリックして図を閉じた後の処理
xmin, xmax = ax.get_xlim()       #選んだ領域の最小、最大
xmin=int(xmin)
xmax=min(int(xmax),datalen)

print("xmin=",xmin, "xmax=",xmax)

#統計処理関数
#ほとんどの場合、自分で関数を書かなくても用意されているが、今回は練習のため作成
# data（リスト）のstartからendまでに対する統計
def getstat(data, start, end):  
    sumx=0                     
    sumy=0                    
    sumxy=0
    sumxx=0
    for i in range(start, end):
        sumx  +=  i
        sumy  +=  data[i]
        sumxy +=  i*data[i]
        sumxx +=  i*i

    n= end-start
    a=(n*sumxy-sumx*sumy)/(n*sumxx-sumx*sumx)
    b=(sumxx*sumy-sumx*sumxy)/(n*sumxx-sumx*sumx) 
    return a,b  #  y=ax+b

a, b = getstat(datanp, xmin, xmax)
print("Linear a b ", a, b)

logdata = [ np.log(s) for s in  datanp[xmin:xmax] ]  # 対数変換
k, logg = getstat(logdata, 0, xmax-xmin)
print("Exponential  k log(g) ", k, logg)

#関数の定義　
def LinearReg(x, a,b):     # 1次回帰
    return  a*x+b

def ExpReg(x,xmin, k,logg):  #指数関数回帰
    return  np.exp(k*(x-xmin)) * np.exp(logg)

fig2, ax2 = plt.subplots()
fig2.suptitle("COVID-19 positive in Tokyo", fontsize = 20)

#描画領域を2倍にしてグラフを書く
x2min = xmin-(xmax-xmin)
x2max = xmax+(xmax-xmin)

y2min=0
y2max = np.max(datanp[x2min:x2max]) 

x = np.linspace(x2min, x2max, x2max-x2min)

ylin = LinearReg(x,a, b) 
ax2.plot(x,ylin, label="Linear  Regression",linestyle='dashed')

yexp = ExpReg(x,xmin, k,logg) 
ax2.plot(x,yexp, label="Exponential Regression",linestyle='dashed')

ax2.plot(datanp, label="Reported")  
ax2.plot(np.arange(xmin, xmax),datanp[xmin:xmax])  #選択領域データを色を変えて表示

ax2.legend()
ax2.set_xlabel("days")            
ax2.set_ylabel("COVID-19 positive / day ")             
ax2.set_xlim(x2min, x2max)         
ax2.set_ylim(y2min, y2max*2)  #y方向の上の部分にlabelを書くスペースを作る。            

plt.savefig(pathdir+"Fig2.pdf")  
plt.savefig(pathdir+"Fig2.png")  
plt.show() 
