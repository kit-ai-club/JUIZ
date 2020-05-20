# 参考：https://spjai.com/python-tutorial/


"""
6. 各種データを扱うモジュール
6-1. 数学でよく扱う関数が扱える（math）
6-2. 配列の高速処理が可能（numpy）

について
"""
print("ウメザキが担当します")
"""
6-1. 数学でよく扱う関数が扱える（math）
数学でよく扱う関数が扱えるモジュール。
"""
import math # 数学の関数使いますよ～的な合図
#切り上げ
a1 = math.ceil(1.2)
print("1.2を小数点以下切り上げると...")
print(a1) #2
#切り捨て
a2 = math.floor(1.2)
print("1.2を小数点以下切り捨てると...")
print(a2) #1
#絶対値
a3 = math.fabs(-5)
print("-5の絶対値は...")
print(a3) #5
#累乗
a4 = math.pow(3,2)
print("3の2乗は...")
print(a4) #9
#余弦
a5 = math.cos(math.pi)
print("cosπは...")
print(a5) #-1


"""
6-2. 配列の高速処理が可能（numpy）

Pythonは他のコンパイラ言語と比べると処理が遅いが、numpyの配列オブジェクト「ndarray」を使用することで配列に関しては高速なデータ処理をすることが可能。

ndarrayとは一定の大きさをもつ、同じサイズや型で構成された複数の要素の多次元の配列である。
"""
# numpyはインストールして使用できる前にインポートすることが必要。
import numpy as np #numpyをnpとしてインポート

"""
一次元配列の作成
numpyで配列を作成する時はasarray関数を使用する。asarrayには３つの引数を渡すことができる。

asarrayの構文は下記：
"""
# np.asarray(配列したいデータ・必須,データタイプ・任意,順位・任意)
# listから配列を作成する時は
b1 = np.asarray([1,2,3])
print(b1)


# データタイプを渡すことで作成される配列の型を指定することができる。
# 例えばnp.int32,np.float32,np.float64などがある。
b2 = np.asarray([1,2,3],np.int32)
print(b2)
b3 = np.asarray([1,2,3],np.float32)
print(b3)
b4 = np.asarray([1,2,3],np.float64)
print(b4)
"""
ここら辺よくわかんないです泣！！

# 各要素が数値型の配列が作成される。
# 既存の配列のタイプを変えたい時はastype関数を使用する。
a = np.array([1, 2, 3])
print(a)
print(a.dtype)
# [1 2 3]
# int64

a_float = a.astype(np.float32)
print(a_float)
print(a_float.dtype)
# [1. 2. 3.]
# float32

print(a)
print(a.dtype)
# [1 2 3]
# int64

"""
"""
行列(多次元配列)の作成
行列を作成する時もasarray()関数を使用する
"""
#例えば[[1,2,3],[4,5,6]]の行列を作成したい時は
b5 = np.asarray([[1,2,3],[4,5,6]])
print(b5)

#numpyを使って配列の計算を簡単にできる。
#配列の各要素に対して演算処理がいっぺんに可能
my_arr = np.asarray([1,2,3],np.int32)
print(my_arr * 3)#[3 6 9]
print(my_arr+ 3)#[4 5 6]


#dot関数を使って行列の積を求める
my_arr1 = np.asarray([[1,2,3],[4,5,6]])
my_arr2 = np.asarray([[7,8],[9,10],[11,12]])
my_arr3 = my_arr1.dot(my_arr2)
print(my_arr3)# [[ 58  64] [139 154]]

#numpyでは様々な関数を配列に適用することができる。その関数は各要素に対して処理される。
my_arr = np.asarray([1,2,3,4])
b6 = np.exp(my_arr)# array([  2.71828183,   7.3890561 ,  20.08553692,  54.59815003])
print(b6)
b7 = np.log(my_arr) #array([ 0. ,  0.69314718,  1.09861229,  1.38629436])
print(b7)
b8 = np.sqrt(my_arr) #array([ 1.,  1.41421356,  1.73205081,  2.])
print(b8)

