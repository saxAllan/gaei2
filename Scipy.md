# Sci.pyの使い方

## 注意

- `scipy.py`という名前のファイルが存在するとエラーを起こすので、作成しないようにしてください。

- `scipy`のインストールが必要です。(下のは冗長かも)
```
python -m pip install --user numpy scipy matplotlib ipython jupyter pandas sympy nose
```

## 呼び出し方

実行するファイルは`pathfinding.py`です。  
~~~Python
import Sci
s = Sci.SciSearch([50, 50, 50], [0, 0, 0], [3, 2, 1], [[1, 0, 1], [2, 2, 1], [5, 1, 0], [7, 4, 0]], "fileName")
print(s.search())
~~~
- 1行目:`Sci.py`をimportします
- 2行目:`__init__()`が呼ばれ、探索に必要な情報を生成します
- 3行目:`search()`でScipyを用いた最短経路探索を行います

## 2行目の引数
~~~Python
変数 = Sci.SciSearch(サイズ,始点,終点,障害物,モード)
~~~
- 第1引数:リスト`[x方向の幅,y方向の幅,z方向の幅]`
- 第2引数:リスト`[始点のx座標,始点のy座標,始点のz座標]`
- 第3引数:リスト`[終点のx座標,終点のy座標,終点のz座標]`
- ~~第4引数:座標のリスト`[x,y,z]`を2点セットで格納したリスト`[点1,点2]`を有限個格納したリスト`[障害物1,障害物2,...,障害物n]`~~
    - ~~`[点1,点2]`:ある１つの障害物が存在する範囲の、一番座標が小さい点の座標と、一番大きい点の座標のセットです（直方体にしか対応できません）~~

    **7/9更新**
- 第4引数:x,y座標とそれに**対応した高さ**のリスト`[x,y,h]`を有限個格納したリスト`[障害物1,障害物2,...,障害物n]`
- 第5引数:~~生成モード~~ 障害物ファイル名（**7/11更新**）

    この名前が入出力用一時データファイルの名前に反映されます

    - ~~1:ファイル読み込みを行わず、その場で生成します（試行時はこのモードで行ってください）~~
    - ~~2:ファイル読み込みを行わず、その場で生成し、その結果をファイル出力します~~
    - ~~3:ファイルを読み込みます~~

        ~~**7/9更新**~~
    - ~~1:ファイル読み込みを行わず、その場で生成し、その結果をファイル出力します~~
    - ~~2:ファイルを読み込みます~~
    

## 更新情報
- 7/3 Ver.1 : 疎行列導入・関数化など
- 7/9 Ver.2 : 障害物設定の改良（内部：スライスの利用、入力：単純化）・ファイル入出力の改良（`io.savemat,io.loadmat`の導入）
- 7/11 Ver.3 : 障害物反映済のものをファイルに入出力 など

    