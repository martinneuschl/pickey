import streamlit as st
import pandas as pd


header = st.container()
dataset = st.container()
features = st.container()
model_training = st.container()

with header:
	st.title('Pickey.cz')
	st.markdown('Analytika pro tvůrce - proof-of-concept. Cílem tohoto dema je ukázat interaktivní reporting, který ukazuje data z Google Analytics 4. Každý tvůrce bude mít náhled pouze na svá data a má tak možnost získat okamžitý přehled o výkonu svého profilu na Pickey.')

with dataset:
	st.header('Reporting pro tvůrce')
	st.markdown('Tohle je ukázka JavaScript snippetu:')
	st.code('console.log("Ahoj!")')

	taxi_data = pd.read_csv('')
with features:
	st.header('Základní data')

#with model_training:
