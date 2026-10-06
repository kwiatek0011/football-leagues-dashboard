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
                return row[c]
        for col_name in row.index:
            col_lower = str(col_name).lower()
            for cand in candidates:
                if cand.lower() in col_lower and pd.notna(row[col_name]):
                    return row[col_name]
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
    
    return matches_df, team_stats

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
