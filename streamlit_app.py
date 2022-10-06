import streamlit as st
import numpy as np
import pandas as pd
from st_aggrid import AgGrid
import plost

# Modified from Plost
@st.experimental_memo
def get_datasets():
    N = 50
    rand = pd.DataFrame()
    rand['a'] = np.arange(N)
    rand['b'] = np.random.rand(N)
    rand['c'] = np.random.rand(N)

    N = 500
    events = pd.DataFrame()
    events['time_delta_s'] = np.random.randn(N)
    events['servers'] = np.random.choice(['server 1', 'server 2', 'server 3'], N)

    N = 500
    randn = pd.DataFrame(
        np.random.randn(N, 4),
        columns=['a', 'b', 'c', 'd'],
    )

    stocks = pd.DataFrame(dict(
        company=['goog', 'fb', 'ms', 'amazon'],
        q1=[3, 5, 4, 6],
        q2=[4, 6, 8, 2],
        q3=[2, 5, 2, 6],
        q4=[4, 5, 6, 7],
    ))

    N = 200
    pageviews = pd.DataFrame()
    pageviews['pagenum'] = [f'page-{i:03d}' for i in range(N)]
    pageviews['pageviews'] = np.random.randint(0, 1000, N)

    return dict(
        rand=rand,
        randn=randn,
        events=events,
        pageviews=pageviews,
        stocks=stocks,
        seattle_weather=pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/seattle-weather.csv', parse_dates=['date']),
        sp500=pd.read_csv('https://raw.githubusercontent.com/tvst/plost/master/data/sp500.csv', parse_dates=['date']),
    )

datasets = get_datasets()



######################################################
st.markdown('*Research article*')
st.title('Writing a research article using Streamlit')

st.markdown('''
**Chanin Nantasenamat**

*Data Professor, YouTube channel, https://youtube.com/dataprofessor*

''')

st.header('Abstract')
st.info('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.
''')

st.markdown('**Keywords:** *Streamlit*, *machine learning*, *data science*, *Python*')

st.header('Introduction')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua [1]. Tempus quam pellentesque nec nam aliquam sem et tortor. Vestibulum rhoncus est pellentesque elit ullamcorper. Diam vulputate ut pharetra sit amet aliquam. Sed turpis tincidunt id aliquet risus feugiat in ante. Auctor urna nunc id cursus metus aliquam eleifend mi. Tortor at risus viverra adipiscing at. Cras sed felis eget velit aliquet. Diam phasellus vestibulum lorem sed risus ultricies tristique nulla. Arcu risus quis varius quam quisque id diam. Tempor orci eu lobortis elementum nibh tellus molestie nunc. Ultricies mi eget mauris pharetra et ultrices neque ornare. Odio eu feugiat pretium nibh ipsum. Vulputate dignissim suspendisse in est ante in nibh mauris. Rutrum quisque non tellus orci ac auctor. Ultrices dui sapien eget mi. Volutpat diam ut venenatis tellus in. Congue nisi vitae suscipit tellus mauris a. Elementum sagittis vitae et leo.

Sit amet nisl suscipit adipiscing bibendum est ultricies integer quis. Praesent elementum facilisis leo vel fringilla est ullamcorper eget nulla. Elementum pulvinar etiam non quam lacus suspendisse faucibus interdum posuere. Sapien et ligula ullamcorper malesuada proin. Feugiat nibh sed pulvinar proin gravida hendrerit lectus. Eget egestas purus viverra accumsan in nisl nisi. Libero id faucibus nisl tincidunt eget nullam non nisi. Arcu odio ut sem nulla pharetra diam sit amet nisl. Mollis nunc sed id semper risus. Quam elementum pulvinar etiam non quam lacus suspendisse faucibus interdum. Ac odio tempor orci dapibus. In hac habitasse platea dictumst vestibulum rhoncus est. Sit amet dictum sit amet justo donec enim. Accumsan tortor posuere ac ut. Id aliquet risus feugiat in ante. Pulvinar pellentesque habitant morbi tristique senectus et netus et malesuada. Etiam tempor orci eu lobortis elementum nibh tellus.

Vitae turpis massa sed elementum. Arcu non sodales neque sodales ut etiam. Non pulvinar neque laoreet suspendisse interdum consectetur libero id faucibus. Viverra tellus in hac habitasse platea dictumst vestibulum rhoncus est. Augue ut lectus arcu bibendum at varius vel pharetra. Diam in arcu cursus euismod quis. Vitae aliquet nec ullamcorper sit amet risus nullam eget. Vel eros donec ac odio tempor orci dapibus ultrices in. Nec dui nunc mattis enim ut. Malesuada proin libero nunc consequat interdum. In fermentum et sollicitudin ac orci. Pellentesque habitant morbi tristique senectus et netus et. Faucibus vitae aliquet nec ullamcorper sit.
''')

