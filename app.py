import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import numpy as np

# Słownik tłumaczeń (PL / EN)
TRANSLATIONS = {
    "PL": {
        
        
        "league_header": "Zaawansowany Dashboard Analityczny",
        "league_caption": "Dashboard analityczny oparty na danych meczowych FotMob • Sezon 2026/2027",
        "choose_league": "Wybierz ligę do analizy:",
        "tab_general": "📋 Statystyki Ogólne",
        "tab_offense": "⚽ Statystyki Ofensywne", 
        "tab_defense": "🛡️ Statystyki Defensywne",
        "tab_passing": "🎯 Dystrybucja i Podania",
        "tab_teams": "Statystyki Drużyn",
        "tab_radar": "🎯 Profil Drużyny (Radar)", 
        "tab_h2h": "⚔️ Porównanie Zespołów", 
        "tab_insights": "🔬 Zależności",
        "tab_scatter": "📈 Analiza xG vs xGA",
        
        # Moduły Ogólne
        "gen_select": "🔎 Wybierz moduł tabeli ligowej:",
        "gen_opt1": "Tabela Realna vs Tabela xG",
        "gen_opt2": "Mecze u Siebie vs Mecze na Wyjeździe",
        "gen_opt3": "Pełna Tabela Zbiorcza (Metryki zaawansowane)",

        # Moduły Ataku
        "att_select": "Wybierz moduł analizy ofensywnej:",
        "att_opt1": "Tabela Główna Ofensywy",
        "att_opt2": "Ogólne xG na mecz (Total xG)",
        "att_opt3": "xG z gry otwartej (xG Open Play)",
        "att_opt4": "xG ze stałych fragmentów (xG Set Play)",
        "att_opt5": "xG bez rzutów karnych (npxG)",
        "att_opt6": "Jakość celnych strzałów (xGOT)",
        "att_opt7": "Jakość prób: xG na jeden strzał (xG / Shot)",
        "att_opt8": "Efektywność xG: Ile xG na gola? (xG / Goal)",
        "att_opt9": "Skuteczność: Ile celnych strzałów na gola? (SoT / Goal)",
        "att_opt10": "Bilans: Gole - xG (Over/Underperformance)",
        "att_opt11": "Strzały z pola karnego (Shots inside box)",
        "att_opt12": "Strzały zza pola karnego (Shots outside box)",
        "att_opt13": "Rozkład xG: Open Play vs Set Play",
        "att_opt14": "Celność strzałów (Shot Accuracy %)",
        "att_opt15": "Analiza Big Chances i Symulacja Tabeli",
        "att_opt16": "Matryca Skuteczności: xG vs xG na gola",
        "att_opt17": "Relacja xG vs xGOT (Jakość kreacji vs Strzału)",
        "att_opt18": "Efektywność w szesnastce: Kontakty vs Strzały",
        "att_opt19": "Strzały potrzebne na gola",
        "att_opt20": "xGOT vs Bramki zdobyte (Over/Underperformance)",
        "def_select": "🛡️ Wybierz moduł analizy defensywnej:",
    "def_opt1": "Tabela Główna Defensywy",
    "def_opt2": "1. Ogólne xGA na mecz (Dopuszczona jakość szans)",
    "def_opt3": "2. xGA z gry otwartej (Open Play xGA)",
    "def_opt4": "3. xGA ze stałych fragmentów (Set Play xGA)",
    "def_opt5": "4. xGA bez rzutów karnych (npxGA)",
    "def_opt6": "5. Jakość celnych strzałów rywala (xAGOT)",
    "def_opt7": "6. Jakość szans rywala: xGA na jeden strzał (xGA / Shot Against)",
    "def_opt8": "7. Odporność: Ile xGA potrzeba, by strzelić nam gola? (xGA / Goal Conceded)",
    "def_opt9": "8. Ile celnych strzałów rywala na gola straconego? (SoT Against / Goal)",
    "def_opt10": "9. Bilans: Gole Stracone - xGA (Defensive Over/Underperformance)",
    "def_opt11": "10. Strzały dopuszczone z pola karnego (Shots inside box against)",
    "def_opt12": "11. Strzały dopuszczone zza pola karnego (Shots outside box against)",
    "def_opt13": "12. Rozkład xGA: Open Play vs Set Play",
    "def_opt14": "13. Celność strzałów rywali (Opponent Shot Accuracy %)",
    "def_opt15": "14. Dopuszczone Wielkie Szanse (Big Chances Conceded)",
    "def_opt16": "Matryca Odporności: xGA vs xGA na gola straconego",
    "def_opt17": "Relacja xGA vs xAGOT (Dopuszczona kreacja vs Jakość strzałów)",
    "def_opt18": "Efektywność w szesnastce: Kontakty rywala vs Strzały rywala",
    "def_opt19": "Strzały rywali potrzebne na zdobycie bramki",
    "def_opt20": "xAGOT vs Bramki Stracone (Goals Prevented / Bramkarz)",

    "pass_select": "Wybierz perspektywę analityczną:",
    "pass_opt1": "1. Tabela Zbiorcza Dystrybucji (Własne vs Przeciwko)",
    "pass_opt2": "2. Średnie Posiadanie Piłki (% Kontroli meczu)",
    "pass_opt3": "3. Liczba Podań Ogółem (Własne vs Dopuszczone rywalom)",
    "pass_opt4": "4. Budowanie akcji: Podania na własnej połowie",
    "pass_opt5": "5. Dominacja terytorialna: Podania na połowie przeciwnika",
    "pass_opt6": "6. Bezpośredni styl gry: Zagrywane długie piłki (Long Balls)",
    "pass_opt7": "7. Efektywność rozegrania: Co ile podań pada gol? (Passes per Goal)",
    "pass_opt8": "8. Matryca Kontroli: Podania na połowie rywala vs Podania rywala u nas",
    "pass_opt9": "9. Profil Drużyny: Wykres mecz po meczu (Własne vs Rywal)",
       



        # Etykiety ogólne
        "shots_needed_goal": "Liczba oddanych strzałów potrzebna do zdobycia 1 bramki",
        "shots_per_1_goal": "Liczba strzałów / 1 gol",
        "league_avg": "Średnia ligowa",
        "matches": "M",
        "team": "Drużyna"
    },
    "EN": {
        "league_header": "Advanced Analytics Dashboard",
        "league_caption": "Analytical dashboard powered by FotMob match data • Season 2026/2027",
        "choose_league": "Select league for analysis:",
        "tab_general": "📋 General Standings",
        "tab_offense": "⚽ Offensive Stats", 
        "tab_defense": "🛡️ Defensive Stats",
        "tab_passing": "🎯 Passing & Distribution",
        "tab_teams": "Team Profiles",
        "tab_radar": "🎯 Team Radar Profile", 
        "tab_h2h": "⚔️ Head-to-Head", 
        "tab_insights": "🔬 Insights & Correlations",
        "tab_scatter": "📈 xG vs xGA Map",

        # Moduły Ogólne
        "gen_select": "🔎 Select league table module:",
        "gen_opt1": "Real Table vs xG Table",
        "gen_opt2": "Home vs Away Form",
        "gen_opt3": "Full Table (Advanced Metrics)",

        # Moduły Ataku
        "att_select": "Select offensive analysis view:",
        "att_opt1": "Main Attack Table",
        "att_opt2": "Total Expected Goals (xG / 90)",
        "att_opt3": "Open Play Expected Goals (xG OP)",
        "att_opt4": "Set Piece Expected Goals (xG SP)",
        "att_opt5": "Non-Penalty Expected Goals (npxG)",
        "att_opt6": "Post-Shot Expected Goals (xGOT)",
        "att_opt7": "Shot Quality: xG per Shot",
        "att_opt8": "Finishing Cost: xG Needed per Goal",
        "att_opt9": "Precision: Shots on Target per Goal",
        "att_opt10": "Over/Underperformance: Goals - xG",
        "att_opt11": "Shots Inside Penalty Box",
        "att_opt12": "Shots Outside Box (Long Range)",
        "att_opt13": "xG Breakdown: Open Play vs Set Play",
        "att_opt14": "Shot Accuracy (%)",
        "att_opt15": "Big Chances Analysis & Alternate Table",
        "att_opt16": "Efficiency Matrix: xG vs xG per Goal",
        "att_opt17": "xG vs xGOT (Shot Creation vs Execution)",
        "att_opt18": "Box Efficiency: Touches vs Shots",
        "att_opt19": "Shots Needed per Goal",
        "att_opt20": "xGOT vs Real Goals Scored",
        "def_select": "🛡️ Select defensive analysis module:",
    "def_opt1": "Main Defensive Table",
    "def_opt2": "1. Total Expected Goals Against (xGA / 90)",
    "def_opt3": "2. Open Play xGA (Open Play xGA)",
    "def_opt4": "3. Set Play xGA (Set Play xGA)",
    "def_opt5": "4. Non-Penalty xGA (npxGA)",
    "def_opt6": "5. Opponent Shot Quality on Target (xAGOT)",
    "def_opt7": "6. Opponent Shot Quality: xGA per Shot Against",
    "def_opt8": "7. Resilience: xGA Needed per Goal Conceded",
    "def_opt9": "8. Opponent Shots on Target per Goal Conceded",
    "def_opt10": "9. Goals Conceded - xGA (Defensive Over/Under)",
    "def_opt11": "10. Shots Conceded Inside Penalty Box",
    "def_opt12": "11. Shots Conceded Outside Box (Long Range)",
    "def_opt13": "12. xGA Breakdown: Open Play vs Set Play",
    "def_opt14": "13. Opponent Shot Accuracy (%)",
    "def_opt15": "14. Big Chances Conceded / 90",
    "def_opt16": "Resilience Matrix: xGA vs xGA per Goal Conceded",
    "def_opt17": "xGA vs xAGOT (Chances Conceded vs Shot Execution)",
    "def_opt18": "Box Control: Opponent Touches vs Opponent Shots",
    "def_opt19": "Opponent Shots Needed to Score",
    "def_opt20": "xAGOT vs Goals Conceded (Goalkeeper Goals Prevented)",

    "pass_select": "Select distribution perspective:",
    "pass_opt1": "1. Full Distribution Table (For vs Against)",
    "pass_opt2": "2. Average Ball Possession (%)",
    "pass_opt3": "3. Total Passes Volume (For vs Conceded)",
    "pass_opt4": "4. Build-up Phase: Passes in Own Half",
    "pass_opt5": "5. Territorial Control: Passes in Opponent Half",
    "pass_opt6": "6. Direct Play: Accurate Long Balls",
    "pass_opt7": "7. Passing Efficiency: Passes per Goal (PpG)",
    "pass_opt8": "8. Control Matrix: Passes in Opp Half vs Conceded at Home",
    "pass_opt9": "9. Match-by-Match Passing Profile (Team vs Opponent)",




        # Etykiety ogólne
        "shots_needed_goal": "Shots Needed to Score 1 Goal",
        "shots_per_1_goal": "Shots / 1 Goal",
        "league_avg": "League Average",
        "matches": "MP",
        "team": "Team"
    }
}

st.set_page_config(page_title="Ekstraklasa Team Analytics", layout="wide")

@st.cache_data
def load_and_process_team_data(file_path="Ekstraklasa 2026-2027.xlsx"):
    df = pd.read_excel(file_path)
    df.columns = [str(c).strip() for c in df.columns]
    
    def get_col(row, *candidates):
        for c in candidates:
            if c in row and pd.notna(row[c]):
                val = row[c]
                if isinstance(val, str) and val.strip().lower() in ["none", "-", ""]:
                    return 0.0
                try:
                    return float(val)
                except (ValueError, TypeError):
                    return 0.0
        for col_name in row.index:
            col_lower = str(col_name).lower()
            for cand in candidates:
                if cand.lower() in col_lower and pd.notna(row[col_name]):
                    val = row[col_name]
                    if isinstance(val, str) and val.strip().lower() in ["none", "-", ""]:
                        return 0.0
                    try:
                        return float(val)
                    except (ValueError, TypeError):
                        return 0.0
        return 0.0

    records = []
    for _, row in df.iterrows():
        pts_h = 3 if row["home_goals"] > row["away_goals"] else (1 if row["home_goals"] == row["away_goals"] else 0)
        pts_a = 3 if row["away_goals"] > row["home_goals"] else (1 if row["away_goals"] == row["home_goals"] else 0)

        xg_h = get_col(row, "Expected goals (xG) home")
        xg_a = get_col(row, "Expected goals (xG) away")
        xg_op_h = get_col(row, "xG open play home")
        xg_op_a = get_col(row, "xG open play away")
        xg_sp_h = get_col(row, "xG set play home")
        xg_sp_a = get_col(row, "xG set play away")
        npxg_h = get_col(row, "xG non-penalty home")
        npxg_a = get_col(row, "xG non-penalty away")
        xgot_h = get_col(row, "xG on target (xGOT) home")
        xgot_a = get_col(row, "xG on target (xGOT) away")

        xpts_h = 3 if xg_h > xg_a else (1 if xg_h == xg_a else 0)
        xpts_a = 3 if xg_a > xg_h else (1 if xg_a == xg_h else 0)

        bcm_h = get_col(row, "Big chances missed home")
        bcm_a = get_col(row, "Big chances missed away")

        poss_h = get_col(row, "Ball possession home")
        poss_a = get_col(row, "Ball possession away")

        p_own_h = get_col(row, "Own half home")
        p_own_a = get_col(row, "Own half away")
        p_opp_h = get_col(row, "Opposition half home")
        p_opp_a = get_col(row, "Opposition half away")
        
        shots_off_h = get_col(row, "Shots off target home")
        shots_off_a = get_col(row, "Shots off target away")
        blocked_h = get_col(row, "Blocked shots home")
        blocked_a = get_col(row, "Blocked shots away")

        cross_acc_h = get_col(row, "Accurate crosses home")
        cross_acc_a = get_col(row, "Accurate crosses away")
        offsides_h = get_col(row, "Offsides home")
        offsides_a = get_col(row, "Offsides away")

        saves_h = get_col(row, "Keeper saves home")
        saves_a = get_col(row, "Keeper saves away")

        long_h = get_col(row, "Accurate long balls home")
        long_a = get_col(row, "Accurate long balls away")
        box_t_h = get_col(row, "Touches in opposition box home")
        box_t_a = get_col(row, "Touches in opposition box away")

        # W pętli for _, row in df.iterrows():
        shots_h = get_col(row, "Total shots home")
        shots_a = get_col(row, "Total shots away")
        sot_h = get_col(row, "Shots on target home")
        sot_a = get_col(row, "Shots on target away")
        box_s_h = get_col(row, "Shots inside box home")
        box_s_a = get_col(row, "Shots inside box away")
        out_s_h = get_col(row, "Shots outside box home")
        out_s_a = get_col(row, "Shots outside box away")
        bc_h = get_col(row, "Big chances home")
        bc_a = get_col(row, "Big chances away")

        # Nowo dodane metryki z pliku
        blocks_h = get_col(row, "Blocks home")
        blocks_a = get_col(row, "Blocks away")
        clearances_h = get_col(row, "Clearances home")
        clearances_a = get_col(row, "Clearances away")
        fouls_h = get_col(row, "Fouls committed home")
        fouls_a = get_col(row, "Fouls committed away")
        woodwork_h = get_col(row, "Hit woodwork home")
        woodwork_a = get_col(row, "Hit woodwork away")
        dribbles_h = get_col(row, "Successful dribbles home")
        dribbles_a = get_col(row, "Successful dribbles away")
        throws_h = get_col(row, "Throws home")
        throws_a = get_col(row, "Throws away")
        yellows_h = get_col(row, "Yellow cards home")
        yellows_a = get_col(row, "Yellow cards away")
        reds_h = get_col(row, "Red cards home")
        reds_a = get_col(row, "Red cards away")
        duels_tot_h = get_col(row, "Duels home")
        duels_tot_a = get_col(row, "Duels away")

        # Rekord gospodarza (Home)
        records.append({
            "Team": row["home_team"],
            "Opponent": row["away_team"],
            "Venue": "Home",
            "Goals_For": row["home_goals"],
            "Goals_Against": row["away_goals"],
            "xG_For": xg_h, "xG_Against": xg_a,
            "xG_OP_For": xg_op_h, "xG_OP_Against": xg_op_a,
            "xG_SP_For": xg_sp_h, "xG_SP_Against": xg_sp_a,
            "npxG_For": npxg_h, "npxG_Against": npxg_a,
            "xGOT_For": xgot_h, "xGOT_Against": xgot_a,
            "Possession": poss_h,
            "Shots": get_col(row, "Total shots home"),
            "Shots_On_Target": get_col(row, "Shots on target home"),
            "Shots_Off_Target": shots_off_h,
            "Blocked_Shots": blocked_h,
            "Big_Chances": get_col(row, "Big chances home"),
            "Box_Touches": box_t_h,
            "Box_Touches_Against": box_t_a,
            "Box_Shots": get_col(row, "Shots inside box home"),
            "Outside_Box_Shots": get_col(row, "Shots outside box home"),
            "Passes_Total": get_col(row, "Passes home"),
            "Passes_Total_Against": get_col(row, "Passes away"),
            "Passes_Acc": get_col(row, "Accurate passes home"),
            "Passes_Acc_Against": get_col(row, "Accurate passes away"),
            "Corners": get_col(row, "Corners home"),
            "Corners_Against": get_col(row, "Corners away"),
            "Tackles": get_col(row, "Tackles home"),
            "Interceptions": get_col(row, "Interceptions home"),
            "Duels_Won": get_col(row, "Duels won home"),
            "Ground_Duels_Won": get_col(row, "Ground duels won home"),
            "Aerial_Duels_Won": get_col(row, "Aerial duels won home"),
            "Duels_Won_Against": get_col(row, "Duels won away"),
            "Ground_Duels_Won_Against": get_col(row, "Ground duels won away"),
            "Aerial_Duels_Won_Against": get_col(row, "Aerial duels won away"),
            "Long_Balls": long_h,
            "Long_Balls_Against": long_a,
            "Points": pts_h, "xPoints": xpts_h,
            "Big_Chances_Missed": bcm_h, "Opp_BCM": bcm_a,
            "Passes_Own_Half": p_own_h,
            "Passes_Own_Half_Against": p_own_a,
            "Passes_Opp_Half": p_opp_h,
            "Passes_Opp_Half_Against": p_opp_a,
            "Accurate_Crosses": cross_acc_h,
            "Offsides": offsides_h,
            "Keeper_Saves": saves_h,
            "Keeper_Saves_Against": saves_a,
            "Clean_Sheet": 1 if row["away_goals"] == 0 else 0,
            "Shots_Against": shots_a,
            "Shots_On_Target_Against": sot_a,
            "Box_Shots_Against": box_s_a,
            "Outside_Box_Shots_Against": out_s_a,
            "Big_Chances_Against": bc_a,
            "Wygrana": 1 if pts_h == 3 else 0,
            "Blocks": blocks_h, "Blocks_Against": blocks_a,
            "Clearances": clearances_h, "Clearances_Against": clearances_a,
            "Fouls": fouls_h, "Fouls_Against": fouls_a,
            "Hit_Woodwork": woodwork_h, "Hit_Woodwork_Against": woodwork_a,
            "Successful_Dribbles": dribbles_h, "Successful_Dribbles_Against": dribbles_a,
            "Throws": throws_h, "Throws_Against": throws_a,
            "Yellow_Cards": yellows_h, "Yellow_Cards_Against": yellows_a,
            "Red_Cards": reds_h, "Red_Cards_Against": reds_a,
            "Duels_Total": duels_tot_h, "Duels_Total_Against": duels_tot_a,
        })
        
        # Rekord gościa (Away)
        records.append({
            "Team": row["away_team"],
            "Opponent": row["home_team"],
            "Venue": "Away",
            "Goals_For": row["away_goals"],
            "Goals_Against": row["home_goals"],
            "xG_For": xg_a, "xG_Against": xg_h,
            "xG_OP_For": xg_op_a, "xG_OP_Against": xg_op_h,
            "xG_SP_For": xg_sp_a, "xG_SP_Against": xg_sp_h,
            "npxG_For": npxg_a, "npxG_Against": npxg_h,
            "xGOT_For": xgot_a, "xGOT_Against": xgot_h,
            "Possession": poss_a,
            "Shots": get_col(row, "Total shots away"),
            "Shots_On_Target": get_col(row, "Shots on target away"),
            "Shots_Off_Target": shots_off_a,
            "Blocked_Shots": blocked_a,
            "Big_Chances": get_col(row, "Big chances away"),
            "Box_Touches": box_t_a,
            "Box_Touches_Against": box_t_h,
            "Box_Shots": get_col(row, "Shots inside box away"),
            "Outside_Box_Shots": get_col(row, "Shots outside box away"),
            "Passes_Total": get_col(row, "Passes away"),
            "Passes_Total_Against": get_col(row, "Passes home"),
            "Passes_Acc": get_col(row, "Accurate passes away"),
            "Passes_Acc_Against": get_col(row, "Accurate passes home"),
            "Corners": get_col(row, "Corners away"),
            "Corners_Against": get_col(row, "Corners home"),
            "Tackles": get_col(row, "Tackles away"),
            "Interceptions": get_col(row, "Interceptions away"),
            "Duels_Won": get_col(row, "Duels won away"),
            "Ground_Duels_Won": get_col(row, "Ground duels won away"),
            "Aerial_Duels_Won": get_col(row, "Aerial duels won away"),
            "Duels_Won_Against": get_col(row, "Duels won home"),
            "Ground_Duels_Won_Against": get_col(row, "Ground duels won home"),
            "Aerial_Duels_Won_Against": get_col(row, "Aerial duels won home"),
            "Long_Balls": long_a,
            "Long_Balls_Against": long_h,
            "Points": pts_a, "xPoints": xpts_a,
            "Big_Chances_Missed": bcm_a, "Opp_BCM": bcm_h,
            "Passes_Own_Half": p_own_a,
            "Passes_Own_Half_Against": p_own_h,
            "Passes_Opp_Half": p_opp_a,
            "Passes_Opp_Half_Against": p_opp_h,
            "Accurate_Crosses": cross_acc_a,
            "Offsides": offsides_a,
            "Keeper_Saves": saves_a,
            "Keeper_Saves_Against": saves_h,
            "Clean_Sheet": 1 if row["home_goals"] == 0 else 0,
            "Shots_Against": shots_h,
            "Shots_On_Target_Against": sot_h,
            "Box_Shots_Against": box_s_h,
            "Outside_Box_Shots_Against": out_s_h,
            "Big_Chances_Against": bc_h,
            "Wygrana": 1 if pts_a == 3 else 0,
            "Blocks": blocks_a, "Blocks_Against": blocks_h,
            "Clearances": clearances_a, "Clearances_Against": clearances_h,
            "Fouls": fouls_a, "Fouls_Against": fouls_h,
            "Hit_Woodwork": woodwork_a, "Hit_Woodwork_Against": woodwork_h,
            "Successful_Dribbles": dribbles_a, "Successful_Dribbles_Against": dribbles_h,
            "Throws": throws_a, "Throws_Against": throws_h,
            "Yellow_Cards": yellows_a, "Yellow_Cards_Against": yellows_h,
            "Red_Cards": reds_a, "Red_Cards_Against": reds_h,
            "Duels_Total": duels_tot_a, "Duels_Total_Against": duels_tot_h,
        })
        
    matches_df = pd.DataFrame(records)
    
    team_stats = matches_df.groupby("Team").agg(
        Mecze=("Points", "count"),
        Punkty=("Points", "sum"),
        xPunkty=("xPoints", "sum"),
        Gole_Strzelone=("Goals_For", "sum"),
        Gole_Stracone=("Goals_Against", "sum"),
        Gole_na_mecz=("Goals_For", "mean"),
        Gole_stracone_na_mecz=("Goals_Against", "mean"),
        xG_na_mecz=("xG_For", "mean"),
        xGA_na_mecz=("xG_Against", "mean"),
        xG_OP_na_mecz=("xG_OP_For", "mean"),
        xGA_OP_na_mecz=("xG_OP_Against", "mean"),
        xG_SP_na_mecz=("xG_SP_For", "mean"),
        xGA_SP_na_mecz=("xG_SP_Against", "mean"),
        npxG_na_mecz=("npxG_For", "mean"),
        npxGA_na_mecz=("npxG_Against", "mean"),
        xGOT_na_mecz=("xGOT_For", "mean"),
        xAGOT_na_mecz=("xGOT_Against", "mean"),
        xG_Suma=("xG_For", "sum"),
        xGA_Suma=("xG_Against", "sum"),
        xGOT_Suma=("xGOT_For", "sum"),
        Posiadanie=("Possession", "mean"),
        Podania_ogolem=("Passes_Total", "mean"),
        Passes_Total_Sum=("Passes_Total", "sum"),
        Passes_Total_Against_Mean=("Passes_Total_Against", "mean"),
        Passes_Own_Half_Mean=("Passes_Own_Half", "mean"),
        Passes_Own_Half_Sum=("Passes_Own_Half", "sum"),
        Passes_Own_Half_Against_Mean=("Passes_Own_Half_Against", "mean"),
        Passes_Opp_Half_Mean=("Passes_Opp_Half", "mean"),
        Passes_Opp_Half_Sum=("Passes_Opp_Half", "sum"),
        Passes_Opp_Half_Against_Mean=("Passes_Opp_Half_Against", "mean"),
        Podania_celne=("Passes_Acc", "mean"),
        Strzaly_na_mecz=("Shots", "mean"),
        Shots_Sum=("Shots", "sum"),
        Celne_strzaly=("Shots_On_Target", "mean"),
        Shots_On_Target_Sum=("Shots_On_Target", "sum"),
        Shots_Off_Target_Mean=("Shots_Off_Target", "mean"),
        Shots_Off_Target_Sum=("Shots_Off_Target", "sum"),
        Blocked_Shots_Mean=("Blocked_Shots", "mean"),
        Blocked_Shots_Sum=("Blocked_Shots", "sum"),
        Big_Chances=("Big_Chances", "mean"),
        Kontakty_w_polu_karnym=("Box_Touches", "mean"),
        Box_Touches_Mean=("Box_Touches", "mean"),
        Box_Touches_Against_Mean=("Box_Touches_Against", "mean"),
        Strzaly_z_pola_karnego=("Box_Shots", "mean"),
        Rzuty_Rozne=("Corners", "mean"),
        Odbiory=("Tackles", "mean"),
        Przejecia=("Interceptions", "mean"),
        Pojedynki_Wygrane=("Duels_Won", "mean"),
        Big_Chances_Missed=("Big_Chances_Missed", "mean"),
        Big_Chances_Missed_Suma=("Big_Chances_Missed", "sum"),
        Big_Chances_Suma=("Big_Chances", "sum"),
        Possession_Mean=("Possession", "mean"),
        Goals_For_Sum=("Goals_For", "sum"),
        Goals_Against_Sum=("Goals_Against", "sum"),
        Long_Balls_Mean=("Long_Balls", "mean"),
        Long_Balls_Sum=("Long_Balls", "sum"),
        Long_Balls_Against_Mean=("Long_Balls_Against", "mean"),
        Accurate_Crosses_Mean=("Accurate_Crosses", "mean"),
        Accurate_Crosses_Sum=("Accurate_Crosses", "sum"),
        Offsides_Mean=("Offsides", "mean"),
        Offsides_Sum=("Offsides", "sum"),
        Keeper_Saves_Mean=("Keeper_Saves", "mean"),
        Keeper_Saves_Sum=("Keeper_Saves", "sum"),
        Keeper_Saves_Against_Mean=("Keeper_Saves_Against", "mean"),
        Clean_Sheets=("Clean_Sheet", "sum"),
        Shots_Against_Mean=("Shots_Against", "mean"),
        Shots_On_Target_Against_Mean=("Shots_On_Target_Against", "mean"),
        Box_Shots_Against_Mean=("Box_Shots_Against", "mean"),
        Outside_Box_Shots_Against_Mean=("Outside_Box_Shots_Against", "mean"),
        Big_Chances_Against_Mean=("Big_Chances_Against", "mean"),
        Wygrane=("Wygrana", "sum"),
        Win_Rate=("Wygrana", lambda s: round(s.mean() * 100, 1)),
        Clearances_Mean=("Clearances", "mean"),
        Blocks_Mean=("Blocks", "mean"),
        Fouls_Mean=("Fouls", "mean"),
        Fouls_Against_Mean=("Fouls_Against", "mean"),
        Dribbles_Mean=("Successful_Dribbles", "mean"),
        Woodwork_Mean=("Hit_Woodwork", "mean"),
        Woodwork_Sum=("Hit_Woodwork", "sum"),
        Yellow_Cards_Mean=("Yellow_Cards", "mean"),
        Yellow_Cards_Sum=("Yellow_Cards", "sum"),
        Red_Cards_Sum=("Red_Cards", "sum"),
        Throws_Mean=("Throws", "mean"),
        Ground_Duels_Won_Mean=("Ground_Duels_Won", "mean"),
        Aerial_Duels_Won_Mean=("Aerial_Duels_Won", "mean"),
        Corners_Against_Mean=("Corners_Against", "mean"),
        Red_Cards_Mean=("Red_Cards", "mean"),
        
    ).reset_index()
    
    team_stats["Bilans_Bramkowy"] = team_stats["Gole_Strzelone"] - team_stats["Gole_Stracone"]
    team_stats["Bilans_xG"] = team_stats["xG_na_mecz"] - team_stats["xGA_na_mecz"]
    team_stats["Bilans_xG_Suma"] = (team_stats["xG_Suma"] - team_stats["xGA_Suma"]).round(2)
    team_stats["Roznica_Pkt"] = team_stats["Punkty"] - team_stats["xPunkty"]
    team_stats["Strzaly_na_gola"] = (team_stats["Strzaly_na_mecz"] / team_stats["Gole_na_mecz"]).round(2)
    team_stats["Konwersja_proc"] = ((team_stats["Gole_na_mecz"] / team_stats["Strzaly_na_mecz"]) * 100).round(1)
    team_stats["xG_na_strzal"] = (team_stats["xG_na_mecz"] / team_stats["Strzaly_na_mecz"]).round(3)
    team_stats["xG_na_gola"] = team_stats.apply(lambda row: round(row["xG_na_mecz"] / row["Gole_na_mecz"], 2) if row["Gole_na_mecz"] > 0 else 0.0, axis=1)
    team_stats["Odchylenie_xG_gola"] = (1.00 - team_stats["xG_na_gola"]).round(2) 
    team_stats["xGOT_minus_xG"] = (team_stats["xGOT_na_mecz"] - team_stats["xG_na_mecz"]).round(2)
    team_stats["Celne_na_gola"] = team_stats.apply(lambda row: round(row["Celne_strzaly"] / row["Gole_na_mecz"], 2) if row["Gole_na_mecz"] > 0 else 0.0, axis=1)
    team_stats["Gole_minus_xG"] = (team_stats["Gole_Strzelone"] - team_stats["xG_Suma"]).round(2)
    team_stats = team_stats.sort_values(by=["Punkty", "Bilans_Bramkowy", "Gole_Strzelone"], ascending=False).reset_index(drop=True)
    team_stats["Strzaly_zza_pola_karnego"] = (team_stats["Strzaly_na_mecz"] - team_stats["Strzaly_z_pola_karnego"]).round(2)
    team_stats["Celnosc_strzalow_proc"] = ((team_stats["Celne_strzaly"] / team_stats["Strzaly_na_mecz"]) * 100).round(2)
    team_stats["Goals_Prevented_Suma"] = (team_stats["xAGOT_na_mecz"] * team_stats["Mecze"] - team_stats["Gole_Stracone"]).round(2)
    team_stats["Goals_Prevented_Mecz"] = (team_stats["xAGOT_na_mecz"] - team_stats["Gole_stracone_na_mecz"]).round(2)
    team_stats["Clean_Sheets_Pct"] = ((team_stats["Clean_Sheets"] / team_stats["Mecze"]) * 100).round(1)
    team_stats["Saves_per_xGA"] = (team_stats["Keeper_Saves_Mean"] / team_stats["xGA_na_mecz"]).round(2)
    team_stats["xGA_na_strzal_rywala"] = (team_stats["xGA_na_mecz"] / team_stats["Shots_Against_Mean"]).round(3)
    team_stats["xGA_na_gola_straconego"] = team_stats.apply(
        lambda r: round(r["xGA_na_mecz"] / r["Gole_stracone_na_mecz"], 2) if r["Gole_stracone_na_mecz"] > 0 else 0.0, axis=1
    )
    team_stats["Celne_rywala_na_gola"] = team_stats.apply(
        lambda r: round(r["Shots_On_Target_Against_Mean"] / r["Gole_stracone_na_mecz"], 2) if r["Gole_stracone_na_mecz"] > 0 else 0.0, axis=1
    )
    team_stats["Strzaly_rywala_na_gola"] = team_stats.apply(
        lambda r: round(r["Shots_Against_Mean"] / r["Gole_stracone_na_mecz"], 2) if r["Gole_stracone_na_mecz"] > 0 else 0.0, axis=1
    )
    team_stats["Gole_stracone_minus_xGA"] = (team_stats["xGA_Suma"] - team_stats["Gole_Stracone"]).round(2)
    team_stats["Celnosc_strzalow_rywala_proc"] = ((team_stats["Shots_On_Target_Against_Mean"] / team_stats["Shots_Against_Mean"]) * 100).round(2)
    team_stats["xAGOT_minus_xGA"] = (team_stats["xAGOT_na_mecz"] - team_stats["xGA_na_mecz"]).round(2)

    # Wskaźniki podań i posiadania
    team_stats["Possession_Against"] = (100.0 - team_stats["Posiadanie"]).round(1)
    team_stats["Celnosc_podan_proc"] = ((team_stats["Podania_celne"] / team_stats["Podania_ogolem"]) * 100).round(1)
    team_stats["Udzial_podań_atak_proc"] = ((team_stats["Passes_Opp_Half_Mean"] / team_stats["Podania_ogolem"]) * 100).round(1)
    team_stats["Udzial_dlugich_pilek_proc"] = ((team_stats["Long_Balls_Mean"] / team_stats["Podania_ogolem"]) * 100).round(1)
    team_stats["Udzial_dlugich_rywala_proc"] = ((team_stats["Long_Balls_Against_Mean"] / team_stats["Passes_Total_Against_Mean"]) * 100).round(1)
    team_stats["Bilans_Podan"] = (team_stats["Podania_ogolem"] - team_stats["Passes_Total_Against_Mean"]).round(1)
    team_stats["Bilans_Podan_Atak"] = (team_stats["Passes_Opp_Half_Mean"] - team_stats["Passes_Opp_Half_Against_Mean"]).round(1)

    # Efektywność podań: Podania na 1 gola zdobytego oraz straconego
    team_stats["Podania_na_gola"] = team_stats.apply(
        lambda r: round(r["Podania_ogolem"] / r["Gole_na_mecz"], 1) if r["Gole_na_mecz"] > 0 else 0.0, axis=1
    )
    team_stats["Podania_rywala_na_gola"] = team_stats.apply(
        lambda r: round(r["Passes_Total_Against_Mean"] / r["Gole_stracone_na_mecz"], 1) if r["Gole_stracone_na_mecz"] > 0 else 0.0, axis=1
    )

    # Nowa metryka: ile kontaktów w polu karnym przypada na 1 oddany strzał
    team_stats["Kontakty_na_strzal_box"] = team_stats.apply(
        lambda r: round(r["Box_Touches_Mean"] / r["Strzaly_z_pola_karnego"], 2) if r["Strzaly_z_pola_karnego"] > 0 else 0.0, axis=1
    )
    
    return matches_df, team_stats

@st.cache_data
def load_and_process_top5_leagues():
    """Wczytuje i scala dane meczowe ze wszystkich lig Top 5 (bez Ekstraklasy)."""
    top5_files = [
        "Premier League 2026-2027.xlsx",
        "La Liga 26-27.xlsx",
        "Serie A 26-27.xlsx",
        "Bundesliga 26-27.xlsx",
        "Ligue 1 26-27.xlsx",
    ]
    all_matches = []
    all_teams = []
    
    for f in top5_files:
        try:
            m_df, t_df = load_and_process_team_data(f)
            all_matches.append(m_df)
            all_teams.append(t_df)
        except Exception:
            # Zabezpieczenie na wypadek literówki w nazwie któregoś pliku
            continue
            
    combined_matches = pd.concat(all_matches, ignore_index=True)
    combined_teams = pd.concat(all_teams, ignore_index=True)
    
    # Przeliczenie rankingów / sortowania dla połączonej puli drużyn
    combined_teams = combined_teams.sort_values(
        by=["Punkty", "Bilans_Bramkowy", "Gole_Strzelone"], 
        ascending=False
    ).reset_index(drop=True)
    
    return combined_matches, combined_teams


def calculate_team_zscores(df, selected_team, metrics_dict):
    """
    Oblicza Z-Score dla wybranego zespołu względem całej stawki ligowej / europejskiej.
    metrics_dict: słownik {'Wyświetlana Etykieta': 'Nazwa_Kolumny_w_DF'}
    """
    records = []
    team_row = df[df["Team"] == selected_team].iloc[0]
    
    for label, col in metrics_dict.items():
        if col in df.columns:
            mean_val = df[col].mean()
            std_val = df[col].std()
            val = team_row[col]
            
            # Zabezpieczenie przed dzieleniem przez zero
            z_score = (val - mean_val) / std_val if std_val > 0 else 0.0
            
            records.append({
                "Metric": label,
                "Value": val,
                "Mean": mean_val,
                "Z_Score": round(z_score, 2)
            })
            
    return pd.DataFrame(records)




