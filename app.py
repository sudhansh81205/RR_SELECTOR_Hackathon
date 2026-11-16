import os
import sys
import streamlit as st
import pandas as pd
import numpy as np

# Set page configuration
st.set_page_config(
    page_title="Rajasthan Royals | SupeRR Selector War Room",
    page_icon="👑",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Colors
RR_PINK = "#E73895"
RR_BLUE = "#0C2340"
GOLD = "#F59E0B"

# Custom CSS
st.markdown(f"""
<style>
    .main {{
        background-color: #f8fafc;
    }}
    .rr-header {{
        background: linear-gradient(135deg, {RR_PINK} 0%, {RR_BLUE} 100%);
        color: white;
        padding: 30px;
        border-radius: 12px;
        margin-bottom: 25px;
        box-shadow: 0 4px 15px rgba(231, 56, 149, 0.2);
    }}
    .metric-card {{
        background: white;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid {RR_PINK};
        box-shadow: 0 2px 8px rgba(0,0,0,0.06);
    }}
    .badge {{
        background-color: {RR_PINK};
        color: white;
        padding: 4px 10px;
        border-radius: 12px;
        font-size: 12px;
        font-weight: 700;
    }}
</style>
""", unsafe_allow_html=True)

# Data paths
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUTPUT_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'outputs')

@st.cache_data
def load_rankings():
    bat_file = os.path.join(OUTPUT_DIR, 'calibrated_top_batters.csv')
    bowl_file = os.path.join(OUTPUT_DIR, 'calibrated_top_bowlers.csv')
    bat_df = pd.read_csv(bat_file)
    bowl_df = pd.read_csv(bowl_file)
    return bat_df, bowl_df

bat_df, bowl_df = load_rankings()

# Header
st.markdown(f"""
<div class="rr-header">
    <div style="display:flex; justify-content:space-between; align-items:center;">
        <div>
            <span class="badge">Rajasthan Royals Proprietary Analytics</span>
            <h1 style="margin: 10px 0 5px 0; font-size: 34px; font-weight: 800;">SupeRR Selector Season 2: War Room Dashboard</h1>
            <p style="margin: 0; font-size: 16px; opacity: 0.9;">Identifying the Most Reliable Players Under Pressure for the IPL 2027 Auction</p>
        </div>
        <div style="font-size: 55px;">👑</div>
    </div>
</div>
""", unsafe_allow_html=True)

# Sidebar
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/5/5c/Rajasthan_Royals_Logo.svg/240px-Rajasthan_Royals_Logo.svg.png", width=120)
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Go to",
    ["🏆 Official Top 10 Picks", "🎯 RR IPL 2027 Auction Targets", "📊 Head-to-Head Comparison", "⚡ Live Pressure Simulator", "📑 Methodology & Formulas"]
)

st.sidebar.markdown("---")
st.sidebar.markdown("### Model Parameters")
st.sidebar.markdown("- **Dataset:** 200,999 Deliveries (2022–2026)")
st.sidebar.markdown("- **High Pressure Threshold:** CPI ≥ 0.28")
st.sidebar.markdown("- **Par Framework:** Format-Calibrated Par (FCCP)")

