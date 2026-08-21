import streamlit as st
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

st.set_page_config(
    page_title="MAS Monetary Policy Stance Dataset",
    page_icon="🇸🇬",
    layout="wide"
)

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('mas_policy_stance.csv')
    df['date_parsed'] = pd.to_datetime(df['date'], format='%Y-%m')
    df['year'] = df['date_parsed'].dt.year
    df['cycle'] = df['date'].apply(lambda x: 
        'Post Dot-Com' if x <= '2003-10' else
        'Pre-GFC Expansion' if x <= '2008-04' else
        'GFC Recovery' if x <= '2010-10' else
        'Post-GFC Steady' if x <= '2021-04' else
        'COVID Recovery' if x <= '2021-04' else
        '2021-2022 Tightening Cycle' if x <= '2022-10' else
        '2023-2025 Pause & Easing' 
    )
    return df

df = load_data()

# ── HEADER ──────────────────────────────────────────────────────────────────
st.markdown("""
<div style='background: linear-gradient(135deg, #1B2A4A 0%, #2a4a8a 100%); 
     padding: 2rem; border-radius: 12px; margin-bottom: 1.5rem;'>
<h1 style='color: white; margin: 0; font-size: 2rem;'>🇸🇬 MAS Monetary Policy Stance Dataset</h1>
<p style='color: #aac4ff; margin: 0.5rem 0 0 0; font-size: 1rem;'>
All S$NEER policy decisions classified by slope, width, and centring · 2001–2026 · 55 statements
</p>
<p style='color: #7a9fd4; margin: 0.3rem 0 0 0; font-size: 0.85rem;'>
Built on Gokhale (2026) · ssrn.com/abstract=6514338
</p>
</div>
""", unsafe_allow_html=True)

# ── METRICS ROW ──────────────────────────────────────────────────────────────
col1, col2, col3, col4, col5 = st.columns(5)
with col1:
    st.metric("Total Statements", len(df))
with col2:
    st.metric("Tightening", len(df[df['stance']=='tighten']), delta="+13")
with col3:
    st.metric("Neutral / Hold", len(df[df['stance']=='neutral']))
with col4:
    st.metric("Easing", len(df[df['stance']=='ease']), delta="-11")
with col5:
    peak = df.loc[df['score'].idxmax(), 'date']
    st.metric("Peak Hawkishness", peak)

st.markdown("---")

# ── MAIN CHART ──────────────────────────────────────────────────────────────
st.subheader("Hawkishness Score Over Time")
st.caption("Score: +2 = aggressive tightening (steepen + recentre up) · 0 = hold · -2 = aggressive easing (flatten + recentre down)")

fig = go.Figure()

# Colour by stance
colours = {'tighten': '#e63946', 'neutral': '#457b9d', 'ease': '#2a9d8f'}

for stance, grp in df.groupby('stance'):
    fig.add_trace(go.Bar(
        x=grp['date'],
        y=grp['score'],
        name=stance.capitalize(),
        marker_color=colours[stance],
        hovertemplate='<b>%{x}</b><br>Score: %{y}<br>%{customdata}<extra></extra>',
        customdata=grp['note']
    ))

# Add cycle labels as shapes
cycles = [
    ('2003-04', 'SARS', '#ff9f1c'),
    ('2008-10', 'GFC', '#e63946'),
    ('2020-03', 'COVID', '#6a4c93'),
    ('2021-10', 'Tightening Cycle', '#e63946'),
    ('2025-01', 'Easing', '#2a9d8f'),
]

fig.update_layout(
    barmode='relative',
    plot_bgcolor='white',
    paper_bgcolor='white',
    height=380,
    legend=dict(orientation='h', y=1.08),
    xaxis=dict(title='', tickangle=-45, gridcolor='#f0f0f0'),
    yaxis=dict(title='Hawkishness Score', gridcolor='#f0f0f0', 
               zeroline=True, zerolinecolor='#ccc', zerolinewidth=2,
               tickvals=[-2,-1,0,1,2],
               ticktext=['Aggressive ease','Ease','Neutral','Tighten','Aggressive tighten']),
    margin=dict(t=40, b=60, l=120, r=20),
)

st.plotly_chart(fig, use_container_width=True)

# ── CLASSIFICATION BREAKDOWN ─────────────────────────────────────────────────
st.subheader("Policy Lever Classification")

col1, col2, col3 = st.columns(3)

with col1:
    slope_counts = df['slope'].value_counts()
    fig_s = px.pie(values=slope_counts.values, names=slope_counts.index,
                   title='Slope Changes',
                   color_discrete_map={'maintain':'#457b9d','steepen':'#e63946','flatten':'#2a9d8f'})
    fig_s.update_layout(height=280, margin=dict(t=40,b=0,l=0,r=0))
    st.plotly_chart(fig_s, use_container_width=True)

with col2:
    centring_counts = df['centring'].value_counts()
    fig_c = px.pie(values=centring_counts.values, names=centring_counts.index,
                   title='Centring Changes',
                   color_discrete_map={'maintain':'#457b9d','recentre_up':'#e63946','recentre_down':'#2a9d8f'})
    fig_c.update_layout(height=280, margin=dict(t=40,b=0,l=0,r=0))
    st.plotly_chart(fig_c, use_container_width=True)

with col3:
    width_counts = df['width'].value_counts()
    fig_w = px.pie(values=width_counts.values, names=width_counts.index,
                   title='Width Changes',
                   color_discrete_map={'maintain':'#457b9d','widen':'#e63946','narrow':'#2a9d8f'})
    fig_w.update_layout(height=280, margin=dict(t=40,b=0,l=0,r=0))
    st.plotly_chart(fig_w, use_container_width=True)

# ── FILTER + TABLE ─────────────────────────────────────────────────────────
st.subheader("Browse All Statements")

col1, col2, col3 = st.columns(3)
with col1:
    stance_filter = st.multiselect('Stance', ['tighten','neutral','ease'], default=['tighten','neutral','ease'])
with col2:
    year_range = st.slider('Year range', 2001, 2026, (2001, 2026))
with col3:
    slope_filter = st.multiselect('Slope', ['steepen','maintain','flatten'], default=['steepen','maintain','flatten'])

filtered = df[
    (df['stance'].isin(stance_filter)) &
    (df['year'] >= year_range[0]) &
    (df['year'] <= year_range[1]) &
    (df['slope'].isin(slope_filter))
][['date','slope','width','centring','stance','score','note']]

st.dataframe(
    filtered.rename(columns={
        'date':'Date','slope':'Slope','width':'Width',
        'centring':'Centring','stance':'Stance',
        'score':'Score','note':'Key Note'
    }),
    use_container_width=True,
    height=300
)

# ── DOWNLOAD ─────────────────────────────────────────────────────────────────
st.markdown("---")
col1, col2 = st.columns([1,3])
with col1:
    csv = df.to_csv(index=False)
    st.download_button(
        label="📥 Download Full Dataset (CSV)",
        data=csv,
        file_name="mas_policy_stance_gokhale2026.csv",
        mime="text/csv"
    )
with col2:
    st.caption("Dataset compiled by Anuja A. Gokhale (NUS Merit Scholar) from MAS Monetary Policy Statements 2001–2026. "
               "Classification methodology: slope (steepen/maintain/flatten), width (widen/maintain/narrow), "
               "centring (recentre_up/maintain/recentre_down). Hawkishness score: weighted sum of lever changes (-2 to +2). "
               "Research: ssrn.com/abstract=6514338")