def render_paper_ranking(df, title, value_col, value_header, selected_team=None, format_str="{:.2f}"):
    """Generuje minimalistyczną tabelę rankingową w stylu papierowej karty raportowej."""
    rows_html = ""
    for idx, row in df.reset_index(drop=True).iterrows():
        rank = idx + 1
        team = row["Team"]
        val = row[value_col]
        val_display = format_str.format(val)
        
        is_sel = (selected_team and selected_team != "Wszystkie (Liga)" and team == selected_team)
        
        team_color = "#1D70B8" if is_sel else "#2D241E"
        val_color = "#1D70B8" if is_sel else "#2D241E"
        font_weight = "700" if is_sel else "500"
        border_bottom = "border-bottom: 1px dotted #BDB4A8;" if rank < len(df) else ""
        
        rows_html += (
            f'<tr style="{border_bottom} height: 28px;">'
            f'<td style="width: 35px; padding: 3px 6px; color: {team_color}; font-weight: {font_weight}; text-align: left;">{rank}</td>'
            f'<td style="padding: 3px 6px; color: {team_color}; font-weight: {font_weight}; text-align: left;">{team}</td>'
            f'<td style="width: 100px; padding: 3px 6px; color: {val_color}; font-weight: {font_weight}; text-align: right;">{val_display}</td>'
            f'</tr>'
        )
def render_dark_table_html(df, title, is_xg=False):
    """Renderuje kompaktową tabelę w ciemnym stylu bez podświetleń."""
    lang = st.session_state.get("selected_lang", "PL")
    
    if lang == "EN":
        th_team = "Team"
        th_m = "MP"
        th_w = "xW" if is_xg else "W"
        th_d = "xD" if is_xg else "D"
        th_l = "xL" if is_xg else "L"
        th_goals = "xG" if is_xg else "Goals"
        th_diff = "xGD" if is_xg else "GD"
        th_pts = "xPts" if is_xg else "Pts"
    else:
        th_team = "Drużyna"
        th_m = "M"
        th_w = "xZ" if is_xg else "Z"
        th_d = "xR" if is_xg else "R"
        th_l = "xP" if is_xg else "P"
        th_goals = "xG" if is_xg else "Bramki"
        th_diff = "Bilans"
        th_pts = "xPkt" if is_xg else "Pkt"

    header_cols = f"""
        <th style="width: 24px; text-align: left;">#</th>
        <th style="text-align: left; width: 140px;">{th_team}</th>
        <th style="width: 22px; text-align: center;">{th_m}</th>
        <th style="width: 22px; text-align: center;">{th_w}</th>
        <th style="width: 22px; text-align: center;">{th_d}</th>
        <th style="width: 22px; text-align: center;">{th_l}</th>
        <th style="width: 50px; text-align: center;">{th_goals}</th>
        <th style="width: 35px; text-align: center;">{th_diff}</th>
        <th style="width: 32px; text-align: right;">{th_pts}</th>
    """
    
    rows_html = ""
    for idx, row in df.reset_index(drop=True).iterrows():
        rank = idx + 1
        team = row["Team"]
        m = row["M"]
        z = row["Z"]
        r = row["R"]
        p = row["P"]
        goals_str = f"{row['GF']:.1f}:{row['GA']:.1f}" if is_xg else f"{int(row['GF'])}:{int(row['GA'])}"
        bilans_str = f"{row['Bilans']:+.1f}" if is_xg else f"{int(row['Bilans'])}"
        pkt = int(row["Pkt"])
        
        rows_html += f"""
        <tr style="height: 24px; border-bottom: 1px solid #262b32;">
            <td style="font-weight: 700; color: #FFFFFF; text-align: left;">{rank}</td>
            <td style="font-weight: 600; color: #E2E8F0; text-align: left; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{team}</td>
            <td style="color: #CBD5E1; text-align: center;">{m}</td>
            <td style="color: #CBD5E1; text-align: center;">{z}</td>
            <td style="color: #CBD5E1; text-align: center;">{r}</td>
            <td style="color: #CBD5E1; text-align: center;">{p}</td>
            <td style="color: #94A3B8; text-align: center;">{goals_str}</td>
            <td style="color: #94A3B8; text-align: center;">{bilans_str}</td>
            <td style="font-weight: 700; color: #FFFFFF; text-align: right;">{pkt}</td>
        </tr>
        """
        
    return f"""
    <div style="background-color: #1a1d21; border: 1px solid #2d333b; border-radius: 6px; padding: 14px 18px; margin: 4px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-height: 570px; overflow-y: auto;">
        <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">{title}</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12.5px; line-height: 1.2;">
            <thead>
                <tr style="border-bottom: 2px solid #3b434e; color: #94A3B8; font-size: 11.5px; height: 26px;">
                    {header_cols}
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
        
    return f"""
    <div style="background-color: #1a1d21; border: 1px solid #2d333b; border-radius: 6px; padding: 14px 18px; margin: 4px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        <div style="font-size: 16px; font-weight: 700; color: #FFFFFF; margin-bottom: 10px;">{title}</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12.5px; line-height: 1.2;">
            <thead>
                <tr style="border-bottom: 2px solid #3b434e; color: #94A3B8; font-size: 11.5px; height: 26px;">
                    {header_cols}
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """      
def compute_custom_table(matches_subset, is_xg=False):
    """Oblicza pełne statystyki meczowe dla podzbioru spotkań."""
    records = []
    for team, group in matches_subset.groupby("Team"):
        m = len(group)
        if not is_xg:
            z = sum(group["Goals_For"] > group["Goals_Against"])
            r = sum(group["Goals_For"] == group["Goals_Against"])
            p = sum(group["Goals_For"] < group["Goals_Against"])
            gf = group["Goals_For"].sum()
            ga = group["Goals_Against"].sum()
            pkt = group["Points"].sum()
            bilans = gf - ga
        else:
            z = sum(group["xG_For"] > group["xG_Against"])
            r = sum(group["xG_For"] == group["xG_Against"])
            p = sum(group["xG_For"] < group["xG_Against"])
            gf = group["xG_For"].sum()
            ga = group["xG_Against"].sum()
            pkt = group["xPoints"].sum()
            bilans = gf - ga

        records.append({
            "Team": team, "M": m, "Z": z, "R": r, "P": p,
            "GF": gf, "GA": ga, "Bilans": bilans, "Pkt": pkt
        })
    df_res = pd.DataFrame(records)
    return df_res.sort_values(by=["Pkt", "Bilans", "GF"], ascending=False).reset_index(drop=True)  

    html_code = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body {{
            margin: 0;
            padding: 10px;
            background: transparent;
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
            display: flex;
            justify-content: center;
        }}
        .paper-card {{
            background-color: #FAF7F2;
            width: 100%;
            max-width: 580px;
            padding: 20px 24px;
            border-radius: 4px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            box-sizing: border-box;
            color: #2D241E;
        }}
        .title {{
            font-size: 20px;
            font-weight: 800;
            color: #4A2E18;
            margin-bottom: 2px;
        }}
        .subtitle {{
            font-size: 11px;
            color: #7A6F64;
            margin-bottom: 10px;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 13.5px;
        }}
        thead tr {{
            border-top: 2px solid #2D241E;
            border-bottom: 2px solid #2D241E;
        }}
        th {{
            padding: 5px 6px;
            font-weight: 800;
            color: #2D241E;
        }}
        tfoot tr td {{
            border-top: 2px solid #2D241E;
            padding-top: 4px;
        }}
    </style>
    </head>
    <body>
        <div class="paper-card">
            <div class="title">{title}</div>
            <div class="subtitle">Ekstraklasa 2026/2027 • FotMob Data</div>
            <table>
                <thead>
                    <tr>
                        <th style="text-align: left; width: 35px;">#</th>
                        <th style="text-align: left;">Team</th>
                        <th style="text-align: right; width: 100px;">{value_header}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_html}
                </tbody>
                <tfoot>
                    <tr>
                        <td colspan="3"></td>
                    </tr>
                </tfoot>
            </table>
        </div>
    </body>
    </html>
    """
    components.html(html_code, height=720, scrolling=False)

def render_metric_bar_and_paper(df, col_name, title_chart, title_paper, value_header, color_scale="Greens", sort_asc=False):
    """Tworzy zsynchronizowany widok 2-kolumnowy. Napis i filtr Top 20 pojawia się TYLKO dla Top 5 lig."""
    lang = st.session_state.get("selected_lang", "PL")
    
    # Sprawdzamy czy użytkownik analizuje połączoną bazę Top 5 lig (ok. 100 drużyn)
    is_top5 = (current_league.get("file") == "TOP5")
    
    if is_top5:
        scope_opts = ["Top 20", "Pełna Lista (Wszystkie zespoły)"] if lang == "PL" else ["Top 20", "Full List (All Teams)"]
        selected_scope = st.radio(
            "Zakres rankingu:" if lang == "PL" else "Ranking Scope:",
            scope_opts,
            index=0,
            horizontal=True,
            key=f"scope_radio_{col_name}"
        )
        show_all = bool(selected_scope and ("Pełna" in selected_scope or "Full" in selected_scope))
        title_suffix = f" ({len(df)})" if show_all else " (Top 20)"
    else:
        show_all = True
        title_suffix = ""  # Żadnego dopisku (Top 20) dla pojedynczej ligi!

    # Sortowanie danych
    full_sorted_df = df.sort_values(by=col_name, ascending=sort_asc).copy().reset_index(drop=True)
    avg_val = full_sorted_df[col_name].mean()
    
    # Wybór wierszy do wyświetlenia
    sorted_df = full_sorted_df if show_all else full_sorted_df.head(20)

    # 1. Wykres słupkowy
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_df[col_name],
        y=sorted_df["Team"],
        orientation='h',
        text=[
            f"{v:+.2f}" if ("Gole - xG" in value_header or "Gole - xGA" in value_header or "Goals - xG" in value_header)
            else (f"{v:.3f}" if ("strzał" in value_header.lower() or "shot" in value_header.lower()) else f"{v:.2f}")
            for v in sorted_df[col_name]
        ],
        textposition="outside",
        textfont=dict(size=10.5, color="#1E293B"),
        marker=dict(
            color=sorted_df[col_name],
            colorscale=color_scale,
            showscale=False,
            line=dict(color="#0F172A", width=0.5)
        ),
        hovertemplate="<b>%{y}</b><br>" + f"{value_header}: " + "%{x:.2f}<extra></extra>"
    ))
    
    fig.add_vline(
        x=avg_val, line_dash="dash", line_color="#475569", line_width=1.2,
        annotation_text=f"Średnia / Avg: {avg_val:.2f}", 
        annotation_position="bottom right" if avg_val >= 0 else "bottom left",
        annotation_font=dict(size=10, color="#475569")
    )
    
    x_min, x_max = sorted_df[col_name].min(), sorted_df[col_name].max()
    x_range = [x_min * 1.3 if x_min < 0 else 0, x_max * 1.25 if x_max > 0 else 0]
    
    plot_height = 620 if not (is_top5 and show_all) else max(620, len(sorted_df) * 26)

    fig.update_layout(
        height=plot_height,
        template="simple_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#F8FAFC",
        title=dict(
            text=f"<b>{title_chart}</b>{title_suffix}",
            x=0.04,
            y=0.98 if show_all else 0.96,
            font=dict(size=16, color="#0F172A")
        ),
        xaxis=dict(
            title=dict(
                text=f"<b>{value_header}</b>",
                font=dict(size=13, color="#0F172A")
            ),
            tickfont=dict(size=11, color="#0F172A", family="Arial Black, sans-serif"),
            showgrid=True,
            gridcolor="#CBD5E1",
            zeroline=True,
            zerolinecolor="#475569",
            zerolinewidth=1.5,
            range=x_range,
            linecolor="#0F172A",
            linewidth=1.2
        ),
        yaxis=dict(
            autorange="reversed",
            tickfont=dict(size=10.5, color="#0F172A", family="Arial, sans-serif")
        ),
        margin=dict(l=120, r=40, t=50, b=50)
    )
    
    # 2. Generowanie ciemnej tabeli HTML z paskiem przewijania
    rows_html = ""
    for idx, row in sorted_df.iterrows():
        rank = idx + 1
        team = row["Team"]
        val = row[col_name]
        matches = int(row["Mecze"]) if "Mecze" in row else len(sorted_df)
        
        if "Gole - xG" in value_header or "Goals - xG" in value_header:
            val_str = f"{val:+.2f}"
            val_color = "#10B981" if val > 0 else ("#EF4444" if val < 0 else "#FFFFFF")
        else:
            val_str = f"{val:.2f}"
            val_color = "#FFFFFF"
            
        rows_html += f"""
        <tr style="height: 25px; border-bottom: 1px solid #262b32;">
            <td style="font-weight: 700; color: #FFFFFF; text-align: left; width: 28px;">{rank}</td>
            <td style="font-weight: 600; color: #E2E8F0; text-align: left; white-space: nowrap; overflow: hidden; text-overflow: ellipsis;">{team}</td>
            <td style="color: #CBD5E1; text-align: center; width: 35px;">{matches}</td>
            <td style="font-weight: 700; color: {val_color}; text-align: right; width: 65px;">{val_str}</td>
        </tr>
        """
        
    th_bar_team = "Team" if lang == "EN" else "Drużyna"
    th_bar_m = "MP" if lang == "EN" else "M"

    table_html = f"""
    <div style="background-color: #1a1d21; border: 1px solid #2d333b; border-radius: 6px; padding: 14px 18px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; max-height: {plot_height - 20}px; overflow-y: auto;">
        <div style="font-size: 15px; font-weight: 700; color: #FFFFFF; margin-bottom: 8px;">{title_paper}</div>
        <table style="width: 100%; border-collapse: collapse; font-size: 12.5px; line-height: 1.2;">
            <thead>
                <tr style="border-bottom: 2px solid #3b434e; color: #94A3B8; font-size: 11.5px; height: 26px;">
                    <th style="width: 28px; text-align: left;">#</th>
                    <th style="text-align: left;">{th_bar_team}</th>
                    <th style="width: 35px; text-align: center;">{th_bar_m}</th>
                    <th style="width: 65px; text-align: right;">{value_header}</th>
                </tr>
            </thead>
            <tbody>
                {rows_html}
            </tbody>
        </table>
    </div>
    """
    
    col_l, col_r = st.columns([1.35, 1])
    with col_l:
        st.plotly_chart(fig, use_container_width=True)
    with col_r:
        components.html(table_html, height=plot_height, scrolling=True if (is_top5 and show_all) else False)


def render_metric_trend_chart(matches_df, team_stats, match_col, avg_col, metric_label, yaxis_title="Wartość"):
    """Uniwersalny wykres trendu kolejka po kolejce z pełną informacją o meczu po najechaniu."""
    lang = st.session_state.get("selected_lang", "PL")
    st.markdown("---")
    
    team_list = sorted(team_stats["Team"].unique().tolist())
    sel_label = "Select team for trend analysis:" if lang == "EN" else "Wybierz drużynę do analizy serii mecz po meczu:"
    
    selected_trend_team = st.selectbox(sel_label, team_list, index=0, key=f"sb_trend_{match_col}_{avg_col}")
    
    team_matches = matches_df[matches_df["Team"] == selected_trend_team].copy().reset_index(drop=True)
    team_matches["Kolejka"] = team_matches.index + 1
    
    league_avg = team_stats[avg_col].mean()
    
    # Tworzymy czytelny tekst dymka dla każdego meczu
    hover_texts = []
    for _, r in team_matches.iterrows():
        res = f"{int(r['Goals_For'])}:{int(r['Goals_Against'])}"
        venue_str = "Dom" if r["Venue"] == "Home" else "Wyjazd"
        if lang == "EN":
            venue_str = r["Venue"]
            hover_texts.append(
                f"<b>Matchweek {r['Kolejka']}</b><br>"
                f"Opponent: <b>{r['Opponent']}</b> ({venue_str})<br>"
                f"Result: <b>{res}</b><br>"
                f"{metric_label}: <b>{r[match_col]:.2f}</b>"
            )
        else:
            hover_texts.append(
                f"<b>Kolejka {r['Kolejka']}</b><br>"
                f"Rywal: <b>{r['Opponent']}</b> ({venue_str})<br>"
                f"Wynik: <b>{res}</b><br>"
                f"{metric_label}: <b>{r[match_col]:.2f}</b>"
            )

    fig_tr = go.Figure()
    fig_tr.add_trace(go.Scatter(
        x=team_matches["Kolejka"],
        y=team_matches[match_col],
        mode="lines+markers",
        name=selected_trend_team,
        line=dict(color="#38BDF8", width=3),
        marker=dict(size=10, color="#38BDF8", line=dict(width=1.5, color="#FFFFFF")),
        hovertext=hover_texts,
        hoverinfo="text"
    ))
    
    fig_tr.add_hline(
        y=league_avg,
        line_dash="dot",
        line_color="#94A3B8",
        line_width=1.8,
        annotation_text=f"Średnia ligowa / League Avg: {league_avg:.2f}",
        annotation_position="bottom right"
    )
    
    fig_tr.update_layout(
        height=440,
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        title=dict(
            text=f"<b>{selected_trend_team} – {metric_label} (Mecz po meczu)</b>" if lang == "PL" else f"<b>{selected_trend_team} – {metric_label} (Match-by-Match Trend)</b>",
            font=dict(size=15, color="#FFFFFF"),
            x=0.03, y=0.95
        ),
        xaxis=dict(
            title="Numer Kolejki" if lang == "PL" else "Matchweek",
            dtick=1,
            showgrid=True,
            gridcolor="#30363D"
        ),
        yaxis=dict(
            title=yaxis_title,
            showgrid=True,
            gridcolor="#30363D"
        ),
        margin=dict(l=60, r=40, t=50, b=40)
    )
    
    st.plotly_chart(fig_tr, use_container_width=True)

# =========================================================================
# WYBÓR LIGI I DYNAMICZNE WCZYTANIE DANYCH
# =========================================================================
LEAGUES_CONFIG = {
    "PKO BP Ekstraklasa": {
        "file": "Ekstraklasa 2026-2027.xlsx",
        "title": "🇵🇱 Ekstraklasa - Zaawansowany Dashboard Analityczny"
    },
    "Premier League": {
        "file": "Premier League 2026-2027.xlsx",
        "title": " Premier League - Zaawansowany Dashboard Analityczny"
    },
    "La Liga": {
        "file": "La Liga 26-27.xlsx",
        "title": "La Liga - Zaawansowany Dashboard Analityczny"
    },
    "Serie A": {
        "file": "Serie A 26-27.xlsx",
        "title": "Serie A - Zaawansowany Dashboard Analityczny"
    },
    "Bundesliga": {
        "file": "Bundesliga 26-27.xlsx",
        "title": "Bundesliga - Zaawansowany Dashboard Analityczny"
    },
    "Ligue 1": {
        "file": "Ligue 1 26-27.xlsx",
        "title": "Ligue 1 - Zaawansowany Dashboard Analityczny"
    },

    " Top 5 Leagues (Europe)": {
        "file": "TOP5",  # Znacznik informujący o trybie połączonym
        "title": " Top 5 Leagues - Zaawansowany Dashboard Analityczny"
    },



    
}


# Inicjalizacja języka w sesji, jeśli jeszcze nie istnieje
if "selected_lang" not in st.session_state:
    st.session_state["selected_lang"] = "PL"

# Funkcja pobierająca tłumaczenie
def t(key):
    return TRANSLATIONS.get(st.session_state["selected_lang"], {}).get(key, key)

# 1. Nagłówek: Selektor ligi (po lewej) + Klikalne flagi językowe (po prawej)
col_league_sel, col_space, col_lang = st.columns([2.6, 0.4, 1.0])

with col_lang:
    st.markdown("<p style='font-size: 12px; font-weight: 600; color: #94A3B8; margin-bottom: 2px;'>🌐 Język / Language:</p>", unsafe_allow_html=True)
    
    # Dwie małe kolumienki na flagi obok siebie
    c_fl_pl, c_fl_en = st.columns(2)
    
    with c_fl_pl:
        # Przycisk z polską flagą
        is_active_pl = "border: 2px solid #38BDF8;" if st.session_state["selected_lang"] == "PL" else "opacity: 0.5;"
        st.markdown(
            f"""<div style="display:flex; justify-content:center; margin-bottom: 4px;">
                <img src="https://flagcdn.com/w40/pl.png" width="28" style="border-radius: 3px; {is_active_pl}">
            </div>""",
            unsafe_allow_html=True
        )
        if st.button("PL", key="btn_lang_pl", use_container_width=True):
            st.session_state["selected_lang"] = "PL"
            st.rerun()

    with c_fl_en:
        # Przycisk z brytyjską flagą
        is_active_en = "border: 2px solid #38BDF8;" if st.session_state["selected_lang"] == "EN" else "opacity: 0.5;"
        st.markdown(
            f"""<div style="display:flex; justify-content:center; margin-bottom: 4px;">
                <img src="https://flagcdn.com/w40/gb.png" width="28" style="border-radius: 3px; {is_active_en}">
            </div>""",
            unsafe_allow_html=True
        )
        if st.button("EN", key="btn_lang_en", use_container_width=True):
            st.session_state["selected_lang"] = "EN"
            st.rerun()

selected_lang = st.session_state["selected_lang"]

selected_lang = st.session_state["selected_lang"]

with col_league_sel:
    selected_league_name = st.selectbox(
        t("choose_league"), # Dynamiczny napis nad ligą
        list(LEAGUES_CONFIG.keys()),
        index=0,
        key="sb_main_league_selector"
    )

current_league = LEAGUES_CONFIG[selected_league_name]

# 2. Wczytanie danych wybranej ligi (lub scalonej bazy Top 5)
if current_league["file"] == "TOP5":
    matches_df, team_stats = load_and_process_top5_leagues()
else:
    matches_df, team_stats = load_and_process_team_data(current_league["file"])

# 3. Dynamiczny nagłówek i podtytuł (PL / EN)
league_pure_title = current_league["title"].replace(" - Zaawansowany Dashboard Analityczny", "").strip()
if selected_lang == "EN":
    page_main_title = f"{league_pure_title} - Advanced Analytics Dashboard"
    page_main_caption = "Analytical dashboard powered by FotMob match data • Season 2026/2027"
else:
    page_main_title = f"{league_pure_title} - Zaawansowany Dashboard Analityczny"
    page_main_caption = "Dashboard analityczny oparty na danych meczowych FotMob • Sezon 2026/2027"

st.title(page_main_title)
st.caption(page_main_caption)
st.markdown("---")


# Przygotowanie danych do wyświetlania w tabelach zbiorczych
display_df = team_stats.copy()
float_cols = display_df.select_dtypes(include=["float"]).columns
display_df[float_cols] = display_df[float_cols].round(2)
display_df.columns = [col.replace("_", " ") for col in display_df.columns]

# =========================================================================
# ZAKŁADKI (Wszystko poniżej działa automatycznie dla wybranej ligi!)



# Przygotowanie danych do wyświetlania
display_df = team_stats.copy()
float_cols = display_df.select_dtypes(include=["float"]).columns
display_df[float_cols] = display_df[float_cols].round(2)
display_df.columns = [col.replace("_", " ") for col in display_df.columns]

# Zakładki
tab_ogolne, tab_ofensywa, tab_defensywa, tab_podania, tab_druzyny, tab_h2h, tab_analiza_ligowa, tab_asystent_ai, tab_zaleznosci = st.tabs([
    t("tab_general"),
    t("tab_offense"), 
    t("tab_defense"),
    t("tab_passing"),
    t("tab_teams"),
    t("tab_h2h"),
    " Analiza Ligowa AI" if selected_lang == "PL" else " League AI Scout",
    " Asystent AI (Zapytania)" if selected_lang == "PL" else " AI Scout Copilot",
    t("tab_insights"),
    
]) 

# Słownik wspólnego formatowania kolumn

# =========================================================================
# KROK 3: SŁOWNIK FORMATOWANIA KOLUMN TABEL (PL / EN)
# =========================================================================
common_col_config = {
    "Gole na mecz": st.column_config.NumberColumn("Goals / 90" if selected_lang == "EN" else "Gole na mecz", format="%.2f"),
    "Gole stracone na mecz": st.column_config.NumberColumn("GA / 90" if selected_lang == "EN" else "Gole stracone na mecz", format="%.2f"),
    "xG na mecz": st.column_config.NumberColumn("xG / 90", format="%.2f"),
    "xGA na mecz": st.column_config.NumberColumn("xGA / 90", format="%.2f"),
    "Bilans xG": st.column_config.NumberColumn("xG Diff" if selected_lang == "EN" else "Bilans xG", format="%+.2f"),
    "xGOT na mecz": st.column_config.NumberColumn("xGOT / 90", format="%.2f"),
    "xAGOT na mecz": st.column_config.NumberColumn("xAGOT / 90", format="%.2f"),
    "Posiadanie": st.column_config.NumberColumn("Possession %" if selected_lang == "EN" else "Posiadanie", format="%.2f %%"),
    "Podania ogolem": st.column_config.NumberColumn("Passes / 90" if selected_lang == "EN" else "Podania ogółem", format="%.2f"),
    "Podania celne": st.column_config.NumberColumn("Acc. Passes / 90" if selected_lang == "EN" else "Podania celne", format="%.2f"),
    "Strzaly na mecz": st.column_config.NumberColumn("Shots / 90" if selected_lang == "EN" else "Strzały na mecz", format="%.2f"),
    "Celne strzaly": st.column_config.NumberColumn("SoT / 90" if selected_lang == "EN" else "Celne strzały", format="%.2f"),
    "Big Chances": st.column_config.NumberColumn("Big Chances", format="%.2f"),
    "Kontakty w polu karnym": st.column_config.NumberColumn("Box Touches / 90" if selected_lang == "EN" else "Kontakty w polu karnym", format="%.2f"),
    "Rzuty Rozne": st.column_config.NumberColumn("Corners / 90" if selected_lang == "EN" else "Rzuty Rożne", format="%.2f"),
    "Odbiory": st.column_config.NumberColumn("Tackles / 90" if selected_lang == "EN" else "Odbiory", format="%.2f"),
    "Przejecia": st.column_config.NumberColumn("Interceptions / 90" if selected_lang == "EN" else "Przejęcia", format="%.2f"),
    "Pojedynki Wygrane": st.column_config.NumberColumn("Duels Won / 90" if selected_lang == "EN" else "Pojedynki Wygrane", format="%.2f"),
}

