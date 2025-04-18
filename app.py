import streamlit as st

# --- App configuration ---
st.set_page_config(page_title="Unit Converter", page_icon="⚡", layout="wide")

# --- Custom CSS for styling ---
st.markdown("""
    <style>
    body, .main {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: 'Segoe UI', sans-serif;
    }

    h1 { 
        text-align: center;
        color: #58a6ff;
        text-shadow: 1px 1px 4px #000;
    }

    .stButton>button {
        background-color: #238636;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 0.6em 1.5em;
        margin-top: 10px;
        transition: all 0.2s ease-in-out;
    }

    .stButton>button:hover {
        background-color: #2ea043;
        transform: scale(1.05);
    }

    .stSelectbox, .stNumberInput {
        background: #161b22;
        color: #fff;
        border-radius: 10px;
    }

    .stSuccess {
        border-left: 5px solid #238636;
        background-color: #1c2c1c;
        padding: 1rem;
        font-size: 1.2rem;
        font-weight: bold;
    }
    </style>
""", unsafe_allow_html=True)


# --- Conversion logic ---
def convert_units(value, unit_from, unit_to):
    conversions = {
        "meter_kilometer": 0.001,
        "kilometer_meter": 1000,
        "gram_kilogram": 0.001,
        "kilogram_gram": 1000,
        "milliliter_liter": 0.001,
        "liter_milliliter": 1000,
    }
    key = f"{unit_from}_{unit_to}"
    return value * conversions[key] if key in conversions else f"❌ Conversion from {unit_from} to {unit_to} not supported"


# --- App Title ---
st.title("⚙️ Ultimate Unit Converter")
st.markdown("""
    <h4 style='text-align: center; color: #CCCCCC; font-weight: 400;'>
        Welcome to your personalized unit converter 🔄<br>Convert measurements instantly!
    </h4>
""", unsafe_allow_html=True)

# --- UI Layout ---
st.markdown("### 🔢 Enter the value you want to convert")
value = st.number_input("", min_value=0.0, step=0.1)

col1, col2 = st.columns(2)
with col1:
    unit_from = st.selectbox("📤 From Unit", ["meter", "kilometer", "gram", "kilogram", "milliliter", "liter"])
with col2:
    unit_to = st.selectbox("📥 To Unit", ["meter", "kilometer", "gram", "kilogram", "milliliter", "liter"])

# --- Convert Button ---
if st.button("🚀 Convert Now"):
    result = convert_units(value, unit_from, unit_to)
    st.success(f"✅ **Converted Value:** {result}")

# --- Footer ---
st.markdown("---")
st.markdown("<div style='text-align:center'>✨ Made with ❤️ by Ahsham Alam</div>", unsafe_allow_html=True)

