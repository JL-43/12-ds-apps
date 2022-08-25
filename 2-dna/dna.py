import pandas as pd
import streamlit as st
import altair as alt
from PIL import Image

image = Image.open('dna-logo.jpeg')

st.image(image, use_column_width=True)

st.write("""

# DNA Nucleotide Count Web App

This app counts the nucleotide composition of query DNA!

***
""")

st.header('Enter DNA Sequence')

sequence_input = ">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence = st.text_area("Sequence Input", sequence_input, height=250)
sequence = sequence.splitlines()
sequence = sequence[1:]  # Skips the first line (sequence name)
sequence = ''.join(sequence)  # Concatenates list to a string

st.write("""
***
""")

st.header('INPUT (DNA Query)')
sequence

st.header('OUTPUT (DNA Nucleotide Count)')

st.subheader('1. Print dictionary')


def DNA_nucleotide_count(seq):
    d = dict([
        ('A', seq.count('A')),
        ('T', seq.count('T')),
        ('G', seq.count('G')),
        ('C', seq.count('C')),
    ])
    return d


X = DNA_nucleotide_count(sequence)
X_label = list(X)
X_values = list(X.values())
X

st.subheader('2.Print text')
st.write('There are ' + str(X['A']) + ' Adenine (A)')
st.write('There are ' + str(X['T']) + ' Thymine (T)')
st.write('There are ' + str(X['G']) + ' Guanine (G)')
st.write('There are ' + str(X['C']) + ' Cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns={'index': 'nucleotide'})
st.write(df)

st.subheader('4. Display Bar Chart')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p = p.properties(width=alt.Step(80))

st.write(p)
