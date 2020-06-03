"""
5. 関数・例外処理
5-1. 関数
5-2. 呼び出し方
5-3. 引数
5-4. 戻り値
について
"""
"""
関数
"""
# これが関数です
print("hello world")
# 関数は
#kansu0()
def kansu0():
    print("これが関数です")
    print("関数は1行のプログラムで複数の命令を持つ処理を実行するために使用します")
    print("関数を自分で作る場合、def構文を使って関数を定義する必要があります")
    print("関数を定義している場所よりも上で実行することはできません。")
#kansu0()
"""
関数の作り方
"""
def kansu1():
    print("私は社畜だ")
    print("魔材はジュースだ")
    print("終電帰りがデフォルトだ")
# 関数の呼び出し方
kansu1()
"""
演習1
"""
# 次のプログラムを関数にまとめて実行してみましょう
print("reilaが仲間になりたそうにこちらを見つめている！")
print("あなたはreilaに敗北した")
print("あなたはreilaの仲間になった")
"""
引数
"""
# 引数って何だろう
def kansu2():
    print("〇〇は関数を実行した！")
kansu2()
# 引数を使ってみる
def kansu3(one,two):
    three=one+two
    print(three)
kansu3(2,5)

"""
演習2
"""
#引数に2つの値を渡すとその足し算の結果がprintで表示される関数tasizanを作ってみましょう


# def tasizan(){
#
# }

#tasizan(2,4)
#tasizan(5,10)

"""
戻り値
"""
def kansu4(name,role):
    text=name+"は"+role+"になった!"
    return text
def kansu5(one,two):
    result=(one+two)/2
    return result
avarage=kansu5(3,9)
print(avarage)
#関数の引数ででさらに関数を実行できる
print(kansu4("森迫学長","日本史の黒幕"))
"""
演習3
"""
# 数字を3つかけあわせて返す関数multiを書きましょう
#def multi(#ここにsums関数の引数を書きましょう){
    #ここに関数の処理を実装しましょう
#}
##printf(multi())