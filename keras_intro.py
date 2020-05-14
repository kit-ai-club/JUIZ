
"""
我流プログラミングのすゝめ
コツ①興味があることしか、やらない僕は、プログラミングそのものではなく、AIに興味があったので、AIやるうえで使う技術しかない。他は全部忘れた。
コツ②覚えない頑張ってコーディングを覚えようとしない。忘れたらググる。エラー吐いたらググる。ともかくググる。ググって忘れる。
コツ③コピペする自分の目的と似たようなコードが、たいていネットとくにgithubにある。それをコピペして、ちょこっと改変してできあがり。
コツ④デバッグ機能を活用するなんかエラー吐いたら、とりあえずデバッグ。コピペしたコードの挙動が、ぱっと見でよくわからんかったら、とりあえずデバッグ。

"""


# 脳死で覚えるkeras入門
# https://qiita.com/wataoka/items/5c6766d3e1c674d61425
"""
データを用意する。Deep Learning においては、「ビッグデータ」と言う通り、大量かつ整ったデータが必要。
モデルを構築する。モデル＝NN。深さは、何層(layer)にするか、幅はどれくらいにするか。など。
モデルにデータを学習(train)させる。ミス山を下山させる＝誤差関数(loss)を最小化(minimize)させる。訓練専用データを用いる。
モデルを評価(evaluate)する。評価専用データ（テストデータ）を用いて、線引きのlossを測定する。未知のデータを用いることで、公平なジャッジができる。

"""






from keras.datasets import mnist

# keras.datasetsってところから、mnistというなんかを、借りるよ～

# keras. のドットは、「の中の」って意味。
# 「の中の」が使えるのは、kerasという「ディレクトリ」の中に、datasetsが入ってるから。

# import 単品でも使う。

(x_train, y_train), (x_test, y_test) = mnist.load_data()
# おきまりとして、x = 入力データinput、y = 教師データ。NNにいれたoutputとyを近づけるのがtrain.

# importできるのは、「クラスclass」か「関数function」で、関数は必ず「関数名()」となるから、
# mnist = class,  load_data() = function
# load_data() は、mnist「の中の」function

# 関数とは、inputになんやかんやしてoutputにする変換器。
# クラスとは、いくつかの関数や変数を保存しておいて、いつでも引っ張り出せる箱。

# ただし、load_data() はinputがなくて、outputだけある。データを吐き出すだけの関数。
# train とあるのは訓練データ、test とあるのはテストデータ。


# デバッグdebug してみよう。


from keras.utils.np_utils import to_categorical

# 画像を1次元化
x_train = x_train.reshape(60000, 784)
x_test = x_test.reshape(10000, 784)

# 画素を0~1の範囲に変換(正規化)
x_train = x_train.astype('float32') / 255
x_test = x_test.astype('float32') / 255

# 正解ラベルをone-hot-encoding
y_train = to_categorical(y_train, 10)
y_test = to_categorical(y_test, 10)

from keras.models import Sequential
from keras.layers import Dense

model = Sequential()
model.add(Dense(64, activation='relu', input_dim=784))
model.add(Dense(10, activation='softmax'))

model.compile(optimizer='rmsprop',
              loss='categorical_crossentropy',
              metrics=['accuracy'])

model.fit(x_train, y_train,
          batch_size=100,
          epochs=12,
          verbose=1)

score = model.evaluate(x_test, y_test)
print(score[0])
print(score[1])