st.header('Materials and Methods')

st.subheader('Semper viverra nam libero')
st.markdown('''
Ut consequat semper viverra nam libero. Arcu vitae elementum curabitur vitae [2]. Neque convallis a cras semper auctor neque vitae tempus. Tempus quam pellentesque nec nam aliquam. Libero nunc consequat interdum varius sit amet mattis vulputate. Nibh tortor id aliquet lectus. Netus et malesuada fames ac turpis egestas. Euismod in pellentesque massa placerat duis ultricies. Amet volutpat consequat mauris nunc congue nisi. Vulputate eu scelerisque felis imperdiet proin.
''')

st.caption('**Table 1.** Seattle weather data.')
AgGrid(datasets['seattle_weather'], height=300)


st.caption('**Table 2.** Stocks data.')
AgGrid(datasets['stocks'])



st.subheader('Pellentesque massa placerat')
st.markdown('''
Quisque egestas diam in arcu cursus euismod quis. A pellentesque sit amet porttitor eget dolor. Euismod in pellentesque massa placerat duis ultricies. In ante metus dictum at tempor commodo ullamcorper a lacus. Sit amet nisl purus in mollis nunc sed id semper. Adipiscing elit pellentesque habitant morbi. Vitae sapien pellentesque habitant morbi tristique senectus et netus. Vestibulum lectus mauris ultrices eros in. Pellentesque elit eget gravida cum sociis natoque. Accumsan in nisl nisi scelerisque eu ultrices vitae auctor. Id venenatis a condimentum vitae. Nec ultrices dui sapien eget mi proin sed libero enim. Tellus at urna condimentum mattis pellentesque. Non sodales neque sodales ut etiam sit. Ut aliquam purus sit amet. Volutpat diam ut venenatis tellus in metus vulputate.
''')


st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^{n-1} =
    \sum_{k=0}^{n-1} ar^k =
    a \left(\frac{1-r^{n}}{1-r}\right)
    ''')


st.subheader('Sed do eiusmod')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Integer vitae justo eget magna fermentum iaculis eu non. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. In nulla posuere sollicitudin aliquam ultrices sagittis. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Eget felis eget nunc lobortis mattis aliquam faucibus purus. Placerat in egestas erat imperdiet sed euismod nisi porta. Dictum at tempor commodo ullamcorper. Malesuada pellentesque elit eget gravida cum. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula.
''')

st.header('Results and Discussion')

