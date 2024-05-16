import streamlit as st
from music21 import converter, pitch
import matplotlib.pyplot as plt
from collections import Counter

def process_music(file):
    # Load the music file using music21
    score = converter.parse(file)
    # Extract pitches from all notes
    pitches = [note.pitch.midi for note in score.flat.notes]
    return pitches

st.title("Musical Piece Processor")

uploaded_file = st.file_uploader("Upload a musical piece (symbolic format, e.g., MIDI, MusicXML)", type=["mid", "xml", "mxl"])

if uploaded_file is not None:
    st.write("Processing your file...")
    pitches = process_music(uploaded_file)

    st.write(f"Number of notes: {len(pitches)}")

    # Generate histogram
    pitch_counts = Counter(pitches)
    fig, ax = plt.subplots()
    ax.bar(pitch_counts.keys(), pitch_counts.values())
    ax.set_xlabel("MIDI Pitch")
    ax.set_ylabel("Frequency")
    ax.set_title("Histogram of Pitches")

    st.pyplot(fig)

st.write("Upload a file to see the processed result.")