# =========================================================================
# TAB 1: OGÓLNE STATYSTYKI (PL / EN)
# =========================================================================
with tab_ogolne:
    ogolne_widok = st.selectbox(
        t("gen_select"),
        [
            t("gen_opt1"),
            t("gen_opt2"),
            t("gen_opt3")
        ]
    )
    st.markdown("---")

    # 1. Widok: Tabela Realna vs Tabela xG
    # 1. Widok: Tabela Realna vs Tabela xG
    if ogolne_widok == t("gen_opt1"):
        tab_real_full = compute_custom_table(matches_df, is_xg=False)
        tab_xg_comp_full = compute_custom_table(matches_df, is_xg=True)
        
        # Przełącznik widoku: Top 20 vs Cała tabela (przydatne zwłaszcza przy Top 5 Leagues)
        # Przełącznik widoku: Top 20 vs Cała tabela
        # Przełącznik widoku wyświetlamy TYLKO gdy wybrano Top 5 lig Europy
        is_top5_selected = (current_league["file"] == "TOP5")
        
        if is_top5_selected:
            scope_opts = ["Top 20", "Pełna Tabela (Wszystkie zespoły)"] if selected_lang == "PL" else ["Top 20", "Full Standings (All Teams)"]
            selected_scope = st.radio(
                "Zakres tabeli:" if selected_lang == "PL" else "Standings Scope:",
                scope_opts,
                index=0,
                horizontal=True,
                key="radio_table_scope"
            )
            show_all = bool(selected_scope and ("Pełna" in selected_scope or "Full" in selected_scope))
            tab_real = tab_real_full if show_all else tab_real_full.head(20)
            tab_xg_comp = tab_xg_comp_full if show_all else tab_xg_comp_full.head(20)
            suffix_real = f" ({len(tab_real)})" if show_all else " (Top 20)"
            suffix_xg = f" ({len(tab_xg_comp)})" if show_all else " (Top 20)"
        else:
            show_all = True
            tab_real = tab_real_full
            tab_xg_comp = tab_xg_comp_full
            suffix_real = ""
            suffix_xg = ""
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            title_real = ("Real Standings" if selected_lang == "EN" else "Tabela Realna") + suffix_real
            components.html(render_dark_table_html(tab_real, title_real, is_xg=False), height=620, scrolling=True if show_all else False)
        with col_t2:
            title_xg = ("Expected Goals (xG) Table" if selected_lang == "EN" else "Tabela xG") + suffix_xg
            components.html(render_dark_table_html(tab_xg_comp, title_xg, is_xg=True), height=620, scrolling=True if show_all else False)
        
        


    # 2. Widok: Dom vs Wyjazd
    elif ogolne_widok == t("gen_opt2"):
        home_matches = matches_df[matches_df["Venue"] == "Home"]
        away_matches = matches_df[matches_df["Venue"] == "Away"]
        
        tab_home = compute_custom_table(home_matches, is_xg=False)
        tab_away = compute_custom_table(away_matches, is_xg=False)
        
        col_h, col_a = st.columns(2)
        with col_h:
            t_home = " Home Table" if selected_lang == "EN" else " Tabela: Mecze u Siebie"
            components.html(render_dark_table_html(tab_home, t_home, is_xg=False), height=590, scrolling=False)
        with col_a:
            t_away = " Away Table" if selected_lang == "EN" else " Tabela: Mecze na Wyjeździe"
            components.html(render_dark_table_html(tab_away, t_away, is_xg=False), height=590, scrolling=False)

        st.markdown("---")
        st.subheader("Home Advantage Analysis (xG Home vs Away)" if selected_lang == "EN" else "Wpływ Własnego Boiska na Jakość Gry (Expected Goals Dom vs Wyjazd)")
        st.caption("Do teams create more threat at home and concede more chances on the road?" if selected_lang == "EN" else "Czy drużyny kreują więcej zagrożenia przed własną publicznością i czy defensywy dopuszczają groźniejsze okazje w delegacji?")

        venue_summary = matches_df.groupby(["Team", "Venue"]).agg(
            xG_mean=("xG_For", "mean"),
            xGA_mean=("xG_Against", "mean"),
            Mecze=("Points", "count")
        ).unstack()

        venue_df = pd.DataFrame({
            "Team": venue_summary.index,
            "xG_Home": venue_summary[("xG_mean", "Home")].round(2),
            "xG_Away": venue_summary[("xG_mean", "Away")].round(2),
            "xGA_Home": venue_summary[("xGA_mean", "Home")].round(2),
            "xGA_Away": venue_summary[("xGA_mean", "Away")].round(2),
        }).reset_index(drop=True)

        venue_df["xG_Diff"] = (venue_df["xG_Home"] - venue_df["xG_Away"]).round(2)
        venue_df["xGA_Diff"] = (venue_df["xGA_Away"] - venue_df["xGA_Home"]).round(2)

        league_home_xg = venue_df["xG_Home"].mean()
        league_away_xg = venue_df["xG_Away"].mean()
        league_home_xga = venue_df["xGA_Home"].mean()
        league_away_xga = venue_df["xGA_Away"].mean()

        col_k1, col_k2, col_k3 = st.columns(3)
        col_k1.metric(
            label="Avg Home xG" if selected_lang == "EN" else "Średnie xG Gospodarzy (Dom)", 
            value=f"{league_home_xg:.2f}",
            delta=f"{league_home_xg - league_away_xg:+.2f} vs Away" if selected_lang == "EN" else f"{league_home_xg - league_away_xg:+.2f} vs Wyjazdy"
        )
        col_k2.metric(
            label="Avg Away xG" if selected_lang == "EN" else "Średnie xG Gości (Wyjazd)", 
            value=f"{league_away_xg:.2f}",
            delta="Baseline" if selected_lang == "EN" else "Baza odniesienia",
            delta_color="off"
        )
        col_k3.metric(
            label="Avg Away xGA Conceded" if selected_lang == "EN" else "Średnie xGA Dopuszczone na Wyjazdach", 
            value=f"{league_away_xga:.2f}",
            delta=f"{league_away_xga - league_home_xga:+.2f} vs Home" if selected_lang == "EN" else f"{league_away_xga - league_home_xga:+.2f} vs Dom",
            delta_color="inverse"
        )

        pills_opts = [
            "1. Attack: xG Created (Home vs Away)" if selected_lang == "EN" else "1. Kreacja: xG Wygenerowane (Dom vs Wyjazd)",
            "2. Defense: xGA Conceded (Home vs Away)" if selected_lang == "EN" else "2. Defensywa: xGA Dopuszczone (Dom vs Wyjazd)",
            "3. Home Advantage Delta (xG)" if selected_lang == "EN" else "3. Ranking Przewagi Domowej (xG Home Advantage)"
        ]
        xg_venue_mode = st.pills("Perspective:" if selected_lang == "EN" else "Wybierz perspektywę analizy:", pills_opts, default=pills_opts[0], key="pills_xg_venue_analysis")

        if xg_venue_mode == pills_opts[0]:
            df_plot = venue_df.sort_values(by="xG_Home", ascending=False).reset_index(drop=True)
            fig_v = go.Figure()
            fig_v.add_trace(go.Bar(
                name="🏠 Home (xG / 90)" if selected_lang == "EN" else "🏠 Dom (xG / mecz)",
                x=df_plot["Team"], y=df_plot["xG_Home"], marker_color="#38BDF8",
                text=[f"{v:.2f}" for v in df_plot["xG_Home"]], textposition="outside", textfont=dict(size=10, color="#FFFFFF")
            ))
            fig_v.add_trace(go.Bar(
                name="🚌 Away (xG / 90)" if selected_lang == "EN" else "🚌 Wyjazd (xG / mecz)",
                x=df_plot["Team"], y=df_plot["xG_Away"], marker_color="#94A3B8",
                text=[f"{v:.2f}" for v in df_plot["xG_Away"]], textposition="outside", textfont=dict(size=10, color="#FFFFFF")
            ))
            fig_v.update_layout(barmode="group", height=480, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", xaxis=dict(tickangle=-35), yaxis=dict(title="xG / 90"))
            st.plotly_chart(fig_v, use_container_width=True)

        elif xg_venue_mode == pills_opts[1]:
            df_plot = venue_df.sort_values(by="xGA_Home", ascending=True).reset_index(drop=True)
            fig_v = go.Figure()
            fig_v.add_trace(go.Bar(
                name="🏠 Home (xGA / 90)" if selected_lang == "EN" else "🏠 Dom (xGA / mecz)",
                x=df_plot["Team"], y=df_plot["xGA_Home"], marker_color="#10B981",
                text=[f"{v:.2f}" for v in df_plot["xGA_Home"]], textposition="outside", textfont=dict(size=10, color="#FFFFFF")
            ))
            fig_v.add_trace(go.Bar(
                name="🚌 Away (xGA / 90)" if selected_lang == "EN" else "🚌 Wyjazd (xGA / mecz)",
                x=df_plot["Team"], y=df_plot["xGA_Away"], marker_color="#EF4444",
                text=[f"{v:.2f}" for v in df_plot["xGA_Away"]], textposition="outside", textfont=dict(size=10, color="#FFFFFF")
            ))
            fig_v.update_layout(barmode="group", height=480, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", xaxis=dict(tickangle=-35), yaxis=dict(title="xGA / 90"))
            st.plotly_chart(fig_v, use_container_width=True)
        else:
            df_diff = venue_df.sort_values(by="xG_Diff", ascending=False).reset_index(drop=True)
            diff_colors = ["#10B981" if v >= 0 else "#EF4444" for v in df_diff["xG_Diff"]]
            fig_diff = go.Figure(go.Bar(
                x=df_diff["Team"], y=df_diff["xG_Diff"], marker_color=diff_colors,
                text=[f"{v:+.2f}" for v in df_diff["xG_Diff"]], textposition="outside", textfont=dict(size=10.5, color="#FFFFFF")
            ))
            fig_diff.update_layout(height=450, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", xaxis=dict(tickangle=-35), yaxis=dict(title="Delta (Home - Away xG)"))
            st.plotly_chart(fig_diff, use_container_width=True)

    # 3. Widok: Pełna Tabela Zbiorcza
    elif ogolne_widok == t("gen_opt3"):
        st.subheader("Full Standings & Advanced Metrics" if selected_lang == "EN" else "Pełna Tabela Zbiorcza ze Wszystkimi Wskaźnikami")
        ogolne_cols = [
            "Team", "Mecze", "Punkty", "Gole Strzelone", "Gole na mecz",
            "Gole Stracone", "Gole stracone na mecz", "xG na mecz", "xGA na mecz",
            "Posiadanie", "Podania ogolem", "Podania celne", "Pojedynki Wygrane"
        ]
        st.dataframe(display_df[ogolne_cols], use_container_width=True, hide_index=True, column_config=common_col_config)


with tab_ofensywa:
    ofensywa_widok = st.selectbox(
        t("att_select"),
        [t(f"att_opt{i}") for i in range(1, 21)]
    )
    st.markdown("---")

    # 1. Tabela Główna
    if ofensywa_widok == t("att_opt1"):
        st.subheader("Attacking Table & Metrics" if selected_lang == "EN" else "Ranking i Metryki Ataku")
        ofensywa_cols = [
            "Team", "Mecze", "Gole Strzelone", "Gole na mecz", "xG na mecz", 
            "xGOT na mecz", "Bilans xG", "Strzaly na mecz", "Celne strzaly", 
            "Big Chances", "Kontakty w polu karnym", "Podania celne", "Posiadanie"
        ]
        st.dataframe(display_df[ofensywa_cols], use_container_width=True, hide_index=True, column_config=common_col_config)

    # 2. Total xG
    elif ofensywa_widok == t("att_opt2"):
        st.subheader("Total Expected Goals (xG)" if selected_lang == "EN" else "Ogólna jakość kreowanych sytuacji (Expected Goals)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_na_mecz", title_chart="Total Expected Goals (xG) Rankings",
            title_paper="Total xG Rankings", value_header="xG / 90", color_scale="Blues"
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_For", "xG_na_mecz", "Expected Goals (xG)", "xG")

    # 3. xG Open Play
    elif ofensywa_widok == t("att_opt3"):
        st.subheader("Open Play xG" if selected_lang == "EN" else "Kreacja sytuacji z gry otwartej (Open Play xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_OP_na_mecz", title_chart="Open Play xG Rankings",
            title_paper="Open Play xG Rankings", value_header="xG OP / 90", color_scale="Greens"
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_OP_For", "xG_OP_na_mecz", "Open Play xG", "xG OP")

    # 4. xG Set Play
    elif ofensywa_widok == t("att_opt4"):
        st.subheader("Set Play xG" if selected_lang == "EN" else "Groźność po stałych fragmentach gry (Set Play xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_SP_na_mecz", title_chart="Set Play xG Rankings",
            title_paper="Set Play xG Rankings", value_header="SP xG / 90", color_scale="Oranges"
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_SP_For", "xG_SP_na_mecz", "Set Play xG", "SP xG")

    # 5. npxG
    elif ofensywa_widok == t("att_opt5"):
        st.subheader("Non-Penalty xG" if selected_lang == "EN" else "Czyste zagrożenie bez rzutów karnych (Non-Penalty xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="npxG_na_mecz", title_chart="Non-Penalty xG Rankings",
            title_paper="Non-Penalty xG Rankings", value_header="npxG / 90", color_scale="Purples"
        )
        render_metric_trend_chart(matches_df, team_stats, "npxG_For", "npxG_na_mecz", "Non-Penalty xG", "npxG")

    # 6. xGOT
    elif ofensywa_widok == t("att_opt6"):
        st.subheader("Expected Goals on Target (xGOT)" if selected_lang == "EN" else "Jakość uderzeń zmierzających w światło bramki (xGOT)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGOT_na_mecz", title_chart="Expected Goals on Target (xGOT) Rankings",
            title_paper="xGOT Rankings", value_header="xGOT / 90", color_scale="Tealgrn"
        )
        render_metric_trend_chart(matches_df, team_stats, "xGOT_For", "xGOT_na_mecz", "xGOT on Target", "xGOT")

    # 7. xG / Shot
    elif ofensywa_widok == t("att_opt7"):
        st.subheader("Expected Goals per Shot" if selected_lang == "EN" else "Średnia jakość pojedynczego strzału (xG / Shot)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_na_strzal", title_chart="Expected Goals per Shot (xG/Shot) Rankings",
            title_paper="xG per Shot Rankings", value_header="xG / Shot", color_scale="Viridis"
        )
        # Obliczenie xG / Shot w locie na mecz
        matches_df_temp = matches_df.copy()
        matches_df_temp["xG_Shot_Match"] = (matches_df_temp["xG_For"] / matches_df_temp["Shots"]).fillna(0).round(3)
        render_metric_trend_chart(matches_df_temp, team_stats, "xG_Shot_Match", "xG_na_strzal", "xG / Shot", "xG / Shot")

    # 8. xG / Goal
    elif ofensywa_widok == t("att_opt8"):
        st.subheader("xG Needed per Goal" if selected_lang == "EN" else "Ile xG potrzebuje drużyna, by zdobyć 1 bramkę?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_na_gola", title_chart="xG Needed per Goal Rankings",
            title_paper="xG / Goal Rankings", value_header="xG / 1 Gol" if selected_lang == "PL" else "xG / 1 Goal",
            color_scale="RdYlGn_r", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["xG_Goal_Match"] = matches_df_temp.apply(lambda r: round(r["xG_For"] / r["Goals_For"], 2) if r["Goals_For"] > 0 else 0.0, axis=1)
        render_metric_trend_chart(matches_df_temp, team_stats, "xG_Goal_Match", "xG_na_gola", "xG / Goal", "xG / Gol")

    # 9. SoT / Goal
    elif ofensywa_widok == t("att_opt9"):
        st.subheader("Shots on Target per Goal" if selected_lang == "EN" else "Zabójcza precyzja: Ile celnych strzałów (SoT) potrzeba na 1 bramkę?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celne_na_gola", title_chart="Shots on Target Needed per Goal",
            title_paper="SoT / Goal Rankings", value_header="SoT / Goal" if selected_lang == "EN" else "SoT / 1 Gol",
            color_scale="RdYlGn_r", sort_asc=True
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["SoT_Goal_Match"] = matches_df_temp.apply(lambda r: round(r["Shots_On_Target"] / r["Goals_For"], 2) if r["Goals_For"] > 0 else 0.0, axis=1)
        render_metric_trend_chart(matches_df_temp, team_stats, "SoT_Goal_Match", "Celne_na_gola", "Celne na gola (SoT/Goal)", "SoT / Gol")

    # 10. Gole - xG
    elif ofensywa_widok == t("att_opt10"):
        st.subheader("Finishing Over/Underperformance (Goals - xG)" if selected_lang == "EN" else "Przestrzelone okazje czy genialni napastnicy? (Zdobyte bramki - Suma xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Gole_minus_xG", title_chart="Finishing Overperformance (Goals - xG)",
            title_paper="Goals - xG Rankings" if selected_lang == "EN" else "Gole - xG Rankings",
            value_header="Goals - xG" if selected_lang == "EN" else "Gole - xG",
            color_scale="RdYlGn", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["Delta_xG_Match"] = (matches_df_temp["Goals_For"] - matches_df_temp["xG_For"]).round(2)
        render_metric_trend_chart(matches_df_temp, team_stats, "Delta_xG_Match", "Gole_na_mecz", "Gole - xG (Delta meczowa)", "Delta")

    # 11. Box Shots
    elif ofensywa_widok == t("att_opt11"):
        st.subheader("Shots Inside Box" if selected_lang == "EN" else "Obecność w szesnastce: Średnia strzałów z pola karnego")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Strzaly_z_pola_karnego", title_chart="Shots Inside Box per Match",
            title_paper="Shots Inside Box Rankings", value_header="Box Shots / 90" if selected_lang == "EN" else "Strzały w polu / 90",
            color_scale="Blues", sort_asc=False
        )
        render_metric_trend_chart(matches_df, team_stats, "Box_Shots", "Strzaly_z_pola_karnego", "Strzały z pola karnego", "Strzały")

    # 12. Outside Box Shots
    elif ofensywa_widok == t("att_opt12"):
        st.subheader("Shots Outside Box (Long Range)" if selected_lang == "EN" else "Średnia strzałów zza pola karnego")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Strzaly_zza_pola_karnego", title_chart="Shots Outside Box per Match",
            title_paper="Shots Outside Box Rankings", value_header="Outside Shots / 90" if selected_lang == "EN" else "Strzały z dystansu / 90",
            color_scale="Purples", sort_asc=False
        )
        render_metric_trend_chart(matches_df, team_stats, "Outside_Box_Shots", "Strzaly_zza_pola_karnego", "Strzały zza pola karnego", "Strzały")

    # 13. Rozkład xG: Open Play vs Set Play
    elif ofensywa_widok == t("att_opt13"):
        st.subheader("xG Breakdown: Open Play vs Set Play" if selected_lang == "EN" else "Struktura kreowania sytuacji: Z gry vs Stałe fragmenty")
        dist_df = team_stats.copy()
        dist_df["Karne_Inne_xG"] = (dist_df["xG_na_mecz"] - dist_df["xG_OP_na_mecz"] - dist_df["xG_SP_na_mecz"]).clip(lower=0).round(2)
        dist_df = dist_df.sort_values(by="xG_na_mecz", ascending=True).reset_index(drop=True)
        
        fig_dist = go.Figure()
        fig_dist.add_trace(go.Bar(y=dist_df["Team"], x=dist_df["xG_OP_na_mecz"], name="Open Play xG", orientation='h', marker=dict(color="#10B981")))
        fig_dist.add_trace(go.Bar(y=dist_df["Team"], x=dist_df["xG_SP_na_mecz"], name="Set Play xG", orientation='h', marker=dict(color="#F59E0B")))
        fig_dist.add_trace(go.Bar(y=dist_df["Team"], x=dist_df["Karne_Inne_xG"], name="Penalties / Other" if selected_lang == "EN" else "Karne / Inne", orientation='h', marker=dict(color="#94A3B8")))
        fig_dist.update_layout(barmode='stack', height=620, template="simple_white", paper_bgcolor="#FFFFFF", plot_bgcolor="#F8FAFC", title=dict(text="<b>xG Breakdown</b>", x=0.04, y=0.96, font=dict(color="#0F172A")), xaxis=dict(title="xG / 90"), yaxis=dict(tickfont=dict(color="#0F172A")), margin=dict(l=120, r=30, t=65, b=40))
        st.plotly_chart(fig_dist, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xG_OP_For", "xG_OP_na_mecz", "Open Play xG", "xG OP")

    # 14. Celność strzałów
    elif ofensywa_widok == t("att_opt14"):
        st.subheader("🎯 Shot Accuracy (%)" if selected_lang == "EN" else "🎯 Celność Strzałów (Shot Accuracy %)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celnosc_strzalow_proc", title_chart="Shot Accuracy %",
            title_paper="Shot Accuracy Rankings", value_header="Accuracy %" if selected_lang == "EN" else "Celność %",
            color_scale="Blues", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["Shot_Acc_Match"] = ((matches_df_temp["Shots_On_Target"] / matches_df_temp["Shots"]) * 100).fillna(0).round(1)
        render_metric_trend_chart(matches_df_temp, team_stats, "Shot_Acc_Match", "Celnosc_strzalow_proc", "Celność Strzałów (%)", "Celność %")

    # 15. Big Chances
    elif ofensywa_widok == t("att_opt15"):
        st.subheader("Big Chances & Simulation" if selected_lang == "EN" else "Wielkie Szanse: Kreacja, Niewykorzystane Okazje oraz Symulacja Tabeli")
        col_bc1, col_bc2 = st.columns(2)
        with col_bc1:
            st.markdown("##### " + ("Big Chances Created / 90" if selected_lang == "EN" else "Wykreowane Wielkie Szanse (Średnia / Mecz)"))
            fig_bc = go.Figure(go.Bar(
                x=team_stats.sort_values(by="Big_Chances", ascending=False)["Big_Chances"],
                y=team_stats.sort_values(by="Big_Chances", ascending=False)["Team"],
                orientation='h', marker_color="#10B981", text=[f"{v:.2f}" for v in team_stats.sort_values(by="Big_Chances", ascending=False)["Big_Chances"]], textposition="outside"
            ))
            fig_bc.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_bc, use_container_width=True)
        with col_bc2:
            st.markdown("##### " + ("Big Chances Missed / 90" if selected_lang == "EN" else "Zmarnowane Wielkie Szanse (Średnia / Mecz)"))
            fig_bcm = go.Figure(go.Bar(
                x=team_stats.sort_values(by="Big_Chances_Missed", ascending=False)["Big_Chances_Missed"],
                y=team_stats.sort_values(by="Big_Chances_Missed", ascending=False)["Team"],
                orientation='h', marker_color="#EF4444", text=[f"{v:.2f}" for v in team_stats.sort_values(by="Big_Chances_Missed", ascending=False)["Big_Chances_Missed"]], textposition="outside"
            ))
            fig_bcm.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_bcm, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Big_Chances", "Big_Chances", "Big Chances (Wielkie Szanse)", "Szanse")

    # 16. Matryca Skuteczności
    elif ofensywa_widok == t("att_opt16"):
        st.subheader("Finishing Matrix: xG vs xG per Goal" if selected_lang == "EN" else "Matryca Skuteczności: Wolumen kreacji vs Efektywność wykończenia")
        avg_xg = team_stats["xG_na_mecz"].mean()
        avg_xg_per_goal = team_stats["xG_na_gola"].mean()
        fig_matrix = go.Figure()
        fig_matrix.add_vline(x=avg_xg, line_dash="dash", line_color="#475569")
        fig_matrix.add_hline(y=avg_xg_per_goal, line_dash="dash", line_color="#475569")
        for _, row in team_stats.iterrows():
            fig_matrix.add_trace(go.Scatter(
                x=[row["xG_na_mecz"]], y=[row["xG_na_gola"]], mode="markers+text", text=[row["Team"]], textposition="top center",
                marker=dict(size=12, color="#38BDF8"), showlegend=False
            ))
        fig_matrix.update_layout(height=600, template="plotly_dark", xaxis=dict(title="xG / 90"), yaxis=dict(title="xG / Goal", autorange="reversed"))
        st.plotly_chart(fig_matrix, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xG_For", "xG_na_mecz", "xG na mecz", "xG")

    # 17. xG vs xGOT
    elif ofensywa_widok == t("att_opt17"):
        st.subheader("Shot Creation (xG) vs Shot Execution (xGOT)" if selected_lang == "EN" else "Relacja xG vs xGOT (Jakość kreacji vs Strzału)")
        fig_rel = px.scatter(team_stats, x="xG_na_mecz", y="xGOT_na_mecz", text="Team", template="plotly_dark", height=580)
        fig_rel.update_traces(textposition="top center", marker=dict(size=12, color="#10B981"))
        st.plotly_chart(fig_rel, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xGOT_For", "xGOT_na_mecz", "xGOT (Strzały w bramkę)", "xGOT")

    # 18. Kontakty vs Strzały
    elif ofensywa_widok == t("att_opt18"):
        st.subheader("Box Efficiency: Touches in Box vs Shots" if selected_lang == "EN" else "Efektywność w szesnastce: Kontakty vs Strzały")
        fig_box = px.scatter(team_stats, x="Kontakty_w_polu_karnym", y="Strzaly_z_pola_karnego", text="Team", template="plotly_dark", height=580)
        fig_box.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
        st.plotly_chart(fig_box, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Box_Touches", "Box_Touches_Mean", "Kontakty w polu karnym", "Kontakty")

    # 19. Strzały potrzebne na gola
    elif ofensywa_widok == t("att_opt19"):
        st.subheader(t("shots_needed_goal"))
        eff_df = team_stats.sort_values(by="Strzaly_na_gola", ascending=True).copy().reset_index(drop=True)
        avg_shots_per_goal = (team_stats["Strzaly_na_mecz"].sum() / team_stats["Gole_na_mecz"].sum())
        
        fig_eff = go.Figure()
        fig_eff.add_trace(go.Bar(
            x=eff_df["Strzaly_na_gola"], y=eff_df["Team"], orientation='h',
            text=[f"{val:.1f} ({conv:.1f}%)" for val, conv in zip(eff_df["Strzaly_na_gola"], eff_df["Konwersja_proc"])],
            textposition="outside", textfont=dict(size=10.5, color="#1E293B"),
            marker=dict(color=eff_df["Strzaly_na_gola"], colorscale="RdYlGn_r", showscale=False, line=dict(color="#0F172A", width=0.5))
        ))
        fig_eff.add_vline(
            x=avg_shots_per_goal, line_dash="dash", line_color="#475569", line_width=1.2,
            annotation_text=f"{t('league_avg')}: {avg_shots_per_goal:.1f}", annotation_position="top right",
            annotation_font=dict(size=11, color="#0F172A")
        )
        fig_eff.update_layout(
            height=620, template="simple_white", paper_bgcolor="#FFFFFF", plot_bgcolor="#F8FAFC",
            title=dict(text=f"<b>{t('shots_needed_goal')}</b>", x=0.04, y=0.96, font=dict(size=16, color="#0F172A")),
            xaxis=dict(title=dict(text=f"<b>{t('shots_per_1_goal')}</b>", font=dict(size=13, color="#0F172A")), tickfont=dict(size=11, color="#0F172A", family="Arial Black, sans-serif"), showgrid=True, gridcolor="#CBD5E1", linecolor="#0F172A", linewidth=1.2),
            yaxis=dict(autorange="reversed", tickfont=dict(size=10.5, color="#0F172A")),
            margin=dict(l=120, r=40, t=55, b=55)
        )
        st.plotly_chart(fig_eff, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Shots", "Strzaly_na_mecz", "Oddane Strzały", "Strzały")

    # 20. xGOT vs Bramki
    elif ofensywa_widok == t("att_opt20"):
        st.subheader("Goals vs xGOT (Finishing Overperformance)" if selected_lang == "EN" else "xGOT vs Bramki zdobyte (Over/Underperformance)")
        fig_xgot = px.scatter(team_stats, x="xGOT_Suma", y="Gole_Strzelone", text="Team", template="plotly_dark", height=560)
        fig_xgot.update_traces(textposition="top center", marker=dict(size=12, color="#AF7AC5"))
        st.plotly_chart(fig_xgot, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Goals_For", "Gole_na_mecz", "Bramki Zdobyte", "Gole")

# =========================================================================
# TAB 3: STATYSTYKI DEFENSYWNE (PL / EN)
with tab_defensywa:
    defensywa_widok = st.selectbox(
        t("def_select"),
        [t(f"def_opt{i}") for i in range(1, 21)],
        key="sb_def_analytics_view"
    )
    st.markdown("---")

    # 1. Tabela Główna Defensywy
    if defensywa_widok == t("def_opt1"):
        st.subheader("🛡️ Defensive Standings & Metrics" if selected_lang == "EN" else "🛡️ Ranking i Metryki Obrony")
        defensywa_cols = [
            "Team", "Mecze", "Gole Stracone", "Gole stracone na mecz", "xGA na mecz", 
            "xAGOT na mecz", "Odbiory", "Przejecia", "Rzuty Rozne", "Pojedynki Wygrane"
        ]
        st.dataframe(display_df[defensywa_cols], use_container_width=True, hide_index=True, column_config=common_col_config)

    # 2. Total xGA
    elif defensywa_widok == t("def_opt2"):
        st.subheader("Expected Goals Against (xGA)" if selected_lang == "EN" else "Dopuszczona jakość sytuacji bramkowych rywali (Expected Goals Against)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGA_na_mecz", 
            title_chart="Total Expected Goals Against (xGA) Rankings",
            title_paper="Total xGA Rankings", 
            value_header="xGA / 90", 
            color_scale="Reds_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_Against", "xGA_na_mecz", "Dopuszczone xGA (xGA)", "xGA")

    # 3. Open Play xGA
    elif defensywa_widok == t("def_opt3"):
        st.subheader("Open Play xGA" if selected_lang == "EN" else "Dopuszczone sytuacje z gry otwartej (Open Play xGA)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGA_OP_na_mecz", 
            title_chart="Open Play xGA Rankings",
            title_paper="Open Play xGA Rankings", 
            value_header="xGA OP / 90", 
            color_scale="Reds_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_OP_Against", "xGA_OP_na_mecz", "Open Play xGA", "xGA OP")

    # 4. Set Play xGA
    elif defensywa_widok == t("def_opt4"):
        st.subheader("Set Play xGA" if selected_lang == "EN" else "Zagrożenie dopuszczone po stałych fragmentach (Set Play xGA)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGA_SP_na_mecz", 
            title_chart="Set Play xGA Rankings",
            title_paper="Set Play xGA Rankings", 
            value_header="SP xGA / 90", 
            color_scale="Oranges_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "xG_SP_Against", "xGA_SP_na_mecz", "Set Play xGA", "SP xGA")

    # 5. npxGA
    elif defensywa_widok == t("def_opt5"):
        st.subheader("Non-Penalty xGA" if selected_lang == "EN" else "Czyste dopuszczone zagrożenie bez rzutów karnych (Non-Penalty xGA)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="npxGA_na_mecz", 
            title_chart="Non-Penalty xGA Rankings",
            title_paper="Non-Penalty xGA Rankings", 
            value_header="npxGA / 90", 
            color_scale="Purples_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "npxG_Against", "npxGA_na_mecz", "Non-Penalty xGA", "npxGA")

    # 6. xAGOT
    elif defensywa_widok == t("def_opt6"):
        st.subheader("Expected Goals on Target Against (xAGOT)" if selected_lang == "EN" else "Jakość uderzeń rywali zmierzających w światło naszej bramki (xAGOT)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xAGOT_na_mecz", 
            title_chart="Expected Goals on Target Against (xAGOT)",
            title_paper="xAGOT Rankings", 
            value_header="xAGOT / 90", 
            color_scale="Reds_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "xGOT_Against", "xAGOT_na_mecz", "xAGOT (Celne Rywala)", "xAGOT")

    # 7. xGA na jeden strzał rywala
    elif defensywa_widok == t("def_opt7"):
        st.subheader("xGA per Opponent Shot" if selected_lang == "EN" else "Średnia jakość pojedynczego strzału rywala (xGA / Shot Against)")
        st.caption("Lower value = Opponents forced to shoot from difficult angles and low-value zones." if selected_lang == "EN" else "Mniejsza wartość = rywale są zmuszani do strzałów z trudnych, nieprzygotowanych pozycji.")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGA_na_strzal_rywala", 
            title_chart="xGA per Opponent Shot Rankings",
            title_paper="xGA / Shot Against", 
            value_header="xGA / Opp Shot" if selected_lang == "EN" else "xGA / Strzał rywala", 
            color_scale="Reds_r", sort_asc=True
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["xGA_Shot_Opp_Match"] = (matches_df_temp["xG_Against"] / matches_df_temp["Shots_Against"]).fillna(0).round(3)
        render_metric_trend_chart(matches_df_temp, team_stats, "xGA_Shot_Opp_Match", "xGA_na_strzal_rywala", "xGA / Strzał Rywala", "xGA / Strzał")

    # 8. Trudność strzelenia gola
    elif defensywa_widok == t("def_opt8"):
        st.subheader("Resilience: xGA Needed to Score Against" if selected_lang == "EN" else "Odporność: Ile xGA musi wykreować rywal, by wbić nam 1 bramkę?")
        st.caption("Higher value = Opponent must work harder; defensive unit and goalkeeper negate quality chances." if selected_lang == "EN" else "Większa wartość = rywal musi się napracować, obrona i bramkarz 'kasują' wykreowane szanse.")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGA_na_gola_straconego", 
            title_chart="xGA Needed to Score Against Rankings",
            title_paper="xGA / Goal Conceded", 
            value_header="xGA / Conceded Goal" if selected_lang == "EN" else "xGA na 1 Gola", 
            color_scale="Greens", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["xGA_GA_Match"] = matches_df_temp.apply(lambda r: round(r["xG_Against"] / r["Goals_Against"], 2) if r["Goals_Against"] > 0 else 0.0, axis=1)
        render_metric_trend_chart(matches_df_temp, team_stats, "xGA_GA_Match", "xGA_na_gola_straconego", "xGA na Gola Straconego", "xGA / Gol")

    # 9. Celne strzały rywala na gola
    elif defensywa_widok == t("def_opt9"):
        st.subheader("Brick Wall: Opponent Shots on Target Needed per Goal" if selected_lang == "EN" else "Ściana w bramce: Ile celnych strzałów rywal musi oddać na 1 gola?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celne_rywala_na_gola", 
            title_chart="Opponent SoT Needed per Goal",
            title_paper="SoT Against / Goal", 
            value_header="Opp SoT / Goal" if selected_lang == "EN" else "SoT rywala / Gol", 
            color_scale="Greens", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["SoT_GA_Match"] = matches_df_temp.apply(lambda r: round(r["Shots_On_Target_Against"] / r["Goals_Against"], 2) if r["Goals_Against"] > 0 else 0.0, axis=1)
        render_metric_trend_chart(matches_df_temp, team_stats, "SoT_GA_Match", "Celne_rywala_na_gola", "Celne Strzały Rywala na Gola", "SoT / Gol")

    # 10. Gole Uratowane / Stracone (xGA - Gole)
    elif defensywa_widok == t("def_opt10"):
        st.subheader("Goals Prevented (xGA - Goals Conceded)" if selected_lang == "EN" else "Bramki Uratowane ponad stan (Suma xGA - Gole Stracone)")
        st.caption("Positive values (green / right) = Team conceded FEWER goals than expected from opponent threat." if selected_lang == "EN" else "Wartości dodatnie (zielone / w prawo) = zespół stracił MNIEJ goli niż wynikało z zagrożenia rywali.")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Gole_stracone_minus_xGA", 
            title_chart="Defensive Goals Prevented (xGA - GA)",
            title_paper="Goals Prevented (xGA - GA)", 
            value_header="Prevented (xGA - GA)" if selected_lang == "EN" else "Gole uratowane (xGA - GA)", 
            color_scale="RdYlGn", sort_asc=False
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["Prevented_Match"] = (matches_df_temp["xG_Against"] - matches_df_temp["Goals_Against"]).round(2)
        render_metric_trend_chart(matches_df_temp, team_stats, "Prevented_Match", "xGA_na_mecz", "Uratowane Gole (xGA - GA)", "Gole")

    # 11. Strzały rywala z pola karnego
    elif defensywa_widok == t("def_opt11"):
        st.subheader("Opponent Shots Inside Box" if selected_lang == "EN" else "Dopuszczone uderzenia z własnej szesnastki")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Box_Shots_Against_Mean", 
            title_chart="Opponent Shots Inside Box per Match",
            title_paper="Shots Inside Box Against", 
            value_header="Opp Box Shots / 90" if selected_lang == "EN" else "W polu / 90", 
            color_scale="Reds_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "Box_Shots_Against", "Box_Shots_Against_Mean", "Dopuszczone Strzały w Polu", "Strzały")

    # 12. Strzały rywala zza pola karnego
    elif defensywa_widok == t("def_opt12"):
        st.subheader("Opponent Long Range Shots Outside Box" if selected_lang == "EN" else "Dopuszczone uderzenia z dystansu")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Outside_Box_Shots_Against_Mean", 
            title_chart="Opponent Shots Outside Box per Match",
            title_paper="Shots Outside Box Against", 
            value_header="Opp Long Range / 90" if selected_lang == "EN" else "Z dystansu / 90", 
            color_scale="Purples_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "Outside_Box_Shots_Against", "Outside_Box_Shots_Against_Mean", "Dopuszczone Strzały z Dystansu", "Strzały")

    # 13. Rozkład xGA: Open Play vs Set Play
    elif defensywa_widok == t("def_opt13"):
        st.subheader("xGA Breakdown: Open Play vs Set Play" if selected_lang == "EN" else "Skąd rywale stwarzają zagrożenie: Gra Otwarta vs Stałe Fragmenty")
        dist_def = team_stats.copy()
        dist_def["Karne_Inne_xGA"] = (dist_def["xGA_na_mecz"] - dist_def["xGA_OP_na_mecz"] - dist_def["xGA_SP_na_mecz"]).clip(lower=0).round(2)
        dist_def = dist_def.sort_values(by="xGA_na_mecz", ascending=True).reset_index(drop=True)

        fig_dist_d = go.Figure()
        fig_dist_d.add_trace(go.Bar(y=dist_def["Team"], x=dist_def["xGA_OP_na_mecz"], name="Open Play xGA", orientation='h', marker=dict(color="#EF4444")))
        fig_dist_d.add_trace(go.Bar(y=dist_def["Team"], x=dist_def["xGA_SP_na_mecz"], name="Set Play xGA", orientation='h', marker=dict(color="#F59E0B")))
        fig_dist_d.add_trace(go.Bar(y=dist_def["Team"], x=dist_def["Karne_Inne_xGA"], name="Penalties / Other" if selected_lang == "EN" else "Karne/Inne xGA", orientation='h', marker=dict(color="#94A3B8")))
        fig_dist_d.update_layout(barmode='stack', height=620, template="simple_white", paper_bgcolor="#FFFFFF", plot_bgcolor="#F8FAFC", title=dict(text="<b>xGA Breakdown</b>", x=0.04, y=0.96), xaxis=dict(title="xGA / 90"), yaxis=dict(tickfont=dict(size=10.5, color="#1E293B")), legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1))
        st.plotly_chart(fig_dist_d, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xG_OP_Against", "xGA_OP_na_mecz", "Dopuszczone Open Play xGA", "xGA OP")

    # 14. Celność strzałów rywala
    elif defensywa_widok == t("def_opt14"):
        st.subheader("Opponent Shot Accuracy (%)" if selected_lang == "EN" else "Jaki procent strzałów rywali zmierza w światło naszej bramki?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celnosc_strzalow_rywala_proc", 
            title_chart="Opponent Shot Accuracy %",
            title_paper="Opponent Shot Accuracy", 
            value_header="Opp Accuracy %" if selected_lang == "EN" else "Celność rywali %", 
            color_scale="Reds_r", sort_asc=True
        )
        matches_df_temp = matches_df.copy()
        matches_df_temp["Opp_Shot_Acc_Match"] = ((matches_df_temp["Shots_On_Target_Against"] / matches_df_temp["Shots_Against"]) * 100).fillna(0).round(1)
        render_metric_trend_chart(matches_df_temp, team_stats, "Opp_Shot_Acc_Match", "Celnosc_strzalow_rywala_proc", "Celność Strzałów Rywala (%)", "%")

    # 15. Big Chances Conceded
    elif defensywa_widok == t("def_opt15"):
        st.subheader("Big Chances Conceded" if selected_lang == "EN" else "Dopuszczone Wielkie Szanse (Big Chances rywali na mecz)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Big_Chances_Against_Mean", 
            title_chart="Big Chances Conceded per Match",
            title_paper="Big Chances Conceded", 
            value_header="Conceded BC / 90" if selected_lang == "EN" else "Dopuszczone BC / 90", 
            color_scale="Reds_r", sort_asc=True
        )
        render_metric_trend_chart(matches_df, team_stats, "Big_Chances_Against", "Big_Chances_Against_Mean", "Dopuszczone Big Chances", "Szanse")

    # 16. Matryca Odporności
    elif defensywa_widok == t("def_opt16"):
        st.subheader("Resilience Matrix: xGA vs xGA per Goal Conceded" if selected_lang == "EN" else "Matryca Odporności: Dopuszczona jakość (xGA) vs Trudność sforsowania (xGA/Gol)")
        avg_xga = team_stats["xGA_na_mecz"].mean()
        avg_res = team_stats["xGA_na_gola_straconego"].mean()
        fig_m = go.Figure()
        fig_m.add_vline(x=avg_xga, line_dash="dash", line_color="#475569")
        fig_m.add_hline(y=avg_res, line_dash="dash", line_color="#475569")
        for _, row in team_stats.iterrows():
            fig_m.add_trace(go.Scatter(
                x=[row["xGA_na_mecz"]], y=[row["xGA_na_gola_straconego"]], mode="markers+text", text=[row["Team"]], textposition="top center",
                marker=dict(size=12, color="#EF4444", line=dict(width=1.2, color="#0F172A")), showlegend=False
            ))
        fig_m.update_layout(height=600, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", xaxis=dict(title="Conceded xGA / 90 (Lower = Better)" if selected_lang == "EN" else "Dopuszczone xGA / mecz (Mniej = Lepiej)", autorange="reversed"), yaxis=dict(title="xGA Needed to Score Against (Higher = Harder)" if selected_lang == "EN" else "xGA potrzebne na strzelenie gola (Więcej = Twardszy mur)"))
        st.plotly_chart(fig_m, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xG_Against", "xGA_na_mecz", "Dopuszczone xGA", "xGA")

    # 17. Relacja xGA vs xAGOT
    elif defensywa_widok == t("def_opt17"):
        st.subheader("xGA (Pre-Shot Quality) vs xAGOT (Post-Shot Quality on Target)" if selected_lang == "EN" else "Dopuszczone xGA (przed strzałem) vs xAGOT (jakość po strzale rywala w bramkę)")
        corr_d = team_stats["xGA_na_mecz"].corr(team_stats["xAGOT_na_mecz"])
        c1, c2, c3 = st.columns(3)
        c1.metric("Correlation (r)" if selected_lang == "EN" else "Współczynnik korelacji (r)", f"{corr_d:.2f}")
        c2.metric("Average xGA / 90" if selected_lang == "EN" else "Średnie xGA / mecz", f"{team_stats['xGA_na_mecz'].mean():.2f}")
        c3.metric("Average xAGOT / 90" if selected_lang == "EN" else "Średnie xAGOT / mecz", f"{team_stats['xAGOT_na_mecz'].mean():.2f}")

        fig_rel_d = px.scatter(
            team_stats, x="xGA_na_mecz", y="xAGOT_na_mecz", text="Team",
            template="plotly_dark", height=580,
            labels={
                "xGA_na_mecz": "Conceded xGA / 90" if selected_lang == "EN" else "Dopuszczone xGA na mecz",
                "xAGOT_na_mecz": "Conceded xAGOT / 90" if selected_lang == "EN" else "xAGOT na mecz"
            }
        )
        fig_rel_d.update_traces(textposition="top center", marker=dict(size=12, color="#EF4444"))
        st.plotly_chart(fig_rel_d, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "xGOT_Against", "xAGOT_na_mecz", "Dopuszczone xAGOT", "xAGOT")

    # 18. Kontakty rywala vs Strzały rywala
    elif defensywa_widok == t("def_opt18"):
        st.subheader("Opponent Box Efficiency: Touches vs Shots" if selected_lang == "EN" else "Dopuszczanie do szesnastki: Kontakty rywala w naszym polu vs Strzały rywala")
        fig_box_d = px.scatter(
            team_stats, x="Box_Touches_Against_Mean", y="Box_Shots_Against_Mean", text="Team",
            template="plotly_dark", height=580,
            labels={
                "Box_Touches_Against_Mean": "Opp Touches in Box / 90" if selected_lang == "EN" else "Kontakty rywala w szesnastce / mecz",
                "Box_Shots_Against_Mean": "Opp Box Shots / 90" if selected_lang == "EN" else "Strzały rywala z pola karnego / mecz"
            }
        )
        fig_box_d.update_traces(textposition="top center", marker=dict(size=12, color="#EF4444"))
        st.plotly_chart(fig_box_d, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Box_Touches_Against", "Box_Touches_Against_Mean", "Kontakty Rywala w Polu", "Kontakty")

    # 19. Strzały rywali potrzebne na zdobycie bramki
    elif defensywa_widok == t("def_opt19"):
        st.subheader("Opponent Shots Needed to Score" if selected_lang == "EN" else "Ile strzałów rywal musi oddać, by strzelić nam gola?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Strzaly_rywala_na_gola", 
            title_chart="Opponent Shots Needed per Goal",
            title_paper="Shots Against / Goal", 
            value_header="Opp Shots / Goal" if selected_lang == "EN" else "Strzały rywala / 1 Gol", 
            color_scale="Greens", sort_asc=False
        )
        render_metric_trend_chart(matches_df, team_stats, "Shots_Against", "Shots_Against_Mean", "Dopuszczone Strzały Rywala", "Strzały")

    # 20. xAGOT vs Bramki Stracone (Goals Prevented)
    elif defensywa_widok == t("def_opt20"):
        st.subheader("Goalkeeping Impact: xAGOT vs Goals Conceded" if selected_lang == "EN" else "Praca Bramkarza: Jakość celnych strzałów rywala (xAGOT) vs Stracone Gole")
        fig_ps_d = px.scatter(
            team_stats, x="xAGOT_na_mecz", y="Gole_stracone_na_mecz", text="Team",
            template="plotly_dark", height=580,
            labels={
                "xAGOT_na_mecz": "Conceded xAGOT / 90" if selected_lang == "EN" else "xAGOT dopuszczone / mecz",
                "Gole_stracone_na_mecz": "Goals Conceded / 90" if selected_lang == "EN" else "Gole stracone / mecz"
            }
        )
        fig_ps_d.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
        st.plotly_chart(fig_ps_d, use_container_width=True)
        render_metric_trend_chart(matches_df, team_stats, "Goals_Against", "Gole_stracone_na_mecz", "Gole Stracone", "Bramki")

# =========================================================================
# TAB 4: DYSTRYBUCJA I PODANIA (PL / EN)
# =========================================================================
with tab_podania:
    st.header("🎯 Passing, Distribution & Possession Stats" if selected_lang == "EN" else "🎯 Statystyki Podań, Dystrybucji i Posiadania Piłki")
    st.caption("Comprehensive analysis of build-up style, territorial dominance, and opponent metrics." if selected_lang == "EN" else "Kompleksowa analiza kontroli tempa gry: styl budowania akcji, dominacja terytorialna oraz zestawienie z grą rywali.")

    podania_widok = st.selectbox(
        t("pass_select"),
        [t(f"pass_opt{i}") for i in range(1, 10)],
        key="sb_passes_view"
    )
    st.markdown("---")

    # 1. Tabela Zbiorcza Dystrybucji
    if podania_widok == t("pass_opt1"):
        st.subheader("📋 Passing & Possession Overview" if selected_lang == "EN" else "📋 Zestawienie Wskaźników Podań i Posiadania")
        t_cols = [
            "Team", "Mecze", "Posiadanie", "Podania_ogolem", "Passes_Total_Against_Mean", 
            "Podania_celne", "Passes_Own_Half_Mean", "Passes_Opp_Half_Mean", 
            "Passes_Opp_Half_Against_Mean", "Long_Balls_Mean", "Long_Balls_Against_Mean"
        ]
        df_p_show = team_stats[t_cols].copy()
        st.dataframe(
            df_p_show,
            use_container_width=True,
            hide_index=True,
            column_config={
                "Team": "Team" if selected_lang == "EN" else "Drużyna",
                "Mecze": "MP" if selected_lang == "EN" else "M",
                "Posiadanie": st.column_config.NumberColumn("Possession %" if selected_lang == "EN" else "Posiadanie %", format="%.1f %%"),
                "Podania_ogolem": st.column_config.NumberColumn("Passes / 90" if selected_lang == "EN" else "Podania / 90", format="%.1f"),
                "Passes_Total_Against_Mean": st.column_config.NumberColumn("Opp Passes / 90" if selected_lang == "EN" else "Podania rywala / 90", format="%.1f"),
                "Podania_celne": st.column_config.NumberColumn("Acc. Passes / 90" if selected_lang == "EN" else "Celne / 90", format="%.1f"),
                "Passes_Own_Half_Mean": st.column_config.NumberColumn("Own Half" if selected_lang == "EN" else "Własna połowa", format="%.1f"),
                "Passes_Opp_Half_Mean": st.column_config.NumberColumn("Opp Half" if selected_lang == "EN" else "Połowa rywala", format="%.1f"),
                "Passes_Opp_Half_Against_Mean": st.column_config.NumberColumn("Opp at Our Half" if selected_lang == "EN" else "Rywal na naszej", format="%.1f"),
                "Long_Balls_Mean": st.column_config.NumberColumn("Long Balls" if selected_lang == "EN" else "Długie piłki", format="%.1f"),
                "Long_Balls_Against_Mean": st.column_config.NumberColumn("Opp Long Balls" if selected_lang == "EN" else "Długie rywala", format="%.1f"),
            }
        )

    # 2. Posiadanie Piłki
    elif podania_widok == t("pass_opt2"):
        st.subheader("Average Ball Possession (%)" if selected_lang == "EN" else "Średnie Posiadanie Piłki w Sezonie (%)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Posiadanie", 
            title_chart="Average Ball Possession (%)",
            title_paper="Possession Rankings", 
            value_header="Possession %" if selected_lang == "EN" else "Posiadanie %", 
            color_scale="Blues", sort_asc=False
        )

    # 3. Podania Ogółem
    elif podania_widok == t("pass_opt3"):
        st.subheader("Pass Volume: Team Passes vs Opponent Passes" if selected_lang == "EN" else "Wolumen Podań: Podania Własne vs Podania Rywala na mecz")
        sort_opts = ["Team Passes (Highest)", "Passing Differential"] if selected_lang == "EN" else ["Podania Własne (Najwięcej)", "Bilans podań (Własne minus Rywal)"]
        sort_mode = st.radio("Ranking sorting criteria:" if selected_lang == "EN" else "Wybierz kryterium rankingu:", sort_opts, horizontal=True)
        col_sort = "Podania_ogolem" if (sort_mode == sort_opts[0]) else "Bilans_Podan"

        df_sorted_p = team_stats.sort_values(by=col_sort, ascending=False).reset_index(drop=True)
        fig_p_tot = go.Figure()
        fig_p_tot.add_trace(go.Bar(
            y=df_sorted_p["Team"], x=df_sorted_p["Podania_ogolem"], 
            name="Team Passes" if selected_lang == "EN" else "Własne podania", orientation='h',
            marker_color="#38BDF8", text=[f"{v:.0f}" for v in df_sorted_p["Podania_ogolem"]], textposition="outside"
        ))
        fig_p_tot.add_trace(go.Bar(
            y=df_sorted_p["Team"], x=df_sorted_p["Passes_Total_Against_Mean"], 
            name="Opponent Passes" if selected_lang == "EN" else "Podania rywala", orientation='h',
            marker_color="#EF4444", text=[f"{v:.0f}" for v in df_sorted_p["Passes_Total_Against_Mean"]], textposition="outside"
        ))
        fig_p_tot.update_layout(
            barmode="group", height=640, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text="<b>Passes Completed vs Conceded per 90</b>" if selected_lang == "EN" else "<b>Podania wykonane vs Podania dopuszczone rywalom (Śr. / mecz)</b>", x=0.03, y=0.96),
            xaxis=dict(title="Passes / 90" if selected_lang == "EN" else "Średnia liczba podań / mecz", showgrid=True, gridcolor="#21262D"),
            yaxis=dict(autorange="reversed"), legend=dict(orientation="h", y=1.02, x=1)
        )
        st.plotly_chart(fig_p_tot, use_container_width=True)

    # 4. Własna Połowa
    elif podania_widok == t("pass_opt4"):
        st.subheader("Build-up Phase: Passes in Own Half" if selected_lang == "EN" else "Rozegranie w strefie niskiej: Podania na Własnej Połowie")
        own_half_opts = ["1. Team Passes in Own Half", "2. Opponent Passes in Their Own Half"] if selected_lang == "EN" else ["1. Podania własne na swojej połowie", "2. Podania rywali na ich własnej połowie (Czy rywale mają spokój w rozegraniu?)"]
        col_sel_p_sub = st.radio("Perspective:" if selected_lang == "EN" else "Wybierz perspektywę:", own_half_opts, horizontal=True)
        c_name = "Passes_Own_Half_Mean" if col_sel_p_sub == own_half_opts[0] else "Passes_Own_Half_Against_Mean"
        t_header = ("Own Half / 90" if col_sel_p_sub == own_half_opts[0] else "Opp Own Half / 90") if selected_lang == "EN" else ("Własna połowa / 90" if col_sel_p_sub == own_half_opts[0] else "Rywal u siebie / 90")
        
        render_metric_bar_and_paper(
            df=team_stats, col_name=c_name, 
            title_chart="Passes in Own Half Rankings",
            title_paper="Own Half Passes", 
            value_header=t_header, 
            color_scale="Teal", sort_asc=False
        )

    # 5. Połowa Przeciwnika
    elif podania_widok == t("pass_opt5"):
        st.subheader("Territorial Dominance: Passes in Opponent Half" if selected_lang == "EN" else "Obecność w strefie ataku: Podania na Połowie Przeciwnika")
        opp_half_opts = ["1. Team Passes in Opponent Half", "2. Opponent Passes in Our Half (Less = Better)"] if selected_lang == "EN" else ["1. Nasze podania na połowie rywala", "2. Dopuszczone podania rywala na naszej połowie (Mniej = Lepsza kontrola)"]
        col_sel_opp = st.radio("Perspective:" if selected_lang == "EN" else "Wybierz perspektywę:", opp_half_opts, horizontal=True)
        if col_sel_opp == opp_half_opts[0]:
            render_metric_bar_and_paper(
                df=team_stats, col_name="Passes_Opp_Half_Mean", 
                title_chart="Passes in Opposition Half Rankings",
                title_paper="Opposition Half Passes", 
                value_header="Opp Half / 90" if selected_lang == "EN" else "Na połowie rywala / 90", 
                color_scale="Greens", sort_asc=False
            )
        else:
            render_metric_bar_and_paper(
                df=team_stats, col_name="Passes_Opp_Half_Against_Mean", 
                title_chart="Opponent Passes in Our Half Rankings",
                title_paper="Opponent Passes in Our Half", 
                value_header="Opp at Our Half / 90" if selected_lang == "EN" else "Rywal u nas / 90", 
                color_scale="Reds_r", sort_asc=True
            )

    # 6. Długie Piłki
    elif podania_widok == t("pass_opt6"):
        st.subheader("Accurate Long Balls: Team vs Opponent" if selected_lang == "EN" else "Długie zagrania (Accurate Long Balls): Własne vs Rywala")
        col_lb1, col_lb2 = st.columns(2)
        with col_lb1:
            st.markdown("##### " + ("🚀 Team Accurate Long Balls / 90" if selected_lang == "EN" else "🚀 Celne długie piłki własne"))
            fig_lb_w = go.Figure(go.Bar(
                x=team_stats.sort_values(by="Long_Balls_Mean", ascending=False)["Long_Balls_Mean"],
                y=team_stats.sort_values(by="Long_Balls_Mean", ascending=False)["Team"],
                orientation='h', marker_color="#F59E0B",
                text=[f"{v:.1f}" for v in team_stats.sort_values(by="Long_Balls_Mean", ascending=False)["Long_Balls_Mean"]],
                textposition="outside"
            ))
            fig_lb_w.update_layout(height=520, template="simple_white", margin=dict(l=110, r=30, t=30, b=30), yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_lb_w, use_container_width=True)

        with col_lb2:
            st.markdown("##### " + ("🛡️ Opponent Long Balls Conceded / 90" if selected_lang == "EN" else "🛡️ Celne długie piłki zmuszonych do tego rywali"))
            fig_lb_a = go.Figure(go.Bar(
                x=team_stats.sort_values(by="Long_Balls_Against_Mean", ascending=False)["Long_Balls_Against_Mean"],
                y=team_stats.sort_values(by="Long_Balls_Against_Mean", ascending=False)["Team"],
                orientation='h', marker_color="#8B5CF6",
                text=[f"{v:.1f}" for v in team_stats.sort_values(by="Long_Balls_Against_Mean", ascending=False)["Long_Balls_Against_Mean"]],
                textposition="outside"
            ))
            fig_lb_a.update_layout(height=520, template="simple_white", margin=dict(l=110, r=30, t=30, b=30), yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_lb_a, use_container_width=True)

    # 7. Passes per Goal (PpG)
    elif podania_widok == t("pass_opt7"):
        st.subheader("Passes per Goal (PpG)" if selected_lang == "EN" else "⚡ Efektywność Rozegrania: Co ile podań drużyna zdobywa bramkę?")
        ppg_opts = ["1. Team Efficiency (Passes per Goal Scored)", "2. Defensive Wall (Opponent Passes per Goal Conceded)"] if selected_lang == "EN" else ["1. Własna efektywność (Co ile naszych podań strzelamy gola)", "2. Odporność obrony (Co ile podań rywal strzela nam gola)"]
        ppg_perspective = st.radio("Perspective:" if selected_lang == "EN" else "Wybierz perspektywę:", ppg_opts, horizontal=True)

        if ppg_perspective == ppg_opts[0]:
            render_metric_bar_and_paper(
                df=team_stats, col_name="Podania_na_gola",
                title_chart="Passes per Goal Scored",
                title_paper="Passes / Goal Scored",
                value_header="Passes / Goal" if selected_lang == "EN" else "Podań na 1 Gola",
                color_scale="Viridis_r", sort_asc=True
            )
        else:
            render_metric_bar_and_paper(
                df=team_stats, col_name="Podania_rywala_na_gola",
                title_chart="Opponent Passes per Goal",
                title_paper="Opponent Passes / Goal",
                value_header="Opp Passes / Goal" if selected_lang == "EN" else "Podań rywala / Gol",
                color_scale="Greens", sort_asc=False
            )

    # 8. Matryca Kontroli Terytorialnej
    elif podania_widok == t("pass_opt8"):
        st.subheader("Territorial Dominance Matrix" if selected_lang == "EN" else "Matryca Dominacji Terytorialnej: Gra na połowie rywala vs Obrona własnej połowy")
        avg_x_pass = team_stats["Passes_Opp_Half_Mean"].mean()
        avg_y_pass = team_stats["Passes_Opp_Half_Against_Mean"].mean()

        fig_p_matrix = go.Figure()
        fig_p_matrix.add_vline(x=avg_x_pass, line_dash="dash", line_color="#475569")
        fig_p_matrix.add_hline(y=avg_y_pass, line_dash="dash", line_color="#475569")

        for _, row in team_stats.iterrows():
            t_team = row["Team"]
            x_val = row["Passes_Opp_Half_Mean"]
            y_val = row["Passes_Opp_Half_Against_Mean"]
            
            if x_val >= avg_x_pass and y_val <= avg_y_pass:
                col = "#10B981"
            elif x_val < avg_x_pass and y_val > avg_y_pass:
                col = "#EF4444"
            else:
                col = "#38BDF8"

            fig_p_matrix.add_trace(go.Scatter(
                x=[x_val], y=[y_val], mode="markers+text", text=[t_team], textposition="top center",
                marker=dict(size=12, color=col, line=dict(width=1, color="#0F172A")),
                hovertemplate=f"<b>{t_team}</b><br>Opp Half Passes: %{{x:.1f}}<br>Conceded at Home Half: %{{y:.1f}}<extra></extra>",
                showlegend=False
            ))

        fig_p_matrix.update_layout(
            height=600, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text="<b>Territorial Dominance Matrix</b>" if selected_lang == "EN" else "<b>Dominacja Terytorialna: Nasze podania w ataku vs Dopuszczone u siebie</b>", x=0.03, y=0.96),
            xaxis=dict(title="Team Passes in Opposition Half / 90 (More = Better)" if selected_lang == "EN" else "Nasze podania na połowie przeciwnika / mecz (Więcej = Lepiej)"),
            yaxis=dict(title="Opponent Passes in Our Half / 90" if selected_lang == "EN" else "Podania rywala na naszej połowie", autorange="reversed"),
            margin=dict(l=60, r=40, t=60, b=50)
        )
        st.plotly_chart(fig_p_matrix, use_container_width=True)

    # 9. Profil Drużyny: Wykres mecz po meczu
    elif podania_widok == t("pass_opt9"):
        st.subheader("Match-by-Match Passing Profile" if selected_lang == "EN" else "Dynamika Podań Mecz po Meczu dla Wybranego Zespołu")
        team_list_pass = sorted(team_stats["Team"].unique().tolist())
        col_sel_p_team, col_sel_metric = st.columns([1.2, 1.2])
        
        stat_types_en = ["Total Passes", "Own Half Passes", "Opponent Half Passes", "Long Balls"]
        stat_types_pl = ["Podania Ogółem", "Własna Połowa", "Połowa Przeciwnika", "Długie Piłki"]
        
        with col_sel_p_team:
            sel_t_pass = st.selectbox("Select Team:" if selected_lang == "EN" else "Wybierz drużynę:", team_list_pass, index=0, key="sb_pass_team_sel")
        with col_sel_metric:
            sel_m_pass = st.selectbox("Select Metric Type:" if selected_lang == "EN" else "Wybierz rodzaj statystyki:", stat_types_en if selected_lang == "EN" else stat_types_pl, index=0)

        t_m_df = matches_df[matches_df["Team"] == sel_t_pass].copy().reset_index(drop=True)
        t_m_df["Kolejka"] = t_m_df.index + 1

        if sel_m_pass in ["Total Passes", "Podania Ogółem"]:
            y_home, y_opp, lbl_txt = t_m_df["Passes_Total"], t_m_df["Passes_Total_Against"], "Total Passes" if selected_lang == "EN" else "Podania Ogółem"
        elif sel_m_pass in ["Own Half Passes", "Własna Połowa"]:
            y_home, y_opp, lbl_txt = t_m_df["Passes_Own_Half"], t_m_df["Passes_Own_Half_Against"], "Own Half Passes" if selected_lang == "EN" else "Podania na Własnej Połowie"
        elif sel_m_pass in ["Opponent Half Passes", "Połowa Przeciwnika"]:
            y_home, y_opp, lbl_txt = t_m_df["Passes_Opp_Half"], t_m_df["Passes_Opp_Half_Against"], "Opponent Half Passes" if selected_lang == "EN" else "Podania na Połowie Przeciwnika"
        else:
            y_home, y_opp, lbl_txt = t_m_df["Long_Balls"], t_m_df["Long_Balls_Against"], "Accurate Long Balls" if selected_lang == "EN" else "Celne Długie Piłki"

        fig_p_trend = go.Figure()
        fig_p_trend.add_trace(go.Scatter(
            x=t_m_df["Kolejka"], y=y_home, mode="lines+markers", name=f"{sel_t_pass} (Team)",
            line=dict(color="#38BDF8", width=2.5), marker=dict(size=9, color="#38BDF8")
        ))
        fig_p_trend.add_trace(go.Scatter(
            x=t_m_df["Kolejka"], y=y_opp, mode="lines+markers", name="Opponent" if selected_lang == "EN" else "Rywal",
            line=dict(color="#EF4444", width=2.5), marker=dict(size=9, color="#EF4444")
        ))
        fig_p_trend.update_layout(
            height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>{sel_t_pass} - {lbl_txt}: Team vs Opponent</b>" if selected_lang == "EN" else f"<b>{sel_t_pass} - {lbl_txt}: Własne vs Rywal w poszczególnych meczach</b>", x=0.03, y=0.95),
            xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", tickmode="linear", dtick=1),
            yaxis=dict(title=lbl_txt),
            legend=dict(orientation="h", y=1.02, x=1)
        )
        st.plotly_chart(fig_p_trend, use_container_width=True)


# =========================================================================
# TAB 5: STATYSTYKI DRUŻYN (PL / EN)
# =========================================================================
with tab_druzyny:
    st.header("Team Profile & Detailed Match Analytics" if selected_lang == "EN" else "Szczegółowy Profil i Statystyki Drużyny")
    team_list_prof = sorted(team_stats["Team"].unique().tolist())
    col_sel_team, _ = st.columns([1, 2])
    with col_sel_team:
        selected_prof_team = st.selectbox(
            "Select Team:" if selected_lang == "EN" else "Wybierz drużynę:", 
            team_list_prof, 
            index=0, 
            key="sb_team_profile_select"
        )

    team_row = team_stats[team_stats["Team"] == selected_prof_team].iloc[0]
    t_matches = matches_df[matches_df["Team"] == selected_prof_team].copy().reset_index(drop=True)
    t_matches["Kolejka"] = t_matches.index + 1
    m_count = len(t_matches)

    avg_gf_league = team_stats["Gole_na_mecz"].mean()
    avg_ga_league = team_stats["Gole_stracone_na_mecz"].mean()
    avg_xgf_league = team_stats["xG_na_mecz"].mean()
    avg_xga_league = team_stats["xGA_na_mecz"].mean() if "xGA_na_mecz" in team_stats.columns else 0.0
    avg_poss_league = team_stats["Possession_Mean"].mean() if "Possession_Mean" in team_stats.columns else 50.0

    st.markdown("##### " + ("Season Summary" if selected_lang == "EN" else "Podsumowanie Sezonu"))
    col1, col2, col3, col4, col5 = st.columns(5)
    
    gf_sum = int(team_row.get("Goals_For_Sum", t_matches["Goals_For"].sum()))
    gf_avg = team_row.get("Gole_na_mecz", gf_sum / m_count if m_count > 0 else 0)
    col1.metric(
        label="Goals Scored" if selected_lang == "EN" else "Gole Strzelone",
        value=f"{gf_sum} (avg {gf_avg:.2f})" if selected_lang == "EN" else f"{gf_sum} (śr. {gf_avg:.2f})",
        delta=f"{gf_avg - avg_gf_league:+.2f} vs league" if selected_lang == "EN" else f"{gf_avg - avg_gf_league:+.2f} vs liga"
    )

    ga_sum = int(team_row.get("Goals_Against_Sum", t_matches["Goals_Against"].sum()))
    ga_avg = team_row.get("Gole_stracone_na_mecz", ga_sum / m_count if m_count > 0 else 0)
    col2.metric(
        label="Goals Conceded" if selected_lang == "EN" else "Gole Stracone",
        value=f"{ga_sum} (avg {ga_avg:.2f})" if selected_lang == "EN" else f"{ga_sum} (śr. {ga_avg:.2f})",
        delta=f"{ga_avg - avg_ga_league:+.2f} vs league" if selected_lang == "EN" else f"{ga_avg - avg_ga_league:+.2f} vs liga",
        delta_color="inverse"
    )

    xg_sum = float(team_row.get("xG_For_Sum", t_matches["xG_For"].sum()))
    xg_avg = team_row.get("xG_na_mecz", xg_sum / m_count if m_count > 0 else 0)
    col3.metric(
        label="Created xG" if selected_lang == "EN" else "xG Utworzone",
        value=f"{xg_sum:.2f} (avg {xg_avg:.2f})" if selected_lang == "EN" else f"{xg_sum:.2f} (śr. {xg_avg:.2f})",
        delta=f"{xg_avg - avg_xgf_league:+.2f} vs league" if selected_lang == "EN" else f"{xg_avg - avg_xgf_league:+.2f} vs liga"
    )

    xga_col_match = "xG_Against" if "xG_Against" in t_matches.columns else "xGA_For"
    xga_sum = float(t_matches[xga_col_match].sum()) if xga_col_match in t_matches.columns else 0.0
    xga_avg = team_row.get("xGA_na_mecz", xga_sum / m_count if m_count > 0 else 0)
    col4.metric(
        label="Conceded xGA" if selected_lang == "EN" else "xG Dopuszczone",
        value=f"{xga_sum:.2f} (avg {xga_avg:.2f})" if selected_lang == "EN" else f"{xga_sum:.2f} (śr. {xga_avg:.2f})",
        delta=f"{xga_avg - avg_xga_league:+.2f} vs league" if selected_lang == "EN" else f"{xga_avg - avg_xga_league:+.2f} vs liga",
        delta_color="inverse"
    )

    poss_avg = team_row.get("Possession_Mean", t_matches["Possession"].mean() if "Possession" in t_matches.columns else 50.0)
    col5.metric(
        label="Avg Possession" if selected_lang == "EN" else "Śr. Posiadanie Piłki",
        value=f"{poss_avg:.1f}%",
        delta=f"{poss_avg - avg_poss_league:+.1f}% vs league" if selected_lang == "EN" else f"{poss_avg - avg_poss_league:+.1f}% vs liga"
    )

    st.markdown("---")

    team_modules_en = [
        "1. Goals Balance: Scored vs Conceded",
        "2. Threat Balance: xG Created vs xGA Conceded",
        "3. xG Difference (Dominance Trend)",
        "4. Open Play xG: Team vs Conceded",
        "5. Set Play xG: Team vs Conceded",
        "6. Shot Quality on Target (xGOT): Team vs Conceded",
        "7. Shots Inside vs Outside Penalty Box",
        "8. Penalty Box Touches (Touches in Opp Box)",
        "9. Corners: Won vs Conceded",
        "10. Passes & Build-up (Total / Own Half / Opp Half)",
        "11. Duels (Total / Ground / Aerial)",
        "12. Form Tracker: 5-Match Rolling Avg (xG vs xGA)"
    ]
    team_modules_pl = [
        "1. Bilans Bramek: Strzelone vs Stracone",
        "2. Bilans Zagrożenia: xG Utworzone vs xG Dopuszczone",
        "3. Różnice xG (xG Difference): Dominacja mecz po meczu",
        "4. xG z Gry Otwartej (Open Play xG): Własne vs Dopuszczone",
        "5. xG ze Stałych Fragmentów (Set Play xG): Własne vs Dopuszczone",
        "6. Jakość Strzałów Celnych (xGOT): Własne vs Dopuszczone",
        "7. Strzały z pola karnego i z dystansu",
        "8. Kontakty w polu karnym (Touches in Opp Box)",
        "9. Rzuty Rożne (Corners): Wywalczone vs Dopuszczone",
        "10. Dystrybucja i Podania (Ogółem / Własna połowa / Połowa rywala)",
        "11. Pojedynki (Ogółem / Ziemia / Powietrze)",
        "12. Trend Formy: 5-meczowa średnia krocząca (xG vs xGA)"
    ]

    team_view_category = st.selectbox(
        "Select match-by-match module:" if selected_lang == "EN" else "Wybierz moduł analizy mecz po meczu:",
        team_modules_en if selected_lang == "EN" else team_modules_pl,
        key="sb_team_match_view"
    )

    # 1. Gole
    if team_view_category in [team_modules_en[0], team_modules_pl[0]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["Goals_For"], mode="lines+markers", 
            name="Goals Scored" if selected_lang == "EN" else "Gole Strzelone",
            line=dict(color="#10B981", width=2.5), marker=dict(size=9, color="#10B981", line=dict(width=1, color="#FFFFFF")),
            hovertemplate="<b>Matchweek %{x}</b><br>Opponent: " + t_matches["Opponent"] + " (" + t_matches["Venue"] + ")<br>Goals Scored: <b>%{y}</b><extra></extra>" if selected_lang == "EN" else "<b>Kolejka %{x}</b><br>Rywal: " + t_matches["Opponent"] + " (" + t_matches["Venue"] + ")<br>Gole Strzelone: <b>%{y}</b><extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["Goals_Against"], mode="lines+markers", 
            name="Goals Conceded" if selected_lang == "EN" else "Gole Stracone",
            line=dict(color="#EF4444", width=2.5), marker=dict(size=9, color="#EF4444", line=dict(width=1, color="#FFFFFF")),
            hovertemplate="<b>Matchweek %{x}</b><br>Opponent: " + t_matches["Opponent"] + " (" + t_matches["Venue"] + ")<br>Goals Conceded: <b>%{y}</b><extra></extra>" if selected_lang == "EN" else "<b>Kolejka %{x}</b><br>Rywal: " + t_matches["Opponent"] + " (" + t_matches["Venue"] + ")<br>Gole Stracone: <b>%{y}</b><extra></extra>"
        ))
        max_g = max(t_matches["Goals_For"].max(), t_matches["Goals_Against"].max()) if len(t_matches) > 0 else 3
        fig.update_layout(
            height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>{selected_prof_team} - Goals Balance per Matchweek</b>" if selected_lang == "EN" else f"<b>{selected_prof_team} - bilans bramek w poszczególnych meczach</b>", font=dict(size=16, color="#FFFFFF"), x=0.03, y=0.95),
            xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", tickmode="linear", tick0=1, dtick=1, showgrid=True, gridcolor="#30363D"),
            yaxis=dict(title="Goals" if selected_lang == "EN" else "Liczba Goli", tickmode="linear", tick0=0, dtick=1, range=[-0.2, max(3.5, max_g + 0.8)], showgrid=True, gridcolor="#30363D"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)

    # 2. xG vs xGA
    elif team_view_category in [team_modules_en[1], team_modules_pl[1]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["xG_For"], mode="lines+markers", 
            name="Created xG" if selected_lang == "EN" else "xG Utworzone",
            line=dict(color="#38BDF8", width=2.5), marker=dict(size=9, color="#38BDF8", line=dict(width=1, color="#FFFFFF")),
            hovertemplate="<b>Matchweek %{x}</b><br>Opponent: " + t_matches["Opponent"] + "<br>xG: <b>%{y:.2f}</b><extra></extra>" if selected_lang == "EN" else "<b>Kolejka %{x}</b><br>Rywal: " + t_matches["Opponent"] + "<br>xG: <b>%{y:.2f}</b><extra></extra>"
        ))
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["xG_Against"], mode="lines+markers", 
            name="Conceded xGA" if selected_lang == "EN" else "xG Dopuszczone (xGA)",
            line=dict(color="#F59E0B", width=2.5), marker=dict(size=9, color="#F59E0B", line=dict(width=1, color="#FFFFFF")),
            hovertemplate="<b>Matchweek %{x}</b><br>Opponent: " + t_matches["Opponent"] + "<br>xGA: <b>%{y:.2f}</b><extra></extra>" if selected_lang == "EN" else "<b>Kolejka %{x}</b><br>Rywal: " + t_matches["Opponent"] + "<br>xGA: <b>%{y:.2f}</b><extra></extra>"
        ))
        max_v = max(t_matches["xG_For"].max(), t_matches["xG_Against"].max()) if len(t_matches) > 0 else 2.5
        fig.update_layout(
            height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>{selected_prof_team} - Chance Quality: xG vs xGA</b>" if selected_lang == "EN" else f"<b>{selected_prof_team} - bilans jakości sytuacji: xG vs xGA</b>", font=dict(size=16, color="#FFFFFF"), x=0.03, y=0.95),
            xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", tickmode="linear", tick0=1, dtick=1, showgrid=True, gridcolor="#30363D"),
            yaxis=dict(title="Expected Goals (xG)", tickformat=".1f", dtick=0.5, range=[0, max(2.5, max_v * 1.2)], showgrid=True, gridcolor="#30363D"),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)

    # 3. Różnice xG
    elif team_view_category in [team_modules_en[2], team_modules_pl[2]]:
        diff_opts = ["Overall xG Diff", "Open Play xG Diff", "Set Play xG Diff", "npxG Diff", "xGOT Diff"] if selected_lang == "EN" else ["Ogólne xG Diff", "Open Play xG Diff", "Set Play xG Diff", "npxG Diff", "xGOT Diff"]
        metric_choice = st.pills("Balance Variant:" if selected_lang == "EN" else "Wariant bilansu:", diff_opts, default=diff_opts[0], key="pills_sub_xg_diff")
        
        if metric_choice == diff_opts[0]:
            diff = (t_matches["xG_For"] - t_matches["xG_Against"]).round(2)
            lbl = "xG Differential" if selected_lang == "EN" else "Różnica Ogólnego xG"
        elif metric_choice == diff_opts[1]:
            diff = (t_matches["xG_OP_For"] - t_matches["xG_OP_Against"]).round(2)
            lbl = "Open Play xG Diff" if selected_lang == "EN" else "Różnica xG z Gry Otwartej"
        elif metric_choice == diff_opts[2]:
            diff = (t_matches["xG_SP_For"] - t_matches["xG_SP_Against"]).round(2)
            lbl = "Set Play xG Diff" if selected_lang == "EN" else "Różnica xG ze SFG"
        elif metric_choice == diff_opts[3]:
            diff = (t_matches["npxG_For"] - t_matches["npxG_Against"]).round(2)
            lbl = "npxG Diff" if selected_lang == "EN" else "Różnica npxG"
        else:
            diff = (t_matches["xGOT_For"] - t_matches["xGOT_Against"]).round(2)
            lbl = "xGOT Diff" if selected_lang == "EN" else "Różnica xGOT"

        b_colors = ["#10B981" if v >= 0 else "#EF4444" for v in diff]
        fig = go.Figure(go.Bar(
            x=t_matches["Kolejka"], y=diff, marker=dict(color=b_colors, line=dict(color="#0F172A", width=1)),
            text=[f"{v:+.2f}" for v in diff], textposition="outside", textfont=dict(size=11, color="#FFFFFF")
        ))
        max_abs = max(abs(diff.min()), abs(diff.max())) if len(diff) > 0 else 1.5
        fig.update_layout(
            height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>{selected_prof_team} - {lbl} Match-by-Match</b>", font=dict(size=16, color="#FFFFFF"), x=0.03, y=0.95),
            xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", dtick=1, showgrid=True, gridcolor="#30363D"),
            yaxis=dict(title=lbl, range=[-max(1.2, max_abs * 1.3), max(1.2, max_abs * 1.3)], zeroline=True, zerolinecolor="#FFFFFF", zerolinewidth=1.8, showgrid=True, gridcolor="#30363D")
        )
        st.plotly_chart(fig, use_container_width=True)

    # 4. Open Play xG
    elif team_view_category in [team_modules_en[3], team_modules_pl[3]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xG_OP_For"], mode="lines+markers", name="xG OP (Team)" if selected_lang == "EN" else "xG OP (Własne)", line=dict(color="#10B981", width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xG_OP_Against"], mode="lines+markers", name="xG OP (Conceded)" if selected_lang == "EN" else "xG OP (Dopuszczone)", line=dict(color="#EF4444", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - Open Play xG</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="xG OP"))
        st.plotly_chart(fig, use_container_width=True)

    # 5. Set Play xG
    elif team_view_category in [team_modules_en[4], team_modules_pl[4]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xG_SP_For"], mode="lines+markers", name="xG SP (Team)" if selected_lang == "EN" else "xG SFG (Własne)", line=dict(color="#F59E0B", width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xG_SP_Against"], mode="lines+markers", name="xG SP (Conceded)" if selected_lang == "EN" else "xG SFG (Dopuszczone)", line=dict(color="#EC4899", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - Set Play xG</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="xG SP"))
        st.plotly_chart(fig, use_container_width=True)

    # 6. xGOT
    elif team_view_category in [team_modules_en[5], team_modules_pl[5]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xGOT_For"], mode="lines+markers", name="xGOT (Team)" if selected_lang == "EN" else "xGOT (Własne)", line=dict(color="#14B8A6", width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["xGOT_Against"], mode="lines+markers", name="xGOT (Opponent)" if selected_lang == "EN" else "xGOT (Rywala)", line=dict(color="#A855F7", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - xGOT on Target</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="xGOT"))
        st.plotly_chart(fig, use_container_width=True)

    # 7. Strzały w polu i z dystansu
    elif team_view_category in [team_modules_en[6], team_modules_pl[6]]:
        col_s1, col_s2 = st.columns(2)
        with col_s1:
            fig1 = go.Figure()
            fig1.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Box_Shots"], mode="lines+markers", name="Team" if selected_lang == "EN" else "Własne", line=dict(color="#10B981", width=2.5)))
            fig1.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Box_Shots_Against"], mode="lines+markers", name="Opponent" if selected_lang == "EN" else "Rywala", line=dict(color="#EF4444", width=2.5)))
            fig1.update_layout(height=380, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text="<b>Shots Inside Box</b>" if selected_lang == "EN" else "<b>Strzały z pola karnego</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Shots"))
            st.plotly_chart(fig1, use_container_width=True)

        with col_s2:
            fig2 = go.Figure()
            fig2.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Outside_Box_Shots"], mode="lines+markers", name="Team" if selected_lang == "EN" else "Własne", line=dict(color="#38BDF8", width=2.5)))
            fig2.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Outside_Box_Shots_Against"], mode="lines+markers", name="Opponent" if selected_lang == "EN" else "Rywala", line=dict(color="#F59E0B", width=2.5)))
            fig2.update_layout(height=380, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text="<b>Shots Outside Box</b>" if selected_lang == "EN" else "<b>Strzały zza pola karnego</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Shots"))
            st.plotly_chart(fig2, use_container_width=True)

    # 8. Kontakty w polu karnym
    elif team_view_category in [team_modules_en[7], team_modules_pl[7]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Box_Touches"], mode="lines+markers", name="Team Touches in Box" if selected_lang == "EN" else "Kontakty w szesnastce (Własne)", line=dict(color="#14B8A6", width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Box_Touches_Against"], mode="lines+markers", name="Opp Touches in Our Box" if selected_lang == "EN" else "Kontakty rywala w naszym polu", line=dict(color="#EF4444", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - Penalty Box Touches</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Touches"))
        st.plotly_chart(fig, use_container_width=True)

    # 9. Rzuty Rożne
    elif team_view_category in [team_modules_en[8], team_modules_pl[8]]:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Corners"], mode="lines+markers", name="Corners Won" if selected_lang == "EN" else "Rożne Wywalczone", line=dict(color="#38BDF8", width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=t_matches["Corners_Against"], mode="lines+markers", name="Corners Conceded" if selected_lang == "EN" else "Rożne Dopuszczone", line=dict(color="#EF4444", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - Corners Trend</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Corners"))
        st.plotly_chart(fig, use_container_width=True)

    # 10. Podania
    elif team_view_category in [team_modules_en[9], team_modules_pl[9]]:
        pass_pills = ["Total Passes", "Own Half", "Opponent Half", "Long Balls"] if selected_lang == "EN" else ["Podania Ogółem", "Własna Połowa", "Połowa Przeciwnika", "Celne Długie Piłki"]
        pass_sub = st.pills("Zone:" if selected_lang == "EN" else "Wybierz strefę podań:", pass_pills, default=pass_pills[0], key="pills_sub_passes")
        if pass_sub == pass_pills[0]:
            y_w, y_o, col_w, col_o, title_txt = t_matches["Passes_Total"], t_matches["Passes_Total_Against"], "#38BDF8", "#EF4444", "Total Passes" if selected_lang == "EN" else "podania ogółem: własne vs rywal"
        elif pass_sub == pass_pills[1]:
            y_w, y_o, col_w, col_o, title_txt = t_matches["Passes_Own_Half"], t_matches["Passes_Own_Half_Against"], "#10B981", "#F59E0B", "Own Half Passes" if selected_lang == "EN" else "podania na własnej połowie (budowanie akcji)"
        elif pass_sub == pass_pills[2]:
            y_w, y_o, col_w, col_o, title_txt = t_matches["Passes_Opp_Half"], t_matches["Passes_Opp_Half_Against"], "#A855F7", "#EC4899", "Opposition Half Passes" if selected_lang == "EN" else "podania na połowie przeciwnika (dominacja w ataku)"
        else:
            y_w, y_o, col_w, col_o, title_txt = t_matches["Long_Balls"], t_matches["Long_Balls_Against"], "#F59E0B", "#A855F7", "Accurate Long Balls" if selected_lang == "EN" else "celne długie piłki (long balls): własne vs rywal"

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=y_w, mode="lines+markers", name="Team" if selected_lang == "EN" else "Własne", line=dict(color=col_w, width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=y_o, mode="lines+markers", name="Opponent" if selected_lang == "EN" else "Rywala", line=dict(color=col_o, width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - {title_txt}</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Passes"))
        st.plotly_chart(fig, use_container_width=True)

    # 11. Pojedynki
    elif team_view_category in [team_modules_en[10], team_modules_pl[10]]:
        duel_pills = ["Total Duels", "Ground Duels", "Aerial Duels"] if selected_lang == "EN" else ["Pojedynki Ogółem", "Starcia na Ziemi", "Walka w Powietrzu"]
        duel_sub = st.pills("Type:" if selected_lang == "EN" else "Typ pojedynków:", duel_pills, default=duel_pills[0], key="pills_sub_duels")
        if duel_sub == duel_pills[0]:
            y_w, y_o, col_w, title_txt = t_matches["Duels_Won"], t_matches["Duels_Won_Against"], "#38BDF8", "Total Duels Won" if selected_lang == "EN" else "pojedynki ogółem: wygrane własne vs rywal"
        elif duel_sub == duel_pills[1]:
            y_w, y_o, col_w, title_txt = t_matches["Ground_Duels_Won"], t_matches["Ground_Duels_Won_Against"], "#10B981", "Ground Duels Won" if selected_lang == "EN" else "pojedynki na ziemi: wygrane własne vs rywal"
        else:
            y_w, y_o, col_w, title_txt = t_matches["Aerial_Duels_Won"], t_matches["Aerial_Duels_Won_Against"], "#A855F7", "Aerial Duels Won" if selected_lang == "EN" else "pojedynki w powietrzu: wygrane własne vs rywal"

        fig = go.Figure()
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=y_w, mode="lines+markers", name="Won" if selected_lang == "EN" else "Wygrane Własne", line=dict(color=col_w, width=2.5)))
        fig.add_trace(go.Scatter(x=t_matches["Kolejka"], y=y_o, mode="lines+markers", name="Conceded" if selected_lang == "EN" else "Wygrane Rywala", line=dict(color="#EF4444", width=2.5)))
        fig.update_layout(height=430, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", title=dict(text=f"<b>{selected_prof_team} - {title_txt}</b>"), xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Kolejka", dtick=1), yaxis=dict(title="Duels"))
        st.plotly_chart(fig, use_container_width=True)

    
    # 12. Średnia Krocząca (Rolling Average) z wyborem parametrów
    elif team_view_category in [team_modules_en[11], team_modules_pl[11]]:
        col_roll_opt1, col_roll_opt2 = st.columns(2)
        
        # Słownik powiązań: Nazwa opcji -> (Kolumna Drużyny, Kolumna Rywala)
        if selected_lang == "EN":
            roll_metrics = {
                "Expected Goals (xG)": ("xG_For", "xG_Against"),
                "Open Play xG": ("xG_OP_For", "xG_OP_Against"),
                "Shot Quality (xGOT)": ("xGOT_For", "xGOT_Against"),
                "Big Chances": ("Big_Chances", "Big_Chances_Against"),
                "Total Shots": ("Shots", "Shots_Against"),
                "Shots on Target": ("Shots_On_Target", "Shots_On_Target_Against"),
                "Shots Inside Box": ("Box_Shots", "Box_Shots_Against"),
                "Shots Outside Box": ("Outside_Box_Shots", "Outside_Box_Shots_Against"),
                "Total Passes": ("Passes_Total", "Passes_Total_Against"),
                "Accurate Long Balls": ("Long_Balls", "Long_Balls_Against"),
                "Duels Won": ("Duels_Won", "Duels_Won_Against"),
                "Ball Possession (%)": ("Possession", "Possession_Against_Temp")

            }
        else:
            roll_metrics = {
                "Expected Goals (xG)": ("xG_For", "xG_Against"),
                "xG z Gry Otwartej (Open Play)": ("xG_OP_For", "xG_OP_Against"),
                "Jakość Strzałów (xGOT)": ("xGOT_For", "xGOT_Against"),
                "Wielkie Szanse (Big Chances)": ("Big_Chances", "Big_Chances_Against"),
                "Strzały Ogółem": ("Shots", "Shots_Against"),
                "Strzały Celne": ("Shots_On_Target", "Shots_On_Target_Against"),
                "Strzały z pola karnego": ("Box_Shots", "Box_Shots_Against"),
                "Strzały z dystansu": ("Outside_Box_Shots", "Outside_Box_Shots_Against"),
                "Podania Ogółem": ("Passes_Total", "Passes_Total_Against"),
                "Celne Długie Piłki": ("Long_Balls", "Long_Balls_Against"),
                "Wygrane Pojedynki": ("Duels_Won", "Duels_Won_Against"),
                "Posiadanie Piłki (%)": ("Possession", "Possession_Against_Temp")
            }

        with col_roll_opt1:
            selected_roll = st.selectbox(
                "Select Metric to Track:" if selected_lang == "EN" else "Wybierz statystykę do analizy:",
                list(roll_metrics.keys()),
                key="sb_roll_metric"
            )
        with col_roll_opt2:
            roll_window = st.slider(
                "Rolling Window (Matches):" if selected_lang == "EN" else "Okno uśredniania (Liczba meczów):",
                min_value=2, max_value=10, value=5, step=1,
                key="slider_roll_window"
            )

        col_team_m, col_opp_m = roll_metrics[selected_roll]
        
        # Wyliczanie posiadania rywala w locie dla konkretnego meczu
        if selected_roll in ["Ball Possession (%)", "Posiadanie Piłki (%)"]:
            t_matches["Possession_Against_Temp"] = 100.0 - t_matches["Possession"]

        # Matematyka: wygładzona średnia krocząca na podstawie suwaka
        t_matches["Team_Roll"] = t_matches[col_team_m].rolling(window=roll_window, min_periods=1).mean()
        t_matches["Opp_Roll"] = t_matches[col_opp_m].rolling(window=roll_window, min_periods=1).mean()
        
        fig = go.Figure()
        
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["Team_Roll"], 
            mode="lines", 
            name="Team (Avg)" if selected_lang == "EN" else "Własne (Średnia)",
            line=dict(color="#38BDF8", width=3.5, shape="spline"),
            hovertemplate="<b>%{x}</b><br>Team: %{y:.2f}<extra></extra>"
        ))
        
        fig.add_trace(go.Scatter(
            x=t_matches["Kolejka"], y=t_matches["Opp_Roll"], 
            mode="lines", 
            name="Opponent (Avg)" if selected_lang == "EN" else "Rywala (Średnia)",
            line=dict(color="#EF4444", width=3.5, shape="spline"),
            hovertemplate="<b>%{x}</b><br>Opponent: %{y:.2f}<extra></extra>"
        ))
        
        fig.update_layout(
            height=450, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(
                text=f"<b>{selected_prof_team} - {selected_roll} ({roll_window}-Match Rolling Average)</b>" if selected_lang == "EN" else f"<b>{selected_prof_team} - {selected_roll} (Średnia krocząca: {roll_window} m.)</b>", 
                font=dict(size=16, color="#FFFFFF"), x=0.03, y=0.95
            ),
            xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", dtick=1, showgrid=True, gridcolor="#30363D"),
            yaxis=dict(title="Average Value" if selected_lang == "EN" else "Średnia wartość", showgrid=True, gridcolor="#30363D", zeroline=False),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
        )
        st.plotly_chart(fig, use_container_width=True)
    
    
    # Raport kafelkowy (mini-tabele)
    st.markdown("---")
    st.markdown(f"##### " + (f"Detailed Execution & Finishing Report: {selected_prof_team}" if selected_lang == "EN" else f"Szczegółowy Raport Wykonania i Finalizacji: {selected_prof_team}"))

    def get_rank_badge(df, team, sort_col, asc=False):
        df_sorted = df.sort_values(by=sort_col, ascending=asc).reset_index(drop=True)
        idx = df_sorted.index[df_sorted['Team'] == team].tolist()
        if not idx:
            return "-"
        rank = idx[0] + 1
        badge_bg = "#064E3B" if rank <= 3 else ("#1E293B" if rank <= 14 else "#7F1D1D")
        badge_color = "#34D399" if rank <= 3 else ("#94A3B8" if rank <= 14 else "#F87171")
        suf = "th" if rank > 3 else ("st" if rank == 1 else ("nd" if rank == 2 else "rd"))
        txt = f"{rank}{suf}" if selected_lang == "EN" else f"{rank}. msc"
        return f'<span style="background: {badge_bg}; color: {badge_color}; padding: 2px 7px; border-radius: 10px; font-weight: 700; font-size: 11px;">{txt}</span>'

    passes_data = [
        ("Total Passes" if selected_lang == "EN" else "Podania ogółem", int(team_row.get("Passes_Total_Sum", 0)), team_row.get("Podania_ogolem", 0), get_rank_badge(team_stats, selected_prof_team, "Podania_ogolem")),
        ("Own Half" if selected_lang == "EN" else "Własna połowa", int(team_row.get("Passes_Own_Half_Sum", 0)), team_row.get("Passes_Own_Half_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Passes_Own_Half_Mean")),
        ("Opponent Half" if selected_lang == "EN" else "Połowa rywala", int(team_row.get("Passes_Opp_Half_Sum", 0)), team_row.get("Passes_Opp_Half_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Passes_Opp_Half_Mean")),
    ]

    shots_data = [
        ("Total Shots" if selected_lang == "EN" else "Strzały ogółem", int(team_row.get("Shots_Sum", 0)), team_row.get("Strzaly_na_mecz", 0), get_rank_badge(team_stats, selected_prof_team, "Strzaly_na_mecz")),
        ("Shots on Target" if selected_lang == "EN" else "Strzały celne", int(team_row.get("Shots_On_Target_Sum", 0)), team_row.get("Celne_strzaly", 0), get_rank_badge(team_stats, selected_prof_team, "Celne_strzaly")),
        ("Off Target" if selected_lang == "EN" else "Strzały niecelne", int(team_row.get("Shots_Off_Target_Sum", 0)), team_row.get("Shots_Off_Target_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Shots_Off_Target_Mean")),
        ("Blocked Shots" if selected_lang == "EN" else "Zablokowane", int(team_row.get("Blocked_Shots_Sum", 0)), team_row.get("Blocked_Shots_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Blocked_Shots_Mean")),
    ]

    delivery_data = [
        ("Long Balls" if selected_lang == "EN" else "Celne długie piłki", int(team_row.get("Long_Balls_Sum", 0)), team_row.get("Long_Balls_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Long_Balls_Mean")),
        ("Crosses" if selected_lang == "EN" else "Celne dośrodkowania", int(team_row.get("Accurate_Crosses_Sum", 0)), team_row.get("Accurate_Crosses_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Accurate_Crosses_Mean")),
        ("Offsides" if selected_lang == "EN" else "Spalone", int(team_row.get("Offsides_Sum", 0)), team_row.get("Offsides_Mean", 0), get_rank_badge(team_stats, selected_prof_team, "Offsides_Mean", asc=True)),
    ]

    def build_mini_table(title, data_list):
        rows = ""
        for name, total, avg, badge in data_list:
            rows += f"""
            <tr style="border-bottom: 1px solid #21262D; height: 32px;">
                <td style="color: #C9D1D9; font-weight: 500; font-size: 12.5px; padding: 4px 6px;">{name}</td>
                <td style="color: #FFFFFF; font-weight: 700; font-size: 13px; text-align: center; padding: 4px 6px;">{total}</td>
                <td style="color: #8B949E; font-size: 12.5px; text-align: center; padding: 4px 6px;">{avg:.1f}</td>
                <td style="text-align: right; padding: 4px 6px;">{badge}</td>
            </tr>
            """
        m_txt = "Metric" if selected_lang == "EN" else "Metryka"
        tot_txt = "Sum" if selected_lang == "EN" else "Suma"
        avg_txt = "Avg/90" if selected_lang == "EN" else "Śr/M"
        rank_txt = "Rank" if selected_lang == "EN" else "Liga"
        
        return f"""
        <div style="background-color: #161B22; border: 1px solid #30363D; border-radius: 8px; padding: 12px 14px; flex: 1; min-width: 280px;">
            <div style="font-size: 13px; font-weight: 700; color: #58A6FF; margin-bottom: 8px; border-bottom: 1px solid #30363D; padding-bottom: 6px;">
                {title}
            </div>
            <table style="width: 100%; border-collapse: collapse;">
                <thead>
                    <tr style="color: #8B949E; font-size: 11px; text-transform: uppercase;">
                        <th style="text-align: left; padding: 2px 6px;">{m_txt}</th>
                        <th style="text-align: center; padding: 2px 6px;">{tot_txt}</th>
                        <th style="text-align: center; padding: 2px 6px;">{avg_txt}</th>
                        <th style="text-align: right; padding: 2px 6px;">{rank_txt}</th>
                    </tr>
                </thead>
                <tbody>{rows}</tbody>
            </table>
        </div>
        """

    t_shots = "Shots" if selected_lang == "EN" else "Strzały"
    t_passes = "Passing" if selected_lang == "EN" else "Podania"
    t_deliv = "Long Balls & Crosses" if selected_lang == "EN" else "Długie piłki i Dośrodkowania"

    table_html = f"""
    <div style="font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif; display: flex; gap: 14px; flex-wrap: wrap; margin-top: 4px;">
        {build_mini_table(t_shots, shots_data)}
        {build_mini_table(t_passes, passes_data)}
        {build_mini_table(t_deliv, delivery_data)}
    </div>
    """
    components.html(table_html, height=210, scrolling=False)

# =========================================================
    # =========================================================
    # WIZUALIZACJA: MAPA STRZAŁÓW (SYMULACJA: ATAK)
    # =========================================================
    st.markdown("---")
    
    col_map_head, col_map_toggle = st.columns([2.6, 1.4])
    
    with col_map_head:
        if selected_lang == "EN":
            st.markdown(f"##### Shot Map Visualization (Simulated): {selected_prof_team}")
            st.caption("Approximate distribution of shots inside and outside the penalty box. Attacking towards the right goal.")
        else:
            st.markdown(f"##### Wizualizacja Mapy Strzałów (Symulacja): {selected_prof_team}")
            st.caption("Przybliżone rozmieszczenie strzałów z pola karnego i z dystansu. Atak prowadzony na prawą bramkę.")
            
    with col_map_toggle:
        mode_opts = ["Suma (Cały Sezon)", "Średnia (Na mecz)", "Pojedynczy Mecz"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)", "Single Match"]
        shot_mode = st.radio(
            "Tryb wyświetlania:" if selected_lang == "PL" else "Display Mode:", 
            mode_opts, 
            key="radio_shot_map_mode"
        )

    # Przygotowanie listy meczów do wyboru
    pitch_match_labels = [
        f"Kolejka {r['Kolejka']}: vs {r['Opponent']} ({r['Venue']}) [{int(r['Goals_For'])}:{int(r['Goals_Against'])}]"
        for _, r in t_matches.iterrows()
    ]

    sel_pitch_match_idx = 0
    if "Pojedynczy" in shot_mode or "Single" in shot_mode:
        sel_pitch_match_label = st.selectbox(
            "Wybierz mecz do analizy strzałów:" if selected_lang == "PL" else "Select match for shot map:",
            pitch_match_labels,
            index=len(pitch_match_labels) - 1 if len(pitch_match_labels) > 0 else 0,
            key="sb_shot_map_match_sel"
        )
        sel_pitch_match_idx = pitch_match_labels.index(sel_pitch_match_label)

    # Wyznaczenie liczby strzałów w ataku
    if "Pojedynczy" in shot_mode or "Single" in shot_mode:
        m_row_pitch = t_matches.iloc[sel_pitch_match_idx]
        raw_box = m_row_pitch['Box_Shots']
        raw_out = m_row_pitch['Outside_Box_Shots']
        dots_box = int(raw_box)
        dots_out = int(raw_out)
        box_label = f"Inside Box ({dots_box})" if selected_lang == "EN" else f"W polu karnym ({dots_box})"
        out_label = f"Outside Box ({dots_out})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out})"
    elif "Średnia" in shot_mode or "Average" in shot_mode:
        raw_box = t_matches['Box_Shots'].mean()
        raw_out = t_matches['Outside_Box_Shots'].mean()
        dots_box = int(round(raw_box))
        dots_out = int(round(raw_out))
        box_label = f"Inside Box ({raw_box:.1f})" if selected_lang == "EN" else f"W polu karnym ({raw_box:.1f})"
        out_label = f"Outside Box ({raw_out:.1f})" if selected_lang == "EN" else f"Zza pola karnego ({raw_out:.1f})"
    else:
        raw_box = t_matches['Box_Shots'].sum()
        raw_out = t_matches['Outside_Box_Shots'].sum()
        dots_box = int(raw_box)
        dots_out = int(raw_out)
        box_label = f"Inside Box ({dots_box})" if selected_lang == "EN" else f"W polu karnym ({dots_box})"
        out_label = f"Outside Box ({dots_out})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out})"

    # Funkcja rysująca ciemne boisko
    def draw_dark_pitch():
        fig_p = go.Figure()
        line_col = "#475569" 
        fig_p.add_shape(type="rect", x0=0, y0=0, x1=105, y1=68, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="line", x0=52.5, y0=0, x1=52.5, y1=68, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="circle", x0=52.5-9.15, y0=34-9.15, x1=52.5+9.15, y1=34+9.15, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=0, y0=13.84, x1=16.5, y1=54.16, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=88.5, y0=13.84, x1=105, y1=54.16, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=0, y0=24.84, x1=5.5, y1=43.16, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=99.5, y0=24.84, x1=105, y1=43.16, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=-2, y0=30.34, x1=0, y1=37.66, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="rect", x0=105, y0=30.34, x1=107, y1=37.66, line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="circle", x0=10.8, y0=33.8, x1=11.2, y1=34.2, fillcolor=line_col, line_color=line_col)
        fig_p.add_shape(type="circle", x0=93.8, y0=33.8, x1=94.2, y1=34.2, fillcolor=line_col, line_color=line_col)
        fig_p.add_shape(type="path", path="M 16.5, 26.5 A 9.15,9.15 0 0,1 16.5, 41.5", line=dict(color=line_col, width=1.5))
        fig_p.add_shape(type="path", path="M 88.5, 26.5 A 9.15,9.15 0 0,0 88.5, 41.5", line=dict(color=line_col, width=1.5))

        fig_p.update_layout(
            height=530,
            xaxis=dict(visible=False, range=[-3, 108], fixedrange=True),
            yaxis=dict(visible=False, range=[-3, 71], scaleanchor="x", scaleratio=1, fixedrange=True),
            plot_bgcolor="#0E1117", paper_bgcolor="#0E1117", margin=dict(l=10, r=10, t=30, b=10),
            showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5, font=dict(color="#FFFFFF"))
        )
        return fig_p

    fig_pitch = draw_dark_pitch()
    seed_val = sum(ord(c) for c in selected_prof_team) + (sel_pitch_match_idx * 17)

    if dots_box > 0:
        np.random.seed(seed_val)
        box_x = np.random.triangular(88.5, 96.0, 103.0, dots_box)
        box_y = np.random.triangular(18.0, 34.0, 50.0, dots_box)
        fig_pitch.add_trace(go.Scatter(
            x=box_x, y=box_y, mode="markers", name=box_label,
            marker=dict(color="#10B981", size=9 if ("Średnia" in shot_mode or "Pojedynczy" in shot_mode) else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    if dots_out > 0:
        np.random.seed(seed_val + 1)
        out_x = np.random.triangular(65.0, 85.0, 88.4, dots_out) 
        out_y = np.random.triangular(12.0, 34.0, 56.0, dots_out)
        fig_pitch.add_trace(go.Scatter(
            x=out_x, y=out_y, mode="markers", name=out_label,
            marker=dict(color="#38BDF8", size=9 if ("Średnia" in shot_mode or "Pojedynczy" in shot_mode) else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    col_map1, col_map2, col_map3 = st.columns([0.15, 4, 0.15])
    with col_map2:
        st.plotly_chart(fig_pitch, use_container_width=True)

    # =========================================================
    # WIZUALIZACJA: MAPA DOPUSZCZONYCH STRZAŁÓW (SYMULACJA: OBRONA)
    # =========================================================
    st.markdown("---")
    
    col_map_head_def, col_map_toggle_def = st.columns([2.6, 1.4])
    
    with col_map_head_def:
        if selected_lang == "EN":
            st.markdown(f"##### Conceded Shot Map (Simulated): {selected_prof_team}")
            st.caption("Approximate distribution of shots conceded. Opponents attacking towards the left goal.")
        else:
            st.markdown(f"##### Wizualizacja Dopuszczonych Strzałów (Symulacja): {selected_prof_team}")
            st.caption("Przybliżone rozmieszczenie strzałów dopuszczonych rywalom z pola karnego i z dystansu. Obrona na lewą bramkę.")
            
    with col_map_toggle_def:
        mode_opts_def = ["Suma (Cały Sezon)", "Średnia (Na mecz)", "Pojedynczy Mecz"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)", "Single Match"]
        shot_mode_def = st.radio(
            "Tryb wyświetlania:" if selected_lang == "PL" else "Display Mode:", 
            mode_opts_def, 
            key="radio_shot_map_mode_def"
        )

    sel_pitch_def_match_idx = 0
    if "Pojedynczy" in shot_mode_def or "Single" in shot_mode_def:
        sel_pitch_def_match_label = st.selectbox(
            "Wybierz mecz do analizy obrony:" if selected_lang == "PL" else "Select match for defense map:",
            pitch_match_labels,
            index=len(pitch_match_labels) - 1 if len(pitch_match_labels) > 0 else 0,
            key="sb_shot_map_def_match_sel"
        )
        sel_pitch_def_match_idx = pitch_match_labels.index(sel_pitch_def_match_label)

    if "Pojedynczy" in shot_mode_def or "Single" in shot_mode_def:
        m_row_def = t_matches.iloc[sel_pitch_def_match_idx]
        raw_box_def = m_row_def['Box_Shots_Against']
        raw_out_def = m_row_def['Outside_Box_Shots_Against']
        dots_box_def = int(raw_box_def)
        dots_out_def = int(raw_out_def)
        box_label_def = f"Inside Box ({dots_box_def})" if selected_lang == "EN" else f"W polu karnym ({dots_box_def})"
        out_label_def = f"Outside Box ({dots_out_def})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out_def})"
    elif "Średnia" in shot_mode_def or "Average" in shot_mode_def:
        raw_box_def = t_matches['Box_Shots_Against'].mean()
        raw_out_def = t_matches['Outside_Box_Shots_Against'].mean()
        dots_box_def = int(round(raw_box_def))
        dots_out_def = int(round(raw_out_def))
        box_label_def = f"Inside Box ({raw_box_def:.1f})" if selected_lang == "EN" else f"W polu karnym ({raw_box_def:.1f})"
        out_label_def = f"Outside Box ({raw_out_def:.1f})" if selected_lang == "EN" else f"Zza pola karnego ({raw_out_def:.1f})"
    else:
        raw_box_def = t_matches['Box_Shots_Against'].sum()
        raw_out_def = t_matches['Outside_Box_Shots_Against'].sum()
        dots_box_def = int(raw_box_def)
        dots_out_def = int(raw_out_def)
        box_label_def = f"Inside Box ({dots_box_def})" if selected_lang == "EN" else f"W polu karnym ({dots_box_def})"
        out_label_def = f"Outside Box ({dots_out_def})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out_def})"

    fig_pitch_def = draw_dark_pitch()
    seed_val_def = sum(ord(c) for c in selected_prof_team) + (sel_pitch_def_match_idx * 19) + 99

    if dots_box_def > 0:
        np.random.seed(seed_val_def)
        box_x_def = np.random.triangular(2.0, 9.0, 16.5, dots_box_def)
        box_y_def = np.random.triangular(18.0, 34.0, 50.0, dots_box_def)
        fig_pitch_def.add_trace(go.Scatter(
            x=box_x_def, y=box_y_def, mode="markers", name=box_label_def,
            marker=dict(color="#EF4444", size=9 if ("Średnia" in shot_mode_def or "Pojedynczy" in shot_mode_def) else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    if dots_out_def > 0:
        np.random.seed(seed_val_def + 1)
        out_x_def = np.random.triangular(16.6, 22.0, 40.0, dots_out_def) 
        out_y_def = np.random.triangular(12.0, 34.0, 56.0, dots_out_def)
        fig_pitch_def.add_trace(go.Scatter(
            x=out_x_def, y=out_y_def, mode="markers", name=out_label_def,
            marker=dict(color="#F59E0B", size=9 if ("Średnia" in shot_mode_def or "Pojedynczy" in shot_mode_def) else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    col_map1_def, col_map2_def, col_map3_def = st.columns([0.15, 4, 0.15])
    with col_map2_def:
        st.plotly_chart(fig_pitch_def, use_container_width=True)

    # =========================================================
    # MODUŁ STATYSTYCZNY: PROFIL Z-SCORE (STANDARYZACJA)
    # =========================================================
    st.markdown("---")
    st.subheader(
        f" Statistical DNA: {selected_prof_team} (Z-Score Standardization)" 
        if selected_lang == "EN" 
        else f"Statystyczne DNA: {selected_prof_team} (Standaryzacja Z-Score)"
    )
    st.caption(
        "Shows how many standard deviations (σ) the team deviates from the average (0.00 = Average, +1.50 = European Elite, -1.50 = Bottom tier)."
        if selected_lang == "EN"
        else "Pokazuje, o ile odchyleń standardowych (σ) zespół odstaje od średniej stawki (0.00 = Średnia, +1.50 = Elita, -1.50 = Strefa słabości)."
    )

    # Zestaw 8 kluczowych metryk taktycznych do profilu Z-Score
    if selected_lang == "EN":
        z_metrics = {
            "Expected Goals (xG / 90)": "xG_na_mecz",
            "Open Play Threat (xG OP)": "xG_OP_na_mecz",
            "Finishing Edge (Goals - xG)": "Gole_minus_xG",
            "Box Threat (Box Shots)": "Strzaly_z_pola_karnego",
            "Defensive Resilience (1 / xGA)": "xGA_na_mecz",  # odwrócimy znak dla obrony
            "Goalkeeper Impact (Prevented)": "Goals_Prevented_Mecz",
            "Territorial Dominance (Opp Half)": "Passes_Opp_Half_Mean",
            "Ball Possession (%)": "Posiadanie",
            "Duels Won / 90": "Pojedynki_Wygrane"
        }
    else:
        z_metrics = {
            "Kreacja Zagrożenia (xG / mecz)": "xG_na_mecz",
            "Atak Pozycyjny (xG Open Play)": "xG_OP_na_mecz",
            "Skuteczność (Gole - Suma xG)": "Gole_minus_xG",
            "Strzały z pola karnego": "Strzaly_z_pola_karnego",
            "Szczelność Defensywy (1 / xGA)": "xGA_na_mecz",
            "Interwencje Bramkarza (Prevented)": "Goals_Prevented_Mecz",
            "Gra na połowie rywala": "Passes_Opp_Half_Mean",
            "Posiadanie Piłki (%)": "Posiadanie",
            "Wygrane Pojedynki": "Pojedynki_Wygrane"
        }

    z_df = calculate_team_zscores(team_stats, selected_prof_team, z_metrics)

    # Odwracamy Z-Score dla dopuszczonego xGA: mniej xGA = lepszy wynik (w prawo)
    for idx, row in z_df.iterrows():
        if "xGA" in row["Metric"]:
            z_df.at[idx, "Z_Score"] = -row["Z_Score"]

    # Kolorowanie słupków: zielony dla atutów, czerwony dla mankamentów
    z_colors = ["#10B981" if z >= 0 else "#EF4444" for z in z_df["Z_Score"]]

    fig_z = go.Figure()
    fig_z.add_trace(go.Bar(
        x=z_df["Z_Score"],
        y=z_df["Metric"],
        orientation='h',
        marker=dict(color=z_colors, line=dict(color="#0F172A", width=0.8)),
        text=[f"{z:+.2f}σ" for z in z_df["Z_Score"]],
        textposition="outside",
        textfont=dict(size=11, color="#FFFFFF"),
        hovertemplate="<b>%{y}</b><br>Z-Score: <b>%{x:+.2f}σ</b><extra></extra>"
    ))

    # Linie referencyjne odchylenia standardowego
    fig_z.add_vline(x=0, line_color="#FFFFFF", line_width=1.5)
    fig_z.add_vline(x=1.5, line_dash="dash", line_color="#10B981", line_width=1, annotation_text="Elite (+1.5σ)", annotation_position="top right")
    fig_z.add_vline(x=-1.5, line_dash="dash", line_color="#EF4444", line_width=1, annotation_text="Weak (-1.5σ)", annotation_position="top left")

    fig_z.update_layout(
        height=480,
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        xaxis=dict(
            title="Deviation from Baseline (Z-Score in Standard Deviations σ)" if selected_lang == "EN" else "Odchylenie od średniej stawki (Z-Score w odchyleniach σ)",
            range=[-2.8, 2.8],
            zeroline=False,
            showgrid=True,
            gridcolor="#21262D"
        ),
        yaxis=dict(autorange="reversed"),
        margin=dict(l=150, r=40, t=40, b=40)
    )

    st.plotly_chart(fig_z, use_container_width=True)

    # =========================================================
    # MODUŁ: CO NAPRAWDĘ DAJE PUNKTY TEJ DRUŻYNIE? (KEY DRIVERS)
    # =========================================================
    st.markdown("---")
    st.subheader(
        f" Key Performance Drivers: What Actually Wins Games for {selected_prof_team}?"
        if selected_lang == "EN"
        else f" Co Naprawdę Daje Punkty Drużynie: {selected_prof_team}?"
    )
    st.caption(
        "Correlation between specific match metrics and Points gained by this team. Identifies which tactical elements are critical to their success."
        if selected_lang == "EN"
        else "Współczynnik korelacji pomiędzy elementami gry w meczu a zdobytymi punktami przez ten zespół. Pokazuje, co realnie napędza ich zwycięstwa."
    )

    # Pula metryk meczowych do zbadania w meczach tej drużyny
    driver_metrics = [
        ("Wygrane Pojedynki", "Duels Won", "Duels_Won"),
        ("Kontakty w Szesnastce", "Box Touches", "Box_Touches"),
        ("Strzały z Pola Karnego", "Box Shots", "Box_Shots"),
        ("xG z Gry Otwartej", "Open Play xG", "xG_OP_For"),
        ("xG ze SFG", "Set Play xG", "xG_SP_For"),
        ("Podania na Połowie Rywala", "Opp Half Passes", "Passes_Opp_Half"),
        ("Podania na Własnej Połowie", "Own Half Passes", "Passes_Own_Half"),
        ("Posiadanie Piłki (%)", "Possession %", "Possession"),
        ("Długie Piłki", "Long Balls", "Long_Balls"),
        ("Rzuty Rożne", "Corners", "Corners"),
        ("Obrony Bramkarza", "Saves", "Keeper_Saves")
    ]

    drivers_list = []
    
    # Liczymy korelację dla każdego parametru z punktami (Points)
    for lbl_pl, lbl_en, col in driver_metrics:
        if col in t_matches.columns and t_matches[col].std() > 0:
            corr = t_matches[col].corr(t_matches["Points"])
            if not np.isnan(corr):
                lbl = lbl_en if selected_lang == "EN" else lbl_pl
                drivers_list.append({
                    "Metric": lbl,
                    "Correlation": round(corr, 2),
                    "AbsCorr": abs(corr)
                })

    if len(drivers_list) > 0:
        df_drivers = pd.DataFrame(drivers_list).sort_values(by="Correlation", ascending=False).reset_index(drop=True)

        col_drv_chart, col_drv_txt = st.columns([1.3, 1.0])

        with col_drv_chart:
            bar_colors = [
                "#10B981" if c >= 0.3 else ("#EF4444" if c <= -0.3 else "#64748B")
                for c in df_drivers["Correlation"]
            ]

            fig_drv = go.Figure(go.Bar(
                y=df_drivers["Metric"],
                x=df_drivers["Correlation"],
                orientation='h',
                marker=dict(color=bar_colors),
                text=[f"{c:+.2f}" for c in df_drivers["Correlation"]],
                textposition="outside",
                textfont=dict(color="#FFFFFF", size=11)
            ))

            fig_drv.update_layout(
                height=450,
                template="plotly_dark",
                paper_bgcolor="#0E1117",
                plot_bgcolor="#161B22",
                margin=dict(l=160, r=40, t=30, b=30),
                yaxis=dict(autorange="reversed"),
                xaxis=dict(
                    title="Correlation with Points (-1 to +1)" if selected_lang == "EN" else "Korelacja ze zdobytymi punktami (-1 do +1)",
                    range=[-1.0, 1.0],
                    zeroline=True,
                    zerolinecolor="#FFFFFF",
                    gridcolor="#21262D"
                )
            )
            st.plotly_chart(fig_drv, use_container_width=True)

        with col_drv_txt:
            top_positive = df_drivers.iloc[0]
            bottom_metric = df_drivers.iloc[-1]
            
            duels_row = df_drivers[df_drivers["Metric"].str.contains("Pojedynki|Duels")]
            own_pass_row = df_drivers[df_drivers["Metric"].str.contains("Własnej|Own Half")]

            st.markdown("####  Wnioski Taktyczne" if selected_lang == "PL" else "####  Tactical Takeaways")
            
            st.success(
                f" **Główny motor napędowy:** Najsilniejszy związek z punktami ma **{top_positive['Metric']}** (r = {top_positive['Correlation']:+.2f}). Gdy ten element funkcjonuje, zespół regularnie punktuje."
                if selected_lang == "PL"
                else f" **Primary Success Driver:** The highest correlation with points belongs to **{top_positive['Metric']}** (r = {top_positive['Correlation']:+.2f})."
            )

            if bottom_metric["Correlation"] < 0:
                st.warning(
                    f" **Pułapka stylu:** **{bottom_metric['Metric']}** ma ujemną korelację z punktami (r = {bottom_metric['Correlation']:+.2f}). Często duża liczba w tej statystyce oznacza, że mecz nie układał się po ich myśli (np. gonienie wyniku)."
                    if selected_lang == "PL"
                    else f" **Style Trap:** **{bottom_metric['Metric']}** is negatively correlated with points (r = {bottom_metric['Correlation']:+.2f})."
                )

            if not duels_row.empty and not own_pass_row.empty:
                r_d = duels_row.iloc[0]["Correlation"]
                r_p = own_pass_row.iloc[0]["Correlation"]
                
                if r_d > r_p:
                    porownanie_txt = f"Wygrane pojedynki (r = {r_d:+.2f}) są dla {selected_prof_team} **znacznie cenniejsze** niż bezpieczne klepanie na własnej połowie (r = {r_p:+.2f})."
                else:
                    porownanie_txt = f"Spokojne rozegranie od tyłu (r = {r_p:+.2f}) daje tej drużynie **więcej korzyści punktowych** niż bezpośrednia walka fizyczna o pojedynki (r = {r_d:+.2f})."
                
                st.info(f" **Pojedynki vs Rozegranie:** {porownanie_txt}")


    # =========================================================
    # MODUŁ: RAPORT POMECZOWY AI (SINGLE MATCH DEBRIEF - FULL)
    # =========================================================
    st.markdown("---")
    st.subheader(
        f" Single Match Tactical Debrief: {selected_prof_team}"
        if selected_lang == "EN"
        else f" Pomeczowy Raport Analityczny AI: {selected_prof_team}"
    )
    st.caption(
        "Complete statistical breakdown across all available match metrics comparing the performance to team seasonal norms and league baselines."
        if selected_lang == "EN"
        else "Kompletna pomeczowa analiza wszystkich dostępnych metryk: zderzenie występu z normą sezonową drużyny oraz średnią ligową."
    )

    # Budujemy etykiety meczów do wyboru z listy
    match_labels = []
    for idx, r_m in t_matches.iterrows():
        res_str = f"{int(r_m['Goals_For'])}:{int(r_m['Goals_Against'])}"
        lbl = f"Kolejka {r_m['Kolejka']}: vs {r_m['Opponent']} ({r_m['Venue']}) [{res_str}]"
        match_labels.append(lbl)

    col_match_sel, col_sens_sel = st.columns([2.2, 1.2])
    with col_match_sel:
        selected_match_label = st.selectbox(
            "Wybierz spotkanie do analizy:" if selected_lang == "PL" else "Select fixture to analyze:",
            match_labels,
            index=len(match_labels) - 1 if len(match_labels) > 0 else 0,
            key="sb_single_match_debrief"
        )
    with col_sens_sel:
        # Suwak czułości wykrywania odchyleń pomeczowych
        match_threshold_pct = st.slider(
            "Próg anomalii meczowej (% odchyłki):" if selected_lang == "PL" else "Match Anomaly Threshold (% dev):",
            min_value=10, max_value=50, value=20, step=5,
            key="slider_match_anomaly_sens"
        )

    sel_idx = match_labels.index(selected_match_label)
    m_row = t_matches.iloc[sel_idx]

    # Kompletna pula wszystkich dostępnych w bazie danych metryk meczowych:
    # (Nazwa PL, Nazwa EN, Kolumna w meczu, Kolumna średniej w team_stats, Czy_mniej_znaczy_lepiej)
    match_eval_pool = [
        # BRAMKI I FINISZ
        ("Gole Strzelone", "Goals Scored", "Goals_For", "Gole_na_mecz", False),
        ("Gole Stracone", "Goals Conceded", "Goals_Against", "Gole_stracone_na_mecz", True),
        ("Wykreowane xG", "Created xG", "xG_For", "xG_na_mecz", False),
        ("Dopuszczone xGA", "Conceded xGA", "xG_Against", "xGA_na_mecz", True),
        ("xG z Gry Otwartej (OP)", "Open Play xG", "xG_OP_For", "xG_OP_na_mecz", False),
        ("xGA z Gry Otwartej (OP)", "Open Play xGA", "xG_OP_Against", "xGA_OP_na_mecz", True),
        ("xG ze SFG", "Set Play xG", "xG_SP_For", "xG_SP_na_mecz", False),
        ("xGA ze SFG", "Set Play xGA", "xG_SP_Against", "xGA_SP_na_mecz", True),
        ("npxG (bez karnych)", "Non-Penalty xG", "npxG_For", "npxG_na_mecz", False),
        ("npxGA (dopuszczone bez karnych)", "Non-Penalty xGA", "npxG_Against", "npxGA_na_mecz", True),
        ("xGOT (Jakość Strzałów Celnych)", "Shot Quality (xGOT)", "xGOT_For", "xGOT_na_mecz", False),
        ("xAGOT (Czyste Strzały Rywali)", "Opponent Shot Quality (xAGOT)", "xGOT_Against", "xAGOT_na_mecz", True),
        
        # STRZAŁY I POLE KARNE
        ("Strzały Ogółem", "Total Shots", "Shots", "Strzaly_na_mecz", False),
        ("Strzały Dopuszczone Rywalom", "Shots Conceded", "Shots_Against", "Shots_Against_Mean", True),
        ("Strzały Celne", "Shots on Target", "Shots_On_Target", "Celne_strzaly", False),
        ("Strzały Celne Rywali", "Shots on Target Conceded", "Shots_On_Target_Against", "Shots_On_Target_Against_Mean", True),
        ("Strzały z Szesnastki", "Box Shots", "Box_Shots", "Strzaly_z_pola_karnego", False),
        ("Strzały Rywala z Naszej Szesnastki", "Opponent Box Shots", "Box_Shots_Against", "Box_Shots_Against_Mean", True),
        ("Strzały z Dystansu", "Outside Box Shots", "Outside_Box_Shots", "Strzaly_zza_pola_karnego", False),
        ("Kontakty w Polu Karnym Rywala", "Box Touches", "Box_Touches", "Box_Touches_Mean", False),
        ("Kontakty Rywala w Naszym Polu", "Opponent Touches in Our Box", "Box_Touches_Against", "Box_Touches_Against_Mean", True),
        ("Wielkie Szanse (Big Chances)", "Big Chances", "Big_Chances", "Big_Chances", False),
        ("Zmarnowane Wielkie Szanse", "Big Chances Missed", "Big_Chances_Missed", "Big_Chances_Missed", True),
        
        # DYSTRYBUCJA I KONTROLA
        ("Posiadanie Piłki (%)", "Ball Possession (%)", "Possession", "Posiadanie", False),
        ("Podania Ogółem", "Total Passes", "Passes_Total", "Podania_ogolem", False),
        ("Podania Celne", "Accurate Passes", "Passes_Acc", "Podania_celne", False),
        ("Podania na Połowie Rywala", "Opponent Half Passes", "Passes_Opp_Half", "Passes_Opp_Half_Mean", False),
        ("Podania na Własnej Połowie", "Own Half Passes", "Passes_Own_Half", "Passes_Own_Half_Mean", False),
        ("Dopuszczone Podania na Naszej Połowie", "Opp Passes at Our Half", "Passes_Opp_Half_Against", "Passes_Opp_Half_Against_Mean", True),
        ("Celne Długie Piłki", "Accurate Long Balls", "Long_Balls", "Long_Balls_Mean", False),
        ("Celne Dośrodkowania", "Accurate Crosses", "Accurate_Crosses", "Accurate_Crosses_Mean", False),
        
        # FAZA PRZEJŚCIOWA, DEFENSIWA I WALKA
        ("Wygrane Pojedynki Ogółem", "Duels Won", "Duels_Won", "Pojedynki_Wygrane", False),
        ("Pojedynki na Ziemi Wygrane", "Ground Duels Won", "Ground_Duels_Won", "Ground_Duels_Won", False),
        ("Pojedynki w Powietrzu Wygrane", "Aerial Duels Won", "Aerial_Duels_Won", "Aerial_Duels_Won", False),
        ("Odbiory", "Tackles", "Tackles", "Odbiory", False),
        ("Przejęcia", "Interceptions", "Interceptions", "Przejecia", False),
        ("Obrony Bramkarza", "Goalkeeper Saves", "Keeper_Saves", "Keeper_Saves_Mean", False),
        ("Rzuty Rożne Wywalczone", "Corners Won", "Corners", "Rzuty_Rozne", False),
        ("Rzuty Rożne Dopuszczone", "Corners Conceded", "Corners_Against", "Corners_Against", True),
        ("Spalone", "Offsides", "Offsides", "Offsides_Mean", True),

        # DYSCYPLINA I INTERWENCJE
        ("Faule Popełnione", "Fouls Committed", "Fouls", "Fouls_Mean", True),
        ("Faule Wymuszone na Rywalu", "Fouls Won", "Fouls_Against", "Fouls_Against_Mean", False),
        ("Żółte Kartki", "Yellow Cards", "Yellow_Cards", "Yellow_Cards_Mean", True),
        ("Wybicia Piłki (Clearances)", "Clearances", "Clearances", "Clearances_Mean", False),
        ("Zablokowane Strzały (Bloki)", "Shots Blocked", "Blocks", "Blocks_Mean", False),
        ("Udane Dryblingi", "Successful Dribbles", "Successful_Dribbles", "Dribbles_Mean", False),
        ("Strzały w Obramowanie (Słupki/Poprzeczki)", "Hit Woodwork", "Hit_Woodwork", "Woodwork_Mean", False),
        ("Wrzuty z Autu", "Throw-ins", "Throws", "Throws_Mean", False),
        ("Czerwone Kartki", "Red Cards", "Red_Cards", "Red_Cards_Mean", True),

        
    ]

    m_positives = []
    m_negatives = []
    m_diff_table = []

    for lbl_pl, lbl_en, m_col, team_col, lower_is_better in match_eval_pool:
        if m_col in m_row and team_col in team_stats.columns:
            m_val = float(m_row[m_col])
            t_avg = float(team_row[team_col])
            lg_avg = float(team_stats[team_col].mean())
            lg_std = float(team_stats[team_col].std()) if team_stats[team_col].std() > 0 else 1.0

            # Odchylenie od własnej normy
            delta_team = m_val - t_avg
            pct_team = (delta_team / t_avg * 100.0) if t_avg > 0 else 0.0

            # Z-Score względem ligi w tym meczu
            z_match = (m_val - lg_avg) / lg_std

            lbl = lbl_en if selected_lang == "EN" else lbl_pl

            # Rejestracja w tabeli zbiorczej
            fmt = "{:.1f}%" if "%" in lbl else ("{:.0f}" if any(w in lbl for w in ["Gole", "Goals", "Strzały", "Shots", "Podania", "Passes", "Pojedynki", "Duels", "Odbiory", "Rożne", "Corners"]) else "{:.2f}")
            m_diff_table.append({
                "Metryka": lbl,
                "Mecz": fmt.format(m_val),
                "Śr. Zespołu": fmt.format(t_avg),
                "Delta vs Zespół": f"{delta_team:+.2f} ({pct_team:+.0f}%)",
                "Śr. Ligi": fmt.format(lg_avg),
                "Z-Score Ligi": f"{z_match:+.2f}σ"
            })

            # Klasyfikacja wniosków AI z uwzględnieniem suwaka
            if (delta_team > 0 and not lower_is_better and pct_team >= match_threshold_pct) or (delta_team < 0 and lower_is_better and pct_team <= -match_threshold_pct):
                m_positives.append(
                    f" **{lbl}**: **{m_val:.2f}** (Aż **{pct_team:+.0f}%** powyżej własnej normy {t_avg:.2f} | {z_match:+.1f}σ w skali ligi)"
                )
            elif (delta_team < 0 and not lower_is_better and pct_team <= -match_threshold_pct) or (delta_team > 0 and lower_is_better and pct_team >= match_threshold_pct):
                m_negatives.append(
                    f" **{lbl}**: **{m_val:.2f}** (Aż **{pct_team:+.0f}%** poniżej własnej normy {t_avg:.2f} | {z_match:+.1f}σ w skali ligi)"
                )

    # Wyświetlanie kart wniosków AI
    col_rep_pos, col_rep_neg = st.columns(2)

    with col_rep_pos:
        st.markdown(f"####  Co Funkcjonowało Ponad Stan? ({len(m_positives)})" if selected_lang == "PL" else f"####  Overperformed Metrics ({len(m_positives)})")
        if m_positives:
            for item in m_positives:
                st.success(item)
        else:
            st.info("Brak spektakularnych odskoków in plus — zespół grał na swoim typowym poziomie." if selected_lang == "PL" else "No significant overperformance detected.")

    with col_rep_neg:
        st.markdown(f"####  Co Wyraźnie Zawiodło? ({len(m_negatives)})" if selected_lang == "PL" else f"####  Underperformed Metrics ({len(m_negatives)})")
        if m_negatives:
            for item in m_negatives:
                st.error(item)
        else:
            st.info("Brak drastycznych załamań formy w żadnym z kluczowych parametrów." if selected_lang == "PL" else "No major stylistic collapse detected.")

    # Kompletna tabela ze wszystkimi parametrami
    st.markdown("---")
    st.markdown("#####  " + ("Complete Metric Breakdown (Match vs Team vs League)" if selected_lang == "EN" else "Kompletne Zestawienie Wszystkich Metryk (Mecz vs Średnia Zespołu vs Średnia Ligi)"))
    df_match_display = pd.DataFrame(m_diff_table)
    st.dataframe(df_match_display, use_container_width=True, hide_index=True)


def generate_tactical_ai_insights(df, team_a, team_b, metrics_config, threshold=0.70, clash_threshold=0.80, lang="PL"):
    """
    Silnik analityczny AI:
    Wykrywa anomalie ligowe oraz bezpośrednie dysproporcje na podstawie zadanego progu odchylenia standardowego (sigma).
    """
    row_a = df[df["Team"] == team_a].iloc[0]
    row_b = df[df["Team"] == team_b].iloc[0]
    
    insights_a = []
    insights_b = []
    h2h_clashes = []

    for label_pl, label_en, col, lower_is_better in metrics_config:
        if col not in df.columns:
            continue

        lbl = label_en if lang == "EN" else label_pl
        val_a = float(row_a[col])
        val_b = float(row_b[col])
        mean_val = df[col].mean()
        std_val = df[col].std() if df[col].std() > 0 else 1.0
        
        za = (val_a - mean_val) / std_val
        zb = (val_b - mean_val) / std_val
        
        # Inwersja dla metryk defensywnych (mniej = lepiej)
        norm_za = -za if lower_is_better else za
        norm_zb = -zb if lower_is_better else zb
        
        # Wykrywanie atutów i mankamentów Drużyny A
        if norm_za >= threshold:
            insights_a.append((f" **{lbl}**: {val_a:.2f} *(+{za:+.1f}σ ponad ligę)*", "strength"))
        elif norm_za <= -threshold:
            insights_a.append((f" **{lbl}**: {val_a:.2f} *({za:+.1f}σ poniżej ligi)*", "weakness"))
            
        # Wykrywanie atutów i mankamentów Drużyny B
        if norm_zb >= threshold:
            insights_b.append((f" **{lbl}**: {val_b:.2f} *(+{zb:+.1f}σ ponad ligę)*", "strength"))
        elif norm_zb <= -threshold:
            insights_b.append((f" **{lbl}**: {val_b:.2f} *({zb:+.1f}σ poniżej ligi)*", "weakness"))
            
        # Wykrywanie bezpośrednich dysproporcji stylu
        diff_z = norm_za - norm_zb
        if abs(diff_z) >= clash_threshold:
            leader = team_a if diff_z > 0 else team_b
            chaser = team_b if diff_z > 0 else team_a
            v_lead = val_a if diff_z > 0 else val_b
            v_chase = val_b if diff_z > 0 else val_a
            
            if lang == "EN":
                h2h_clashes.append(
                    f" **Major Disparity in {lbl}**: **{leader}** ({v_lead:.2f}) holds a clear edge over **{chaser}** ({v_chase:.2f}) [Δ {abs(diff_z):.1f}σ]."
                )
            else:
                h2h_clashes.append(
                    f" **Wyraźna przewaga w: {lbl}**: **{leader}** ({v_lead:.2f}) dominuje nad **{chaser}** ({v_chase:.2f}) [Różnica: {abs(diff_z):.1f}σ]."
                )

    return insights_a, insights_b, h2h_clashes


    
    

# =========================================================================
# TAB: PORÓWNANIE DRUŻYN (H2H)
# =========================================================================
with tab_h2h:
    st.header(" Head-to-Head Team Comparison" if selected_lang == "EN" else " Porównanie Zespołów (Head-to-Head)")
    st.caption(
        "Compare two teams directly across tactical styles and key performance metrics." 
        if selected_lang == "EN" 
        else "Zestaw ze sobą dwa zespoły, aby bezpośrednio porównać ich profile taktyczne i kluczowe wskaźniki."
    )
    
    # Pobranie alfabetycznej listy drużyn
    team_list_h2h = sorted(team_stats["Team"].unique().tolist())
    
    # Rozkład na dwie kolumny (Drużyna A i Drużyna B)
    col_h2h_1, col_h2h_2 = st.columns(2)
    
    with col_h2h_1:
        team_a = st.selectbox(
            "Select Team A:" if selected_lang == "EN" else "Wybierz Drużynę A:",
            team_list_h2h,
            index=0,  # Domyślnie pierwsza drużyna na liście
            key="sb_h2h_team_a"
        )
        
    with col_h2h_2:
        team_b = st.selectbox(
            "Select Team B:" if selected_lang == "EN" else "Wybierz Drużynę B:",
            team_list_h2h,
            index=1 if len(team_list_h2h) > 1 else 0,  # Domyślnie druga drużyna, żeby nie porównywać z samą sobą
            key="sb_h2h_team_b"
        )
        
    st.markdown("---")
    
    # Wyciągamy wiersze dla obu drużyn
    row_a = team_stats[team_stats["Team"] == team_a].iloc[0]
    row_b = team_stats[team_stats["Team"] == team_b].iloc[0]

    # Lista metryk: (Etykieta, Nazwa_kolumny, Czy_mniej_znaczy_lepiej)
    if selected_lang == "EN":
        h2h_metrics = [
            ("Goals Scored / 90", "Gole_na_mecz", False),
            ("Goals Conceded / 90", "Gole_stracone_na_mecz", True),
            ("Expected Goals (xG / 90)", "xG_na_mecz", False),
            ("Conceded Expected Goals (xGA / 90)", "xGA_na_mecz", True),
            ("Open Play xG / 90", "xG_OP_na_mecz", False),
            ("Open Play xGA / 90", "xGA_OP_na_mecz", True),
            ("Set Play xG / 90", "xG_SP_na_mecz", False),
            ("Set Play xGA / 90", "xGA_SP_na_mecz", True),
            ("Non-Penalty xG (npxG / 90)", "npxG_na_mecz", False),
            ("Non-Penalty xGA (npxGA / 90)", "npxGA_na_mecz", True),
            ("Post-Shot xG (xGOT / 90)", "xGOT_na_mecz", False),
            ("Conceded Post-Shot xGA (xAGOT / 90)", "xAGOT_na_mecz", True),
            ("Ball Possession (%)", "Posiadanie", False),
            ("Passes in Own Half / 90", "Passes_Own_Half_Mean", False),
            ("Passes in Opponent Half / 90", "Passes_Opp_Half_Mean", False),
        ]
    else:
        h2h_metrics = [
            ("Gole Strzelone / mecz", "Gole_na_mecz", False),
            ("Gole Stracone / mecz", "Gole_stracone_na_mecz", True),
            ("Expected Goals (xG / mecz)", "xG_na_mecz", False),
            ("Dopuszczone xGA / mecz", "xGA_na_mecz", True),
            ("xG z gry otwartej (Open Play)", "xG_OP_na_mecz", False),
            ("xGA z gry otwartej (Open Play)", "xGA_OP_na_mecz", True),
            ("xG ze stałych fragmentów", "xG_SP_na_mecz", False),
            ("xGA ze stałych fragmentów", "xGA_SP_na_mecz", True),
            ("npxG (bez rzutów karnych)", "npxG_na_mecz", False),
            ("npxGA (dopuszczone bez karnych)", "npxGA_na_mecz", True),
            ("xGOT (jakość celnych strzałów)", "xGOT_na_mecz", False),
            ("xAGOT (jakość celnych rywali)", "xAGOT_na_mecz", True),
            ("Posiadanie Piłki (%)", "Posiadanie", False),
            ("Podania na własnej połowie", "Passes_Own_Half_Mean", False),
            ("Podania na połowie przeciwnika", "Passes_Opp_Half_Mean", False),
        ]

    # Budowa wierszy tabeli HTML z podświetleniem lepszego wyniku
    rows_h2h_html = ""
    plot_labels = []
    plot_vals_a = []
    plot_vals_b = []

    for label, col, lower_is_better in h2h_metrics:
        val_a = float(row_a.get(col, 0.0))
        val_b = float(row_b.get(col, 0.0))
        
        plot_labels.append(label)
        plot_vals_a.append(val_a)
        plot_vals_b.append(val_b)

        if lower_is_better:
            win_a = val_a < val_b
            win_b = val_b < val_a
        else:
            win_a = val_a > val_b
            win_b = val_b > val_a

        color_a = "#10B981; font-weight: 700;" if win_a else "#94A3B8;"
        color_b = "#10B981; font-weight: 700;" if win_b else "#94A3B8;"

        fmt = "{:.1f}%" if "%" in label else "{:.2f}"
        str_a = fmt.format(val_a)
        str_b = fmt.format(val_b)

        rows_h2h_html += f"""
        <tr style="height: 32px; border-bottom: 1px solid #21262D;">
            <td style="text-align: right; width: 25%; font-size: 13.5px; color: {color_a}">{str_a}</td>
            <td style="text-align: center; width: 50%; font-size: 12.5px; color: #E2E8F0; font-weight: 600;">{label}</td>
            <td style="text-align: left; width: 25%; font-size: 13.5px; color: {color_b}">{str_b}</td>
        </tr>
        """

    card_h2h_html = f"""
    <div style="background-color: #161B22; border: 1px solid #30363D; border-radius: 8px; padding: 16px 20px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
        <table style="width: 100%; border-collapse: collapse;">
            <thead>
                <tr style="border-bottom: 2px solid #30363D; height: 36px;">
                    <th style="text-align: right; width: 25%; color: #38BDF8; font-size: 16px; font-weight: 800;">{team_a}</th>
                    <th style="text-align: center; width: 50%; color: #8B949E; font-size: 12px; text-transform: uppercase;">VS</th>
                    <th style="text-align: left; width: 25%; color: #F59E0B; font-size: 16px; font-weight: 800;">{team_b}</th>
                </tr>
            </thead>
            <tbody>
                {rows_h2h_html}
            </tbody>
        </table>
    </div>
    """

    col_h2h_table, col_h2h_chart = st.columns([1.05, 1.35])

    with col_h2h_table:
        components.html(card_h2h_html, height=590, scrolling=False)

    with col_h2h_chart:
        # Predefiniowane grupy metryk, aby nie mieszać skali (np. podania z golami)
        cat_options = [
            "Wszystkie metryki" if selected_lang == "PL" else "All Metrics",
            "Gole i Jakość Szans (xG, xGA, xGOT)" if selected_lang == "PL" else "Goals & Chances (xG, xGA, xGOT)",
            "Dystrybucja i Posiadanie Piłki" if selected_lang == "PL" else "Passing & Possession",
            "Własny wybór (Personalizowany)" if selected_lang == "PL" else "Custom Selection"
        ]
        
        selected_cat = st.selectbox(
            "Zakres metryk na wykresie:" if selected_lang == "PL" else "Chart Metric Scope:",
            cat_options,
            index=1,  # Domyślnie 'Gole i Jakość Szans' - idealna, spójna skala 0-3
            key="sb_h2h_chart_scope"
        )
        
        # Filtrowanie metryk do wykresu
        if "Gole" in selected_cat or "Goals" in selected_cat:
            filtered_labels = [m[0] for m in h2h_metrics if "Podania" not in m[0] and "Passes" not in m[0] and "Posiadanie" not in m[0] and "Possession" not in m[0]]
        elif "Dystrybucja" in selected_cat or "Passing" in selected_cat:
            filtered_labels = [m[0] for m in h2h_metrics if "Podania" in m[0] or "Passes" in m[0] or "Posiadanie" in m[0] or "Possession" in m[0]]
        elif "Własny" in selected_cat or "Custom" in selected_cat:
            filtered_labels = st.multiselect(
                "Wybierz metryki do porównania:" if selected_lang == "PL" else "Select metrics to compare:",
                options=plot_labels,
                default=plot_labels[:4],
                key="ms_h2h_custom_metrics"
            )
        else:
            filtered_labels = plot_labels

        # Przygotowanie danych po filtrze
        chart_labels = []
        chart_vals_a = []
        chart_vals_b = []
        for lbl in filtered_labels:
            if lbl in plot_labels:
                idx = plot_labels.index(lbl)
                chart_labels.append(lbl)
                chart_vals_a.append(plot_vals_a[idx])
                chart_vals_b.append(plot_vals_b[idx])

        # Rysowanie wykresu słupkowego
        fig_h2h = go.Figure()
        
        fig_h2h.add_trace(go.Bar(
            y=chart_labels,
            x=chart_vals_a,
            name=team_a,
            orientation='h',
            marker=dict(color="#38BDF8"),
            text=[f"{v:.2f}" for v in chart_vals_a],
            textposition="outside",
            textfont=dict(color="#FFFFFF", size=10.5)
        ))
        
        fig_h2h.add_trace(go.Bar(
            y=chart_labels,
            x=chart_vals_b,
            name=team_b,
            orientation='h',
            marker=dict(color="#F59E0B"),
            text=[f"{v:.2f}" for v in chart_vals_b],
            textposition="outside",
            textfont=dict(color="#FFFFFF", size=10.5)
        ))

        # Dynamiczny margines osi X, aby etykiety się mieściły
        max_val = max(chart_vals_a + chart_vals_b) if (chart_vals_a and chart_vals_b) else 5
        x_limit = max_val * 1.22 if max_val > 0 else 5

        fig_h2h.update_layout(
            barmode='group',
            height=530,
            template="plotly_dark",
            paper_bgcolor="#0E1117",
            plot_bgcolor="#161B22",
            margin=dict(l=190, r=30, t=20, b=20),  # Wyraźny margines po lewej na nazwy metryk
            yaxis=dict(autorange="reversed", tickfont=dict(size=11, color="#E2E8F0")),
            xaxis=dict(showgrid=True, gridcolor="#21262D", range=[0, x_limit]),
            legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
        )
        st.plotly_chart(fig_h2h, use_container_width=True)


            
 
# =========================================================
    # =========================================================
        # AUTOMATYCZNY SILNIK RAPORTOWY AI (TACTICAL INSIGHTS)
        # =========================================================
        st.markdown("---")
        
        col_ai_head, col_ai_sens = st.columns([2.2, 1.2])
        with col_ai_head:
            st.subheader(" Automated Tactical Scouting Report (AI Insights)" if selected_lang == "EN" else " Automatyczny Raport Taktyczny AI (Analiza Anomalii i Przewag)")
            st.caption(
                "Algorithmic anomaly detection based on standardized league deviations and direct match clashes."
                if selected_lang == "EN"
                else "Algorytmiczny system wykrywania anomalii względem ligi oraz bezpośrednich dysproporcji stylów obu zespołów."
            )
        with col_ai_sens:
            # Suwak czułości: mniejsza sigma = więcej wykrytych niuansów
            ai_sensitivity = st.slider(
                "Czułość algorytmu (Próg σ):" if selected_lang == "PL" else "Algorithm Sensitivity (σ threshold):",
                min_value=0.40,
                max_value=1.30,
                value=0.70,
                step=0.05,
                key="slider_ai_threshold"
            )

        # Rozszerzona baza 18 metryk taktycznych
        ai_metrics_pool = [
            ("Gole Strzelone", "Goals Scored", "Gole_na_mecz", False),
            ("Gole Stracone", "Goals Conceded", "Gole_stracone_na_mecz", True),
            ("Wykreowane xG", "Created xG", "xG_na_mecz", False),
            ("Dopuszczone xGA", "Conceded xGA", "xGA_na_mecz", True),
            ("Bilans Bramkowy", "Goal Difference", "Bilans_Bramkowy", False),
            ("Bilans Wykreowanego Zagrożenia (xG - xGA)", "xG Delta (xG - xGA)", "Bilans_xG", False),
            ("xG z Gry Otwartej", "Open Play xG", "xG_OP_na_mecz", False),
            ("xGA Dopuszczone z Gry Otwartej", "Open Play xGA", "xGA_OP_na_mecz", True),
            ("xG ze Stałych Fragmentów", "Set Play xG", "xG_SP_na_mecz", False),
            ("xGA Dopuszczone ze SFG", "Set Play xGA", "xGA_SP_na_mecz", True),
            ("Jakość Wykończenia Strzałów (xGOT)", "Shot Quality (xGOT)", "xGOT_na_mecz", False),
            ("Jakość Czystych Strzałów Rywala (xAGOT)", "Opponent Shot Quality (xAGOT)", "xAGOT_na_mecz", True),
            ("Strzały z Szesnastki", "Box Shots", "Strzaly_z_pola_karnego", False),
            ("Kontakty w Polu Karnym Rywala", "Box Touches", "Box_Touches_Mean", False),
            ("Posiadanie Piłki (%)", "Ball Possession (%)", "Posiadanie", False),
            ("Podania na Połowie Rywala", "Opponent Half Passes", "Passes_Opp_Half_Mean", False),
            ("Długie Piłki", "Long Balls", "Long_Balls_Mean", False),
            ("Wygrane Pojedynki", "Duels Won", "Pojedynki_Wygrane", False)
        ]

        ins_a, ins_b, clashes = generate_tactical_ai_insights(
            team_stats, 
            team_a, 
            team_b, 
            ai_metrics_pool, 
            threshold=ai_sensitivity, 
            clash_threshold=ai_sensitivity * 1.15,
            lang="EN" if selected_lang == "EN" else "PL"
        )

        col_ai_a, col_ai_b = st.columns(2)

        with col_ai_a:
            st.markdown(f"####  {team_a} vs Liga ({len(ins_a)} anomalii)")
            if ins_a:
                for text, kind in ins_a:
                    if kind == "strength":
                        st.success(text)
                    else:
                        st.error(text)
            else:
                st.info("Brak istotnych odchyleń przy bieżącym progu czułości." if selected_lang == "PL" else "No significant deviations at current threshold.")

        with col_ai_b:
            st.markdown(f"####  {team_b} vs Liga ({len(ins_b)} anomalii)")
            if ins_b:
                for text, kind in ins_b:
                    if kind == "strength":
                        st.success(text)
                    else:
                        st.error(text)
            else:
                st.info("Brak istotnych odchyleń przy bieżącym progu czułości." if selected_lang == "PL" else "No significant deviations at current threshold.")

        if clashes:
            st.markdown(f"####  Główne Różnice Stylistyczne w tym Meczu ({len(clashes)})" if selected_lang == "PL" else f"####  Critical Stylistic Clashes ({len(clashes)})")
            for c in clashes:
                st.warning(c)    


    # =========================================================
    # MODUŁ: WYKRES RADAROWY H2H (SPIDER CHART - PERCENTYLE)
    # =========================================================
    st.markdown("---")
    st.subheader("🕸️ Tactical Radar Profile (H2H Spider Chart)" if selected_lang == "EN" else "🕸️ Radar Taktyczny H2H (Spider Chart)")
    st.caption(
        "Percentile ranks (0-100) relative to the league. 100 = League best, 0 = League lowest. Defensive metrics are inverted."
        if selected_lang == "EN"
        else "Wartości w percentylach (0-100) względem całej ligi. 100 = Elita ligowa, 0 = Najsłabszy wynik. Metryki obronne są odwrócone."
    )

    # 8 zrównoważonych filarów taktycznych do radaru
    radar_config = [
        ("Kreacja xG", "xG Creation", "xG_na_mecz", False),
        ("Atak Pozycyjny", "Open Play xG", "xG_OP_na_mecz", False),
        ("Szesnastka (Strzały)", "Box Threat", "Strzaly_z_pola_karnego", False),
        ("Posiadanie Piłki", "Possession", "Posiadanie", False),
        ("Kontrola Połowy Rywala", "Field Tilt", "Passes_Opp_Half_Mean", False),
        ("Wygrane Pojedynki", "Duels Won", "Pojedynki_Wygrane", False),
        ("Gra Bezpośrednia", "Directness", "Long_Balls_Mean", False),
        ("Szczelność Obrony (1/xGA)", "Defensive Solidity", "xGA_na_mecz", True),
    ]

    radar_categories = []
    pct_a = []
    pct_b = []

    for pl_name, en_name, col, lower_is_better in radar_config:
        lbl = en_name if selected_lang == "EN" else pl_name
        radar_categories.append(lbl)
        
        # Wyliczanie rangi percentylowej w lidze (0 do 100)
        series = team_stats[col].rank(pct=True) * 100.0
        
        # Inwersja dla obrony (im niższe dopuszczone xGA, tym wyższy percentyl)
        if lower_is_better:
            series = 100.0 - series
            
        team_a_idx = team_stats[team_stats["Team"] == team_a].index[0]
        team_b_idx = team_stats[team_stats["Team"] == team_b].index[0]
        
        pct_a.append(round(series.loc[team_a_idx], 1))
        pct_b.append(round(series.loc[team_b_idx], 1))

    # Zamknięcie obwodu wielokąta w radarze (pierwszy punkt powtórzony na końcu)
    radar_cats_closed = radar_categories + [radar_categories[0]]
    pct_a_closed = pct_a + [pct_a[0]]
    pct_b_closed = pct_b + [pct_b[0]]

    fig_radar = go.Figure()

    # Zarys Drużyny A
    fig_radar.add_trace(go.Scatterpolar(
        r=pct_a_closed,
        theta=radar_cats_closed,
        fill='toself',
        name=team_a,
        line=dict(color='#38BDF8', width=2.5),
        fillcolor='rgba(56, 189, 248, 0.25)',
        hovertemplate="<b>%{theta}</b><br>" + f"{team_a}: " + "<b>%{r:.1f}th percentile</b><extra></extra>"
    ))

    # Zarys Drużyny B
    fig_radar.add_trace(go.Scatterpolar(
        r=pct_b_closed,
        theta=radar_cats_closed,
        fill='toself',
        name=team_b,
        line=dict(color='#F59E0B', width=2.5),
        fillcolor='rgba(245, 158, 11, 0.25)',
        hovertemplate="<b>%{theta}</b><br>" + f"{team_b}: " + "<b>%{r:.1f}th percentile</b><extra></extra>"
    ))

    fig_radar.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 100],
                showticklabels=True,
                ticksuffix="%",
                tickfont=dict(size=9, color="#64748B"),
                gridcolor="#21262D"
            ),
            angularaxis=dict(
                tickfont=dict(size=11, color="#E2E8F0", family="sans-serif"),
                linecolor="#30363D",
                gridcolor="#21262D"
            ),
            bgcolor="#161B22"
        ),
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        height=580,
        margin=dict(l=60, r=60, t=40, b=40),
        legend=dict(
            orientation="h",
            yanchor="bottom",
            y=1.04,
            xanchor="center",
            x=0.5,
            font=dict(size=13)
        )
    )

    st.plotly_chart(fig_radar, use_container_width=True)

    # =========================================================
    # =========================================================
    # =========================================================
    # MODUŁ: MATRYCA PRZEWAG (ATAK VS OBRONA) & DYNAMICZNE KLUCZE
    # =========================================================
    st.markdown("---")
    st.subheader(
        " Tactical Matchup Matrix & Pre-Match Game Plan"
        if selected_lang == "EN"
        else " Matryca Zderzenia Formacji & Wytyczne Taktyczne AI"
    )
    st.caption(
        "Dynamic pre-match directives generated based on statistical mismatches between both teams."
        if selected_lang == "EN"
        else "Dynamiczne wytyczne przedmeczowe generowane automatycznie na podstawie wykrytych dysproporcji i słabości rywala."
    )

    clash_dimensions = [
        (
            "Atak Pozycyjny (Open Play)", "Open Play Threat", 
            "xG_OP_na_mecz", "xGA_OP_na_mecz",
            "Gra kombinacyjna i sforsowanie niskiego bloku"
        ),
        (
            "Stałe Fragmenty Gry (SFG)", "Set Piece Threat", 
            "xG_SP_na_mecz", "xGA_SP_na_mecz",
            "Rzuty rożne, wolne i walka o drugą piłkę"
        ),
        (
            "Obecność w Szesnastce", "Box Penetration", 
            "Strzaly_z_pola_karnego", "Box_Shots_Against_Mean",
            "Wchodzenie w pole karne i wykończenie z bliska"
        ),
        (
            "Kontrola Terytorialna", "Territorial Grip", 
            "Passes_Opp_Half_Mean", "Passes_Opp_Half_Against_Mean",
            "Utrzymanie piłki na połowie rywala i spychaniе do obrony"
        ),
        (
            "Gra Skrzydłami i Dośrodkowania", "Flank & Cross Threat", 
            "Accurate_Crosses_Mean", "Aerial_Duels_Won_Mean",
            "Centry w pole karne vs dominacja stoperów w powietrzu"
        ),
        (
            "Pressing i Odbiór w Fazie Przejścia", "High Press & Disruption", 
            "Tackles", "Passes_Own_Half_Mean",
            "Agresywny doskok vs płynność wyjścia spod pressingu"
        ),
        (
            "Strzały z Dystansu (Druga Linia)", "Outside Box Threat", 
            "Strzaly_zza_pola_karnego", "Outside_Box_Shots_Against_Mean",
            "Uderzenia zza pola karnego vs blokowanie przedpola"
        ),
        (
            "Jakość Wykończenia vs Bramkarz", "Finishing vs GK Wall", 
            "xGOT_na_mecz", "Goals_Prevented_Mecz",
            "Jakość strzałów w światło bramki vs refleks golkipera"
        ),
    ]

    matchup_rows_a = []
    matchup_rows_b = []

    for name_pl, name_en, att_col, def_col, desc in clash_dimensions:
        dim_name = name_en if selected_lang == "EN" else name_pl
        
        # Starcie A (Atak A vs Obrona B)
        val_att_a = float(row_a.get(att_col, 0.0))
        val_def_b = float(row_b.get(def_col, 0.0))
        mean_att = float(team_stats[att_col].mean()) if att_col in team_stats else 1.0
        mean_def = float(team_stats[def_col].mean()) if def_col in team_stats else 1.0
        std_att = float(team_stats[att_col].std()) if (att_col in team_stats and team_stats[att_col].std() > 0) else 1.0
        
        score_a = ((val_att_a - mean_att) / std_att) + ((val_def_b - mean_def) / std_att)
        power_pct_a = int(np.clip(50 + (score_a * 22), 5, 95))

        matchup_rows_a.append({
            "name": dim_name, "desc": desc, "att": val_att_a, "def": val_def_b,
            "score": score_a, "power_pct": power_pct_a
        })

        # Starcie B (Atak B vs Obrona A)
        val_att_b = float(row_b.get(att_col, 0.0))
        val_def_a = float(row_a.get(def_col, 0.0))
        score_b = ((val_att_b - mean_att) / std_att) + ((val_def_a - mean_def) / std_att)
        power_pct_b = int(np.clip(50 + (score_b * 22), 5, 95))

        matchup_rows_b.append({
            "name": dim_name, "desc": desc, "att": val_att_b, "def": val_def_a,
            "score": score_b, "power_pct": power_pct_b
        })

    def render_clash_card(m, team_att, team_def):
        if m["score"] >= 0.5:
            badge_text = " Wyraźna Przewaga Ataku" if selected_lang == "PL" else " Major Offensive Edge"
            badge_bg = "#064E3B"
            badge_color = "#34D399"
            bar_color = "#10B981"
        elif m["score"] <= -0.5:
            badge_text = " Szczelny Mur Obrony" if selected_lang == "PL" else " Defensive Wall"
            badge_bg = "#7F1D1D"
            badge_color = "#F87171"
            bar_color = "#EF4444"
        else:
            badge_text = " Wyrównana Walka" if selected_lang == "PL" else " Even Matchup"
            badge_bg = "#1E293B"
            badge_color = "#94A3B8"
            bar_color = "#38BDF8"

        html_card = (
            f'<div style="background-color: #161B22; border: 1px solid #30363D; border-radius: 8px; padding: 12px 16px; margin-bottom: 10px;">'
            f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 4px;">'
            f'<span style="font-weight: 700; color: #FFFFFF; font-size: 13.5px;">{m["name"]}</span>'
            f'<span style="background-color: {badge_bg}; color: {badge_color}; font-size: 11px; font-weight: 700; padding: 3px 8px; border-radius: 12px;">{badge_text}</span>'
            f'</div>'
            f'<div style="font-size: 11px; color: #8B949E; margin-bottom: 8px;">{m["desc"]}</div>'
            f'<div style="background-color: #21262D; border-radius: 4px; height: 6px; width: 100%; overflow: hidden; margin-bottom: 8px;">'
            f'<div style="background-color: {bar_color}; height: 100%; width: {m["power_pct"]}%;"></div>'
            f'</div>'
            f'<div style="display: flex; justify-content: space-between; font-size: 12px; color: #CBD5E1;">'
            f'<span>Atak ({team_att}): <b style="color: #FFFFFF;">{m["att"]:.2f}</b></span>'
            f'<span>Obrona ({team_def}): <b style="color: #FFFFFF;">{m["def"]:.2f}</b></span>'
            f'</div>'
            f'</div>'
        )
        st.markdown(html_card, unsafe_allow_html=True)

    col_clash_1, col_clash_2 = st.columns(2)

    with col_clash_1:
        st.markdown(
            f'<div style="background-color: #161B22; border-left: 4px solid #38BDF8; border-radius: 6px; padding: 10px 14px; margin-bottom: 12px;">'
            f'<span style="font-weight: 800; color: #38BDF8; font-size: 15px;">🔵 Atak {team_a} ➔ Obrona {team_b}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
        for row in matchup_rows_a:
            render_clash_card(row, team_a, team_b)

    with col_clash_2:
        st.markdown(
            f'<div style="background-color: #161B22; border-left: 4px solid #F59E0B; border-radius: 6px; padding: 10px 14px; margin-bottom: 12px;">'
            f'<span style="font-weight: 800; color: #F59E0B; font-size: 15px;">🟠 Atak {team_b} ➔ Obrona {team_a}</span>'
            f'</div>',
            unsafe_allow_html=True
        )
        for row in matchup_rows_b:
            render_clash_card(row, team_b, team_a)

    
    # =========================================================
    # SILNIK DYNAMICZNYCH WYTYCZNYCH TAKTYCZNYCH (BRAK SZTYWNYCH LIMITÓW)
    # =========================================================
    def build_dynamic_gameplan(team_target, team_opp, r_target, r_opp):
        plan = []

        # 1. Słabości rywala po stałych fragmentach (Szansa w ataku)
        if float(r_opp.get("xGA_SP_na_mecz", 0)) >= team_stats["xGA_SP_na_mecz"].quantile(0.65):
            plan.append(f"Szukać rzutów rożnych i wolnych: {team_opp} traci po SFG aż {float(r_opp.get('xGA_SP_na_mecz', 0)):.2f} xGA na mecz (jeden ze słabszych wyników w lidze).")

        # 2. Własne braki przy SFG (Zagrożenie w obronie)
        if float(r_target.get("xGA_SP_na_mecz", 0)) >= team_stats["xGA_SP_na_mecz"].quantile(0.65) and float(r_opp.get("xG_SP_na_mecz", 0)) >= team_stats["xG_SP_na_mecz"].median():
            plan.append(f"Maksymalna koncentracja przy obronie SFG: dopuszczacie {float(r_target.get('xGA_SP_na_mecz', 0)):.2f} xGA, a {team_opp} kreuje ze stałych fragmentów groźne {float(r_opp.get('xG_SP_na_mecz', 0)):.2f} xG.")

        # 3. Przestrzeń w szesnastce
        if float(r_target.get("Strzaly_z_pola_karnego", 0)) > float(r_opp.get("Box_Shots_Against_Mean", 0)):
            plan.append(f"Wstrzeliwać piłki w pole karne: średnia {float(r_target.get('Strzaly_z_pola_karnego', 0)):.1f} uderzeń z szesnastki przewyższa opór rywala ({float(r_opp.get('Box_Shots_Against_Mean', 0)):.1f}).")
        if float(r_opp.get("Box_Shots_Against_Mean", 0)) >= team_stats["Box_Shots_Against_Mean"].quantile(0.70):
            plan.append(f"Intensywna obecność w polu karnym: defensywa rywala dopuszcza aż {float(r_opp.get('Box_Shots_Against_Mean', 0)):.1f} strzałów z bliska na mecz.")

        # 4. Zagrożenie ze strony ataku rywala z szesnastki
        if float(r_opp.get("Strzaly_z_pola_karnego", 0)) >= team_stats["Strzaly_z_pola_karnego"].quantile(0.75):
            plan.append(f"Odciąć dośrodkowania i podania prostopadłe: {team_opp} oddaje z szesnastki aż {float(r_opp.get('Strzaly_z_pola_karnego', 0)):.1f} strzału na mecz.")

        # 5. Rozegranie od tyłu a pressing
        opp_own_half_p = float(r_opp.get("Passes_Own_Half_Mean", 0))
        if opp_own_half_p >= team_stats["Passes_Own_Half_Mean"].quantile(0.70):
            plan.append(f"Wysoki pressing na stoperach: {team_opp} buduje ataki cierpliwie od tyłu ({opp_own_half_p:.0f} podań na własnej połowie).")
        elif opp_own_half_p <= team_stats["Passes_Own_Half_Mean"].quantile(0.30):
            plan.append(f"Uwaga na drugą piłkę i wertykalne podania: {team_opp} gra bezpośrednio i szybko omija własną połowę.")

        # 6. Pojedynki i fizyczność
        duels_diff = float(r_opp.get("Pojedynki_Wygrane", 0)) - float(r_target.get("Pojedynki_Wygrane", 0))
        if duels_diff >= 4.0:
            plan.append(f"Unikać twardej walki 1 na 1 i przyspieszać grę na 1-2 kontakty: {team_opp} wygrywa fizycznie o {duels_diff:+.1f} pojedynków na mecz więcej.")
        elif duels_diff <= -4.0:
            plan.append(f"Narzucić twarde warunki fizyczne: posiadacie przewagę w wygranych pojedynkach ({float(r_target.get('Pojedynki_Wygrane', 0)):.1f} vs {float(r_opp.get('Pojedynki_Wygrane', 0)):.1f}).")

        # 7. Dyscyplina / Faule i kartki
        if float(r_opp.get("Fouls_Mean", 0)) >= team_stats["Fouls_Mean"].quantile(0.75):
            plan.append(f"Prowokować przewinienia dryblingiem w strefie 20-30m: {team_opp} gra bardzo agresywnie i fauluje średnio {float(r_opp.get('Fouls_Mean', 0)):.1f} razy na mecz.")
        if float(r_target.get("Fouls_Mean", 0)) >= team_stats["Fouls_Mean"].quantile(0.75):
            plan.append(f"Ostrożność w odbiorze: popełniacie średnio {float(r_target.get('Fouls_Mean', 0)):.1f} faulu na mecz, co grozi niepotrzebnymi rzutami wolnymi.")

        # 8. Strzały z dystansu
        if float(r_opp.get("Outside_Box_Shots_Against_Mean", 0)) >= team_stats["Outside_Box_Shots_Against_Mean"].quantile(0.70):
            plan.append(f"Szukać uderzeń zza pola karnego: defensywa rywala zostawia sporo miejsca przed szesnastką (dopuszcza {float(r_opp.get('Outside_Box_Shots_Against_Mean', 0)):.1f} strzałów z dystansu).")

        # 9. Skuteczność bramkarza rywala
        if float(r_opp.get("Keeper_Saves_Mean", 0)) <= team_stats["Keeper_Saves_Mean"].quantile(0.30):
            plan.append(f"Często zmuszać bramkarza rywala do interwencji: notuje poniżej {float(r_opp.get('Keeper_Saves_Mean', 0)):.1f} obrony na mecz.")

        return plan

    plan_a = build_dynamic_gameplan(team_a, team_b, row_a, row_b)
    plan_b = build_dynamic_gameplan(team_b, team_a, row_b, row_a)

    st.markdown("---")
    st.markdown(
        f"#####  Kluczowe Wytyczne i Punkty Zapalne ({team_a}: {len(plan_a)} | {team_b}: {len(plan_b)})"
        if selected_lang == "PL"
        else f"#####  Match Directives & Critical Flashpoints ({team_a}: {len(plan_a)} | {team_b}: {len(plan_b)})"
    )

    col_plan_a, col_plan_b = st.columns(2)

    with col_plan_a:
        st.markdown(f"**Wytyczne dla: {team_a}**")
        for i, directive in enumerate(plan_a, 1):
            st.info(f"**{i}.** {directive}")

    with col_plan_b:
        st.markdown(f"**Wytyczne dla: {team_b}**")
        for i, directive in enumerate(plan_b, 1):
            st.warning(f"**{i}.** {directive}")


# =========================================================================
# NOWA ZAKŁADKA: LIGOWY DETEKTOR TRENDÓW I ANOMALII AI
# =========================================================================
with tab_analiza_ligowa:
    st.header(" Ligowy Detektor Trendów & Analiza Stylów AI" if selected_lang == "PL" else " League-Wide Trend Detector & Tactical Intelligence")
    st.caption(
        "Wybierz dowolną metrykę, aby algorytm zanalizował całą stawkę ligową: wykrył dynamikę formy (wzrosty/spadki kolejka po kolejce) oraz podzielił ligę na profile efektywności."
        if selected_lang == "PL" else
        "Select any metric to analyze the entire league: detect momentum (match-by-match slopes/trends) and performance tier categorizations."
    )

    # 1. Baza metryk do wyboru: (Nazwa PL, Nazwa EN, Kolumna meczowa, Kolumna ligowa, Czy mniej=lepiej)
    LEAGUE_METRICS_REGISTRY = [
        ("xG z Gry Otwartej (Open Play)", "Open Play xG", "xG_OP_For", "xG_OP_na_mecz", False),
        ("xG ze Stałych Fragmentów (SFG)", "Set Play xG", "xG_SP_For", "xG_SP_na_mecz", False),
        ("Ogólne xG (Kreacja Zagrożenia)", "Total xG Created", "xG_For", "xG_na_mecz", False),
        ("Dopuszczone xGA (Jakość szans rywala)", "Conceded xGA", "xG_Against", "xGA_na_mecz", True),
        ("xGA z Gry Otwartej", "Open Play xGA Conceded", "xG_OP_Against", "xGA_OP_na_mecz", True),
        ("xGA ze Stałych Fragmentów", "Set Play xGA Conceded", "xG_SP_Against", "xGA_SP_na_mecz", True),
        ("Strzały z Pola Karnego", "Box Shots", "Box_Shots", "Strzaly_z_pola_karnego", False),
        ("Kontakty w Szesnastce Rywala", "Box Touches", "Box_Touches", "Box_Touches_Mean", False),
        ("Posiadanie Piłki (%)", "Ball Possession (%)", "Possession", "Posiadanie", False),
        ("Podania na Połowie Rywala", "Opponent Half Passes", "Passes_Opp_Half", "Passes_Opp_Half_Mean", False),
        ("Celne Długie Piłki", "Accurate Long Balls", "Long_Balls", "Long_Balls_Mean", False),
        ("Wygrane Pojedynki", "Duels Won", "Duels_Won", "Pojedynki_Wygrane", False),
        ("Faule Popełnione", "Fouls Committed", "Fouls", "Fouls_Mean", True),
    ]

    metric_names = [m[0] if selected_lang == "PL" else m[1] for m in LEAGUE_METRICS_REGISTRY]
    
    col_sel_met, col_sel_trend_scope = st.columns([2.2, 1.2])
    with col_sel_met:
        selected_league_metric_name = st.selectbox(
            "Wybierz wskaźnik do przeskanowania ligi:" if selected_lang == "PL" else "Select metric to scan the league:",
            metric_names,
            index=0,
            key="sb_league_ai_metric_sel"
        )
    with col_sel_trend_scope:
        trend_window = st.slider(
            "Zakres ostatnich meczów do badania pędu (momentum):" if selected_lang == "PL" else "Recent matches window for momentum:",
            min_value=1, max_value=8, value=3, step=1,
            key="slider_trend_window"
        )

    # Odnalezienie konfiguracji metryki
    sel_idx_metric = metric_names.index(selected_league_metric_name)
    m_pl, m_en, m_match_col, m_stat_col, lower_is_better = LEAGUE_METRICS_REGISTRY[sel_idx_metric]

    # 2. Obliczenia pędu lub anomalii ostatniego meczu (Obsługa trend_window == 1)
    trend_results = []
    
    for team_name in team_stats["Team"].unique():
        t_sub = matches_df[matches_df["Team"] == team_name].copy().reset_index(drop=True)
        if len(t_sub) >= 1 and m_match_col in t_sub.columns:
            recent_matches = t_sub.tail(trend_window).copy()
            y_vals = recent_matches[m_match_col].values
            last_match = t_sub.iloc[-1]
            last_opp_info = f"vs {last_match['Opponent']} ({int(last_match['Goals_For'])}:{int(last_match['Goals_Against'])})"
            
            # Gdy badamy 1 mecz: badamy czystą deltę z tego meczu względem sezonu
            if trend_window == 1:
                slope = round(float(y_vals[0] - t_sub[m_match_col].mean()), 2)
            else:
                x_vals = np.arange(len(y_vals))
                if len(y_vals) > 1 and np.var(x_vals) > 0:
                    slope = round(float(np.polyfit(x_vals, y_vals, 1)[0]), 3)
                else:
                    slope = 0.0
                
            curr_avg = y_vals.mean()
            season_avg = t_sub[m_match_col].mean()
            delta_recent = curr_avg - season_avg
            pct_dev = ((delta_recent / season_avg) * 100) if season_avg > 0 else 0.0
            
            trend_results.append({
                "Team": team_name,
                "Slope": slope,
                "Recent_Avg": round(curr_avg, 2),
                "Season_Avg": round(season_avg, 2),
                "Recent_Delta": round(delta_recent, 2),
                "Pct_Dev": round(pct_dev, 1),
                "Last_Opp": last_opp_info
            })

    df_trends = pd.DataFrame(trend_results)

    # 3. Rozdzielenie na całą stawkę ligową (Progres vs Regres bez sztywnego limitu)
    # 3. Podział na 3 stany: Progres, Stabilizacja (na 0), Regres
    # 3. Podział na 3 stany i przygotowanie jednej tabeli ligowej
    margin_neutral = 0.05

    # 3. Podział na 3 stany i przygotowanie jednej tabeli ligowej (Wsparcie PL / EN)
    margin_neutral = 0.05

    def get_status_info(delta, lower_is_better, lang="PL"):
        # Etykiety PL / EN
        lbl_surge = " Progres" if lang == "PL" else "  Progress"
        lbl_base = " Poziom Bazowy" if lang == "PL" else " Baseline"
        lbl_slump = " Regres" if lang == "PL" else " Decline"

        if lower_is_better:
            if delta < -margin_neutral:
                return lbl_surge, "#10B981", "#064E3B", 1
            elif delta > margin_neutral:
                return lbl_slump, "#EF4444", "#7F1D1D", 3
            else:
                return lbl_base, "#38BDF8", "#1E293B", 2
        else:
            if delta > margin_neutral:
                return lbl_surge, "#10B981", "#064E3B", 1
            elif delta < -margin_neutral:
                return lbl_slump, "#EF4444", "#7F1D1D", 3
            else:
                return lbl_base, "#38BDF8", "#1E293B", 2

    # Dodanie statusów do ramki danych z uwzględnieniem wybranego języka
    statuses = [get_status_info(r["Recent_Delta"], lower_is_better, selected_lang) for _, r in df_trends.iterrows()]
    df_trends["Status_Label"] = [s[0] for s in statuses]
    df_trends["Status_Color"] = [s[1] for s in statuses]
    df_trends["Status_Bg"] = [s[2] for s in statuses]
    df_trends["Sort_Rank"] = [s[3] for s in statuses]

    # Sortowanie: najpierw wystrzał formy (od największego plusa), potem neutralne, na końcu kryzys
    if lower_is_better:
        df_trends = df_trends.sort_values(by=["Sort_Rank", "Recent_Delta"], ascending=[True, True]).reset_index(drop=True)
    else:
        df_trends = df_trends.sort_values(by=["Sort_Rank", "Recent_Delta"], ascending=[True, False]).reset_index(drop=True)

    is_single = (trend_window == 1)
    
    # Dynamiczne nagłówki tabeli zależne od języka
    if selected_lang == "EN":
        col_scope_header = "Last Match" if is_single else f"Avg ({trend_window} MP)"
        th_rank = "#"
        th_team = "Team"
        th_season = "Season Avg"
        th_delta = "Delta (Dev %)"
        th_trend = "Trend Rating"
        table_title = " League-Wide Form & Momentum Overview"
    else:
        col_scope_header = "Ostatni Mecz" if is_single else f"Śr. ({trend_window} m.)"
        th_rank = "#"
        th_team = "Drużyna"
        th_season = "Śr. Sezonowa"
        th_delta = "Odchylenie (Delta)"
        th_trend = "Ocena Trendu"
        table_title = " Zbiorcza Tabela Formy & Dynamiki Ligi"

    st.markdown("---")
    st.markdown(f"### {table_title}")

    # Generowanie wierszy tabeli HTML
    rows_table_html = ""
    for idx, r in df_trends.iterrows():
        rank = idx + 1
        team = r["Team"]
        recent_val = f"{r['Recent_Avg']:.2f}"
        season_val = f"{r['Season_Avg']:.2f}"
        
        # Formatowanie delty
        if r["Recent_Delta"] > 0:
            delta_str = f"+{r['Recent_Delta']:.2f} ({r['Pct_Dev']:+.0f}%)"
        else:
            delta_str = f"{r['Recent_Delta']:.2f} ({r['Pct_Dev']:+.0f}%)"

        opp_info = f"<span style='color: #64748B; font-size: 11px;'>({r['Last_Opp']})</span>" if is_single else ""
        badge_html = f"<span style='background: {r['Status_Bg']}; color: {r['Status_Color']}; padding: 3px 8px; border-radius: 10px; font-weight: 700; font-size: 11px;'>{r['Status_Label']}</span>"

        rows_table_html += (
            f'<tr style="height: 36px; border-bottom: 1px solid #21262D;">'
            f'<td style="color: #94A3B8; font-weight: 700; text-align: left; width: 35px; padding: 4px 8px;">{rank}</td>'
            f'<td style="color: #FFFFFF; font-weight: 600; text-align: left; padding: 4px 8px;">{team} {opp_info}</td>'
            f'<td style="color: #FFFFFF; font-weight: 700; text-align: center; width: 110px; padding: 4px 8px;">{recent_val}</td>'
            f'<td style="color: #94A3B8; text-align: center; width: 110px; padding: 4px 8px;">{season_val}</td>'
            f'<td style="color: {r["Status_Color"]}; font-weight: 700; text-align: right; width: 140px; padding: 4px 8px;">{delta_str}</td>'
            f'<td style="text-align: right; width: 170px; padding: 4px 8px;">{badge_html}</td>'
            f'</tr>'
        )

    table_pixel_height = max(350, len(df_trends) * 38 + 75)

    full_table_html = f"""
    <!DOCTYPE html>
    <html>
    <head>
    <meta charset="utf-8">
    <style>
        body {{
            margin: 0;
            padding: 0;
            background-color: transparent;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
        }}
        .table-card {{
            background-color: #161B22;
            border: 1px solid #30363D;
            border-radius: 8px;
            padding: 14px 18px;
            box-sizing: border-box;
            width: 100%;
        }}
        table {{
            width: 100%;
            border-collapse: collapse;
            font-size: 12.5px;
            line-height: 1.4;
        }}
        th {{
            border-bottom: 2px solid #30363D;
            color: #8B949E;
            font-size: 11px;
            text-transform: uppercase;
            padding: 6px 8px;
        }}
    </style>
    </head>
    <body>
        <div class="table-card">
            <table>
                <thead>
                    <tr>
                        <th style="text-align: left; width: 35px;">{th_rank}</th>
                        <th style="text-align: left;">{th_team}</th>
                        <th style="text-align: center; width: 110px;">{col_scope_header}</th>
                        <th style="text-align: center; width: 110px;">{th_season}</th>
                        <th style="text-align: right; width: 140px;">{th_delta}</th>
                        <th style="text-align: right; width: 170px;">{th_trend}</th>
                    </tr>
                </thead>
                <tbody>
                    {rows_table_html}
                </tbody>
            </table>
        </div>
    </body>
    </html>
    """

    components.html(full_table_html, height=table_pixel_height, scrolling=False)



    # 4. Wykres słupkowy
    st.markdown("---")
    bar_title = "#####  Występ w Ostatniej Kolejce vs Średnia z Całego Sezonu" if is_single else f"#####  Zestawienie Średniej Sezonowej ze Średnią Ostatnich {trend_window} Meczów"
    st.markdown(bar_title)
    
    df_plot_comp = df_trends.sort_values(by="Recent_Avg", ascending=False).reset_index(drop=True)
    
    fig_comp = go.Figure()
    fig_comp.add_trace(go.Bar(
        name="Ostatni mecz" if is_single else f"Ostatnie {trend_window} meczów",
        x=df_plot_comp["Team"],
        y=df_plot_comp["Recent_Avg"],
        marker_color="#38BDF8",
        text=[f"{v:.2f}" for v in df_plot_comp["Recent_Avg"]],
        textposition="outside"
    ))
    fig_comp.add_trace(go.Bar(
        name="Średnia z całego sezonu",
        x=df_plot_comp["Team"],
        y=df_plot_comp["Season_Avg"],
        marker_color="#475569",
        text=[f"{v:.2f}" for v in df_plot_comp["Season_Avg"]],
        textposition="outside"
    ))
    
    fig_comp.update_layout(
        barmode="group",
        height=480,
        template="plotly_dark",
        paper_bgcolor="#0E1117",
        plot_bgcolor="#161B22",
        xaxis=dict(tickangle=-40),
        yaxis=dict(title=selected_league_metric_name),
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
    )
    st.plotly_chart(fig_comp, use_container_width=True)

    # 5. Podział ligi na 4 Tiery Jakościowe (Elita, Solidni, Przeciętniacy, Strefa Alarmowa)
    st.markdown("---")
    st.markdown("#####  Podział Ligi na Tiery Jakościowe AI (Rozkład Statystyczny)")
    
    q75 = team_stats[m_stat_col].quantile(0.75)
    q50 = team_stats[m_stat_col].median()
    q25 = team_stats[m_stat_col].quantile(0.25)
    
    tier_elita = team_stats[team_stats[m_stat_col] >= q75]["Team"].tolist() if not lower_is_better else team_stats[team_stats[m_stat_col] <= q25]["Team"].tolist()
    tier_srednia = team_stats[(team_stats[m_stat_col] < q75) & (team_stats[m_stat_col] >= q50)]["Team"].tolist() if not lower_is_better else team_stats[(team_stats[m_stat_col] > q25) & (team_stats[m_stat_col] <= q50)]["Team"].tolist()
    tier_zagrozenie = team_stats[team_stats[m_stat_col] < q25]["Team"].tolist() if not lower_is_better else team_stats[team_stats[m_stat_col] > q75]["Team"].tolist()

    c_t1, c_t2, c_t3 = st.columns(3)
    with c_t1:
        st.success(f" **Elita Ligowa (Top 25%):**\n\n" + ", ".join(tier_elita))
    with c_t2:
        st.info(f" **Górna Połowa Tabeli:**\n\n" + ", ".join(tier_srednia))
    with c_t3:
        st.error(f" **Strefa Problemowa (Dolne 25%):**\n\n" + ", ".join(tier_zagrozenie))


# =========================================================================
# ZAKŁADKA: ASYSTENT AI & ZAAWANSOWANA WYSZUKIWARKA MECZOWA
# =========================================================================
with tab_asystent_ai:
    st.header("🤖 Inteligentny Asystent Analityczny & Wyszukiwarka Meczowa" if selected_lang == "PL" else "🤖 AI Tactical Scout & Advanced Match Query Engine")
    st.caption(
        "Zadaj dowolne pytanie w języku naturalnym lub skorzystaj z filtrów: badaj serie zwycięstw dom/wyjazd, mecze wygrane pomimo gorszych statystyk (xG, strzały z szesnastki) oraz anomalie."
        if selected_lang == "PL" else
        "Search match data in natural language or use tactical filters: analyze home/away winning streaks, paradox matches won against xG/shot metrics, and statistical anomalies."
    )

    # Inicjalizacja klucza w sesji (jeśli jeszcze nie istnieje)
    if "ai_scout_user_query" not in st.session_state:
        st.session_state["ai_scout_user_query"] = ""

    # Funkcja przypisująca pytanie z kafelków do pola tekstowego
    def set_prompt(prompt_text):
        st.session_state["ai_scout_user_query"] = prompt_text

    # 1. Szybkie kafelki z przykładami zapytań
    st.markdown("##### 💡 Przykłady zapytań do przetestowania (kliknij, aby uruchomić):")
    col_q1, col_q2, col_q3 = st.columns(3)
    with col_q1:
        if st.button("🏆 Serie zwycięstw u siebie (min. 3 mecze)", on_click=set_prompt, args=("serie zwycięstw u siebie 3 meczowe",), use_container_width=True):
            pass
        if st.button("🚌 Serie zwycięstw na wyjeździe (min. 2 mecze)", on_click=set_prompt, args=("serie zwycięstw na wyjeździe 2 meczowe",), use_container_width=True):
            pass
    with col_q2:
        if st.button("🎯 Wygrane pomimo niższego xG (Smash & Grab)", on_click=set_prompt, args=("mecze wygrane pomimo niższego xg",), use_container_width=True):
            pass
        if st.button("🥊 Wygrane pomimo mniejszej liczby strzałów w polu", on_click=set_prompt, args=("mecze wygrane pomimo mniejszej ilości strzałów z pola karnego",), use_container_width=True):
            pass
    with col_q3:
        if st.button("⚽ Wyjazdy z min. 1 strzelonym golem", on_click=set_prompt, args=("mecze na wyjeździe z min jednym strzelonym golem",), use_container_width=True):
            pass
        if st.button("⚔️ Wygrane mecze mając więcej wygranych pojedynków", on_click=set_prompt, args=("mecze wygrane mając więcej wygranych pojedynków",), use_container_width=True):
            pass

    # 2. Formularz wyszukiwarki: brak parametru `value=` eliminuje cofanie wpisanego tekstu!
    with st.form(key="ai_scout_form", clear_on_submit=False):
        c_input, c_btn = st.columns([4.2, 0.8])
        with c_input:
            st.text_input(
                "🔎 Wpisz swoje zapytanie:",
                key="ai_scout_user_query",
                placeholder="np. mecze Chelsea wygrane pomimo niższego xG, mecze Evertonu z większą liczbą podań...",
                label_visibility="collapsed"
            )
        with c_btn:
            st.form_submit_button("🔍 Szukaj" if selected_lang == "PL" else "🔍 Search", use_container_width=True)

    # Pobieramy bieżącą treść zapytania bezpośrednio ze stanu sesji
    user_query = st.session_state.get("ai_scout_user_query", "").strip()

    # 3. Rozwijany kreator filtrów (opcjonalny)
    with st.expander("🛠️ Kliknij tutaj, jeśli wolisz precyzyjnie wyklikać filtry zamiast pisać"):
        col_f1, col_f2, col_f3, col_f4 = st.columns(4)
        with col_f1:
            team_choices = ["Wszystkie (Liga)"] + sorted(team_stats["Team"].unique().tolist())
            cr_team = st.selectbox("Drużyna:", team_choices, index=0, key="cr_sb_team")
            cr_venue = st.selectbox("Miejsce meczu:", ["Wszystkie", "Tylko u siebie (Home)", "Tylko na wyjeździe (Away)"], index=0, key="cr_sb_venue")
        with col_f2:
            cr_result = st.selectbox("Wynik meczu:", ["Dowolny", "Tylko Wygrane (3 pkt)", "Tylko Remisy (1 pkt)", "Tylko Porażki (0 pkt)"], index=0, key="cr_sb_res")
            cr_goals_cond = st.selectbox("Warunek bramkowy:", ["Dowolny", "Min. 1 strzelony gol", "Min. 1 stracony gol", "Czyste konto (0 straconych)", "Obie strzeliły (BTTS)"], index=0, key="cr_sb_goals")
        with col_f3:
            cr_paradox = st.selectbox(
                "Wygrana pomimo gorszych statystyk:",
                [
                    "Brak (Dowolne)",
                    "Niższe xGOT niż rywal",
                    "Niższe xG ogólne niż rywal",
                    "Niższe npxG (bez karnych)",
                    "Niższe xG z gry otwartej (Open Play)",
                    "Niższe xG ze SFG niż rywal",
                    "Mniejsza liczba oddanych strzałów",
                    "Mniejsza liczba strzałów z szesnastki",
                    "Niższe posiadanie piłki (< 50%)",
                    "Mniej wygranych pojedynków"
                ],
                index=0, key="cr_sb_paradox"
            )
            cr_anomaly = st.selectbox(
                "Anomalie vs norma zespołu (>25% odchyłki):",
                ["Brak", "Anomalia Podań", "Anomalia Strzałów", "Anomalia Fauli", "Anomalia xG"],
                index=0, key="cr_sb_anom"
            )
        with col_f4:
            cr_is_streak = st.checkbox("Badaj serie meczowe", value=False, key="cr_cb_streak")
            cr_streak_len = st.slider("Minimalna długość serii:", min_value=1, max_value=8, value=3, step=1, key="cr_sl_streak")

    # =========================================================
    # SILNIK PARSUJĄCY I WYKONUJĄCY ZAPYTANIA
    # =========================================================
    def normalize_nlp(txt):
        txt = str(txt).lower()
        rep = {'ą': 'a', 'ć': 'c', 'ę': 'e', 'ł': 'l', 'ń': 'n', 'ó': 'o', 'ś': 's', 'ź': 'z', 'ż': 'z'}
        for k, v in rep.items():
            txt = txt.replace(k, v)
        # Korekta typowych literówek
        txt = txt.replace("pomiimo", "pomimo").replace("wygrene", "wygrane")
        txt = txt.replace("set-play", "set play").replace("open-play", "open play")
        txt = txt.replace("xg-set play", "set play").replace("xg set-play", "set play")
        return txt

    q_norm = normalize_nlp(user_query) if user_query else ""

    # Ustalanie parametrów wyszukiwania
    # Ustalanie parametrów wyszukiwania (albo z tekstu, albo z kreatora)
    # 1. Drużyna (inteligentne dopasowanie bez kolizji 'City', 'United', 'Real' itp.)
    selected_team_filter = None
    if cr_team != "Wszystkie (Liga)":
        selected_team_filter = cr_team
    else:
        # Słowa pospolite w nazwach klubów, które same w sobie NIE mogą decydować o trafieniu
        GENERIC_CLUB_WORDS = {"city", "united", "town", "real", "fc", "gks", "ks", "de", "la", "cf", "ac", "inter", "sporting"}

        # Krok 1: Szukamy pełnej nazwy drużyny (od najdłuższych nazw, aby 'Hull City' wygrało z 'City')
        sorted_teams = sorted(team_stats["Team"].unique(), key=lambda x: len(normalize_nlp(x)), reverse=True)
        for t_cand in sorted_teams:
            t_clean = normalize_nlp(t_cand)
            if t_clean in q_norm:
                selected_team_filter = t_cand
                break

        # Krok 2: Jeśli nie wpisano pełnej nazwy, szukamy po unikalnym członie (np. samo 'Hull', 'Newcastle', 'Lech')
        if not selected_team_filter:
            for t_cand in sorted_teams:
                t_clean = normalize_nlp(t_cand)
                unique_words = [w for w in t_clean.split() if len(w) >= 3 and w not in GENERIC_CLUB_WORDS]
                if any(w in q_norm for w in unique_words):
                    selected_team_filter = t_cand
                    break

    selected_venue_filter = None
    if "u siebie" in cr_venue.lower() or any(w in q_norm for w in ["u siebie", "dom", "domu", "domowe", "gospodarz"]):
        selected_venue_filter = "Home"
    elif "wyjeździe" in cr_venue.lower() or any(w in q_norm for w in ["na wyjezdzie", "wyjazd", "wyjazdowe", "delegacj", "gosc"]):
        selected_venue_filter = "Away"

    detect_streak = cr_is_streak or any(w in q_norm for w in ["seri", "streak", "z rzedu", "pod rzad", "kolejnych"])
    streak_target_len = cr_streak_len
    num_map = {
        "jedno": 1, "jeden": 1, "1": 1,
        "dwu": 2, "dwa": 2, "dwie": 2, "dwuch": 2, "2": 2,
        "trzy": 3, "trzech": 3, "troj": 3, "3": 3,
        "cztero": 4, "cztery": 4, "czterech": 4, "4": 4,
        "piecio": 5, "piec": 5, "pieciu": 5, "5": 5,
        "szescio": 6, "szesc": 6, "szesciu": 6, "6": 6,
        "siedmio": 7, "siedem": 7, "7": 7
    }
    for k_num, v_num in num_map.items():
        if k_num in q_norm:
            streak_target_len = v_num
            break

    has_active_query = bool(user_query or cr_team != "Wszystkie (Liga)" or cr_venue != "Wszystkie" or cr_result != "Dowolny" or cr_paradox != "Brak (Dowolne)" or cr_anomaly != "Brak" or cr_is_streak)

    if has_active_query:
        st.markdown("---")

        # TRYB A: BADANIE SERII MECZOWYCH (STREAKS)
        if detect_streak:
            venue_label = "U Siebie (Dom)" if selected_venue_filter == "Home" else ("Na Wyjeździe" if selected_venue_filter == "Away" else "Ogólne (Dom + Wyjazd)")
            st.subheader(f"🔥 Serie Zwycięstw: {venue_label} (Długość: min. {streak_target_len} meczów)")

            streak_records = []
            pool_teams = [selected_team_filter] if selected_team_filter else team_stats["Team"].unique()

            for tm in pool_teams:
                tm_matches = matches_df[matches_df["Team"] == tm].copy().reset_index(drop=True)
                if selected_venue_filter:
                    tm_matches = tm_matches[tm_matches["Venue"] == selected_venue_filter].reset_index(drop=True)

                current_streak = []
                for idx, r_m in tm_matches.iterrows():
                    if r_m["Points"] == 3:
                        current_streak.append(r_m)
                    else:
                        if len(current_streak) >= streak_target_len:
                            streak_records.append({"Team": tm, "Length": len(current_streak), "Matches": list(current_streak)})
                        current_streak = []
                if len(current_streak) >= streak_target_len:
                    streak_records.append({"Team": tm, "Length": len(current_streak), "Matches": list(current_streak)})

            if streak_records:
                st.success(f"🤖 **Znaleziono {len(streak_records)} serii** spełniających kryteria (długość $\ge {streak_target_len}$ meczów z rzędu).")
                for s_idx, st_data in enumerate(streak_records, 1):
                    team_name = st_data["Team"]
                    s_len = st_data["Length"]
                    st.markdown(
                        f"""<div style="background-color: #161B22; border-left: 4px solid #10B981; border-radius: 6px; padding: 10px 14px; margin-bottom: 6px;">
                            <span style="font-weight: 800; color: #10B981; font-size: 14px;">#{s_idx} {team_name} – Seria {s_len} Zwycięstw z rzędu ({venue_label})</span>
                        </div>""",
                        unsafe_allow_html=True
                    )
                    match_chips = []
                    for m_s in st_data["Matches"]:
                        v_str = "D" if m_s["Venue"] == "Home" else "W"
                        res_str = f"{int(m_s['Goals_For'])}:{int(m_s['Goals_Against'])}"
                        match_chips.append(f"vs {m_s['Opponent']} ({v_str}) [{res_str}]")
                    st.info(" ➔ ".join(match_chips))
            else:
                st.warning(f"Brak serii zwycięstw o długości co najmniej {streak_target_len} meczów dla wybranego filtra ({venue_label}).")

        # TRYB B: FILTROWANIE MECZÓW
        else:
            base_matches = matches_df.copy()
            if selected_team_filter:
                base_matches = base_matches[base_matches["Team"] == selected_team_filter]
            if selected_venue_filter:
                base_matches = base_matches[base_matches["Venue"] == selected_venue_filter]

            # 1. Wynik (odporny na odmiany i literówki typu 'wygrene')
            is_win = any(w in q_norm for w in ["wygr", "zwyc", "win", "won", "3 pkt"]) or cr_result == "Tylko Wygrane (3 pkt)"
            is_loss = any(w in q_norm for w in ["przegr", "poraz", "loss", "lost", "0 pkt"]) or cr_result == "Tylko Porażki (0 pkt)"
            is_draw = any(w in q_norm for w in ["remis", "draw", "1 pkt"]) or cr_result == "Tylko Remisy (1 pkt)"

            if is_win:
                base_matches = base_matches[base_matches["Points"] == 3]
            elif is_loss:
                base_matches = base_matches[base_matches["Points"] == 0]
            elif is_draw:
                base_matches = base_matches[base_matches["Points"] == 1]

            # 2. Bramki
            if "min jednym strzelonym" in q_norm or "ze strzelonym golem" in q_norm or cr_goals_cond == "Min. 1 strzelony gol":
                base_matches = base_matches[base_matches["Goals_For"] >= 1]
            if "min jednym straconym" in q_norm or "ze straconym golem" in q_norm or cr_goals_cond == "Min. 1 stracony gol":
                base_matches = base_matches[base_matches["Goals_Against"] >= 1]
            if "czystym kontem" in q_norm or "bez straty gola" in q_norm or cr_goals_cond == "Czyste konto (0 straconych)":
                base_matches = base_matches[base_matches["Goals_Against"] == 0]
            if "btts" in q_norm or "obie strzelily" in q_norm or cr_goals_cond == "Obie strzeliły (BTTS)":
                base_matches = base_matches[(base_matches["Goals_For"] >= 1) & (base_matches["Goals_Against"] >= 1)]

            # 3. Kierunek porównania
            is_higher = any(w in q_norm for w in ["wyzsz", "wieksz", "wiecej", "lepsz"])
            is_lower = any(w in q_norm for w in ["nizsz", "mniejsz", "mniej", "gorsz"])

            if not is_higher and not is_lower:
                op_greater = True if is_loss else False
            else:
                op_greater = is_higher

            comp_word = "WIĘCEJ / WYŻSZE" if op_greater else "MNIEJ / NIŻSZE"

            # 4. Wykrywanie szukanej statystyki (dokładnie dopasowanej do zapytania)
            metric_label = "xG (Własne : Rywal)"
            col_for = "xG_For"
            col_opp = "xG_Against"
            val_format = "float"

            # POJEDYNKI
            if any(w in q_norm for w in ["pojedyn", "starci", "duels"]) or cr_paradox == "Mniej wygranych pojedynków":
                metric_label = "Pojedynki Wygrane (Własne : Rywal)"
                col_for = "Duels_Won"
                col_opp = "Duels_Won_Against"
                val_format = "int"

            # xGOT
            elif any(w in q_norm for w in ["xgot", "post-shot", "post shot", "on target"]) or cr_paradox == "Niższe xGOT niż rywal":
                metric_label = "xGOT (Własne : Rywal)"
                col_for = "xGOT_For"
                col_opp = "xGOT_Against"
                val_format = "float"

            # xG Set Play (stałe fragmenty)
            elif any(w in q_norm for w in ["set play", "setplay", "sfg", "stalych fragment", "stale fragmenty", "ze stalych"]) or cr_paradox == "Niższe xG ze SFG niż rywal":
                metric_label = "xG Set Play (Własne : Rywal)"
                col_for = "xG_SP_For"
                col_opp = "xG_SP_Against"
                val_format = "float"

            # xG Open Play (gra otwarta)
            elif any(w in q_norm for w in ["open play", "openplay", "gry otwartej", "gra otwarta", "pozycyjn"]) or cr_paradox == "Niższe xG z gry otwartej (Open Play)":
                metric_label = "xG Open Play (Własne : Rywal)"
                col_for = "xG_OP_For"
                col_opp = "xG_OP_Against"
                val_format = "float"

            # npxG
            elif any(w in q_norm for w in ["npxg", "non-penalty", "non penalty", "bez karnych"]) or cr_paradox == "Niższe npxG (bez karnych)":
                metric_label = "npxG (Własne : Rywal)"
                col_for = "npxG_For"
                col_opp = "npxG_Against"
                val_format = "float"

            # Strzały z pola karnego
            elif any(w in q_norm for w in ["pola karnego", "szesnast"]) or cr_paradox == "Mniejsza liczba strzałów z szesnastki":
                metric_label = "Strzały z pola (Własne : Rywal)"
                col_for = "Box_Shots"
                col_opp = "Box_Shots_Against"
                val_format = "int"

            # Strzały ogółem
            elif "strzal" in q_norm or cr_paradox == "Mniejsza liczba oddanych strzałów":
                metric_label = "Strzały ogółem (Własne : Rywal)"
                col_for = "Shots"
                col_opp = "Shots_Against"
                val_format = "int"

            # Posiadanie piłki
            elif "posiadani" in q_norm or cr_paradox == "Niższe posiadanie piłki (< 50%)":
                metric_label = "Posiadanie Piłki"
                col_for = "Possession"
                col_opp = None
                val_format = "pct"

            # Podania
            elif "podan" in q_norm:
                metric_label = "Podania (Własne : Rywal)"
                col_for = "Passes_Total"
                col_opp = "Passes_Total_Against"
                val_format = "int"

            # 5. Filtrowanie meczów wg wykrytego kryterium
            if col_opp:
                if op_greater:
                    base_matches = base_matches[base_matches[col_for] > base_matches[col_opp]]
                else:
                    base_matches = base_matches[base_matches[col_for] < base_matches[col_opp]]
            elif col_for == "Possession":
                if op_greater:
                    base_matches = base_matches[base_matches["Possession"] > 50.0]
                else:
                    base_matches = base_matches[base_matches["Possession"] < 50.0]

            # 6. Prezentacja wyników – dokładnie 5 kolumn
            header_team = selected_team_filter if selected_team_filter else "Wszystkie Drużyny (Skala Ligi)"
            venue_txt = "Dom" if selected_venue_filter == "Home" else ("Wyjazd" if selected_venue_filter == "Away" else "Dom + Wyjazd")

            st.subheader(f"📋 Wyniki Wyszukiwania: {header_team}")
            st.caption(f"Kryterium: **{metric_label} ({comp_word})** | Miejsce: **{venue_txt}**")

            if len(base_matches) > 0:
                st.success(f"🤖 **Znaleziono {len(base_matches)} spotkań** spełniających zadane kryteria!")

                table_rows = []
                for _, r in base_matches.iterrows():
                    res_str = f"{int(r['Goals_For'])}:{int(r['Goals_Against'])}"
                    gdzie_str = "Dom" if r["Venue"] == "Home" else "Wyjazd"

                    if val_format == "float":
                        stat_val_str = f"{r[col_for]:.2f} : {r[col_opp]:.2f}"
                    elif val_format == "int":
                        stat_val_str = f"{int(r[col_for])} : {int(r[col_opp])}"
                    elif val_format == "pct":
                        opp_poss = 100.0 - r["Possession"]
                        stat_val_str = f"{r['Possession']:.1f}% : {opp_poss:.1f}%"

                    table_rows.append({
                        "Drużyna": r["Team"],
                        "Gdzie": gdzie_str,
                        "Rywal": r["Opponent"],
                        "Wynik": res_str,
                        metric_label: stat_val_str
                    })

                df_clean_result = pd.DataFrame(table_rows)
                st.dataframe(df_clean_result, use_container_width=True, hide_index=True)

                if not selected_team_filter:
                    st.markdown("##### 🏆 Kto najczęściej notuje takie mecze?")
                    top_counter = base_matches["Team"].value_counts().reset_index()
                    top_counter.columns = ["Drużyna", "Liczba takich spotkań"]
                    st.dataframe(top_counter, use_container_width=True, hide_index=True)
            else:
                st.warning("Nie znaleziono w bazie spotkań spełniających tę kombinację kryteriów.")


# =========================================================================
# TAB 6: PRACOWNIA ZALEŻNOŚCI (PL / EN)
# =========================================================================
with tab_zaleznosci:
    st.header("🔬 Correlation Lab: X vs Y Metrics" if selected_lang == "EN" else "🔬 Zależności: Wybierz osie X i Y")
    st.caption("Investigate relationships and Pearson correlation coefficients across the league." if selected_lang == "EN" else "Wybierz metryki z bazy, aby sprawdzić ich relację oraz siłę korelacji w lidze.")

    if selected_lang == "EN":
        METRIC_DB = {
            "Points in Table": "Punkty",
            "Goals Scored (Avg / 90)": "Gole_na_mecz",
            "Goals Conceded (Avg / 90)": "Gole_stracone_na_mecz",
            "Goal Difference": "Bilans_Bramkowy",
            "Created xG (Avg / 90)": "xG_na_mecz",
            "Conceded xGA (Avg / 90)": "xGA_na_mecz",
            "xG Difference (xG - xGA)": "Bilans_xG",
            "Open Play xG (Avg / 90)": "xG_OP_na_mecz",
            "Open Play xGA Conceded (Avg / 90)": "xGA_OP_na_mecz",
            "Set-Play xG (Avg / 90)": "xG_SP_na_mecz",
            "Set-Play xGA Conceded (Avg / 90)": "xGA_SP_na_mecz",
            "Non-Penalty xG (Avg / 90)": "npxG_na_mecz",
            "Non-Penalty xGA Conceded (Avg / 90)": "npxGA_na_mecz",
            "Team xGOT on Target (Avg / 90)": "xGOT_na_mecz",
            "Opponent xAGOT Conceded (Avg / 90)": "xAGOT_na_mecz",
            "Total Shots (Avg / 90)": "Strzaly_na_mecz",
            "Shots on Target (Avg / 90)": "Celne_strzaly",
            "Shots Inside Box (Avg / 90)": "Strzaly_z_pola_karnego",
            "Shots Outside Box (Avg / 90)": "Strzaly_zza_pola_karnego",
            "Ball Possession (%)": "Posiadanie",
            "Opponent Box Touches (Avg / 90)": "Box_Touches_Mean",
            "Opponent Touches in Our Box (Avg / 90)": "Box_Touches_Against_Mean",
            "Total Team Passes (Avg / 90)": "Podania_ogolem",
            "Opponent Total Passes (Avg / 90)": "Passes_Total_Against_Mean",
            "Passes in Own Half (Avg / 90)": "Passes_Own_Half_Mean",
            "Passes in Opponent Half (Avg / 90)": "Passes_Opp_Half_Mean",
            "Accurate Long Balls (Avg / 90)": "Long_Balls_Mean",
            "Goalkeeper Saves (Avg / 90)": "Keeper_Saves_Mean",
            "Win Rate (%)": "Win_Rate",
            "Total Matches Won": "Wygrane",
            "Box Touches Conversion (Shots/Touch)": "Strzaly_z_pola_karnego", # lub nowa kolumna
            "Long Ball Share (%)": "Udzial_dlugich_pilek_proc",
            "Finishing Delta (Goals - xG)": "Gole_minus_xG",
            "Pass Dominance Balance": "Bilans_Podan_Atak",
        }
    else:
        METRIC_DB = {
            "Punkty w tabeli": "Punkty",
            "Gole Strzelone (Śr. / Mecz)": "Gole_na_mecz",
            "Gole Stracone (Śr. / Mecz)": "Gole_stracone_na_mecz",
            "Bilans Bramkowy": "Bilans_Bramkowy",
            "xG Utworzone (Śr. / Mecz)": "xG_na_mecz",
            "xG Dopuszczone / xGA (Śr. / Mecz)": "xGA_na_mecz",
            "Bilans xG (xG - xGA)": "Bilans_xG",
            "xG Open Play Utworzone (Śr. / Mecz)": "xG_OP_na_mecz",
            "xG Open Play Dopuszczone (Śr. / Mecz)": "xGA_OP_na_mecz",
            "xG Set-Play Utworzone (Śr. / Mecz)": "xG_SP_na_mecz",
            "xG Set-Play Dopuszczone (Śr. / Mecz)": "xGA_SP_na_mecz",
            "npxG Utworzone (Śr. / Mecz)": "npxG_na_mecz",
            "npxG Dopuszczone (Śr. / Mecz)": "npxGA_na_mecz",
            "xGOT Własne (Śr. / Mecz)": "xGOT_na_mecz",
            "xGOT Dopuszczone / xAGOT (Śr. / Mecz)": "xAGOT_na_mecz",
            "Strzały Ogółem (Śr. / Mecz)": "Strzaly_na_mecz",
            "Strzały Celne (Śr. / Mecz)": "Celne_strzaly",
            "Strzały z pola karnego (Śr. / Mecz)": "Strzaly_z_pola_karnego",
            "Strzały zza pola karnego (Śr. / Mecz)": "Strzaly_zza_pola_karnego",
            "Posiadanie Piłki (%)": "Posiadanie",
            "Kontakty w szesnastce rywala (Śr. / Mecz)": "Box_Touches_Mean",
            "Kontakty rywala w naszym polu (Śr. / Mecz)": "Box_Touches_Against_Mean",
            "Podania Ogółem Własne (Śr. / Mecz)": "Podania_ogolem",
            "Podania Ogółem Rywala (Śr. / Mecz)": "Passes_Total_Against_Mean",
            "Podania na Własnej Połowie (Śr. / Mecz)": "Passes_Own_Half_Mean",
            "Podania na Połowie Rywala (Śr. / Mecz)": "Passes_Opp_Half_Mean",
            "Celne Długie Piłki Własne (Śr. / Mecz)": "Long_Balls_Mean",
            "Obrony Własnego Bramkarza (Śr. / Mecz)": "Keeper_Saves_Mean",
            "% Wygranych Meczów (Win Rate)": "Win_Rate",
            "Liczba Wygranych Spotkań": "Wygrane",
            "Udział Długich Piłek (%)": "Udzial_dlugich_pilek_proc",
            "Bilans Wykończenia (Gole - xG)": "Gole_minus_xG",
            "Bilans Podań w Ataku": "Bilans_Podan_Atak",
        }

    metric_options = list(METRIC_DB.keys())
    col_x, col_y, col_team = st.columns([1.2, 1.2, 1.2])

    with col_x:
        x_choice = st.selectbox("Select X Axis (Horizontal):" if selected_lang == "EN" else "Wybierz oś X (pozioma):", metric_options, index=4 if len(metric_options) > 4 else 0, key="sb_custom_x")
    with col_y:
        y_choice = st.selectbox("Select Y Axis (Vertical):" if selected_lang == "EN" else "Wybierz oś Y (pionowa):", metric_options, index=0, key="sb_custom_y")
    with col_team:
        team_opts = ["All (League)" if selected_lang == "EN" else "Wszystkie (Liga)"] + sorted(team_stats["Team"].unique().tolist())
        selected_team_zal = st.selectbox("Highlight Team:" if selected_lang == "EN" else "Podświetl drużynę:", team_opts, index=0, key="sb_custom_team")

    col_x_name = METRIC_DB[x_choice]
    col_y_name = METRIC_DB[y_choice]

    val_x = team_stats[col_x_name]
    val_y = team_stats[col_y_name]
    corr_val = val_x.corr(val_y)

    r_abs = abs(corr_val)
    if r_abs >= 0.7:
        strength = "Very strong relationship" if selected_lang == "EN" else "Bardzo silna zależność"
    elif r_abs >= 0.4:
        strength = "Moderate relationship" if selected_lang == "EN" else "Umiarkowana zależność"
    else:
        strength = "Weak or no relationship" if selected_lang == "EN" else "Słaba zależność lub brak związku"

    st.markdown("---")
    kpi1, kpi2, kpi3 = st.columns(3)
    kpi1.metric("Correlation coefficient (r)" if selected_lang == "EN" else "Współczynnik korelacji (r)", f"{corr_val:+.2f}", strength)
    kpi2.metric(f"League Avg (X): {x_choice.split('(')[0]}" if selected_lang == "EN" else f"Średnia ligowa (X): {x_choice.split('(')[0]}", f"{val_x.mean():.2f}")
    kpi3.metric(f"League Avg (Y): {y_choice.split('(')[0]}" if selected_lang == "EN" else f"Średnia ligowa (Y): {y_choice.split('(')[0]}", f"{val_y.mean():.2f}")

    fig_scatter = go.Figure()
    fig_scatter.add_vline(x=val_x.mean(), line_dash="dash", line_color="#475569", line_width=1.2)
    fig_scatter.add_hline(y=val_y.mean(), line_dash="dash", line_color="#475569", line_width=1.2)

    for _, row in team_stats.iterrows():
        t_name = row["Team"]
        x_pt = row[col_x_name]
        y_pt = row[col_y_name]
        is_sel = (selected_team_zal not in ["All (League)", "Wszystkie (Liga)"] and t_name == selected_team_zal)

        if selected_team_zal in ["All (League)", "Wszystkie (Liga)"]:
            color = "#38BDF8"
            size = 12
        else:
            color = "#EF4444" if is_sel else "#475569"
            size = 18 if is_sel else 9

        fig_scatter.add_trace(go.Scatter(
            x=[x_pt], y=[y_pt],
            mode="markers+text",
            text=[t_name],
            textposition="top center",
            textfont=dict(size=11 if is_sel else 9.5, color="#FFFFFF" if is_sel else "#CBD5E1"),
            marker=dict(size=size, color=color, line=dict(width=1.2, color="#0F172A")),
            hovertemplate=f"<b>{t_name}</b><br>{x_choice}: <b>%{{x:.2f}}</b><br>{y_choice}: <b>%{{y:.2f}}</b><extra></extra>",
            showlegend=False
        ))

    margin_x = (val_x.max() - val_x.min()) * 0.15 if val_x.max() != val_x.min() else 0.2
    margin_y = (val_y.max() - val_y.min()) * 0.15 if val_y.max() != val_y.min() else 0.2

    fig_scatter.update_layout(
        height=620, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
        title=dict(
            text=f"<b>Relationship: {x_choice} vs {y_choice} (r = {corr_val:+.2f})</b>" if selected_lang == "EN" else f"<b>Zależność: {x_choice} vs {y_choice} (r = {corr_val:+.2f})</b>",
            font=dict(size=16, color="#FFFFFF"), x=0.03, y=0.96
        ),
        xaxis=dict(title=f"<b>{x_choice}</b>", range=[val_x.min() - margin_x, val_x.max() + margin_x], showgrid=True, gridcolor="#21262D"),
        yaxis=dict(title=f"<b>{y_choice}</b>", range=[val_y.min() - margin_y, val_y.max() + margin_y], showgrid=True, gridcolor="#21262D"),
        margin=dict(l=60, r=40, t=60, b=50)
    )
    st.plotly_chart(fig_scatter, use_container_width=True)

    # Regresja liniowa
    st.markdown("---")
    st.subheader(f"📈 Linear Regression Model: {y_choice} vs {x_choice}" if selected_lang == "EN" else f"📈 Model Regresji Liniowej: {y_choice} względem {x_choice}")

    x_arr = val_x.to_numpy()
    y_arr = val_y.to_numpy()

    if len(x_arr) > 1 and np.var(x_arr) > 0:
        a_slope, b_intercept = np.polyfit(x_arr, y_arr, 1)
        r2_score = (corr_val ** 2)
        y_pred = a_slope * x_arr + b_intercept
        residuals = y_arr - y_pred

        col_reg1, col_reg2, col_reg3 = st.columns(3)
        col_reg1.metric("R² Score" if selected_lang == "EN" else "Współczynnik determinacji (R²)", f"{r2_score:.2%}")
        col_reg2.metric("Trendline Equation" if selected_lang == "EN" else "Równanie linii trendu", f"Y = {a_slope:+.2f}·X {b_intercept:+.2f}")
        col_reg3.metric("MAE Error" if selected_lang == "EN" else "Średni błąd bezwzględny (MAE)", f"{np.mean(np.abs(residuals)):.2f}")

        fig_reg = go.Figure()
        x_trend = np.linspace(val_x.min() - margin_x * 0.5, val_x.max() + margin_x * 0.5, 50)
        y_trend = a_slope * x_trend + b_intercept

        fig_reg.add_trace(go.Scatter(x=x_trend, y=y_trend, mode="lines", name="Trendline (OLS)" if selected_lang == "EN" else "Linia trendu (OLS)", line=dict(color="#F59E0B", width=2.5, dash="dash"), hoverinfo="skip"))

        for _, row in team_stats.iterrows():
            t_name = row["Team"]
            x_pt = row[col_x_name]
            y_pt = row[col_y_name]
            expected_y = a_slope * x_pt + b_intercept
            diff_y = y_pt - expected_y
            is_sel = (selected_team_zal not in ["All (League)", "Wszystkie (Liga)"] and t_name == selected_team_zal)

            if selected_team_zal in ["All (League)", "Wszystkie (Liga)"]:
                pt_color = "#10B981" if diff_y >= 0 else "#EF4444"
                pt_size = 11
            else:
                pt_color = "#38BDF8" if is_sel else "#475569"
                pt_size = 18 if is_sel else 9

            fig_reg.add_trace(go.Scatter(
                x=[x_pt], y=[y_pt], mode="markers+text", text=[t_name], textposition="top center",
                textfont=dict(size=11 if is_sel else 9.5, color="#FFFFFF" if is_sel else "#CBD5E1"),
                marker=dict(size=pt_size, color=pt_color, line=dict(width=1.2, color="#0F172A")),
                hovertemplate=f"<b>{t_name}</b><br>{x_choice}: <b>{x_pt:.2f}</b><br>{y_choice}: <b>{y_pt:.2f}</b><br>Expected: <b>{expected_y:.2f}</b><br>Residual: <b>{diff_y:+.2f}</b><extra></extra>" if selected_lang == "EN" else f"<b>{t_name}</b><br>{x_choice}: <b>{x_pt:.2f}</b><br>{y_choice}: <b>{y_pt:.2f}</b><br>Oczekiwana: <b>{expected_y:.2f}</b><br>Odchylenie: <b>{diff_y:+.2f}</b><extra></extra>",
                showlegend=False
            ))

        fig_reg.update_layout(
            height=560, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>Regression Fit (R² = {r2_score:.2f}) | Green = Above Model, Red = Below Model</b>" if selected_lang == "EN" else f"<b>Dopasowanie regresyjne: R² = {r2_score:.2f} | Zielone = Nadwyżka ponad model, Czerwone = Wynik poniżej modelu</b>", font=dict(size=14, color="#FFFFFF"), x=0.03, y=0.96),
            xaxis=dict(title=f"<b>{x_choice}</b>", showgrid=True, gridcolor="#21262D"),
            yaxis=dict(title=f"<b>{y_choice}</b>", showgrid=True, gridcolor="#21262D"),
            margin=dict(l=60, r=40, t=55, b=50)
        )
        st.plotly_chart(fig_reg, use_container_width=True)

    # Atak czy Obrona
    st.markdown("---")
    st.subheader("⚖️ Attack or Defense: What Drives Wins More?" if selected_lang == "EN" else "⚖️ Atak czy Obrona? Co daje więcej wygranych?")
    st.caption("Inspect Pearson correlations with win rates across the league or focus on a specific team." if selected_lang == "EN" else "Sprawdź zależność w skali ligi lub profil konkretnej drużyny.")

    r_gf_pts = team_stats["Gole_na_mecz"].corr(team_stats["Punkty"])
    r_ga_pts = team_stats["Gole_stracone_na_mecz"].corr(team_stats["Punkty"])
    r_gf_win = team_stats["Gole_na_mecz"].corr(team_stats["Win_Rate"]) if "Win_Rate" in team_stats.columns else r_gf_pts
    r_ga_win = team_stats["Gole_stracone_na_mecz"].corr(team_stats["Win_Rate"]) if "Win_Rate" in team_stats.columns else r_ga_pts

    if selected_lang == "EN":
        wplyw_win = "ATTACK (Scoring Goals)" if abs(r_gf_win) > abs(r_ga_win) else "DEFENSE (Clean Sheets)"
    else:
        wplyw_win = "ATAK (Strzelanie goli)" if abs(r_gf_win) > abs(r_ga_win) else "OBRONA (Czyste konta)"

    col_w1, col_w2, col_w3 = st.columns(3)
    col_w1.metric("Correlation: Goals vs Wins" if selected_lang == "EN" else "Korelacja: Gole Strzelone vs Wygrane", f"{r_gf_win:+.2f}")
    col_w2.metric("Correlation: Conceded vs Wins" if selected_lang == "EN" else "Korelacja: Gole Stracone vs Wygrane", f"{r_ga_win:+.2f}", delta_color="inverse")
    col_w3.metric("Stronger Deciding Factor" if selected_lang == "EN" else "Co silniej decyduje o 3 pkt?", wplyw_win, f"Weight: {abs(r_gf_win):.2f} vs {abs(r_ga_win):.2f}" if selected_lang == "EN" else f"Waga: {abs(r_gf_win):.2f} vs {abs(r_ga_win):.2f}")

    st.markdown("---")

    col_sel_dylemat, _ = st.columns([1.5, 2.5])
    with col_sel_dylemat:
        all_league_label = "🌐 Full League (Average)" if selected_lang == "EN" else "🌐 Cała Liga (Średnia ligowa)"
        opcje_zespolow = [all_league_label] + sorted(team_stats["Team"].unique().tolist())
        wybrana_perspektywa = st.selectbox(
            "Select Team Perspective:" if selected_lang == "EN" else "Wybierz zespół do analizy skuteczności:",
            opcje_zespolow,
            index=0,
            key="sb_dylemat_team_select"
        )

    if wybrana_perspektywa == all_league_label:
        target_matches = matches_df.copy()
        tytul_sufiks = "League Average" if selected_lang == "EN" else "w skali całej ligi"
    else:
        target_matches = matches_df[matches_df["Team"] == wybrana_perspektywa].copy()
        tytul_sufiks = f"Team: {wybrana_perspektywa}" if selected_lang == "EN" else f"dla: {wybrana_perspektywa}"

    win_by_gf = []
    for g in [0, 1, 2, 3]:
        sub = target_matches[target_matches["Goals_For"] >= g] if g == 3 else target_matches[target_matches["Goals_For"] == g]
        m_cnt = len(sub)
        pct = (sub["Points"] == 3).mean() * 100 if m_cnt > 0 else 0.0
        w_cnt = int((sub["Points"] == 3).sum())
        lbl = (f"{g} goals" if g < 3 else "3+ goals") if selected_lang == "EN" else (f"{g} goli" if g < 3 else "3+ goli")
        win_by_gf.append({"Liczba": lbl, "Szansa_Wygranej": pct, "Mecze": m_cnt, "Wygrane": w_cnt})

    win_by_ga = []
    for g in [0, 1, 2, 3]:
        sub = target_matches[target_matches["Goals_Against"] >= g] if g == 3 else target_matches[target_matches["Goals_Against"] == g]
        m_cnt = len(sub)
        pct = (sub["Points"] == 3).mean() * 100 if m_cnt > 0 else 0.0
        w_cnt = int((sub["Points"] == 3).sum())
        lbl = (f"{g} conceded" if g < 3 else "3+ conceded") if selected_lang == "EN" else (f"{g} straconych" if g < 3 else "3+ stracone")
        win_by_ga.append({"Liczba": lbl, "Szansa_Wygranej": pct, "Mecze": m_cnt, "Wygrane": w_cnt})

    df_odds_gf = pd.DataFrame(win_by_gf)
    df_odds_ga = pd.DataFrame(win_by_ga)

    col_bar_gf, col_bar_ga = st.columns(2)

    with col_bar_gf:
        fig_gf_odds = go.Figure(go.Bar(
            x=df_odds_gf["Liczba"],
            y=df_odds_gf["Szansa_Wygranej"],
            text=[f"<b>{v:.0f}%</b><br>({w}/{m} w.)" if m > 0 else "-" for v, w, m in zip(df_odds_gf["Szansa_Wygranej"], df_odds_gf["Wygrane"], df_odds_gf["Mecze"])],
            textposition="outside",
            marker_color=["#94A3B8", "#38BDF8", "#10B981", "#059669"]
        ))
        fig_gf_odds.update_layout(
            height=390, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>Win Probability by Goals SCORED ({tytul_sufiks})</b>" if selected_lang == "EN" else f"<b>Szansa na wygraną przy danej liczbie goli ZDOBYTYCH ({tytul_sufiks})</b>", font=dict(size=13, color="#FFFFFF")),
            yaxis=dict(title="Win Rate (%)" if selected_lang == "EN" else "% Wygranych spotkań", range=[0, 120], ticksuffix="%"),
            xaxis=dict(title="Goals Scored" if selected_lang == "EN" else "Gole Strzelone w meczu")
        )
        st.plotly_chart(fig_gf_odds, use_container_width=True)

    with col_bar_ga:
        fig_ga_odds = go.Figure(go.Bar(
            x=df_odds_ga["Liczba"],
            y=df_odds_ga["Szansa_Wygranej"],
            text=[f"<b>{v:.0f}%</b><br>({w}/{m} w.)" if m > 0 else "-" for v, w, m in zip(df_odds_ga["Szansa_Wygranej"], df_odds_ga["Wygrane"], df_odds_ga["Mecze"])],
            textposition="outside",
            marker_color=["#10B981", "#F59E0B", "#EF4444", "#991B1B"]
        ))
        fig_ga_odds.update_layout(
            height=390, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22",
            title=dict(text=f"<b>Win Probability by Goals CONCEDED ({tytul_sufiks})</b>" if selected_lang == "EN" else f"<b>Szansa na wygraną przy danej liczbie goli STRACONYCH ({tytul_sufiks})</b>", font=dict(size=13, color="#FFFFFF")),
            yaxis=dict(title="Win Rate (%)" if selected_lang == "EN" else "% Wygranych spotkań", range=[0, 120], ticksuffix="%"),
            xaxis=dict(title="Goals Conceded" if selected_lang == "EN" else "Gole Stracone w meczu")
        )
        st.plotly_chart(fig_ga_odds, use_container_width=True)

    # Podsumowanie taktyczne
    cs_row = df_odds_ga.iloc[0]
    g1_row = df_odds_gf.iloc[1]
    g2_row = df_odds_gf.iloc[2]

    if wybrana_perspektywa == all_league_label:
        if selected_lang == "EN":
            st.info(
                f"💡 **League Average Insights:** Keeping a clean sheet (0 goals conceded) results in a **{cs_row['Szansa_Wygranej']:.1f}%** win rate. "
                f"Scoring exactly 1 goal yields only a **{g1_row['Szansa_Wygranej']:.1f}%** chance for all 3 points, but scoring 2 goals raises that probability to **{g2_row['Szansa_Wygranej']:.1f}%**."
            )
        else:
            st.info(
                f"💡 **Średnia ligowa:** Zachowanie czystego konta (0 straconych) daje **{cs_row['Szansa_Wygranej']:.1f}%** szans na wygraną. "
                f"Strzelenie 1 gola to zaledwie **{g1_row['Szansa_Wygranej']:.1f}%** szans na 3 punkty, ale już 2 bramki windują to prawdopodobieństwo do **{g2_row['Szansa_Wygranej']:.1f}%**."
            )
    else:
        if selected_lang == "EN":
            st.success(
                f"🎯 **Tactical Profile ({wybrana_perspektywa}):**\n\n"
                f"* **Clean Sheet:** In matches with 0 goals conceded, the team won **{cs_row['Wygrane']} of {cs_row['Mecze']}** games (**{cs_row['Szansa_Wygranej']:.0f}%** win rate).\n"
                f"* **Scoring Output:** When scoring exactly 1 goal, the team won **{g1_row['Wygrane']} of {g1_row['Mecze']}** games (**{g1_row['Szansa_Wygranej']:.0f}%**), "
                f"while scoring 2+ goals secured victories in **{g2_row['Wygrane']} of {g2_row['Mecze']}** occasions (**{g2_row['Szansa_Wygranej']:.0f}%**)."
            )
        else:
            st.success(
                f"🎯 **Profil taktyczny ({wybrana_perspektywa}):**\n\n"
                f"* **Czyste konto:** W meczach bez straty bramki drużyna wygrała **{cs_row['Wygrane']} z {cs_row['Mecze']}** spotkań (**{cs_row['Szansa_Wygranej']:.0f}%** skuteczności).\n"
                f"* **Wymóg strzelecki:** Przy zdobyciu dokładnie 1 gola zespół wygrał **{g1_row['Wygrane']} z {g1_row['Mecze']}** meczów (**{g1_row['Szansa_Wygranej']:.0f}%**), "
                f"podczas gdy strzelenie 2 bramek dało wygraną w **{g2_row['Wygrane']} z {g2_row['Mecze']}** przypadków (**{g2_row['Szansa_Wygranej']:.0f}%**)."
            ) 

        # =========================================================
    # DODATEK: GLOBALNA MACIERZ KORELACJI (HEATMAP)
    # =========================================================
    st.markdown("---")
    st.subheader("Global Correlation Matrix (Heatmap)" if selected_lang == "EN" else "Globalna Macierz Korelacji (Pearson)")
    st.caption(
        "Displays linear correlation coefficients (-1 to 1) between key tactical metrics." 
        if selected_lang == "EN" 
        else "Tabela współczynników korelacji liniowej Pearsona (-1 do 1) dla kluczowych metryk. Czerwień to korelacja dodatnia, błękit to korelacja ujemna."
    )

    if selected_lang == "EN":
        heat_metrics = {
            "Points": "Punkty",
            "Goals Scored": "Gole_na_mecz",
            "Goals Conceded": "Gole_stracone_na_mecz",
            "Created xG": "xG_na_mecz",
            "Conceded xGA": "xGA_na_mecz",
            "Possession %": "Posiadanie",
            "Passes / 90": "Podania_ogolem",
            "Box Shots": "Strzaly_z_pola_karnego",
            "Long Balls": "Long_Balls_Mean",
            "Duels Won": "Pojedynki_Wygrane"
        }
    else:
        heat_metrics = {
            "Punkty": "Punkty",
            "Gole Zdobyte": "Gole_na_mecz",
            "Gole Stracone": "Gole_stracone_na_mecz",
            "xG Wykreowane": "xG_na_mecz",
            "xGA Dopuszczone": "xGA_na_mecz",
            "Posiadanie %": "Posiadanie",
            "Podania / 90": "Podania_ogolem",
            "Strz. z Szesnastki": "Strzaly_z_pola_karnego",
            "Długie Piłki": "Long_Balls_Mean",
            "Wygrane Pojedynki": "Pojedynki_Wygrane"
        }

    # Wyciągamy tylko wybrane kolumny z team_stats
    df_heat = team_stats[list(heat_metrics.values())].copy()
    df_heat.columns = list(heat_metrics.keys())
    
    # Obliczamy macierz korelacji
    corr_matrix = df_heat.corr()

    # Rysujemy mapę cieplną (Heatmap)
    fig_hm = px.imshow(
        corr_matrix, 
        text_auto=".2f", 
        aspect="auto", 
        color_continuous_scale="RdBu_r", 
        zmin=-1, zmax=1,
        template="plotly_dark"
    )
    
    fig_hm.update_layout(
        height=700,
        paper_bgcolor="#0E1117", 
        plot_bgcolor="#161B22",
        margin=dict(l=150, r=40, t=50, b=150),
        xaxis=dict(tickangle=-45)
    )
    
    st.plotly_chart(fig_hm, use_container_width=True)


    # =========================================================
    # DODATEK: KLASYFIKACJA STYLÓW GRY (K-MEANS CLUSTERING)
    # =========================================================
    from sklearn.cluster import KMeans
    from sklearn.preprocessing import StandardScaler

    st.markdown("---")
    st.subheader("Tactical Style Classification (K-Means)" if selected_lang == "EN" else "Klasyfikacja Stylów Gry (K-Means Clustering)")
    st.caption("AI-driven clustering of teams into 4 tactical profiles based on Ball Possession, Long Balls, and xG generation." if selected_lang == "EN" else "Algorytm AI grupuje drużyny w 4 profile taktyczne na podstawie Posiadania Piłki, Długich Podań i kreacji xG.")

    # Wybór cech do modelu K-Means
    features = ["Posiadanie", "Udzial_dlugich_pilek_proc", "xG_na_mecz"]
    cluster_data = team_stats[["Team"] + features].copy().dropna()

    if len(cluster_data) >= 4:  # Bezpieczeństwo - potrzebujemy min 4 drużyn do klastrowania
        # Standaryzacja danych (K-Means jest wrażliwy na skalę)
        scaler = StandardScaler()
        scaled_features = scaler.fit_transform(cluster_data[features])

        # Trenowanie modelu
        kmeans = KMeans(n_clusters=4, random_state=42, n_init=10)
        cluster_data["Cluster"] = kmeans.fit_predict(scaled_features)

        # Mapowanie Klastrów (nadanie im roboczych nazw na podstawie posiadania)
        cluster_means = cluster_data.groupby("Cluster")["Posiadanie"].mean().sort_values()
        
        # Tworzymy mapę w zależności od posiadania (od najniższego do najwyższego)
        style_names_en = ["Low Block / Direct", "Counter-Attacking", "Balanced / Transitional", "Possession Dominators"]
        style_names_pl = ["Niski Blok / Gra Bezpośrednia", "Kontratak", "Zrównoważeni / Faza Przejściowa", "Dominatorzy (Tiki-Taka)"]
        names_list = style_names_en if selected_lang == "EN" else style_names_pl
        
        cluster_map = {cluster_id: name for cluster_id, name in zip(cluster_means.index, names_list)}
        cluster_data["Style"] = cluster_data["Cluster"].map(cluster_map)

        # Wizualizacja 3D (Zmieniona na czytelną wersję Hover)
        fig_km = px.scatter_3d(
            cluster_data, 
            x="Posiadanie", 
            y="Udzial_dlugich_pilek_proc", 
            z="xG_na_mecz", 
            color="Style",
            hover_name="Team",  # Nazwa drużyny wyświetli się tylko po najechaniu myszką
            template="plotly_dark",
            height=700,
            labels={
                "Posiadanie": "Possession %" if selected_lang == "EN" else "Posiadanie %",
                "Udzial_dlugich_pilek_proc": "Long Balls %" if selected_lang == "EN" else "Długie Piłki %",
                "xG_na_mecz": "xG / 90"
            }
        )
        
        # Formatowanie kropek i interaktywnego dymka
        hover_template = "<b>%{hovertext}</b><br>Possession: %{x:.1f}%<br>Long Balls: %{y:.1f}%<br>xG / 90: %{z:.2f}<extra></extra>" if selected_lang == "EN" else "<b>%{hovertext}</b><br>Posiadanie: %{x:.1f}%<br>Długie piłki: %{y:.1f}%<br>xG / 90: %{z:.2f}<extra></extra>"

        fig_km.update_traces(
            marker=dict(size=8, line=dict(width=1, color='#0E1117'), opacity=0.9), # Powiększone kropki bez stałego tekstu
            hovertemplate=hover_template
        )
        
        fig_km.update_layout(
            paper_bgcolor="#0E1117", 
            scene=dict(
                xaxis=dict(backgroundcolor="#161B22", gridcolor="#21262D"),
                yaxis=dict(backgroundcolor="#161B22", gridcolor="#21262D"),
                zaxis=dict(backgroundcolor="#161B22", gridcolor="#21262D")
            ),
            legend=dict(
                title="Tactical Profile" if selected_lang == "EN" else "Profil Taktyczny",
                orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5
            )
        )
        
        st.plotly_chart(fig_km, use_container_width=True)
    else:
        st.info("Not enough data to run K-Means clustering." if selected_lang == "EN" else "Zbyt mało danych do wykonania klastrowania.")

    # =========================================================
# AUDYT KOLUMN: EXCEL VS PROGRAM
# =========================================================
with st.sidebar.expander("🛠️ Audyt brakujących kolumn z Excela"):
    # 1. Pobieramy surowe nazwy kolumn z pliku Excel
    raw_excel_df = pd.read_excel(current_league["file"] if current_league["file"] != "TOP5" else "Ekstraklasa 2026-2027.xlsx")
    raw_columns = set([str(c).strip() for c in raw_excel_df.columns])
    
    # Kolumny czysto techniczne / identyfikacyjne, których nie badamy jako statystyki
    ignored_cols = {
        "id", "match_id", "round", "date", "home_team", "away_team", 
        "home_goals", "away_goals", "home_score", "away_score", "status", "referee"
    }
    
    # 2. Sprawdzamy, które nazwy z Excela NIE występują w matches_df
    # Poniższa lista zbiera słowa kluczowe, które już parsujesz w funkcji get_col
    parsed_keywords = [
        "Expected goals", "xG open play", "xG set play", "xG non-penalty", "xG on target",
        "Big chances", "Ball possession", "Own half", "Opposition half", "Shots off target",
        "Blocked shots", "Accurate crosses", "Offsides", "Keeper saves", "Accurate long balls",
        "Touches in opposition box", "Total shots", "Shots on target", "Shots inside box",
        "Shots outside box", "Passes", "Accurate passes", "Corners", "Tackles", "Interceptions",
        "Duels", "Blocks", "Clearances", "Fouls", "woodwork", "dribbles", "Throws", "cards", "Shots"
    ]
    
    missing_cols = []
    for col in sorted(raw_columns):
        if col.lower() in ignored_cols:
            continue
        # Sprawdzamy czy dana kolumna z Excela została uwzględniona w parserze
        if not any(k.lower() in col.lower() for k in parsed_keywords):
            missing_cols.append(col)
            
    st.write(f"Znaleziono **{len(missing_cols)}** nieużywanych kolumn:")
    st.write(missing_cols)            