#import io
import streamlit as st
from PIL import Image


from PIL import Image
#from torchvision import models, transforms
#from model import predict #これは、model.pyのこと
import webbrowser




#st.title('つくるちゃん')
#st.caption('ものづくりを学ぼう')
st.sidebar.title("つくるchanのＷＥＢアプリ")
image = Image.open('TSUKURU.png')
#st.image(image,width=150)
st.sidebar.image(image,width=300)

st.sidebar.write("●私の名前は「つくる」です。\nあなたがアップロードする道具や工具の画像を見分けて、\
                 使い方などを説明します。")
st.sidebar.write("実験中なので正しく動作しません。")


st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write(" ")
st.sidebar.write("【プロフィール】")
st.sidebar.write("バナナ高等学校 工業科、総合ものづくりコースの２年生１７歳です。\
                 「つくる」という名前は、ものづくりが好きなパパが付けてくれました。\
                 \n好きな食べ物は熟す前のバナナ！！微妙に青臭いのがハオい。そして誕生日は８月７日…バナナの日！(なんてこったぁ～） \
                 \nパパに似て、ものづくりが好きで、特に木材加工や電子工作が大好き。\
                 最近は、パパのクルマの改造や裏の畑で野菜づくりのお手伝いもしています。\
                 運動音痴でスポーツが苦手（…ってかキライ）だけど、作業で動きやすい体育着でいるのが自分らしくておK。\
                 \n中学時代所属した吹奏楽部で出会ったサックスという楽器のおかげで、今は社会人に混じってバンド活動もめちゃ楽しんでます♪\
                 DTM（デスクトップミュージック）やプログラミング、釣りやお料理などなど、やりたいことがあり過ぎて困ったもんだぁ～。\
                 \n「多芸は無芸」ということわざ通り、どれも中途半端ですが、よろしくお願いします。\
                 ちなみに、同級生の「白根くん」は、ただのお友達。")
image = Image.open('SIRANE.png')
st.sidebar.image(image,width=150,caption="白根くん")