# -------------------------------------------------------------
# TAB 1: Official Top 10 Picks
# -------------------------------------------------------------
if menu == "🏆 Official Top 10 Picks":
    st.subheader("Official Top 10 Ranked Players (Round 1 Submission)")
    st.markdown("These ranked lists represent the official selections for the Unstop dropdown fields, backed by our calibrated machine learning pressure model.")
    
    col1, col2 = st.columns(2)
    with col1:
        st.markdown("### 🏏 Top 10 Batters Under Pressure")
        top10_bat = bat_df.head(10)[['rank', 'striker_name', 'rating', 'hp_balls', 'sr_hp', 'sr_lift_vs_par', 'delta_sr', 'rpd_hp', 'boundary_pct_hp', 'hp_matches']]
        top10_bat.columns = ['Rank', 'Player Name', 'Rating', 'Pressure Balls', 'Pressure SR', 'SR Lift vs Par', 'Delta SR', 'Avg/RPD', 'Boundary %', 'Matches']
        st.dataframe(
            top10_bat.style.format({
                'Rating': '{:.1f}',
                'Pressure SR': '{:.1f}',
                'SR Lift vs Par': '+{:.1f}',
                'Delta SR': '+{:.1f}',
                'Avg/RPD': '{:.1f}',
                'Boundary %': '{:.1f}%'
            }).background_gradient(subset=['Rating'], cmap='Greens'),
            use_container_width=True,
            hide_index=True
        )
    
    with col2:
        st.markdown("### 🎯 Top 10 Bowlers Under Pressure")
        top10_bowl = bowl_df.head(10)[['rank', 'bowler_name', 'rating', 'hp_balls', 'econ_hp', 'econ_suppression_vs_par', 'bsr_hp', 'dot_pct_hp', 'bndry_pct_hp', 'hp_matches']]
        top10_bowl.columns = ['Rank', 'Player Name', 'Rating', 'Pressure Balls', 'Pressure Econ', 'Runs Saved/Over', 'Balls/Wkt', 'Dot %', 'Boundary %', 'Matches']
        st.dataframe(
            top10_bowl.style.format({
                'Rating': '{:.1f}',
                'Pressure Econ': '{:.2f}',
                'Runs Saved/Over': '+{:.2f}',
                'Balls/Wkt': '{:.1f}',
                'Dot %': '{:.1f}%',
                'Boundary %': '{:.1f}%'
            }).background_gradient(subset=['Rating'], cmap='Greens'),
            use_container_width=True,
            hide_index=True
        )

