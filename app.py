import streamlit as st 
import pandas as pd 
import pickle as pk
st.title('Salary Prediction')

dbfile = open('salary.pickle', 'rb')    
model = pk.load(dbfile)

#input form
age = st.number_input('Enter your age = ', 18, 60 )
exp = st.number_input('Enter your exp = ', 0, 30)
gender = st.radio('Gender', ['Male' , 'Female'])
education = st.selectbox('Education = ', ["Bachelor's","Master's",'PhD'])

if st.button('Predict'):
	if gender == 'Male':
		gender = True
	else:
		gender = False
	if education == "Bachelor's":
		b=1; m=0; p=0
	elif education == "Master's":
		b=0;m=1;p=0
	else:
		b=0;m=0;p=1
	df = pd.DataFrame({
		'Age':[age],
		'Years of Experience':[exp],
		'Male':[gender],
		"Bachelor's":[b],
		"Master's":[m],
		'PhD':[p] 
		})
	st.dataframe(df)
	result = round(model.predict(df)[0][0],2)
	print(result)
	st.write(result)
	st.write('PREDICTED SALARY')
	st.balloons()
	# st.snow()