st.subheader('Consectetur adipiscing elit')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua [3]. Integer vitae justo eget magna fermentum iaculis eu non. Scelerisque mauris pellentesque pulvinar pellentesque habitant morbi. In nulla posuere sollicitudin aliquam ultrices sagittis. Nisl nunc mi ipsum faucibus vitae aliquet nec ullamcorper. Eget felis eget nunc lobortis mattis aliquam faucibus purus. Placerat in egestas erat imperdiet sed euismod nisi porta. Dictum at tempor commodo ullamcorper. Malesuada pellentesque elit eget gravida cum. Sollicitudin nibh sit amet commodo nulla facilisi nullam vehicula.
''')

selected_temp = st.multiselect('Select data', ['temp_max', 'temp_min'], ['temp_max', 'temp_min'])
st.line_chart(
     data=datasets['seattle_weather'],
     x='date',
     y=selected_temp,
     )
st.caption('**Figure 1.** Line chart of Seattle weather data.')


st.subheader('Arcu non sodales')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua [4]. Nibh tortor id aliquet lectus proin nibh nisl condimentum id. Laoreet id donec ultrices tincidunt [5]. In ornare quam viverra orci sagittis eu volutpat odio facilisis. Cursus turpis massa tincidunt dui ut ornare lectus sit. Quis vel eros donec ac odio tempor. Quis auctor elit sed vulputate mi. Feugiat sed lectus vestibulum mattis. Sed vulputate odio ut enim blandit volutpat. Aliquam eleifend mi in nulla. Egestas sed tempus urna et. Nisl vel pretium lectus quam id leo. Quam elementum pulvinar etiam non quam lacus suspendisse. Lectus magna fringilla urna porttitor rhoncus. Vitae tempus quam pellentesque nec nam aliquam sem et. Mauris in aliquam sem fringilla ut morbi tincidunt augue interdum.
''')

selected_q = st.multiselect('Select Q', ['q1', 'q2', 'q3', 'q4'], ['q1', 'q2', 'q3', 'q4'])
plost.bar_chart(
        data=datasets['stocks'],
        bar='company',
        value=selected_q,
        group='value',
        color='company',
        legend=None,
        )
st.caption('**Figure 2.** Bar chart of stocks data.')


st.header('Conclusion')
st.markdown('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Bibendum at varius vel pharetra vel turpis nunc. Nunc id cursus metus aliquam eleifend mi in nulla. Pellentesque habitant morbi tristique senectus et netus et malesuada fames. Donec et odio pellentesque diam. Eu consequat ac felis donec. Nulla facilisi etiam dignissim diam quis. Vestibulum mattis ullamcorper velit sed ullamcorper. Ipsum suspendisse ultrices gravida dictum fusce. Facilisis sed odio morbi quis commodo odio aenean sed. Enim neque volutpat ac tincidunt.
''')

st.header('Acknowledgements')
st.warning('''
Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Nulla facilisi nullam vehicula ipsum a. Nunc faucibus a pellentesque sit amet porttitor eget dolor. Nunc sed velit dignissim sodales ut eu sem integer vitae. Vel facilisis volutpat est velit. Auctor eu augue ut lectus arcu. Habitant morbi tristique senectus et netus. Quisque sagittis purus sit amet volutpat consequat mauris nunc. Libero justo laoreet sit amet cursus sit. Sed faucibus turpis in eu. Ac orci phasellus egestas tellus rutrum. Malesuada proin libero nunc consequat. Nascetur ridiculus mus mauris vitae ultricies leo integer malesuada. Facilisi morbi tempus iaculis urna id volutpat. Mi bibendum neque egestas congue quisque egestas diam in. Nunc lobortis mattis aliquam faucibus.
''')

st.header('References')
st.markdown('''
1. Li H, Tamang T, Nantasenamat C. Toward insights on antimicrobial selectivity of host defense peptides via machine learning model interpretation. Genomics. 2021;113(6):3851-3863.

2. Schaduangrat N, Malik AA, Nantasenamat C. ERpred: a web server for the prediction of subtype-specific estrogen receptor antagonists. PeerJ. 2021;9:e11716.

3. Schaduangrat N, Lampa S, Simeon S, Gleeson MP, Spjuth O, Nantasenamat C. Towards reproducible computational drug discovery. J Cheminform. 2020;12(1):9. 

4. Li H, Nantasenamat C. Toward insights on determining factors for high activity in antimicrobial peptides via machine learning. PeerJ. 2019;7:e8265.

5. Suvannang N, Preeyanon L, Malik AA, Schaduangrat N, Shoombuatong W, Worachartcheewan A, Tantimongcolwat T, Nantasenamat C. Probing the origin of estrogen receptor alpha inhibition via large-scale QSAR study. RSC Adv. 2018;8(21):11344-11356.
''')