# -------------------------------------------------------------
# TAB 2: RR IPL 2027 Auction Targets
# -------------------------------------------------------------
elif menu == "🎯 RR IPL 2027 Auction Targets":
    st.subheader("Rajasthan Royals IPL 2027 Auction Strategy & Squad Fit")
    st.markdown("How each identified clutch match-winner directly solves Rajasthan Royals' squad vulnerabilities at the Sawai Mansingh Stadium and across high-pressure tournament knockout matches.")
    
    tab_bat, tab_bowl = st.tabs(["Batting Reinforcements", "Bowling Reinforcements"])
    
    with tab_bat:
        st.markdown("#### High-Priority Batting Targets for RR (Middle-Order Crunch & Finishing)")
        
        recs_bat = [
            {
                "name": "Shashank Singh",
                "role": "Crisis Anchor & Death Finisher (Middle-Order #5 / #6)",
                "metrics": "Pressure SR: 174.3 | Pressure Avg: 48.4 | SR Lift: +26.5 | 222 Pressure Balls",
                "fit": "Direct solution to RR's lower-middle order stability. In games where Samson and Jaiswal fall early, Shashank delivers a 48.4 average under severe pressure, rescuing chases without stalling run rates."
            },
            {
                "name": "Rinku Singh",
                "role": "Premier Left-Handed Finisher (#5 / #6)",
                "metrics": "Pressure SR: 188.0 | Delta SR: +62.0 | 418 Pressure Balls in 50 Matches",
                "fit": "The ultimate clutch finisher in modern Indian cricket. Elevates strike rate by an astounding +62.0 points under pressure. Combines seamlessly with Dhruv Jurel and Shimron Hetmyer to build an impenetrable death-overs blitz."
            },
            {
                "name": "Naman Dhir",
                "role": "High-Impact Indian Power-Hitter & Off-Spin Option (#4 / #5)",
                "metrics": "Pressure SR: 192.6 | SR Lift: +44.3 | 30.4% Boundaries | 148 Pressure Balls",
                "fit": "Versatile young Indian batter who takes down high-pressure bowling immediately without needing dot-ball sighters (192.6 SR). Flexible across overs 7 to 20 and adds defensive bowling utility."
            },
            {
                "name": "Phil Salt",
                "role": "Explosive Keeper-Opener (Overseas Backup / Powerplay Dominator)",
                "metrics": "Pressure SR: 189.7 | SR Lift: +49.6 | 27.2% Dot Ball %",
                "fit": "If Jos Buttler faces overseas scheduling conflicts, Salt provides uninterrupted high-tempo powerplay execution and ruthless chase pacing."
            }
        ]
        
        for r in recs_bat:
            with st.expander(f"⭐ **{r['name']}** — {r['role']}", expanded=True):
                st.markdown(f"**Key Pressure Evidence:** `{r['metrics']}`")
                st.markdown(f"**Royals Tactical Fit:** {r['fit']}")

    with tab_bowl:
        st.markdown("#### High-Priority Bowling Targets for RR (Death Overs & Sawai Mansingh Spin Control)")
        
        recs_bowl = [
            {
                "name": "Matheesha Pathirana",
                "role": "Primary Death-Over Wicket Specialist (Overs 17, 19, 20)",
                "metrics": "Pressure Econ: 8.15 (vs Par 9.33) | Balls/Wicket: 9.2 | 421 Pressure Balls",
                "fit": "The single most lethal death-over weapon available in franchise cricket. Striking at 9.15 balls per wicket under pressure solves RR's recurring dilemma of closing tight games at Jaipur."
            },
            {
                "name": "Maheesh Theekshana",
                "role": "Mystery Powerplay & Middle-Overs Strangle",
                "metrics": "Pressure Econ: 6.91 (vs Par 8.62) | Runs Saved/Over: +1.71 | 358 Pressure Balls",
                "fit": "Excels on Jaipur's expansive boundaries. Controls both the powerplay and the 16th/17th over surge with low boundary concession (11.7%) and carrom-ball variations."
            },
            {
                "name": "Kuldeep Yadav",
                "role": "Elite Attacking Left-Arm Wrist Spin",
                "metrics": "Pressure Econ: 6.84 (vs Par 8.30) | Balls/Wkt: 12.6 | 364 Pressure Balls",
                "fit": "Wicket-taking wrist spin in high-leverage middle overs. Paired with Sandeep Sharma's accuracy, Kuldeep chokes opposition acceleration during middle-over collapses."
            },
            {
                "name": "Umran Malik",
                "role": "Express Pace & Middle-Overs Enforcer (150+ km/h)",
                "metrics": "Pressure Balls/Wkt: 9.6 | Dot Ball %: 53.0% | 164 Pressure Balls",
                "fit": "High-upside Indian pacer who creates genuine physical pressure. Bowling at 53.0% dot balls under pressure at 150+ km/h breaks partnerships when games drift."
            }
        ]
        
        for r in recs_bowl:
            with st.expander(f"⭐ **{r['name']}** — {r['role']}", expanded=True):
                st.markdown(f"**Key Pressure Evidence:** `{r['metrics']}`")
                st.markdown(f"**Royals Tactical Fit:** {r['fit']}")

