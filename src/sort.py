import random
import copy

"""
## 参考サイト
[ソートアルゴリズム - qiita ](https://qiita.com/omu58n/items/7160aa9ab8366d2256fd)

## ソートの三大要素

- 交換
- 選択
- 挿入

## 代表的なソートアルゴリズム

- バブルソート
- 挿入ソート
- 選択ソート
- シェルソート　未
- クイックソート　未
- ヒープソート　未
- マージソート　未
- 基数ソート　未
- 分布数え上げソート　未
"""

def Bubble(N):
    for i in range(len(N)-1, 0, -1):
        for j in range(i):
            if N[j] < N[j + 1]: # disccend
            # if N[j] > N[j + 1]: # accend
                N[j], N[j + 1] = N[j + 1], N[j]

def Insertion(N):
    """
    insetion sort (挿入ソート)
    若い要素番号の要素から順番に見ていく．
    jが非負かつj-1番目の要素がj番目の要素より大きかったら，
    ひたすらにに値をスワップして，jをデクリメントする．
    """
    for i in range(1, len(N)):
        j = i
        # while j > 0 and N[j - 1] < N[j]: # disccend
        while j > 0 and N[j - 1] > N[j]: # accend
            N[j - 1], N[j] = N[j], N[j - 1]
            j -= 1

def Selection(N):
    """
    selection sort (選択ソート)
    要素を取り出して，最小値 (or 最小値) の要素のインデックスを
    見つけて，最小値と現在の要素を交換する

    min_idxは昇順のときは最小値の要素番号．降順のときは最大値のそれ
    """
    for i in range(len(N) - 1):
        min_idx = i
        for j in range(i + 1, len(N)):
            if N[j] > N[min_idx]: # disccend
            # if N[j] < N[min_idx]: # accend
                min_idx = j
        N[min_idx], N[i] = N[i], N[min_idx]

def Shell(N):
    pass
def Quick(N):
    pass
def Heap(N):
    pass
def Mearge(N):
    pass
def Kisuu(N):
    pass
def Bunpukazoeage(N):
    pass

if __name__ == '__main__':
    a = [2, 4, 1, 5, 3]
    # a = random.sample(list(range(10)), k=10)
    b = copy.deepcopy(a) # python は参照渡し

    # Bubble(b)
    # Insertion(b)
    Selection(b)

    # Shell(b)
    # Quick(b)
    # Heap(b)
    # Mearge(b)
    # Kisuu(b)

    print(f"before sort: {a}")
    print(f"after sort:  {b}")