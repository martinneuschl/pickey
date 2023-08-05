# streamlit_app.py

import streamlit as st

header = st.container()
with header:
	st.title('Pickey.cz')
st.markdown('Analytika pro tvůrce - proof-of-concept. Cílem tohoto dema je ukázat interaktivní reporting, který ukazuje data z Google Analytics 4. Každý tvůrce bude mít náhled pouze na svá data a má tak možnost získat okamžitý přehled o výkonu svého profilu na Pickey.')
"""
from google.oauth2 import service_account
from google.cloud import bigquery

# Create API client.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"]
)
client = bigquery.Client(credentials=credentials)

# Perform query.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    query_job = client.query(query)
    rows_raw = query_job.result()
    # Convert to list of dicts. Required for st.cache_data to hash the return value.
    rows = [dict(row) for row in rows_raw]
    return rows

rows = run_query("SELECT word FROM `bigquery-public-data.samples.shakespeare` LIMIT 10")

# Print results.
st.write("Some wise words from Shakespeare:")
for row in rows:
    st.write("✍️ " + row['word'])
    """