# -------------------------------------------------------------
# TAB 3: Head-to-Head Comparison
# -------------------------------------------------------------
elif menu == "📊 Head-to-Head Comparison":
    st.subheader("Player Pressure Metric Explorer & Comparison")
    
    category = st.radio("Select Category", ["Batters", "Bowlers"], horizontal=True)
    
    if category == "Batters":
        p1 = st.selectbox("Select Player 1", bat_df['striker_name'].tolist(), index=1)
        p2 = st.selectbox("Select Player 2", bat_df['striker_name'].tolist(), index=2)
        
        row1 = bat_df[bat_df['striker_name'] == p1].iloc[0]
        row2 = bat_df[bat_df['striker_name'] == p2].iloc[0]
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"### {p1} (Rank #{int(row1['rank'])})")
            st.metric("SupeRR Rating", f"{row1['rating']:.1f}")
            st.metric("Pressure Strike Rate", f"{row1['sr_hp']:.1f}", f"+{row1['sr_lift_vs_par']:.1f} vs Par")
            st.metric("Delta vs Baseline", f"+{row1['delta_sr']:.1f}")
            st.metric("Runs Per Dismissal", f"{row1['rpd_hp']:.1f}")
            st.metric("Boundary %", f"{row1['boundary_pct_hp']:.1f}%")
        with c2:
            st.markdown(f"### {p2} (Rank #{int(row2['rank'])})")
            st.metric("SupeRR Rating", f"{row2['rating']:.1f}")
            st.metric("Pressure Strike Rate", f"{row2['sr_hp']:.1f}", f"+{row2['sr_lift_vs_par']:.1f} vs Par")
            st.metric("Delta vs Baseline", f"+{row2['delta_sr']:.1f}")
            st.metric("Runs Per Dismissal", f"{row2['rpd_hp']:.1f}")
            st.metric("Boundary %", f"{row2['boundary_pct_hp']:.1f}%")

    else:
        p1 = st.selectbox("Select Bowler 1", bowl_df['bowler_name'].tolist(), index=1)
        p2 = st.selectbox("Select Bowler 2", bowl_df['bowler_name'].tolist(), index=2)
        
        row1 = bowl_df[bowl_df['bowler_name'] == p1].iloc[0]
        row2 = bowl_df[bowl_df['bowler_name'] == p2].iloc[0]
        
        c1, c2 = st.columns(2)
        with c1:
            st.markdown(f"### {p1} (Rank #{int(row1['rank'])})")
            st.metric("SupeRR Rating", f"{row1['rating']:.1f}")
            st.metric("Pressure Economy", f"{row1['econ_hp']:.2f}", f"-{row1['econ_suppression_vs_par']:.2f} Saved/Ov")
            st.metric("Balls / Wicket", f"{row1['bsr_hp']:.1f}")
            st.metric("Dot Ball %", f"{row1['dot_pct_hp']:.1f}%")
            st.metric("Boundary Conceded %", f"{row1['bndry_pct_hp']:.1f}%")
        with c2:
            st.markdown(f"### {p2} (Rank #{int(row2['rank'])})")
            st.metric("SupeRR Rating", f"{row2['rating']:.1f}")
            st.metric("Pressure Economy", f"{row2['econ_hp']:.2f}", f"-{row2['econ_suppression_vs_par']:.2f} Saved/Ov")
            st.metric("Balls / Wicket", f"{row2['bsr_hp']:.1f}")
            st.metric("Dot Ball %", f"{row2['dot_pct_hp']:.1f}%")
            st.metric("Boundary Conceded %", f"{row2['bndry_pct_hp']:.1f}%")

