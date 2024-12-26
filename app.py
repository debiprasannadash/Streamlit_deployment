import streamlit as st 

st.title('Title-> Welcome to GeeksforGeeks')      # Title
st.header('Header-> GeeksforGeeks')               # Header
st.subheader('Subheader->  GeeksforGeeks')        # Subheader

st.markdown(' Hi')       # Markdown
st.markdown('# Hi')
st.markdown('## Hi')
st.markdown('### Hi') 
st.markdown('#### Hi')

#success
st.success('Data is submitted')

#Info
st.info('Information!')

#warning
st.warning('Warning!')

#error
st.error('Error!')

#Exception
st.exception(ZeroDivisionError('Div not possible'))

#help
st.help(ZeroDivisionError)

#write
st.write("range(1,10)")
st.write(range(1,10))
st.write(1*2*3)

#code
st.code('x = 10\n'
        'for i in range(x):\n'
        '\tprint(i)')

#checkbox
st.checkbox('Male')

#checkbox with validation
if(st.checkbox('Adult')):
    st.write("You are an adult")
    
    
#radio button
radioButton = st.radio('Select :',('Male', 'Female','Other'))
if(radioButton == 'Male'):
    st.write("You are male")
elif(radioButton == 'Female'):
    st.write("You are Female")
elif(radioButton == 'Other'):
    st.write("You are Others")
    
#Select box
st.subheader('Select Box')
selectBox = st.selectbox("Data Science : ", ['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Computer vision', 'Image Processing'])
st.write("You have selected : ", selectBox)

#multi Select box
st.subheader('MultiSelect Box')
multiSelBox = st.multiselect("Data Science : ", ['Data Analysis','Web Scrapping','Machine Learning','Deep Learning','Natural Language Processing','Computer vision', 'Image Processing'])
st.write("You have selected : ", multiSelBox)

st.write("You have selected : ", len(multiSelBox), 'Courses')

st.subheader("Button")
st.button('Click me ')

if(st.button('Click me')):
    st.write('Thanks for clicking me')

#slider
st.subheader('Slider')
vol = st.slider('Select the level ',1,100, step = 1)

st.write("Volume is ",vol)


#Text input 
st.subheader("Text input")
username = st.text_input('Username : ')
password = st.text_input('Password : ', type = 'password')


#Text-area
st.subheader("text-area")
textArea = st.text_area("Write something interesting about yourself in 20 words", height = 20)
st.write(textArea)

#input number
st.subheader("input number")
st.number_input("Select your age",18,110)

#input date
st.subheader("Input date")
st.date_input('Date')

#input time
st.subheader("input time")
st.time_input('Time')