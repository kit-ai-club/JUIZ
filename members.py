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


members = []

# 会員番号順に append していく
reila = ReiLa()
members.append(reila)

sasaki = SasakiHidetaka()
members.append(sasaki)





print("--------メンバー--------")
for i, m in zip(range(len(members)), members):
    name, katei, kaisei = m.status("全部")
    print(f"No.{i}", name, katei, kaisei)

print("--------趣味--------")
for m in members:
    print(m.status("名前") + "の趣味：")
    m.print_hobby()
