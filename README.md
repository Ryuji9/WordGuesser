# WordGuesser

チャットAIを利用した単語当てゲーム<br>
システム開発が計画通りに進まない場合は、開発が進んでいる人が滞っている人の手助けをする、システムが成り立つ必要最低限の機能は残したうえで一部の機能を削る、計画通り進まなくても期限に間に合うよう余裕を持った計画を立てるといった対応をとる。<br>
本システムの開発人数は4人で行う。開発の競合をできるだけ起こさないように4人全員がそれぞれの処理に干渉のないように開発内容を決めている。具体的には指定されたジャンルの中から単語を一つ生成するシステム・人工知能との対話システム・解答した単語との類似度を測るシステム・UIシステムの4つである。 <br>

・ジャンルの中から単語を一つ生成するシステム<br>
・人工知能との対話システム<br>
・解答した単語との類似度を測るシステム<br>
・UIシステム<br>

※類似度計測のファイルについて<br>
類似度の出現率から確率密度関数を別途作成し（rand.py）、0から類似度までを積分することで百分率表示を行っている。
実行するファイルは「correct.py」のみでよい。
ただし実行するには「gensim」というライブラリのインストール，類似度の辞書となる.binファイル，確率密度関数のcsvファイルが必要である．

>pip install gensim

でライブラリはインストール可能である．
.binについては以下のURLよりダウンロードし，実行ファイルと同じディレクトリに入れる必要がある．
.csvファイルも同様である。

類似度辞書のダウンロードリンク（2023/12/20迄）
https://38.gigafile.nu/1220-l4833d668006b7a7f9fd2c67fbf535633
(削除コード：f114)
