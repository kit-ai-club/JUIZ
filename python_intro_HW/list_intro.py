# 参考：https://spjai.com/python-tutorial/


"""
4. 配列
4-1. 他のプログラム言語でいう配列（list）
"""
list = [1, 2, 3, 4]  # 配列の宣言と初期化
print(list)

list1 = [1, 2, 3, 4, 5]
list1 = list1 + [6, 7, 8]  # 要素の追加
print(list1)

list2 = [1, 2, 3, 4, 5]
print(len(list2))  # 要素数の取得

# in演算子を用いた要素の検索
# 出力結果を比較してみましょう！
list3 = [1, 2, 3, 4, 5]
print(3 in list3)
list4 = [1, 2, 3, 4, 5]
print(500 in list4)

# for文との組み合わせ
my_list5 = [1, 2, 3, 4]
for value in my_list5:
    print(value)

# 【演習】
# 1〜10までをリストに格納し、それぞれの値を2乗した値を出力してみましょう！

"""
4-2. 辞書構造（dictionary）
"""
# 辞書型は { から } までの間に複数の要素をカンマ(,)で区切って定義します。
# 要素はキーと対応する値の組み合わせを キー:値 の形式で記述します。
# {キー1:値1, キー2:値2, ...}のようになります。
mydict = {"apple": 1, "orange": 2, "banana": 3}

# 辞書型オブジェクトには順序がないので、要素を取り出すためにはkeyを使うことになります。
val = mydict["apple"]
print(val)

# 【演習】
# 下記のdictionaryオブジェクトを使用してそれぞれのkeyとvalueを取得し
# valueが20以上の場合{keyの中身}:hotと出力し
# 超えていない場合は{keyの中身}:coldと出力してみましょう!
temperatures = {'x': 24, 'y': 18, 'x': 30}

"""
4-3. 変更を許可しない変数等に使う配列（tuple）
"""
# リストは要素を消したり追加したり編集したりできるのに対し、タプルはできない。
# タプルはリストとよく似ているがリストは[]でタプルは()で作成する。
tuple_1 = (1, 2, 3)

tuple_2 = tuple_1 + (4, 5)  # 要素の追加
print(tuple_2)

"""
4-6. リストの内包表記
"""
# 内包表記とはリストのようなシーケンスオブジェクトの各要素に対して処理を行いたい時に便利
# 例として1~5のうち、4と5に２をかけたリストを生成してみる
list1 = [1, 2, 3, 4, 5]
list1 = [x * 2 for x in list1 if x > 3]
print(list1)  # [8, 10]が出力される

# 【演習】
# for文を用いた内包表記で、1~10の数字の内2の倍数のものだけを含むリストを作成してみましょう!
