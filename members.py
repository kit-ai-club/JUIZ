class Inadumi:
    def __init__(self):
        self.name = "稲積 駿"
        self.course = "情報工学課程"
        self.grade = "3"
        self.hobby = ["books","music","coffee"]

    def status(self,element):
        if(element == "名前"):
            return(self.name)
        elif(element == "課程"):
            return(self.course)
        elif(element == "学年"):
            return(self.grade)
        else:
            return(self.name,self.course,self.grade);

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


class DaichiTezuka():  # class名は大文字からと言いつつ、小文字でも実行できたがなぜ？why?
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



members = []

# 会員番号順に append していく
reila = ReiLa()
members.append(reila)

sasaki = SasakiHidetaka()
members.append(sasaki)

tezuka = DaichiTezuka()
members.append(tezuka)

inadumi = Inadumi()
members.append(inadumi)



print("--------メンバー--------")
for i, m in zip(range(len(members)), members):
    name, katei, kaisei = m.status("全部")
    print(f"No.{i}", name, katei, kaisei)

print("--------趣味--------")
for m in members:
    print(m.status("名前") + "の趣味：")
    m.print_hobby()
