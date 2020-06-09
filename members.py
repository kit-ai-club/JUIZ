"""
補足：
・変数・関数・クラス名は本来「自由」。ただ、できるだけ分かりやすくするために、いろんなマナーがある。
・インスタンス作成文は、初期化関数の呼び出し文でもある。初期化関数に引数を用意するなら、インスタンス作成文に引数を書かないといけない。
・関数・クラス・クラス関数・クラス変数は、一度定義すればそれに縛られる。いっぽう一時変数は、じゃんじゃん新しいのを作れる。
・関数の引数名は自由。分かりやすいのをつけてあげよう
・灰色になっている変数は、せっかく定義したのに使われてないよ、のサイン
"""

class Yasuoka:
    def __init__(self):
        hobby = ["歌","美術館巡り","読書","アニメ"]
        self.hobby = hobby

        self.name = "安岡里都"
        self.katei = "情報工学"
        self.gakunenn = "1回生"

    def status(self,a):
        if a == "名前":
            return self.name
        if a == "課程":
            return self.katei
        if a == "gakunenn":
            return self.gakunenn
        else:
            return self.name,self.katei,self.gakunenn
    def print_hobby(self):
        for b in self.hobby:
            print(b)



class Maeno:
    def _init_(self):
        self.name = "前野彩実"
        self.course = "情報工学"
        self.grade = "1年"
        self.hobby = ["pen spinning", "sportscar"]

    def status(self, set):
        if set == "名前":
            return self.name
        elif set == "課程":
            return self.course
        elif set == "学年":
             return self.grade
        else:
            return self.name, self.course, self.grade

    def print_hobby(self):
        for hobby in self.hobby:
            print(hobby)



class Inadumi:
    def __init__(self):
        self.name = "稲積 駿"
        self.course = "情報工学課程"
        self.grade = "3"
        self.hobby = ["books", "music", "coffee"]

    def status(self,element):
        if element == "名前":
            return self.name
        elif element == "課程":
            return self.course
        elif element == "学年":
            return self.grade
        else:
            return self.name, self.course, self.grade

    def print_hobby(self):
        for element in self.hobby:
            print(element)

class ReiLa:
    def __init__(self):
        self.name = "零来"
        self.katei = "なし"
        self.kaisei = "なし"
        self.hobby = ["お話し", "音楽鑑賞"]

    def status(self, input):
        if input == "名前":
            return self.name
        elif input == "課程":
            return self.katei
        elif input == "学年":
            return self.kaisei
        else:
            return self.name, self.katei, self.kaisei

    def print_hobby(self):
        for h in self.hobby:
            print(h)


class SasakiHidetaka:
    def __init__(self):
        self.name = "佐々木秀隆"
        self.katei = "情報"
        self.kaisei = "B4"
        self.hobby = ["ギター", "睡眠"]

    def status(self, input):
        if input == "名前":
            return self.name
        elif input == "課程":
            return self.katei
        elif input == "学年":
            return self.kaisei
        else:
            return self.name, self.katei, self.kaisei

    def print_hobby(self):
        for h in self.hobby:
            print(h)


class DaichiTezuka:  # class名は大文字からと言いつつ、小文字でも実行できたがなぜ？why?
    def __init__(self, *hobby):  # *を付けると任意の数の引数を指定できるらしい
        hobby = ["音楽","キャンプ","仕組みを理解すること"]
        self.hobby = hobby  # classにhobbyという変数を格納

    def status(self,st):
        ST = ["手塚 太地","電子システム工学課程","3回"]
        if st=="名前":
            return(ST[0])
        if st == "課程":
            return(ST[1])
        if st == "学年":
            return(ST[2])
        else:
            return(ST)

    def print_hobby(self):
        [print(i) for i in self.hobby]


class Yoshida:
    def __init__(self):
        self.namae = "吉田健悟"
        self.katei = "応用化学課程"
        self.gakunen = "1回生"
        self.hobby = ["音楽", "水泳", "漫画"]

    def status(self, x):
        if x == "名前":
            return self.namae
        elif x == "課程":
            return self.katei
        elif x == "学年":
            return self.gakunen
        else:
            return self.namae, self.katei, self.gakunen

    def print_hobby(self):
        for y in self.hobby:
            print(y)


class Sanjo:
    def __init__(self):
        self.name="三城史裕"
        self.cource="情報工学課程"
        self.grade="2回生"
        self.hobby=["ロボコン","画像認識","web作成"]
    def status(self,hoge):
        if hoge=="名前":
            return  self.name
        elif hoge=="学年":
            return self.grade
        elif hoge=="課程":
            return self.cource
        else:
            return self.name,self.cource,self.grade
    def print_hobby(self):
        for fuga in self.hobby:
            print(fuga)





members = []

# 会員番号順に append していく
reila = ReiLa()
members.append(reila)

sasaki = SasakiHidetaka()
members.append(sasaki)

maeno = Maeno()
members.append(maeno)

tezuka = DaichiTezuka()
members.append(tezuka)

inadumi = Inadumi()
members.append(inadumi)

yoshida = Yoshida()
members.append(yoshida)

print("--------メンバー--------")
for i, m in zip(range(len(members)), members):
    name, katei, kaisei = m.status("全部")
    print(f"No.{i}", name, katei, kaisei)

print("--------趣味--------")
for m in members:
    print(m.status("名前") + "の趣味：")
    m.print_hobby()
