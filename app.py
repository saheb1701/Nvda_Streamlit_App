import streamlit as st 
import yfinance as fn 


st.title("*NVIDIA & AMD* STOCK MARKET APP")


st.header("STOCK PRICE APP")  

st.sidebar.header("MORE ABOUBT NVDA && AMD") 


def new_ticker(name):
    compny=fn.Ticker(name)   
    return compny 

nv1 = new_ticker("NVDA")
am1 = new_ticker("AMD")

#Dataframe
nvid = fn.download("NVDA" , start="2019-01-02" , end="2022-03-18")
advmicro = fn.download("AMD" , start="2019-01-02" , end="2022-03-18")

#Previous data
hd1 = nv1.history(period="6mo")
hd2 = am1.history(period="6mo")

#Markdown
st.write(""" ## Nvidia """)
#Summary
st.write(nv1.info['longBusinessSummary'])
#Dataframe
st.write(nvid)
#Visuals
st.line_chart(hd1.values)


#Markdown
st.write(""" ## AMD """)
#Summary
st.write(nv1.info['longBusinessSummary'])
#Dataframe
st.write(advmicro)
#Visuals
st.line_chart(hd2.values)