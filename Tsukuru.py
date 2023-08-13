# streamlit run filename.pyで起動する。
# マニュアルはこちら　↓
# https://docs.streamlit.io/

import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image
from torchvision import models, transforms
from model import predict #これは、model.pyのこと
import webbrowser







# https://github.com/yukinaga/ai_webapp/tree/main
# ---------- スライダー ----------
#st.title("st.slider()")
#x = st.slider("xの値")
#st.write(str(x) + "の2乗は" + str(x**2))

# ---------- ボタン ----------
#st.title("st.button()")
#if st.button("Morning?"):
#    st.write("Good morinig!")
#else:
#    st.write("Helllo!")

# ---------- テキスト入力 ----------
#st.title("st.text_input()")
#st.text_input("お住まいの国", key="country")
#st.session_state.country  # keyでアクセス

# ---------- チェックボックス ----------
#st.title("st.checkbox()")
#is_agree = st.checkbox("同意しますか？")
#if is_agree:
#    st.write("了解です！")
#else:
#    st.write("残念です！")

# ---------- セレクトボックス ----------
#st.title("st.selectbox()")
#df_select = pd.DataFrame({
#    "col1": [11, 12, 13, 14],
#    "col2": [111, 112, 113, 114]
#    })
#selected = st.selectbox(
#    "どの番号を選びますか？",
#     df_select["col2"])
#st.write("あなたは" + str(selected) + "番を選びました！")

# ---------- サイドバー ----------
#st.title("st.sidebar")

#y = st.sidebar.slider("yの値")
#st.write(str(y) + "の2倍は" + str(y*2))

#df_side = pd.DataFrame({
#    "animal": ["犬", "猫", "兎", "象", "蛙"],
#    "color": ["赤", "青", "黄", "白", "黒"]
#    })
#selected_side = st.sidebar.selectbox(
#    "どの動物を選びますか？",
#     df_side["animal"])
#st.write("あなたは" + str(selected_side) + "を選びました！")




st.set_option("deprecation.showfileUploaderEncoding", False)


#st.title('つくるちゃん')
#st.caption('ものづくりを学ぼう')
st.sidebar.title("つくるのＡＩ-ＷＥＢアプリ")
image = Image.open('TSUKURU.png')
#st.image(image,width=150)
st.sidebar.image(image,width=300)

st.sidebar.write("●私の名前は「つくる」です。あなたがアップロードする道具や工具の画像を見分けて、\
                 使い方などを説明します。")
st.sidebar.write("")

global img_source
img_source = st.sidebar.radio("画像のアップロード方法を選んでね。",
                              ("画像ファイルをアップロード", "カメラ撮影でアップロード"))
if img_source == "画像ファイルをアップロード":
    img_file = st.sidebar.file_uploader("画像を選択してね。下の枠内に画像ファイルをドラッグ＆ドロップすることもできるよ。", type=["png", "jpg","jpeg"])
elif img_source == "カメラ撮影でアップロード":
    img_file = st.camera_input("カメラ撮影でアップロード")

st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("【プロフィール】")
st.sidebar.write("バナナ高等学校 工業科、総合ものづくりコースの２年生１７歳です。\
                 「つくる」という名前は、ものづくりが好きなパパが付けてくれました。\
                 好きな食べ物は熟す前のバナナ！！微妙に青臭いのがハオい。そして誕生日は８月７日…バナナの日！(なんてこったぁ～） \
                 パパに似て、ものづくりが好きで、特に木材加工や電子工作が大好き。\
                 最近は、パパのクルマの改造や裏の畑で野菜づくりのお手伝いもしています。\
                 運動音痴でスポーツが苦手（…ってかキライ）だけど、作業で動きやすい体育着でいるのが自分らしくておK。\
                 中学時代所属した吹奏楽部で出会ったサックスという楽器のおかげで、今は社会人に混じってバンド活動もめちゃ楽しんでます♪\
                 DTM（デスクトップミュージック）やプログラミング、釣りやお料理などなど、やりたいことがあり過ぎて困ったもんだぁ～。\
                 「多芸は無芸」ということわざ通り、どれも中途半端ですが、よろしくお願いします。\
                 ちなみに、同級生の「白根くん」は、ただのお友達。")
image = Image.open('SIRANE.png')
st.sidebar.image(image,width=150,caption="白根くん")

if img_file is not None:
    with st.spinner("推定中..."):
        img = Image.open(img_file)
        if img_source=="画像ファイルをアップロード":
            st.image(img, caption="アップロードされた画像", width=480)
            st.write("")

        # 予測
        results = predict(img)

        # 結果の表示
        #st.subheader("判定結果")        
        n_top = 1  # 確率が高い順に5位まで返す
        for result in results[:n_top]:
            #st.write(str(round(result[1]*100, 2)) + "%の確率で" + result[0] + "だよね？")
            st.subheader("これって、"+result[0]+"？だよねぇ")
            st.write(str(round(100-result[1]*100,2)) + "％まちがってるかも…てへぺろ")            
            
        # ---------- ボタン ----------
        #st.subheader("下のボタンで説明をはじめるよ")

        
        #if st.button("新しいタブで説明を見る"):
            #st.write("Good morinig!")
        #    webbrowser.open_new_tab('https://hibiki-press.tech/python/webbrowser_module/1884')
        
        url = "https://katagamiedu-my.sharepoint.com/personal/katat00183_katagamiedu_onmicrosoft_com/_layouts/15/stream.aspx?id=%2Fpersonal%2Fkatat00183%5Fkatagamiedu%5Fonmicrosoft%5Fcom%2FDocuments%2FVideos%2F%E3%83%A9%E3%82%B8%E3%82%AA%E3%83%9A%E3%83%B3%E3%83%81%E3%81%AE%E4%BD%BF%E3%81%84%E6%96%B9%2Emp4&ga=1"
        st.subheader(result[0]+"の説明をしますか？ [はい](%s)" % url)
        st.write("（新しいタブが開かれます。）")
        #st.markdown("check out this [link](%s)" % url)



        # 円グラフの表示
        #pie_labels = [result[0] for result in results[:n_top]]
        #pie_labels.append("others")
        #pie_probs = [result[1] for result in results[:n_top]]
        #pie_probs.append(sum([result[1] for result in results[n_top:]]))
        #fig, ax = plt.subplots()
        #wedgeprops={"width":0.3, "edgecolor":"white"}
        #textprops = {"fontsize":6}
        #ax.pie(pie_probs, labels=pie_labels, counterclock=False, startangle=90,
        #       textprops=textprops, autopct="%.2f", wedgeprops=wedgeprops)  # 円グラフ
        #st.pyplot(fig)


# StreamlitでWebアプリ開発！インストールからデプロイまで徹底解説
# https://camp.trainocate.co.jp/magazine/streamlit-web/

# Resnetを転移学習
# http://pchun.work/resnet%E3%82%92fine-tuning%E3%81%97%E3%81%A6%E8%87%AA%E5%88%86%E3%81%8C%E7%94%A8%E6%84%8F%E3%81%97%E3%81%9F%E7%94%BB%E5%83%8F%E3%82%92%E5%AD%A6%E7%BF%92%E3%81%95%E3%81%9B%E3%82%8B/

# Udemy？のオンライン講座の資料？
# https://github.com/yukinaga/ai_webapp/blob/main/section_3/01_image_recognition.ipynb