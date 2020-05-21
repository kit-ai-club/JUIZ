class TestClass:  # クラス名は大文字から
    def __init__(self, x):  # initialize 初期化関数
        self.x = x  # クラス変数。クラスにxという値を保管しておく

    def f(self):  # クラス関数。クラスにfという関数を保管しておく
        print(self.x)


testClass = TestClass("x1")
# インスタンス（実体）の作成。クラスはただの概念。
# 「文字列()」という表記を使っていれば、クラスか関数のどちらか。

testClass.f()  # クラス関数を呼び出す(call)
testClass.x = "x2"  # クラス変数にアクセス
testClass.f()

# ちなみに、これでも同じ意味になる
TestClass("x3").f()


class Parent:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def f(self):
        print(self.x)
        print(self.y)


class Child1(Parent):  # クラスの「継承」をした
    pass  # pass = 「何もしない」


class Child2(Parent):
    def __init__(self, x, y, z):  # 初期化関数をちょっと書き換える
        super().__init__(x, y)
        # self.x = x  self.y = y  と書くのと等価な１行
        # super() = Parent()  親クラスのインスタンスを作成し、そこからすぐに初期化関数を呼び出している
        self.z = z  # 追加する

    def g(self):  # 追加する
        print(self.z)


child1 = Child1("x", "y")
child1.f()  # Parentの変数・関数が丸コピされている

child2 = Child2("x", "y", "z")
child2.f()  # 関数fが丸コピされている
child2.g()
