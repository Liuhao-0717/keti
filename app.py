#如果在st后面加上sidebar的话，输入栏会在页面左侧运行
#%%writefile app.py
from re import A
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

genre = st.sidebar.radio(
     "言語を選んでください",
     ('日本語', '中国語', '英語'))
if genre == '日本語':
     st.title('Streamlit課題')
     st.header("都市を紹介")

     st.write('リュウコウ、21A3810')
     st.markdown("[私のGithub](https://github.com/Liuhao-0717)")
     latest_iteration = st.empty()  #进度条
     bar = st.progress(0)

     for i in range(100):
      latest_iteration.text(f'{i+1}%')
      bar.progress(i+1)
      time.sleep(0.01)
     
     col1, col2, col3 = st.columns(3)
     with col2:
      st.header("東京都")
      st.image("dongjing.webp")
      st.markdown("[東京都を紹介](https://ja.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E9%83%BD)")

     with col1:
      st.header("ハルビン")
      st.image("haerbin.webp")
      st.markdown("[ハルビンを紹介](https://ja.wikipedia.org/wiki/%E3%83%8F%E3%83%AB%E3%83%93%E3%83%B3%E5%B8%82)")

     
     with col3:
      st.header("ジャカルタ") 
      st.image("yajiada.webp")
      st.markdown("[ジャカルタを紹介](https://ja.wikipedia.org/wiki/%E3%82%B8%E3%83%A3%E3%82%AB%E3%83%AB%E3%82%BF)")
     option = st.selectbox(
         '趣味がある都市は?',
         ('趣味がある都市は?','ハルビン', '東京都', 'ジャカルタ'))
     if option  =='ハルビン':
       option1 = st.selectbox(
         '了解したいこと',
         ('了解したいこと','お祭り','料理','風景'))
       if option1 =='お祭り':
         st.header("ハルビン国際氷雪祭り")

         st.write('世界三大雪まつりの一つに数えられる祭りであり、イベント中はハルビン市内至るところに氷の彫刻が並べられる。主な会場は太陽島公園、兆麟公園、そして氷雪大世界の市内3ヶ所である。ハルビン市の各地の公園を中心に氷彫刻や氷の建造物が展示され色とりどりの蛍光灯やLEDでライトアップされ、ハルビン市内の兆麒公園では国際的な氷彫刻大会も開催される。また、松花河の河川敷では高さ40メートル程の塔を中心に大規模な建造物が展示される。氷は松花河より切り出した天然の氷を使用する。')

         video_file = open('haerbin123.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[bilibili-25号底片DPC](https://www.bilibili.com/video/BV1nt411s7X2/?spm_id_from=333.788.recommend_more_video.2)")


         st.header("春節")

         st.write('春節とは元旦、正月元旦とも呼ばれ、中国、中国地方、世界各地の漢民族社会で祝われる伝統的な正月である。 明朝以降、中国の正月は一般的に正月15日の元宵節が終わるまで正式には終わらないし、場所によっては正月が全部終わるまで正月を祝うところもある。')


         video_file = open('chunjie.mp4', 'rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[bilibili-D伊L](https://www.bilibili.com/video/BV1jf4y1F7yY/?spm_id_from=333.788.recommend_more_video.0)")
       elif option1=='料理':
         st.header('焼き冷麺')
         st.write('焼き冷麺は1999年前後、中国黒龍江省密山市のある中学校の前の屋台が発祥とされています。冷麺は元々朝鮮族の伝統的な食べ物で、中国の朝鮮族はほとんど東北で暮らしていますので、「焼冷麺」の屋台には「東北焼冷麺」という文字がよく書かれています。当初は冷麺の揚げもの、炭火焼、鉄板焼の3種類がありましたが、今まで続いてきたのは鉄板焼しかないそうです。')
         st.image("kaolengmian.webp")
         st.header('サンザシ飴')
         st.write('サンザシ飴とは、中国北部の北京・天津周辺が発祥の冬のお菓子です。串に刺したサンザシに飴がけをしたものです。糖葫芦は冬になると屋台や路上、デパートの入口など至るところで売られます。「サンザシ飴」や「冰糖葫芦(ビンタンフールー)」とも呼ばれ、見た目も味も日本のりんご飴と似ています。')
         st.image("tanghulu.jpeg")
         st.header('鍋包肉')
         st.write('鍋包肉は黒龍江省ハルビン生まれの料理で、1907年創業で今日も営業している老舗レストラン「老厨家」の初代調理人の鄭興文が、当時この地にいたロシア人向けに創案した一品です。')
         st.image("guobaorou.webp")
       elif option1==('風景') :
         st.header('中央大街')
         st.write('ハルビンを代表する歴史的な大通りで、南北の直線の通りで全長1450m・幅21.34m（内、車道の幅は10.8m）。南端は経緯街（十字街）、北端は松花江防洪記念塔。')
         st.write('ロシア統治時代の建築物が数多く残され、「東方のパリ」とも称される西洋風の街並みが一直線に北の松花江に向かう。道をはさみ、欧州風建築物が建ち並び、その数は71棟。ほかに、ルネサンス式、バロック式、折衷式など中国でも珍しい多種多様な市指定建築物が13棟、保護建築は36棟ある。現在の花崗岩で敷き詰められた道は1924年に建設されたものである。その後も改築が重ねられ、現在は中心通りは歩行者天国となり、その後の中国の都市の通りの手本となった。')
         st.image('zhongyangdajie.webp')
         st.header('雪郷')
         st.write('雪郷は双峰林場と呼ばれている。黒龍江省牡丹江市の、海林市大海林林業局双峰林場に位置し、面積が500ヘクタール(1ヘクタール＝1万平方メートル)あり、標高は約1200メートル以上ある。雪が頻繁に降り、降雪期間も長いため、「天無三日晴（冬になると、晴れの日が三日間続くことがない）の説」がある。夏は降雨が多い、冬は降雪が多い。積雪期間が７ヶ月間あり(毎年10月ー翌年5月)、雪が果てしなく続き、年平均積雪深が2メートルもあり、雪量は中国一と言える。質が良くて粘性率が高いので、「中国の雪郷」と称されている。白雪、赤の日、雪松、雲があり、美しくて神聖な雪郷の画面を構築している。')
         st.image('xuexiang.webp')
         st.header('ボルガ荘園')
         st.write('ボルガ荘園はハルビン郊外の芦河畔にあり、面積は60万平方メートル以上、ハルビンの歴史、ロシア文化をテーマとして、国家AAAA級文化観光景勝地、ロシアと中国の文化交流基地、ロシア芸術家協会創造基地、モスクワ大学国際交流センターがあります。荘園は「長期的な文化、価値のある味」という経営理念を提唱し、復元された聖ニコラス教会と川辺のレストランは昔のハルビンの人々の思い出を伝え、ペトロフ芸術宮殿とプーシキン展示館は文化芸術交流のプラットフォームを提供します。')
         st.image('fuerjia.jpg')
     elif option == '東京都':
       option2 = st.selectbox(
           '了解したいこと',
           ('了解したいこと','お祭り','料理','風景'))
       if option2 =='お祭り':
         st.header("花火大会")
         st.write('7～8月に行なわれることの多い花火大会は夏の風物詩です。趣向を凝らした花火を楽しみにしている方も多いでしょう。花火は無邪気に見物するだけでも良いのですが、より楽しみたいなら花火に関して知識を深めておくことをおすすめします。花火大会の歴史や花火の種類などを知れば花火の表面的な美しさの裏にある伝統的な側面に気付くことができるでしょう。')
         st.write('日本に花火が伝わったのは江戸時代です。イギリス王の使者が徳川家康に鉄砲や望遠鏡とともに花火を献上しました。当時の花火は火の粉を吹きだすだけの簡素なものでしたが、興味を持った徳川家が改良に乗り出します。ねずみ花火などの玩具花火が開発されて、庶民たちを中心に人気となりました。')


         video_file = open('huahuodahui.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[bilibili-烟花狂人](https://www.bilibili.com/video/BV1sJ411K7cA/?spm_id_from=333.788.recommend_more_video.-1)")



         st.header("深川祭")
         st.write('深川祭は東京都江東区の富岡八幡宮の祭礼で、毎年8月15日を中心に行われる。神田祭、山王祭と並んで江戸三大祭の1つに数えられ約370年の歴史を誇る。')
         st.write('例大祭は毎年8月15日前後に行われ、3年に1度八幡宮の御鳳輦が渡御を行う年は本祭りと呼ばれる。宮入り・宮出しで各町の氏子が各々「わっしょい!」の掛け声と共に町神輿を担いで繰り出し、連合渡御する様は壮観である。その人気は江戸期に永代橋に多数の人が押し入ったことにより永代橋を崩落させたほどである（文化4年（1807年）の永代橋崩落事故）。暑さ避けに水を掛けることから別名「水掛け祭」とも呼ばれ、担ぎ手に水をかける「水掛け」であれば誰でも参加ができる。江戸幕府の命により祭りが行われたことが起源ということもあり、江戸幕府や江戸城跡の皇居にお住まいの天皇陛下に関連のある年には皇居前まで神輿を担ぐこともある。')
         video_file = open('shenchuan.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[bilibili-koswo](https://www.bilibili.com/video/BV1Xx411t7hj?spm_id_from=333.337.search-card.all.click)")
       elif option2=='料理':
         st.header('江戸前天ぷら')
         st.write('東京湾であがる魚介類を中心に、卵を入れた衣にくぐらせ、ゴマ油でからっと揚げる黄金色の江戸前天ぷら。関西は塩派が多いですが、関東は大根おろしと甘辛いつゆでいただきます。天ぷらのルーツは約 400 年前、ポルトガルから鉄砲と共に日本にやってきた西洋式の揚げ物です。当時は屋台で串に刺して売られ、庶民に人気を博したそうです。京橋、築地、赤坂など都内各所で名店の江戸前天ぷらを楽しめます。職人さんが目の前で天ぷらを揚げてくれる「お座敷天ぷら」で、車海老や穴子、ハゼ、キスなど新鮮な魚介類を味わいたいですね。')
         st.image('tpl.webp')

         st.header('江戸前寿司')
         st.write('江戸前寿司は、東京湾で獲れた魚を主にネタに使った、握り寿司が中心の東京の郷土料理。1800 年代初頭に、江戸の人々の間で素早く食べられる、当時のファストフードとして人気になりました。どのネタを選んだらいいか迷ったら、寿司屋の格が決まるといわれるマグロをぜひ。東京湾で獲れるネタの車海老や穴子、シャコ、タコ、ハマグリ、赤貝なども旬に合わせていただきましょう。また、生魚だけでなく江戸の寿司職人の「ひと手間」も江戸前寿司の特徴のひとつ。煮穴子、炙りサバ、〆もののコハダ、焼きものの玉子などがおすすめです。シャリとネタの絶妙な温度が大切な握り寿司は、提供されたら直ぐにいただくのが美味しく食べるポイントです。')
         st.image('shousi.webp')

         st.header('うな丼')
         st.write('古くからうなぎ料理はありましたが、庶民にも親しまれるようになったのは江戸時代から。関西と関東のうなぎには、その調理法に違いがあります。関東はさばき方が背中からで、頭は落とします。そして焼いてから蒸すので、ふっくらと香ばしいのが特長。あっさりとした甘くないタレをつけて焼き上げます。天然鰻を味わえる老舗の名店、天然と養殖の食べ比べやリーズナブルなランチを提供する店などニーズに合わせて選べます。土用の丑の日でなくても、ビタミン A や DHA など栄養満点のうなぎを食べて、東京観光のエネルギーを充電しましょう。')
         st.image('yu.webp')
       elif option2=='風景':
         st.header('東京ディズニーランド')
         st.write('東京ディズニーランドは、千葉県浦安市にある東京ディズニーリゾート内のテーマパーク。 アメリカ以外で建設された最初のディズニー・パークで、1983年4月15日にオープンした。オリエンタルランドが所有し、ウォルト・ディズニー・カンパニーからテーマのライセンスを受けている。 ')
         st.image('dishini.jpg')

         st.header('東京タワー')
         st.write('東京タワーは、日本の東京都港区芝公園にある総合電波塔である。正式名称は日本電波塔（にほんでんぱとう）。創設者は前田久吉。1958年12月23日竣工。東京都のシンボル、観光名所である。')
         st.write('高さは333メートルと広報されており、海抜では351メートル。塔脚の中心を基準とした塔脚の間隔は88.0メートル。総工費約30億円、1年半（197万4,015時間/543日間）と延べ21万9,335人の人員を要して完成した。地上125メートル（海抜約150メートル）と223.55メートル（海抜約250メートル）に展望台を有したトラス構造の電波塔である。')
         st.image('ta.jpg')


         st.header('浅草')
         st.write('浅草には昔の東京の雰囲気が残っており、歴史ある浅草寺の近くの仲見世通り沿いに、伝統的な手工芸品や食べものの屋台があります。19 世紀半ばに建設された花やしき遊園地にはスリルあふれる乗り物アトラクションとカフェがあり、川沿いの区立隅田公園ではフェスティバルや花火大会が定期的に開催されます。近隣にはカジュアルな居酒屋が点在し、串に刺して焼いた肉とビールを提供する焼鳥屋もあります。')

         st.image('qiancao.jpg')
     elif option == 'ジャカルタ':
       option3 = st.selectbox(
           '了解したいこと',
           ('了解したいこと','お祭り','料理','風景'))
       if option3 =='お祭り':
         st.header("イド・アルフィトル")

         st.write('イスラム教の主な祭りの一つ。 イード・アル＝アドハーとともに、イスラム教の二大祭りの一つである。 アラビア語「De Fittur」の翻訳。 ペルシャ語ではRuzi（Meatz）と呼ばれている。 成人のイスラム教徒は、男女を問わず、イスラム暦の毎年9月の1ヶ月間（通称：ラマダン）断食を行い、毎日夜明け前から日没まで飲食や性行為、あらゆる卑猥な行為を断ち、自らの体を調べ、罪を清めるために行っています。 新月を見たら断食、新月を見たら断食」というムハンマドの口癖により、ラマダンは9月上旬に始まり、新月を見たら10月上旬に終わります。')

         video_file = open('yinni.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[Youtube-アレキ紹介](https://www.youtube.com/watch?v=pLPJezrlfMw)")

         st.header("春節")

         st.write('インドネシアで開かれた、春節（旧正月）の終わりを祝う華人の伝統行事「チャップ・ゴ・メ」。華人移民であるペラナカンの人々を中心に、民族協調の象徴として根づく祭りの様子を太田泰彦編集委員が現地からリポートする。')

         video_file = open('yinni2.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("サイトのリンク先:")
         st.markdown("[Youtube-日本経済新聞](https://www.youtube.com/watch?v=HiXZ8hh6h5E)")
       elif option3=='料理':
         st.header('サラ')
         st.write('サテは串に刺した肉を炭火で焼いた、中近東料理のケバブの影響を受けた料理である。サテを食べる時のソースには、刻みトウガラシ、キダチトウガラシ、シャロット、トマト、コショウなどを混ぜたピーナッツソースとケチャップマニスの2種類がある。')
         st.write('サテは肉の種類によって命名され、鶏肉のサテアヤム（sate ayam）、鶏挽肉のサテリリッ（sate lilit）、ヤギ肉のサテカンビン（sate kambing）、牛肉のサテサピ（sate sapi）、豚肉のサテバビ（sate babi）などがある。サテはご飯かロントンやクトゥパッと一緒に食べる。')
         st.image('sara.png')

         st.header('ルンダン')
         st.write('ルンダン、もしくはレンダンは、牛肉などの塊肉をココナッツミルクと香辛料で長時間煮込んだ肉料理である。2017年にCNNによって世界一美味しい料理に選ばれた。 インドネシアの西スマトラ州の郷土料理であり、インドネシアを代表する料理として挙げられることが多い。')
         st.image('rrd.jpg')

         st.header('ナシチャンプル')
         st.write('ナシチャンプル(nasi campur)は、インドネシアおよびその周辺地域のマレーシア、シンガポールなどで見られる、ご飯を盛った皿にお好みで選択したおかずを乗せる形式の食事、転じてその料理名である。インドネシア語やマレー語でnasiは「ご飯」、campurは「混合、混ぜる（ごちゃ混ぜにする）」の意味であるが、韓国のビビンバ（「混ぜご飯」の意）のように必ずしも混ぜ合わせて食べるということではなく、「複数のおかずを寄せ集めて乗せたご飯」の意味が強い。')
         st.image('fan.jpg')
       elif option3 == '風景':
         st.header('タマンミニ・インドネシア・インダー')
         st.write('1万8,110もの大小の島と、約３００もの民族により構成されるというインドネシア。そんなインドネシアの各民族の生活を覗くことができ、インドネシア中を一気に観光したような気分になってしまうテーマパークがジャカルタ中心部から車で約1時間程のところにあります。')
         st.write('バリ館、ジャワ館など各島特有の建造物が立ち並び広い園内にはコモドドラゴン博物館や、水族館もあり、大人も子供も丸一日楽しめるスポットの一つです。')
         st.image('pari.jpg')

         st.header('ジャカルタ大聖堂')
         st.write('はたまた、こちらはキリスト教の大聖堂。なんとイスティクラル・モスクの目の前にあります！')
         st.write('中に入るとそこは別世界。インドネシアはほぼ9割がイスラム教徒の方が占めているようですが、キリスト教の方もいます。賛美歌の中で一心に祈りを捧げる方々に感動しますよ。')
         st.image('jiaotang.jpg')

         st.header('プロウスリブ')
         st.write('ジャカルタから最も近いビーチリゾートです。プロウスリブとはインドネシア語で「千の島」という意味を表します。')
         st.write('実際には数百の島があり、そのうち10島ほどが有人の島となっています。ジャカルタの北部「アンチョール港」からボートで30分〜2時間でジャカルタの海岸からは想像できないほど美しい海が出迎えてくれます！')
         st.write('のんびりと読書を楽しむもよし、シュノーケリングで魚達とたわむれるもよし、オプションでサンセットクルーズもつけられます。ボートが揺れるので、酔いやすい方は酔い止めを持って行って！')
         st.image('dao.jpg')
         

##############################################################################
elif genre == '中国語':
     st.title('Streamlit课题')
     st.header("城市介绍")

     st.write('リュウコウ、21A3810')
     st.markdown("[我的Github](https://github.com/Liuhao-0717)")
     latest_iteration = st.empty()  #进度条
     bar = st.progress(0)

     for i in range(100):
      latest_iteration.text(f'{i+1}%')
      bar.progress(i+1)
      time.sleep(0.01)
     
     col1, col2, col3 = st.columns(3)
     with col2:
      st.header("东京都")
      st.image("dongjing.webp")
      st.markdown("[东京都介绍](https://zh.wikipedia.org/wiki/%E6%9D%B1%E4%BA%AC%E9%83%BD)")

     with col1:
      st.header("哈尔滨")
      st.image("haerbin.webp")
      st.markdown("[哈尔滨介绍](https://zh.wikipedia.org/wiki/%E5%93%88%E5%B0%94%E6%BB%A8%E5%B8%82)")

     
     with col3:
      st.header("雅加达") 
      st.image("yajiada.webp")
      st.markdown("[雅加达介绍](https://zh.wikipedia.org/wiki/%E9%9B%85%E5%8A%A0%E8%BE%BE)")
     option = st.selectbox(
         '你想了解哪个城市呢?',
         ('你想了解哪个城市呢?','哈尔滨', '东京都', '雅加达'))
     if option  =='哈尔滨':
       option1 = st.selectbox(
         '想了解的事',
         ('想了解的事','节日','美食','风景'))
       if option1 =='节日':
         st.header("哈尔滨国际冰雪节")

         st.write('该节日是世界三大雪节之一，活动期间，哈尔滨各地都会布置冰雕。 三个主要场馆是太阳岛公园、兆麟公园和冰雪大世界。 冰雕和冰造物将在哈尔滨市各大公园里展示，并以五颜六色的荧光灯和LED灯进行照明，在哈尔滨市的肇庆公园还将举行国际冰雕比赛。 此外，一个以40米高的塔为中心的大型结构将在松花江畔展出。 这些冰块将由从松花江切割的天然冰块制成。')

         video_file = open('haerbin123.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[bilibili-25号底片DPC](https://www.bilibili.com/video/BV1nt411s7X2/?spm_id_from=333.788.recommend_more_video.2)")


         st.header("春节")

         st.write('春节，为以传统历法计算之华夏新年，即一年之岁首、年节，是中国与华人地区及世界各地汉族社会过的传统新年，又称新春、正旦、正月朔日；口头上亦称为过新年、过年、度岁、庆新春、贺新岁，属于汉族四大传统节日之首。从明代开始，华夏新年节庆一般要到正月十五日元宵节之后才正式结束活动，有些地方的新年庆祝活动甚至到整个正月完结为止。')


         video_file = open('chunjie.mp4', 'rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[bilibili-D伊L](https://www.bilibili.com/video/BV1jf4y1F7yY/?spm_id_from=333.788.recommend_more_video.0)")
       elif option1=='美食':
         st.header('烤冷面')
         st.write('烤冷面起源于1999年左右中国黑龙江省密山市某中学门口的一个摊位。 冷面原本是朝鲜族的传统食品，由于在中国的朝鲜族人大多居住在东北，所以 "烤冷面 "摊位上经常写着 "东北烤冷面 "的字样。 最初，有三种冷面：油炸、炭烤和铁板烧，但只有铁板烧一直延续到现在。')
         st.image("kaolengmian.webp")
         st.header('糖葫芦')
         st.write('糖葫芦是一种冬季小吃，起源于中国北方，在北京和天津附近。 它是由山楂串成的，上面覆盖着糖果。 在冬季，tanfur在街头摊位、街道和百货公司的入口处出售。 也被称为 "山楂糖 "或 "冰糖葫芦"，其外观和味道与日本苹果糖相似。')
         st.image("tanghulu.jpeg")
         st.header('锅包肉')
         st.write('锅包肉是诞生于黑龙江省哈尔滨市的一道菜，是由1907年成立、至今仍在经营的 "老厨房 "餐厅的第一位厨师郑兴文为当时在当地的俄罗斯人发明的。')
         st.image("guobaorou.webp")
       elif option1==('风景') :
         st.header('中央大街')
         st.write('它是哈尔滨有代表性的历史大道，是一条南北走向的直街，总长1450米，宽21.34米（其中车行道宽10.8米）。 其南端是经纬街（十字街），北端是松花江抗洪纪念碑。')
         st.write('一些俄罗斯占领时期的建筑仍然存在，因为有着西式的街道，所以也被称为 "东方小巴黎"，以一条直线向北走向松花江。 马路对面是71座欧式建筑。 此外，还有13个城市指定的建筑和36个保护建筑，具有各种文艺复兴、巴洛克和折衷主义风格，这在中国是很罕见的。 现在的花岗岩铺设的道路建于1924年。 此后被重建，中心街道现在是步行街，为中国后来的城市街道树立了一个榜样。')
         st.image('zhongyangdajie.webp')
         st.header('雪乡')
         st.write('雪乡也被称为双峰林场。 它位于黑龙江省牡丹江市海林市大海林局双峰林场，面积为500公顷（1公顷=10 000平方米），海拔1200多米。 这里经常下雪，而且降雪期非常长，有一种说法是三天一晴（在冬天，晴天不会持续三天）。 夏季降雨频繁，冬季有降雪。 这里有7个月的降雪期（每年10月至次年5月），雪水绵绵不绝，年平均雪深2米，是中国最好的降雪区。 由于其质量好、粘度高，被称为 "中国的雪乡"。 有白雪，有红日，有雪松，有白云，构建了一个美丽而神圣的雪乡画面。')
         st.image('xuexiang.webp')
         st.header('伏尔加庄园')
         st.write('伏尔加庄园位于哈尔滨市郊的阿什河畔，占地面积60多万平方米，以哈尔滨历史和俄罗斯文化为主题，是国家AAAA级文化旅游景区、中俄文化交流基地、俄罗斯艺术家协会创作基地和莫斯科大学国际交流中心。 庄园倡导 "长久的文化，有价值的品位 "的经营理念，修复后的圣尼古拉教堂和江边餐厅传递着哈尔滨人对过去的记忆，而彼得罗夫艺术宫和普希金展览馆则为文化艺术交流提供了平台。')
         st.image('fuerjia.jpg')
     elif option == '东京都':
       option2 = st.selectbox(
           '想了解的事',
           ('想了解的事','节日','美食','风景'))
       if option2 =='节日':
         st.header("烟花大会")
         st.write('通常在7月和8月举行的烟花表演是夏季的一个传统。 许多人期待着精心制作的烟花表演。 虽然只是天真无邪地观看烟花是可以的，但如果你想更多地享受烟花，我们建议你多了解一下烟花。 了解烟花表演的历史和不同类型的烟花将帮助你认识到烟花表面之美的背后的传统方面。')
         st.write('烟花是在江户时代被引入日本的。 英国国王的使者向德川家康赠送了烟花以及枪支和望远镜。 当时的烟花很简单，只是吹出火花，但德川家族对其产生了兴趣并开始改进。 诸如Nezumi Hanabi（老鼠烟花）等玩具烟花被开发出来，并开始流行，特别是在普通人中间。')


         video_file = open('huahuodahui.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[bilibili-烟花狂人](https://www.bilibili.com/video/BV1sJ411K7cA/?spm_id_from=333.788.recommend_more_video.-1)")



         st.header("深川祭")
         st.write('深川祭是东京江东区富冈八幡宫的一个节日，每年8月15日前后举行。 它与神田节和三野节一起，是江户的三大节日之一，拥有约370年的历史。')
         st.write('每年8月15日前后举行，八幡宫御驾亲征的年份被称为主祭，每三年一次。 每个城镇的神龛教友都会把自己的神龛抬到神龛，并在 "wasshoi！"的喊声中把神龛抬出来。 游行队伍是一个壮观的景象。 这个节日的受欢迎程度很高，以至于在江户时代，当大量的人挤到桥上时，永代桥倒塌了（1807年永代桥倒塌）。 这个节日也被称为 "泼水节"，因为为了避免炎热，人们会把水洒在抬轿人身上，只要向抬轿人洒水，任何人都可以参加。 这个节日起源于江户幕府的一项命令，在与江户幕府或居住在江户城废墟上的皇宫的天皇有关的年份，神轿有时会被抬到皇宫前。')
         video_file = open('shenchuan.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[bilibili-koswo](https://www.bilibili.com/video/BV1Xx411t7hj?spm_id_from=333.337.search-card.all.click)")
       elif option2=='美食':
         st.header('江戸前天妇罗')
         st.write('金色的江户前天妇罗，主要是来自东京湾的海鲜，蘸上鸡蛋面糊，用芝麻油炸制。 在关西地区，大多数人喜欢吃盐，而在关东地区，天妇罗是与磨碎的萝卜和甜辣的蘸酱一起食用。 天妇罗起源于西式油炸，大约400年前从葡萄牙随枪传入日本。 当时，它在雅泰摊位上被串起来出售，受到普通民众的欢迎。 你可以在东京的京桥、筑地、赤坂和其他地方的著名餐厅享用江户前天妇罗。 你可以在 "「お座敷天ぷら」 "品尝新鲜的海鲜，如虎虾、海鳗、虾虎鱼和吻，工匠们在你面前炸天妇罗。')
         st.image('tpl.webp')

         st.header('江戸前寿司')
         st.write('江户前寿司是东京的一道地方菜，主要是用东京湾捕获的鱼制作的手握寿司，在19世纪初作为当时的快餐食品，在江户（今东京）人民中流行。 如果你对选择哪种鱼有疑问，不妨试试金枪鱼，据说它决定了一家寿司店的特色。 还可以尝试在东京湾捕获的物品，如虎虾、海鳗、沙子、章鱼、蛤蜊和红蛤蜊，这取决于它们的季节。 除了生鱼之外，江户前寿司的另一个特点是江户寿司厨师所做的 "额外修饰"。 推荐的菜品包括水煮海鳗、烤鲭鱼、醋味可卡达和烤蛋。 享受手握寿司的关键是一上桌就吃，因为饭和鱼的完美温度很重要。')
         st.image('shousi.webp')

         st.header('鳗鱼饭')
         st.write('鳗鱼菜肴自古以来就存在，但直到江户时期才开始受到普通民众的欢迎。 关西和关东地区的鳗鱼烹饪方法存在差异。 在关东地区，鳗鱼被从背部切开，头部被去除。 它们被烧烤，然后被蒸熟，使它们变得松软和芳香。 鳗鱼是用淡而不甜的酱汁烤制的。 你可以根据自己的需要选择，有可以品尝天然鳗鱼的老牌知名餐厅，有可以比较天然和养殖鳗鱼的餐厅，还有提供合理午餐的餐厅。 即使不是属牛的日子，你也可以通过吃鳗鱼来为东京的观光活动补充能量，因为鳗鱼富含维生素A和DHA等营养成分。')
         st.image('yu.webp')
       elif option2=='风景':
         st.header('东京迪士尼乐园')
         st.write('东京迪斯尼乐园是位于日本千叶县浦安市的东京迪斯尼度假村内的一个主题公园。它是第一个在美国之外建造的迪斯尼公园，于1983年4月15日开放。 它由东方乐园拥有，并获得了华特迪士尼公司的主题许可。 ')
         st.image('dishini.jpg')

         st.header('东京塔')
         st.write('东京塔是位于日本东京港区芝公园的一座普通无线电塔。 它的正式名称是日本无线电塔。 它的创始人是前田久吉；建筑于1958年12月23日完成。 它是东京的一个象征，也是一个旅游景点。')
         st.write('宣传的高度是333米，海拔351米。 根据塔腿的中心，塔腿之间的距离为88.0米。 该项目总成本约为30亿日元，历时一年半（1,974,015小时/543天），共花费219,335人。 无线电塔是一个桁架结构，在地面以上125米（海平面以上150米）和223.55米（海平面以上250米）设有观察平台。')
         st.image('ta.jpg')


         st.header('浅草')
         st.write('浅草保留了旧东京的气氛，在历史悠久的浅草寺附近的中美大道上有传统的手工艺品和食品摊位；建于19世纪中期的花屋敷游乐园有惊险的游乐设施和咖啡馆；沿河的隅田公园有节日和焰火表演。 沿河的隅田公园定期举行节庆活动和烟花表演。 附近遍布着休闲的居酒屋（日本风格的酒吧），以及提供烤肉串和啤酒的烤肉店。')

         st.image('qiancao.jpg')
     elif option == '雅加达':
       option3 = st.selectbox(
           '想了解的事',
           ('想了解的事','节日','美食','风景'))
       if option3 =='节日':
         st.header("开斋节")

         st.write('伊斯兰教的主要节日之一。它与宰牲节一起，是伊斯兰教的两个主要节日之一。阿拉伯语 "De Fittur "的翻译。在波斯语中，它被称为Ruzi（Meatz）。成年穆斯林，无论男女，每年都要在伊斯兰教历的9月（俗称斋月）禁食，每天从黎明前到日落时分禁食、禁饮、禁性和禁一切不雅行为，以检查自己的身体，净化自己的罪孽。根据穆罕默德的口谕，"看到新月就斋戒，看到斋戒就斋戒"，斋月在九月初开始，十月初看到新月时结束。')

         video_file = open('yinni.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[Youtube-アレキ紹介](https://www.youtube.com/watch?v=pLPJezrlfMw)")

         st.header("春节")

         st.write('春节也是在印度尼西亚举行的庆祝中国新年结束的传统中国活动。 编辑太田泰彦从现场报道了这一节日，它作为民族合作的象征已经扎根，特别是在作为中国移民的土生华人中。')

         video_file = open('yinni2.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("视频链接:")
         st.markdown("[Youtube-日本経済新聞](https://www.youtube.com/watch?v=HiXZ8hh6h5E)")
       elif option3=='美食':
         st.header('沙嗲')
         st.write('沙嗲（印尼语：Sate，马来语：Satay），又名沙嗲串烧、沙嗲串，是一种东南亚的烤肉串，通常肉以酱汁先腌过再烤。沙嗲的食材可能是切片或切块的鸡肉、羊肉、牛肉、猪肉、鱼，其它肉类，或豆腐。沙嗲虽然经常使用竹签串肉，但比较正统的是以椰子树叶的梗串肉。沙嗲通常以木材或木炭烤，然后吃时可以再加上各种辛辣的沙嗲酱调味。')
         st.image('sara.png')

         st.header('仁当')
         st.write('仁当是一道将牛肉或其他大块肉放在椰奶和香料中长时间炖煮而成的肉菜；2017年被CNN评为世界上最好的菜肴。它是印度尼西亚西苏门答腊岛的一道地方菜，经常被列为印度尼西亚最具代表性的菜肴之一。')
         st.image('rrd.jpg')

         st.header('燕窝饭')
         st.write('燕窝饭是印度尼西亚及其周边地区（如马来西亚和新加坡）的一种膳食名称，或其变体，在那里，一盘米饭与您选择的配菜一起供应。 在印度尼西亚和马来语中，nasi的意思是 "米饭"，campur的意思是 "混合，混杂"，但它不一定是像韩国的bibimbap（意思是 "混合米饭"）那样 "米饭加几个配菜"。')
         st.image('fan.jpg')
       elif option3 == '风景':
         st.header('印度尼西亚缩影公园')
         st.write('印度尼西亚由18110个大小不一的岛屿和大约300个民族组成。 在这个主题公园里，你可以窥探到印度尼西亚各个民族的生活，并感觉到你仿佛一下子参观了整个印度尼西亚，该公园距离雅加达市中心约一小时的车程。')
         st.write('科莫多龙博物馆和水族馆位于一个大型公园内，公园内有每个岛屿特有的建筑，如巴厘岛馆和爪哇岛馆，使其成为成人和儿童都能享受一整天的景点之一。。')
         st.image('pari.jpg')

         st.header('雅加达大教堂')
         st.write('或者说这是个基督教大教堂。 就在Istiqlal清真寺的前面，这是多么壮观的景象啊!')
         st.write('一旦进去，就是一个不同的世界。 几乎90%的印度尼西亚人口似乎都是穆斯林，但也有基督徒。 你会被那些在赞美诗中一心一意祈祷的人们所感动。')
         st.image('jiaotang.jpg')

         st.header('Pulau Seribu')
         st.write('它是离雅加达最近的海滩度假村。 Prouslib在印度尼西亚的意思是 "千岛"。')
         st.write('事实上，这里有数百个岛屿，其中约有10个有人居住。 从雅加达北部的 "锚港 "乘船30分钟至2小时，迎接你的是雅加达海岸线上可以想象到的最美丽的大海!')
         st.write('享受悠闲的阅读，与鱼儿一起浮潜，或参加自选的日落巡航。 船上摇摇晃晃，如果你容易晕船请带好防晕药!')
         st.image('dao.jpg')

##############################################################################
elif genre == '英語':
     st.title('Streamlit Homework')
     st.header("Introducing Cities")

     st.write('リュウコウ、21A3810')
     st.markdown("[My Github](https://github.com/Liuhao-0717)")
     latest_iteration = st.empty()  #进度条
     bar = st.progress(0)

     for i in range(100):
      latest_iteration.text(f'{i+1}%')
      bar.progress(i+1)
      time.sleep(0.01)
     
     col1, col2, col3 = st.columns(3)
     with col2:
      st.header("Tokyo")
      st.image("dongjing.webp")
      st.markdown("[Introduction to Tokyo](https://en.wikipedia.org/wiki/Tokyo)")

     with col1:
      st.header("Haerbin")
      st.image("haerbin.webp")
      st.markdown("[Introduction to Haerbin](https://en.wikipedia.org/wiki/Harbin)")

     
     with col3:
      st.header("Jakarta") 
      st.image("yajiada.webp")
      st.markdown("[Introduction to Jakarta](https://en.wikipedia.org/wiki/Jakarta)")
     option = st.selectbox(
         'Which cities do you enjoy?',
         ('Which cities do you enjoy?','Haerbin', 'Tokyo', 'Jakarta'))
     if option  =='Haerbin':
       option1 = st.selectbox(
         'Things want to know',
         ('Things want to know','festival','Gourmet','Landscapes'))
       if option1 =='festival':
         st.header("Harbin International Ice and Snow Festival")

         st.write('The festival is one of the three major snow festivals in the world, and during the event, ice sculptures are laid out all over Harbin City. The three main venues for the festival are Sun Island Park, Zhaolin Park, and the Great Ice and Snow World. Ice sculptures and ice structures will be displayed in parks throughout Harbin City and lit up with colorful fluorescent and LED lights, and an international ice sculpting competition will be held in Harbin City is Zhaolin Park. An international ice sculpting competition will be held at the Zhaoqi Park in Harbin City, and a large-scale structure centering on a 40-meter-high tower will be exhibited on the banks of the Songhua River. The ice will be made from natural ice cut from the Songhua River.')

         video_file = open('haerbin123.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[bilibili-25号底片DPC](https://www.bilibili.com/video/BV1nt411s7X2/?spm_id_from=333.788.recommend_more_video.2)")


         st.header("Spring Festival")
         """
         ###### Spring Festival, also called New Year's Day , is the traditional New Year celebrated in China, the Chinese provinces, and Han Chinese communities around the world. Since the Ming Dynasty, the Chinese New Year generally does not officially end until after the Lantern Festival on the 15th day of the New Year, and in some places the New Year is celebrated until the entire New Year is over.
         """

         


         video_file = open('chunjie.mp4', 'rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[bilibili-D伊L](https://www.bilibili.com/video/BV1jf4y1F7yY/?spm_id_from=333.788.recommend_more_video.0)")
       elif option1=='Gourmet':
         st.header('KaoLengMian')
         st.write('It is believed that baked cold noodles originated from a stall in front of a certain middle school in Mianshan, Heilongjiang Province, China, around 1999. Cold noodles are originally a traditional food of the Korean people, and since most of the Korean people in China live in the Northeast, the words "Northeast grilled cold noodles" are often written on the "grilled cold noodles" stalls. In the beginning, there were three types of cold noodles: fried, charcoal-grilled, and teppan-yaki, but only teppan-yaki has continued to be served until now.')
         st.image("kaolengmian.webp")
         st.header('hawthorn candy')
         st.write('Hawthorn candy is a winter snack that originated in the Beijing and Tianjin areas of northern China. It is made of hawthorn skewered and covered with candy. In the winter, hawthorn candies are sold at street stalls, on the streets, and at the entrances to department stores. Also called "hawthorn candy" or "冰糖葫芦", it looks and tastes similar to Japanese apple candy.')
         st.image("tanghulu.jpeg")
         st.header('GuoBaoRou')
         st.write('GuoBaoRou is a dish born in Harbin, Heilongjiang Province, and was invented by Zheng Xingwen, the first cook at "The Old Kitchen," an old restaurant established in 1907 that is still in business today, for the Russians who were in the area at the time.')
         st.image("guobaorou.webp")
       elif option1==('Landscapes') :
         st.header('Central Avenue')
         st.write('It is a representative historical boulevard of Harbin, a straight north-south street with a total length of 1,450 m and a width of 21.34 m (of which the width of the roadway is 10.8 m). The southern end of the avenue is the Crossroads Street, and the northern end is the Song Hua Jiang Anti-Hong Monument.')
         st.write('A large number of buildings from the era of Russian colonial rule remain, and the Western-style streets, also known as the "Paris of the East," head north in a straight line to the Songhua River. Across the road, European-style buildings line the street, numbering 71 in all. In addition, there are 13 city-designated buildings of various styles, including Renaissance, Baroque, and eclectic, which are rare in China, and 36 protected buildings. The present granite paved road was built in 1924. The central avenue, which has undergone numerous renovations since then, is now a pedestrian zone and has served as a model for subsequent urban avenues in China.')
         st.image('zhongyangdajie.webp')
         st.header('Snow Village')
         st.write('Snow Village is called Shuangfeng Forestry Field. It is located in the Shuangfeng Forestry Area, Dahai Forestry Bureau, Hailin City, Peotanjiang City, Heilongjiang Province, with an area of 500 hectares (1 hectare = 10,000 square meters) and an altitude of over 1,200 meters. It snows frequently, and the snowfall period is so long that there is a theory that "Heaven is without three sunny days" (in winter, there are never three sunny days in a row). In summer, rainfall is frequent; in winter, snowfall is frequent. The average annual snow depth is 2 meters, which is the highest in China. It is called the "Snow Town of China" because of its high quality and high viscosity. With white snow, red sun, snow pines, and clouds, it has constructed a beautiful and sacred snow township screen.')
         st.image('xuexiang.webp')
         st.header('Volga Manor')
         """
         ###### Volga Manor is located on the banks of the Ashi River in the suburbs of Harbin, covering an area of more than 600,000 square meters, with Harbin's history and Russian culture as its theme, it is a national AAAA-class cultural tourism scenic spot, a base for cultural exchange between Russia and China, a creative base for Russian artists' association, and an international exchange center of Moscow University. The manor advocates the management concept of "long-term culture, valuable taste"; the restored St. Nicholas Church and riverside restaurant convey memories of the people of Harbin in the past; and the Petrov Art Palace and Pushkin Exhibition Hall provide a platform for cultural and artistic exchange.
         """
         st.image('fuerjia.jpg')
     elif option == 'Tokyo':
       option2 = st.selectbox(
           'Things want to know',
           ('Things want to know','festival','Gourmet','Landscapes'))
       if option2 =='festival':
         st.header("Fireworks Display")
         st.write('Fireworks displays, which are often held in July and August, are a summer tradition. Many people look forward to seeing the elaborate fireworks displays. While it is fine to just innocently watch the fireworks, we recommend that you learn more about fireworks if you want to enjoy them more. Knowing the history of fireworks displays and the different types of fireworks will help you realize the traditional aspects behind the superficial beauty of fireworks.')
         st.write('Fireworks were introduced to Japan during the Edo period. An envoy of the King of England presented fireworks to Tokugawa Ieyasu along with guns and telescopes. At the time, fireworks were simple, just spewing fire sparks, but the Tokugawa family became interested in them and started to improve them. Toy fireworks such as "Nezumi Hanabi" (mouse fireworks) were developed and became popular among the general public.')


         video_file = open('huahuodahui.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[bilibili-烟花狂人](https://www.bilibili.com/video/BV1sJ411K7cA/?spm_id_from=333.788.recommend_more_video.-1)")



         st.header("Fukagawa Festival")
         st.write('Fukagawa Matsuri is a festival of Tomioka Hachiman Shrine in Koto-ku, Tokyo, held annually around August 15. Along with the Kanda Festival and the Sanno Festival, it is one of the three major festivals in Edo, and boasts a history of approximately 370 years.')

         """
         ######The annual festival is held around August 15 every year, and the year when the Hachimangu shrine's palanquin is carried out is called the main festival. The shrine parishioners of each town carry their own portable shrines to the shrine and unload them, accompanied by the chants of "wasshoi! The procession is a spectacular sight. The popularity of the festival is so great that the Eitaibashi Bridge collapsed during the Edo period (the Eitaibashi Bridge collapsed in the 4th year of Bunka era (1807)) due to a large number of people crowding into the bridge. The festival is also called "mizukake-matsuri" (water sprinkling festival) because water is sprinkled to avoid the heat, and anyone can participate in the festival as long as they sprinkle water on the bearers. Because the festival originated from an order of the Edo shogunate, the portable shrine is sometimes carried to the front of the Imperial Palace in years when the festival is associated with the Edo shogunate or the Emperor of Japan, who resides in the Imperial Palace on the ruins of Edo Castle.
         """         
         video_file = open('shenchuan.mp4', 'rb')
         video_bytes = video_file.read()
         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[bilibili-koswo](https://www.bilibili.com/video/BV1Xx411t7hj?spm_id_from=333.337.search-card.all.click)")
       elif option2=='Gourmet':
         st.header('Edomae Tempura')
         st.write('Golden Edomae Tempura is made mainly from seafood caught in Tokyo Bay, dipped in egg batter, and deep-fried in sesame oil. While most Kansai people prefer salt, Kanto people eat tempura with grated daikon and sweet and spicy dipping sauce. Tempura has its roots in Western-style deep frying, which arrived in Japan about 400 years ago from Portugal along with guns. At that time, tempura was sold on skewers at yatai (food stalls) and became popular among the common people. You can enjoy Edomae tempura at famous restaurants in Kyobashi, Tsukiji, Akasaka, and other locations in Tokyo. You can enjoy fresh seafood such as tiger prawns, conger eels, gobies, and kisses at "Ozashiki Tempura," where artisans fry tempura right in front of you.')
         st.image('tpl.webp')

         st.header('Edomae-zushi')
         st.write('Edomae-zushi is a local cuisine of Tokyo, mainly consisting of nigirizushi made from fish caught in Tokyo Bay, and became popular in the early 1800s as a fast food of the time that could be eaten quickly by the people of Edo. If you are at a loss as to which fish to choose, try the tuna, which is said to determine the character of a sushi restaurant. Also try the items caught in Tokyo Bay such as tiger prawns, conger eels, shako, octopus, clams, and red clams, depending on their season. In addition to raw fish, another characteristic of Edomae-zushi is the "extra care" taken by the sushi chefs of Edo. We recommend boiled conger eel, seared mackerel, vinegared kohada, and grilled egg. The key to enjoying nigirizushi is to eat it as soon as it is served, as the perfect temperature between the rice and the fish is important.')
         st.image('shousi.webp')

         st.header('eel rice')
         st.write('Eel dishes have existed since ancient times, but it was not until the Edo period (1603-1868) that they became popular among the general public. There is a difference in the way eels are prepared in the Kansai and Kanto regions. In the Kanto region, the eel is cut from the back and the head is removed. The eel is grilled and then steamed, making it fluffy and fragrant. The eel is grilled with a light, non-sweet sauce. You can choose according to your needs from long-established famous restaurants where you can taste natural eel, restaurants where you can compare natural and farm-raised eel, and restaurants that offer reasonable lunches. Even if it is not the day of the Ox, you can recharge your energy for sightseeing in Tokyo by eating eel, which is full of nutrients such as vitamin A and DHA.')
         st.image('yu.webp')
       elif option2=='Landscapes':
         st.header('Tokyo Disneyland')
         st.write('Tokyo Disneyland is a theme park within the Tokyo Disney Resort in Urayasu, Chiba Prefecture, Japan. It was the first Disney park built outside the United States and opened on April 15, 1983. It is owned by Oriental Land and licensed for its theme from The Walt Disney Company. ')
         st.image('dishini.jpg')

         st.header('Tokyo Tower')
         st.write('Tokyo Tower is a comprehensive radio tower located in Shiba Park, Minato-ku, Tokyo, Japan. Its official name is Japan Radio Tower (Nihon Denpa-to). The founder is Hisakichi Maeda, and the construction was completed on December 23, 1958. It is a symbol of Tokyo and a tourist attraction.')
         st.write('The height is publicized as 333 meters, 351 meters above sea level. The distance between the tower legs, based on the center of the tower legs, is 88.0 meters. The total construction cost was approximately 3 billion yen and took one and a half years (1,974,015 hours/ 543 days) and a total of 219,335 personnel to complete. It is a truss structure radio tower with observation decks at 125 meters above ground level (150 meters above sea level) and 223.55 meters above ground level (250 meters above sea level).')
         st.image('ta.jpg')


         st.header('Asakusa ')
         st.write('Asakusa retains the atmosphere of old Tokyo, with traditional handicrafts and food stalls along Nakamise-dori near the historic Senso-ji Temple; the mid-19th century Hanayashiki amusement park with its thrilling ride attractions and cafes; and Sumida Park along the river, where festivals and fireworks displays are held regularly. Festivals and fireworks displays are held regularly in Sumida Park along the river. The neighborhood is dotted with casual izakayas (Japanese-style pubs) and yakitori restaurants serving skewered grilled meats and beer.')

         st.image('qiancao.jpg')
     elif option == 'Jakarta':
       option3 = st.selectbox(
           'Things want to know',
           ('Things want to know','festival','Gourmet','Landscapes'))
       if option3 =='festival':
         st.header("Eid al-Fitr")

         """
         ###### One of the main festivals of Islam. Together with Eid al-Adha, it is one of the two major festivals of Islam. Translation of Arabic "De Fittur". In Persian it is called Ruzi (Meatz). Adult Muslims, both men and women, fast for the month of September (commonly known as Ramadan) each year in the Islamic calendar, abstaining from food, drink, sex, and all indecent acts from before dawn to sunset each day in order to examine their own bodies and purify their sins. According to Muhammad's dictum, "Fast when you see the new moon, fast when you see the new moon," Ramadan begins in early September and ends in early October when the new moon is seen.
         """

         video_file = open('yinni.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[Youtube-アレキ紹介](https://www.youtube.com/watch?v=pLPJezrlfMw)")

         st.header("Spring Festival")

         st.write('The "Chap Go Meh," a traditional Chinese event held in Indonesia to celebrate the end of the Spring Festival (Chinese New Year). Editor Yasuhiko Ota reports from the site on the festival, which has taken root as a symbol of ethnic cooperation, especially among the Peranakan people, who are Chinese immigrants.')

         video_file = open('yinni2.mp4','rb')
         video_bytes = video_file.read()

         st.video(video_bytes)
         st.write("Site Links:")
         st.markdown("[Youtube-日本経済新聞](https://www.youtube.com/watch?v=HiXZ8hh6h5E)")
       elif option3=='Gourmet':
         st.header('Satay')
         st.write('Satay is a char-grilled dish of skewered meat, influenced by the Middle Eastern cuisine of kebabs. There are two types of sauces used to eat satay: peanut sauce, a mixture of chopped peppers, kidachi peppers, shallots, tomatoes, and pepper, and ketchup manis.')
         st.write('Satay is named according to the type of meat: chicken satay ayam, ground chicken satay li li, goat satay kambing, beef satay sapi, and pork satay babi. Satay is served with rice, lontong or kutupap.')
         st.image('sara.png')

         st.header('Rendang')
         """
         ###### Lundang, or rendang, is a meat dish made by simmering beef or other chunks of meat in coconut milk and spices for a long time; it was voted the best dish in the world by CNN in 2017. It is a local dish of West Sumatra, Indonesia, and is often cited as one of Indonesia's most iconic dishes.
         """
         st.image('rrd.jpg')

         st.header('Nasi campur')
         st.write('Nasi campur (nasi chanpur) is the name of a meal, or a dish of rice topped with side dishes of your choice, found in Indonesia and its neighboring regions, such as Malaysia and Singapore. In Indonesian and Malay, nasi means "rice" and campur means "to mix," but it does not necessarily mean "rice with multiple side dishes," as in Korean bibimbap ("mixed rice").')
         st.image('fan.jpg')
       elif option3 == 'Landscapes':
         st.header('Taman Mini Indonesia Indah')
         """
         ######Indonesia is said to consist of 18,110 islands of various sizes and about 300 ethnic groups. A theme park where you can take a peek into the life of each ethnic group and feel as if you have toured all of Indonesia at once is located about an hour's drive from central Jakarta.
         """
         st.write('The park has a Bali Pavilion, a Java Pavilion, and other buildings unique to each island, as well as a Komodo Dragon Museum and an aquarium, making it one of the spots where both adults and children can enjoy the whole day.')
         st.image('pari.jpg')

         st.header('Jakarta Cathedral')


         """
         ######this is a Christian cathedral. What a surprise, it's right in front of the Istiklal Mosque!
         """
         st.write('Once inside, it is a different world. Almost 90% of the Indonesian population seems to be Muslim, but there are Christians as well. You will be moved by the people praying single-mindedly in hymns.')
         st.image('jiaotang.jpg')

         st.header('Pulau Seribu')
         st.write('It is the closest beach resort to Jakarta. Prousrib means "thousand islands" in Indonesian.')
         """
         ######In fact, there are hundreds of islands, about 10 of which are inhabited. A 30-minute to 2-hour boat ride from Jakarta's northern "Anchor Harbor" welcomes you to the most beautiful ocean imaginable from Jakarta's coast!
         """
         st.write('You can enjoy reading a book at leisure, snorkeling with fish, or take a sunset cruise as an option. The boat is very bumpy, so take anti-sickness medicine if you get easily intoxicated!')
         st.image('dao.jpg')
