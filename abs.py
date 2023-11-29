#ファイルを読み込むためのglob
#行列化するためのnumpy
import glob
import numpy as np

#ファイル名は意味を持たせる
#globでテキストファイルを読み込む。絶対参照が無難
#ここでファイルをpython内に取り込んでいる
measurement_files = glob.glob("C:/python/abs/*.txt")
DIWfile = glob.glob("C:/python/abs/*DIW*.txt")
measurement_files = list(set(measurement_files) - set(DIWfile))

#glob.globはリストとして取り込まれる。
#なので一つのファイルを読み込んでも一つ目の要素として[0]のように書いてあげる必要がある。
DIWdata = np.loadtxt(DIWfile[0],skiprows=1)

#filenameの中にmeasurement_filesのデータが入っている。
#forの中でAbsを計算して、保存していく。
for filename in measurement_files:
    data = np.loadtxt(filename,skiprows=1)
    Abs = -np.log10(data[:,1]/DIWdata[:,1])
    filename_split = filename.split(".")
    savename = filename_split[0] + "-111001-N.csv"
    np.savetxt(savename,np.stack([data[:,0],Abs],1),delimiter=",",fmt= "%.1f,%.8e")