import warnings
warnings.filterwarnings('ignore')

import pandas as pd
import openpyxl
import streamlit as st
from io import BytesIO
import xlsxwriter

st.markdown("# Baromètre d'Opinion des Bénévoles 2024")
st.sidebar.markdown("# Présentation")

"*Baromètre d'Opinion des Bénévoles, en ligne 15 février au 22 avril 2024, auprès de 3 717 bénévoles d'horizons différents.*"
