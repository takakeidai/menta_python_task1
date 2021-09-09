
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]


def search():
    word = input("鬼滅の登場人物の名前を入力してくだい >>>")
    if word in source:
        print("{}が見つかりした".format(word))
        with open('task1/character_source.csv', 'w') as f:
            f.write('\n'.join(source))          
    else:
        print("{}が見つかりません".format(word))   # ここで1：「入力したキーワードで、キャラクターリスト(source)を検索して、存在すれば存在する旨を、存在しなければ存在しない旨をPrint文で表示してみましょう」
        source.append(word)                     #　ここで２：「１に追加して結果が存在しなかった場合に、キャラクターリスト(source)に追加できるようにしてみましょう」
        
        with open('task1/character_source.csv', 'w') as f:       #　ここで３と４：「２に追加してキャラクターリスト(source)をCSVから読み込んで登録できるようにしてみましょう」
            f.write('\n'.join(source))                           # 「３に追加してキャラクターリスト(source)をCSVに書き込めるようにしてみましょう」

    



if __name__ == "__main__":
    search()



