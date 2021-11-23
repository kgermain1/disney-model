import streamlit as st
import pandas as pd
from PIL import Image
from millify import millify

DISNEY_LOGO = Image.open('publicis.png')
YOUTUBE_LOGO = Image.open('youtube.jpg')
DV360_LOGO = Image.open('DV360.png')
TTD_LOGO = Image.open('TTD.png')
AMAZON_LOGO = Image.open('amazon.jpg')

#PLATFORMS = ["YouTube", "DV360", "TTD", "Amazon", "Facebook", "Twitter", "Snapchat", "TikTok", "Pinterest"]
PLATFORMS = ["YouTube", "DV360", "TTD", "Amazon"]
DATA_25 = []
DATA_50 = []
DATA_75 = []
DATA_100 = []

header = st.container()
body = st.container()

with header:
    st.image(DISNEY_LOGO)
    st.title("Disney+ Programmatic Data Forecast Model")
    st.markdown("This tool is aimed at forecasting the impact of spend on completed video views for programmatic advertising for Disney+. It uses Disney+'s own past performance data to predict future investments based on completed video views as a main KPI.")
    
with body:
    st.title("Modeling Section")
    
    INPUT_CALCULATION_METHOD = st.selectbox("What would you like to forecast?", options=["Performance based on spend", "Spend based on performance"])
    
    if INPUT_CALCULATION_METHOD == "Performance based on spend":
        INPUT_BUDGET_BOX = st.text_input("Please enter your budget (in USD):", "10000")
        
        YOUTUBE_25 = round(136.84*float(INPUT_BUDGET_BOX) + 2E+06)
        DATA_25.append(YOUTUBE_25)
        
        YOUTUBE_50 = round(101.82*float(INPUT_BUDGET_BOX) + 1E+06)
        DATA_50.append(YOUTUBE_50)
        
        YOUTUBE_75 = round(89.182*float(INPUT_BUDGET_BOX) + 1E+06)
        DATA_75.append(YOUTUBE_75)
        
        YOUTUBE_100 = round(80.907*float(INPUT_BUDGET_BOX) + 1E+06)
        DATA_100.append(YOUTUBE_100)
        
        DV360_25 = round(110.28*float(INPUT_BUDGET_BOX) + 2E+06)
        DATA_25.append(DV360_25)
        
        DV360_50 = round(84.245*float(INPUT_BUDGET_BOX) + 2E+06)
        DATA_50.append(DV360_50)
        
        DV360_75 = round(74.357*float(INPUT_BUDGET_BOX) + 2E+06)
        DATA_75.append(DV360_75)
        
        DV360_100 = round(68.054*float(INPUT_BUDGET_BOX) + 1E+06)
        DATA_100.append(DV360_100)
        
        TTD_25 = round(54.928*float(INPUT_BUDGET_BOX) + 456362)
        DATA_25.append(TTD_25)
        
        TTD_50 = round(53.157*float(INPUT_BUDGET_BOX) + 486825)
        DATA_50.append(TTD_50)
        
        TTD_75 = round(51.807*float(INPUT_BUDGET_BOX) + 513435)
        DATA_75.append(TTD_75)
        
        TTD_100 = round(50.691*float(INPUT_BUDGET_BOX) + 536920)
        DATA_100.append(TTD_100)
        
        AMAZON_25 = round(68.752*float(INPUT_BUDGET_BOX) + 88795)
        DATA_25.append(AMAZON_25)
        
        AMAZON_50 = round(63.357*float(INPUT_BUDGET_BOX) + 72084)
        DATA_50.append(AMAZON_50)
        
        AMAZON_75 = round(59.469*float(INPUT_BUDGET_BOX) + 63588)
        DATA_75.append(AMAZON_75)
        
        AMAZON_100 = round(55.847*float(INPUT_BUDGET_BOX) + 53883)
        DATA_100.append(AMAZON_100)
        
    elif INPUT_CALCULATION_METHOD == "Spend based on performance":
        INPUT_PERFORMANCE_BOX = st.text_input("Please enter your desired views:", "2000000")
        
        YOUTUBE_25 = round((float(INPUT_PERFORMANCE_BOX) - 2E+06)/136.84, 2)
        if (YOUTUBE_25 <0): YOUTUBE_25 = 0
        DATA_25.append(YOUTUBE_25)
        
        YOUTUBE_50 = round((float(INPUT_PERFORMANCE_BOX) - 1E+06)/101.82, 2)
        if (YOUTUBE_50 <0): YOUTUBE_50 = 0
        DATA_50.append(YOUTUBE_50)
        
        YOUTUBE_75 = round((float(INPUT_PERFORMANCE_BOX) - 1E+06)/101.82, 2)
        if (YOUTUBE_75 <0): YOUTUBE_75 = 0
        DATA_75.append(YOUTUBE_75)
        
        YOUTUBE_100 = round((float(INPUT_PERFORMANCE_BOX) - 1E+06)/80.907, 2)
        if (YOUTUBE_100 <0): YOUTUBE_100 = 0
        DATA_100.append(YOUTUBE_100)
        
        DV360_25 = round((float(INPUT_PERFORMANCE_BOX) - 2E+06)/110.28, 2)
        if (DV360_25 <0): DV360_25 = 0
        DATA_25.append(DV360_25)
        
        DV360_50 = round((float(INPUT_PERFORMANCE_BOX) - 2E+06)/84.245, 2)
        if (DV360_50 <0): DV360_50 = 0
        DATA_50.append(DV360_50)
        
        DV360_75 = round((float(INPUT_PERFORMANCE_BOX) - 2E+06)/74.357, 2)
        if (DV360_75 <0): DV360_75 = 0
        DATA_75.append(DV360_75)
        
        DV360_100 = round((float(INPUT_PERFORMANCE_BOX) - 1E+06)/68.054, 2)
        if (DV360_100 <0): DV360_100 = 0
        DATA_100.append(DV360_100)
        
        TTD_25 = round((float(INPUT_PERFORMANCE_BOX) - 456362)/54.928, 2)
        if (TTD_25 <0): TTD_25 = 0
        DATA_25.append(TTD_25)
        
        TTD_50 = round((float(INPUT_PERFORMANCE_BOX) - 486825)/53.157, 2)
        if (TTD_50 <0): TTD_50 = 0
        DATA_50.append(TTD_50)
        
        TTD_75 = round((float(INPUT_PERFORMANCE_BOX) - 513435)/51.807, 2)
        if (TTD_75 <0): TTD_75 = 0
        DATA_75.append(TTD_75)
        
        TTD_100 = round((float(INPUT_PERFORMANCE_BOX) - 536920)/50.691, 2)
        if (TTD_100 <0): TTD_100 = 0
        DATA_100.append(TTD_100)
        
        AMAZON_25 = round((float(INPUT_PERFORMANCE_BOX) - 88795)/68.752, 2)
        if (AMAZON_25 <0): AMAZON_25 = 0
        DATA_25.append(AMAZON_25)
        
        AMAZON_50 = round((float(INPUT_PERFORMANCE_BOX) - 72084)/63.357, 2)
        if (AMAZON_50 <0): AMAZON_50 = 0
        DATA_50.append(AMAZON_50)
        
        AMAZON_75 = round((float(INPUT_PERFORMANCE_BOX) - 63588)/59.469, 2)
        if (AMAZON_75 <0): AMAZON_75 = 0
        DATA_75.append(AMAZON_75)
        
        AMAZON_100 = round((float(INPUT_PERFORMANCE_BOX) - 53883)/55.847, 2)
        if (AMAZON_100 <0): AMAZON_100 = 0
        DATA_100.append(AMAZON_100)
    
    YT_CONTAINER = st.container()
    
    with YT_CONTAINER:
        col1, col2, col3, col4, col5= st.columns(5)
        col1.image(YOUTUBE_LOGO)
        col2.metric('25% Video Views', millify(YOUTUBE_25, precision=2))
        col3.metric('50% Video Views', millify(YOUTUBE_50, precision=2))
        col4.metric('75% Video Views', millify(YOUTUBE_75, precision=2))
        col5.metric('100% Video Views', millify(YOUTUBE_100, precision=2))
        
    DV360_CONTAINER = st.container()

    with DV360_CONTAINER:    
        col1, col2, col3, col4, col5= st.columns(5)
        col1.write("")
        col1.image(DV360_LOGO)
        col2.metric('25% Video Views', millify(DV360_25, precision=2))
        col3.metric('50% Video Views', millify(DV360_50, precision=2))
        col4.metric('75% Video Views', millify(DV360_75, precision=2))
        col5.metric('100% Video Views', millify(DV360_100, precision=2))
        
    TTD_CONTAINER = st.container()

    with TTD_CONTAINER:
        col1, col2, col3, col4, col5= st.columns(5)
        col1.write("")
        col1.write("")
        col1.image(TTD_LOGO)
        col2.metric('25% Video Views', millify(TTD_25, precision=2))
        col3.metric('50% Video Views', millify(TTD_50, precision=2))
        col4.metric('75% Video Views', millify(TTD_75, precision=2))
        col5.metric('100% Video Views', millify(TTD_100, precision=2))
        
    AMAZON_CONTAINER = st.container()

    with AMAZON_CONTAINER:
        col1, col2, col3, col4, col5= st.columns(5)
        col1.image(AMAZON_LOGO)
        col2.metric('25% Video Views', millify(AMAZON_25, precision=2))
        col3.metric('50% Video Views', millify(AMAZON_50, precision=2))
        col4.metric('75% Video Views', millify(AMAZON_75, precision=2))
        col5.metric('100% Video Views', millify(AMAZON_100, precision=2))
    
    resultsDict = {
            'platform': PLATFORMS,
            '25% Video Views': DATA_25,
            '50% Video Views': DATA_50,
            '75% Video Views': DATA_75,
            '100% Video Views': DATA_100,
    }
    
    df = pd.DataFrame.from_dict(resultsDict)
    st.write(df.head(9))