# -------------------------------------------------------------
# TAB 4: Live Pressure Simulator
# -------------------------------------------------------------
elif menu == "⚡ Live Pressure Simulator":
    st.subheader("Interactive Match State & Cricket Pressure Index (CPI) Simulator")
    st.markdown("Adjust the live match variables to simulate how the trained machine learning model calculates **Win Probability**, **Leverage Index**, and the composite **Cricket Pressure Index (CPI)**.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        inn = st.radio("Innings", [2, 1], horizontal=True, format_func=lambda x: "Innings 2 (Chasing)" if x == 2 else "Innings 1 (Target Setting)")
        over = st.slider("Current Over", 1, 20, 18)
        balls_rem = (20 - over + 1) * 6
        st.write(f"Balls Remaining: **{balls_rem}**")
        
        if inn == 2:
            runs_needed = st.slider("Runs Needed to Win", 1, 100, 36)
            wkts_lost = st.slider("Wickets Lost", 0, 9, 5)
            target = st.number_input("Target Total", 120, 260, 185)
            rrr = (runs_needed / (balls_rem / 6.0)) if balls_rem > 0 else 36.0
            st.write(f"Required Run Rate (RRR): **{rrr:.2f} RPO**")
        else:
            current_score = st.slider("Current Score", 10, 220, 155)
            wkts_lost = st.slider("Wickets Lost", 0, 9, 4)
            is_ko = st.checkbox("Knockout / Playoff Match Stage", value=True)

    with col_b:
        st.markdown("### Simulated Pressure Calculation")
        if inn == 2:
            # Approximate ML Win Prob curve for illustration
            z = -0.06 * runs_needed + 0.05 * balls_rem - 0.35 * wkts_lost + 0.15 * (target / 20.0)
            wp = 1.0 / (1.0 + np.exp(-z))
            uncert = 4.0 * wp * (1.0 - wp)
            leverage = uncert * (0.4 + 0.6 * (120.0 - balls_rem) / 120.0)
            stress_rrr = np.clip((rrr - 7.5) / 10.0, 0.0, 1.0)
            stress_wkt = np.clip((wkts_lost - 4.0) / 5.0, 0.0, 1.0)
            chase_stress = 0.50 * stress_rrr + 0.30 * stress_wkt + 0.20 * (1.0 if balls_rem <= 36 else 0.0)
            cpi = float(np.clip(0.50 * leverage + 0.40 * chase_stress + 0.10 * 1.0, 0.0, 1.0))
            
            st.metric("Estimated Chasing Win Probability", f"{wp*100:.1f}%")
            st.metric("Win Probability Uncertainty (U)", f"{uncert:.3f}")
            st.metric("Leverage Index (LI)", f"{leverage:.3f}")
            st.markdown(f"### **Cricket Pressure Index (CPI): `{cpi:.3f}`**")
            if cpi >= 0.28:
                st.error("🚨 HIGH PRESSURE SITUATION (CPI ≥ 0.28) — Clutch Execution Required")
            else:
                st.success("🟢 Standard / Moderate Pressure Situation")
        else:
            stress_death = float(np.where(over >= 16, (over - 15) / 5.0, 0.0))
            stress_collapse = float(np.clip((wkts_lost - (over * 0.35 + 0.5)) / 3.0, 0.0, 1.0))
            cpi = float(np.clip(0.45 * stress_death + 0.35 * stress_collapse + 0.10 * 0.2 + 0.10 * (1.0 if is_ko else 0.0), 0.0, 1.0))
            st.metric("Death Phase Stress", f"{stress_death:.2f}")
            st.metric("Collapse Crisis Stress", f"{stress_collapse:.2f}")
            st.markdown(f"### **Cricket Pressure Index (CPI): `{cpi:.3f}`**")
            if cpi >= 0.28:
                st.error("🚨 HIGH PRESSURE SITUATION (CPI ≥ 0.28)")
            else:
                st.success("🟢 Standard / Moderate Pressure Situation")

# -------------------------------------------------------------
# TAB 5: Methodology & Formulas
# -------------------------------------------------------------
elif menu == "📑 Methodology & Formulas":
    st.subheader("Mathematical Methodology & Engineering Details")
    st.markdown("""
    ### 1. The Multi-Dimensional Pressure Index (CPI)
    Every delivery in the 200,999-ball dataset is assigned a continuous score $CPI in [0, 1]$:
    - **Innings 2:** $CPI = 0.50 \cdot LI + 0.40 \cdot S_{\text{chase}} + 0.10 \cdot \text{Knockout}$
    - **Innings 1:** $CPI = 0.45 \cdot S_{\text{death}} + 0.35 \cdot S_{\text{collapse}} + 0.10 \cdot \text{ParDeficit} + 0.10 \cdot \text{Knockout}$
    - **Super Overs:** $CPI = 1.0$ (Maximum Stress)

    ### 2. Format-Calibrated Contextual Par (FCCP)
    To resolve the **Baseline Distortion Paradox** (where death bowlers are unfairly compared to their own low-leverage overs, and IPL matches average 9.95 RPO vs T20Is at 9.08 RPO):
    - Par benchmark computed by `(is_ipl, innings, overid, is_high_pressure)`.
    - **Runs Saved / Over** = $Econ_{\text{par}} - Econ_{\text{observed}}$.
    - **Strike Rate Lift** = $SR_{\text{observed}} - SR_{\text{par}}$.

    ### 3. Empirical Bayes Shrinkage
   st.markdown(
    r"""
    All rates are regularized with prior weight $K = 50$ balls
    to protect against small-sample noise:
    """
)

st.latex(
    r"\text{Shrunk Rate} = "
    r"\frac{N_{\text{balls}}\cdot \text{Observed} + "
    r"K\cdot \text{LeaguePar}}{N_{\text{balls}}+K}"
))
