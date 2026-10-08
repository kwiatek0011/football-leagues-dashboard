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
    """Tworzy zsynchronizowany widok 2-kolumnowy wspierający ujemne wartości oraz dynamiczny zakres (Top 20 vs Całość)."""
    lang = st.session_state.get("selected_lang", "PL")
    
    # 0. Bezpieczny przełącznik zakresu (Top 20 vs Całość) z unikalnym kluczem dla każdego wykresu
    scope_opts = ["Top 20", "Pełna Lista (Wszystkie zespoły)"] if lang == "PL" else ["Top 20", "Full List (All Teams)"]
    selected_scope = st.radio(
        "Zakres rankingu:" if lang == "PL" else "Ranking Scope:",
        scope_opts,
        index=0,
        horizontal=True,
        key=f"scope_radio_{col_name}"
    )
    show_all = bool(selected_scope and ("Pełna" in selected_scope or "Full" in selected_scope))

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
    
    # Dynamiczna wysokość wykresu w zależności od liczby drużyn
    plot_height = 620 if not show_all else max(620, len(sorted_df) * 26)

    fig.update_layout(
        height=plot_height,
        template="simple_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#F8FAFC",
        title=dict(
            text=f"<b>{title_chart}</b>" + (f" ({len(sorted_df)})" if show_all else " (Top 20)"),
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
        components.html(table_html, height=plot_height, scrolling=True if show_all else False)

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
tab_ogolne, tab_ofensywa, tab_defensywa, tab_podania, tab_druzyny, tab_h2h,tab_zaleznosci = st.tabs([
    t("tab_general"),
    t("tab_offense"), 
    t("tab_defense"),
    t("tab_passing"),
    t("tab_teams"),
    t("tab_h2h"),
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
        
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            title_real = ("Real Standings" if selected_lang == "EN" else "Tabela Realna") + (f" ({len(tab_real)})" if show_all else " (Top 20)")
            components.html(render_dark_table_html(tab_real, title_real, is_xg=False), height=620, scrolling=True if show_all else False)
        with col_t2:
            title_xg = ("Expected Goals (xG) Table" if selected_lang == "EN" else "Tabela xG") + (f" ({len(tab_xg_comp)})" if show_all else " (Top 20)")
            components.html(render_dark_table_html(tab_xg_comp, title_xg, is_xg=True), height=620, scrolling=True if show_all else False)


    # 2. Widok: Dom vs Wyjazd
    elif ogolne_widok == t("gen_opt2"):
        home_matches = matches_df[matches_df["Venue"] == "Home"]
        away_matches = matches_df[matches_df["Venue"] == "Away"]
        
        tab_home = compute_custom_table(home_matches, is_xg=False)
        tab_away = compute_custom_table(away_matches, is_xg=False)
        
        col_h, col_a = st.columns(2)
        with col_h:
            t_home = "🏠 Home Table" if selected_lang == "EN" else "🏠 Tabela: Mecze u Siebie"
            components.html(render_dark_table_html(tab_home, t_home, is_xg=False), height=590, scrolling=False)
        with col_a:
            t_away = "🚌 Away Table" if selected_lang == "EN" else "🚌 Tabela: Mecze na Wyjeździe"
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


# =========================================================================
# TAB 2: STATYSTYKI OFENSYWNE (PL / EN)
# =========================================================================
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
        st.markdown("---")
        team_list = sorted(team_stats["Team"].unique().tolist())
        selected_line_team = st.selectbox("Select team for trend analysis:" if selected_lang == "EN" else "Wybierz drużynę do analizy serii bramkowej:", team_list, index=0)
        team_matches = matches_df[matches_df["Team"] == selected_line_team].copy().reset_index(drop=True)
        team_matches["Kolejka"] = team_matches.index + 1
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(
            x=team_matches["Kolejka"], y=team_matches["xG_For"], mode="lines+markers",
            name="Created xG" if selected_lang == "EN" else "Utworzone xG",
            line=dict(color="#38BDF8", width=3), marker=dict(size=11, color="#38BDF8")
        ))
        league_avg_xg = team_stats["xG_na_mecz"].mean()
        fig_trend.add_hline(
            y=league_avg_xg, line_dash="dot", line_color="#94A3B8", line_width=2,
            annotation_text=f"{t('league_avg')}: {league_avg_xg:.2f} xG", annotation_position="bottom right"
        )
        fig_trend.update_layout(height=460, template="plotly_dark", paper_bgcolor="#0E1117", plot_bgcolor="#161B22", xaxis=dict(title="Matchweek" if selected_lang == "EN" else "Numer Kolejki", dtick=1), yaxis=dict(title="xG"))
        st.plotly_chart(fig_trend, use_container_width=True)

    # 3. xG Open Play
    elif ofensywa_widok == t("att_opt3"):
        st.subheader("Open Play xG" if selected_lang == "EN" else "Kreacja sytuacji z gry otwartej (Open Play xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_OP_na_mecz", title_chart="Open Play xG Rankings",
            title_paper="Open Play xG Rankings", value_header="xG OP / 90", color_scale="Greens"
        )

    # 4. xG Set Play
    elif ofensywa_widok == t("att_opt4"):
        st.subheader("Set Play xG" if selected_lang == "EN" else "Groźność po stałych fragmentach gry (Set Play xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_SP_na_mecz", title_chart="Set Play xG Rankings",
            title_paper="Set Play xG Rankings", value_header="SP xG / 90", color_scale="Oranges"
        )

    # 5. npxG
    elif ofensywa_widok == t("att_opt5"):
        st.subheader("Non-Penalty xG" if selected_lang == "EN" else "Czyste zagrożenie bez rzutów karnych (Non-Penalty xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="npxG_na_mecz", title_chart="Non-Penalty xG Rankings",
            title_paper="Non-Penalty xG Rankings", value_header="npxG / 90", color_scale="Purples"
        )

    # 6. xGOT
    elif ofensywa_widok == t("att_opt6"):
        st.subheader("Expected Goals on Target (xGOT)" if selected_lang == "EN" else "Jakość uderzeń zmierzających w światło bramki (xGOT)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xGOT_na_mecz", title_chart="Expected Goals on Target (xGOT) Rankings",
            title_paper="xGOT Rankings", value_header="xGOT / 90", color_scale="Tealgrn"
        )

    # 7. xG / Shot
    elif ofensywa_widok == t("att_opt7"):
        st.subheader("Expected Goals per Shot" if selected_lang == "EN" else "Średnia jakość pojedynczego strzału (xG / Shot)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_na_strzal", title_chart="Expected Goals per Shot (xG/Shot) Rankings",
            title_paper="xG per Shot Rankings", value_header="xG / Shot", color_scale="Viridis"
        )

    # 8. xG / Goal
    elif ofensywa_widok == t("att_opt8"):
        st.subheader("xG Needed per Goal" if selected_lang == "EN" else "Ile xG potrzebuje drużyna, by zdobyć 1 bramkę?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="xG_na_gola", title_chart="xG Needed per Goal Rankings",
            title_paper="xG / Goal Rankings", value_header="xG / 1 Gol" if selected_lang == "PL" else "xG / 1 Goal",
            color_scale="RdYlGn_r", sort_asc=False
        )

    # 9. SoT / Goal
    elif ofensywa_widok == t("att_opt9"):
        st.subheader("Shots on Target per Goal" if selected_lang == "EN" else "Zabójcza precyzja: Ile celnych strzałów (SoT) potrzeba na 1 bramkę?")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celne_na_gola", title_chart="Shots on Target Needed per Goal",
            title_paper="SoT / Goal Rankings", value_header="SoT / Goal" if selected_lang == "EN" else "SoT / 1 Gol",
            color_scale="RdYlGn_r", sort_asc=True
        )

    # 10. Gole - xG
    elif ofensywa_widok == t("att_opt10"):
        st.subheader("Finishing Over/Underperformance (Goals - xG)" if selected_lang == "EN" else "Przestrzelone okazje czy genialni napastnicy? (Zdobyte bramki - Suma xG)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Gole_minus_xG", title_chart="Finishing Overperformance (Goals - xG)",
            title_paper="Goals - xG Rankings" if selected_lang == "EN" else "Gole - xG Rankings",
            value_header="Goals - xG" if selected_lang == "EN" else "Gole - xG",
            color_scale="RdYlGn", sort_asc=False
        )


    # 11. Box Shots
    elif ofensywa_widok == t("att_opt11"):
        st.subheader("Shots Inside Box" if selected_lang == "EN" else "Obecność w szesnastce: Średnia strzałów z pola karnego")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Strzaly_z_pola_karnego", title_chart="Shots Inside Box per Match",
            title_paper="Shots Inside Box Rankings", value_header="Box Shots / 90" if selected_lang == "EN" else "Strzały w polu / 90",
            color_scale="Blues", sort_asc=False
        )

    # 12. Outside Box Shots
    elif ofensywa_widok == t("att_opt12"):
        st.subheader("Shots Outside Box (Long Range)" if selected_lang == "EN" else "Średnia strzałów zza pola karnego")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Strzaly_zza_pola_karnego", title_chart="Shots Outside Box per Match",
            title_paper="Shots Outside Box Rankings", value_header="Outside Shots / 90" if selected_lang == "EN" else "Strzały z dystansu / 90",
            color_scale="Purples", sort_asc=False
        )

        

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

    # 14. Celność strzałów
    elif ofensywa_widok == t("att_opt14"):
        st.subheader("🎯 Shot Accuracy (%)" if selected_lang == "EN" else "🎯 Celność Strzałów (Shot Accuracy %)")
        render_metric_bar_and_paper(
            df=team_stats, col_name="Celnosc_strzalow_proc", title_chart="Shot Accuracy %",
            title_paper="Shot Accuracy Rankings", value_header="Accuracy %" if selected_lang == "EN" else "Celność %",
            color_scale="Blues", sort_asc=False
        )

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

    # 17. xG vs xGOT
    elif ofensywa_widok == t("att_opt17"):
        st.subheader("Shot Creation (xG) vs Shot Execution (xGOT)" if selected_lang == "EN" else "Relacja xG vs xGOT (Jakość kreacji vs Strzału)")
        fig_rel = px.scatter(team_stats, x="xG_na_mecz", y="xGOT_na_mecz", text="Team", template="plotly_dark", height=580)
        fig_rel.update_traces(textposition="top center", marker=dict(size=12, color="#10B981"))
        st.plotly_chart(fig_rel, use_container_width=True)

    # 18. Kontakty vs Strzały
    elif ofensywa_widok == t("att_opt18"):
        st.subheader("Box Efficiency: Touches in Box vs Shots" if selected_lang == "EN" else "Efektywność w szesnastce: Kontakty vs Strzały")
        fig_box = px.scatter(team_stats, x="Kontakty_w_polu_karnym", y="Strzaly_z_pola_karnego", text="Team", template="plotly_dark", height=580)
        fig_box.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
        st.plotly_chart(fig_box, use_container_width=True)

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

    # 20. xGOT vs Bramki
    elif ofensywa_widok == t("att_opt20"):
        st.subheader("Goals vs xGOT (Finishing Overperformance)" if selected_lang == "EN" else "xGOT vs Bramki zdobyte (Over/Underperformance)")
        fig_xgot = px.scatter(team_stats, x="xGOT_Suma", y="Gole_Strzelone", text="Team", template="plotly_dark", height=560)
        fig_xgot.update_traces(textposition="top center", marker=dict(size=12, color="#AF7AC5"))
        st.plotly_chart(fig_xgot, use_container_width=True)

# =========================================================================
# TAB 3: STATYSTYKI DEFENSYWNE (PL / EN)
# =========================================================================
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
    # WIZUALIZACJA: MAPA STRZAŁÓW (SYMULACJA)
    # =========================================================
    st.markdown("---")
    
    # Nagłówek i przełącznik trybu w dwóch kolumnach (tytuł po lewej, przełącznik "z boczku")
    col_map_head, col_map_toggle = st.columns([3, 1])
    
    with col_map_head:
        if selected_lang == "EN":
            st.markdown(f"##### Shot Map Visualization (Simulated): {selected_prof_team}")
            st.caption("Approximate distribution of shots inside and outside the penalty box. Assumes attacking towards the right side.")
        else:
            st.markdown(f"##### Wizualizacja Mapy Strzałów (Symulacja): {selected_prof_team}")
            st.caption("Przybliżone rozmieszczenie strzałów z pola karnego i z dystansu. Atak prowadzony na prawą bramkę.")
            
    with col_map_toggle:
        mode_opts = ["Suma (Cały Sezon)", "Średnia (Na mecz)"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)"]
        shot_mode = st.radio(
            "Tryb wyświetlania:" if selected_lang == "PL" else "Display Mode:", 
            mode_opts, 
            key="radio_shot_map_mode"
        )
        
    is_avg = "Średnia" in shot_mode or "Average" in shot_mode

    # Pobranie danych w zależności od wybranego trybu
    if is_avg:
        raw_box = t_matches['Box_Shots'].mean()
        raw_out = t_matches['Outside_Box_Shots'].mean()
        # Do narysowania kropek potrzebujemy liczb całkowitych
        dots_box = int(round(raw_box))
        dots_out = int(round(raw_out))
        # Tekst do legendy (z jednym miejscem po przecinku dla dokładności)
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
        
        # Obrys, środek i pola
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
            height=550,
            xaxis=dict(visible=False, range=[-3, 108], fixedrange=True),
            yaxis=dict(visible=False, range=[-3, 71], scaleanchor="x", scaleratio=1, fixedrange=True),
            plot_bgcolor="#0E1117", paper_bgcolor="#0E1117", margin=dict(l=10, r=10, t=30, b=10),
            showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5, font=dict(color="#FFFFFF"))
        )
        return fig_p

    fig_pitch = draw_dark_pitch()
    seed_val = sum(ord(c) for c in selected_prof_team)

    # Nanoszenie strzałów z pola karnego (liczba kropek = dots_box)
    if dots_box > 0:
        np.random.seed(seed_val)
        box_x = np.random.triangular(88.5, 96.0, 103.0, dots_box)
        box_y = np.random.triangular(18.0, 34.0, 50.0, dots_box)
        
        fig_pitch.add_trace(go.Scatter(
            x=box_x, y=box_y, mode="markers", name=box_label,
            marker=dict(color="#10B981", size=8 if is_avg else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    # Nanoszenie strzałów z dystansu (liczba kropek = dots_out)
    if dots_out > 0:
        np.random.seed(seed_val + 1)
        out_x = np.random.triangular(65.0, 85.0, 88.4, dots_out) 
        out_y = np.random.triangular(12.0, 34.0, 56.0, dots_out)
        
        fig_pitch.add_trace(go.Scatter(
            x=out_x, y=out_y, mode="markers", name=out_label,
            marker=dict(color="#38BDF8", size=8 if is_avg else 7, line=dict(width=1, color="#0E1117")),
            hoverinfo="name"
        ))

    col_map1, col_map2, col_map3 = st.columns([0.15, 4, 0.15])
    with col_map2:
        st.plotly_chart(fig_pitch, use_container_width=True)

# =========================================================
    # WIZUALIZACJA: MAPA DOPUSZCZONYCH STRZAŁÓW (OBRONA)
    # =========================================================
    st.markdown("---")
    
    # Nagłówek i przełącznik trybu dla mapy defensywnej
    col_map_head_def, col_map_toggle_def = st.columns([3, 1])
    
    with col_map_head_def:
        if selected_lang == "EN":
            st.markdown(f"##### Conceded Shot Map (Simulated): {selected_prof_team}")
            st.caption("Approximate distribution of shots conceded by the team. Assumes opponents attacking towards the left side (defending).")
        else:
            st.markdown(f"##### Wizualizacja Dopuszczonych Strzałów (Symulacja): {selected_prof_team}")
            st.caption("Przybliżone rozmieszczenie strzałów dopuszczonych rywalom z pola karnego i z dystansu. Obrona na lewą bramkę.")
            
    with col_map_toggle_def:
        mode_opts_def = ["Suma (Cały Sezon)", "Średnia (Na mecz)"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)"]
        shot_mode_def = st.radio(
            "Tryb wyświetlania:" if selected_lang == "PL" else "Display Mode:", 
            mode_opts_def, 
            key="radio_shot_map_mode_def" # Ważne: inny klucz niż wyżej!
        )
        
    is_avg_def = "Średnia" in shot_mode_def or "Average" in shot_mode_def

    # Pobranie statystyk rywala (Against)
    if is_avg_def:
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

    # Wykorzystujemy zdefiniowaną wyżej funkcję rysującą boisko
    fig_pitch_def = draw_dark_pitch()
    
    # Inny seed losowania, żeby kropki ułożyły się inaczej niż w ataku
    seed_val_def = sum(ord(c) for c in selected_prof_team) + 99 

    # Nanoszenie DOPUSZCZONYCH strzałów z pola karnego (atak rywala na LEWĄ bramkę)
    if dots_box_def > 0:
        np.random.seed(seed_val_def)
        # Szesnastka z lewej strony ma współrzędne X od 0 do 16.5
        box_x_def = np.random.triangular(2.0, 9.0, 16.5, dots_box_def)
        box_y_def = np.random.triangular(18.0, 34.0, 50.0, dots_box_def)
        
        fig_pitch_def.add_trace(go.Scatter(
            x=box_x_def, y=box_y_def, mode="markers", name=box_label_def,
            marker=dict(color="#EF4444", size=8 if is_avg_def else 7, line=dict(width=1, color="#0E1117")), # Czerwone kropki zagrożenia
            hoverinfo="name"
        ))

    # Nanoszenie DOPUSZCZONYCH strzałów z dystansu (przed lewą szesnastką)
    if dots_out_def > 0:
        np.random.seed(seed_val_def + 1)
        # Przedpole lewej bramki to X od ok. 16.6 do 40
        out_x_def = np.random.triangular(16.6, 22.0, 40.0, dots_out_def) 
        out_y_def = np.random.triangular(12.0, 34.0, 56.0, dots_out_def)
        
        fig_pitch_def.add_trace(go.Scatter(
            x=out_x_def, y=out_y_def, mode="markers", name=out_label_def,
            marker=dict(color="#F59E0B", size=8 if is_avg_def else 7, line=dict(width=1, color="#0E1117")), # Pomarańczowe kropki
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
        f"📊 Statistical DNA: {selected_prof_team} (Z-Score Standardization)" 
        if selected_lang == "EN" 
        else f"📊 Statystyczne DNA: {selected_prof_team} (Standaryzacja Z-Score)"
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


def generate_tactical_ai_insights(df, team_a, team_b, metrics_config, lang="PL"):
    """
    Silnik analityczny AI:
    1. Wykrywa anomalie ligowe (Z-Score > 1.0σ lub < -1.0σ)
    2. Wykrywa kluczowe dysproporcje bezpośrednie pomiędzy Drużyną A i Drużyną B
    """
    row_a = df[df["Team"] == team_a].iloc[0]
    row_b = df[df["Team"] == team_b].iloc[0]
    
    insights_a = []
    insights_b = []
    h2h_clashes = []

    for label_pl, label_en, col, lower_is_better in metrics_config:
        lbl = label_en if lang == "EN" else label_pl
        val_a = float(row_a[col])
        val_b = float(row_b[col])
        mean_val = df[col].mean()
        std_val = df[col].std() if df[col].std() > 0 else 1.0
        
        # Z-Score względem ligi
        za = (val_a - mean_val) / std_val
        zb = (val_b - mean_val) / std_val
        
        # Odwracamy interpretację dla xGA i goli straconych (mniej = lepiej)
        norm_za = -za if lower_is_better else za
        norm_zb = -zb if lower_is_better else zb
        
        # Wykrywanie anomalii ligowych dla Drużyny A
        if norm_za >= 1.0:
            insights_a.append((f" **{lbl}**: {val_a:.2f} *(+{za:+.1f}σ ponad ligę)*", "strength"))
        elif norm_za <= -1.0:
            insights_a.append((f" **{lbl}**: {val_a:.2f} *({za:+.1f}σ poniżej ligi)*", "weakness"))
            
        # Wykrywanie anomalii ligowych dla Drużyny B
        if norm_zb >= 1.0:
            insights_b.append((f" **{lbl}**: {val_b:.2f} *(+{zb:+.1f}σ ponad ligę)*", "strength"))
        elif norm_zb <= -1.0:
            insights_b.append((f" **{lbl}**: {val_b:.2f} *({zb:+.1f}σ poniżej ligi)*", "weakness"))
            
        # Bezpośrednie zderzenie H2H (różnica > 1.2 odchylenia standardowego między nimi)
        diff_z = norm_za - norm_zb
        if abs(diff_z) >= 1.2:
            leader = team_a if diff_z > 0 else team_b
            chaser = team_b if diff_z > 0 else team_a
            v_lead = val_a if diff_z > 0 else val_b
            v_chase = val_b if diff_z > 0 else val_a
            
            if lang == "EN":
                h2h_clashes.append(
                    f" **Major Disparity in {lbl}**: **{leader}** ({v_lead:.2f}) completely outclasses **{chaser}** ({v_chase:.2f})."
                )
            else:
                h2h_clashes.append(
                    f" **Wyraźna przewaga w: {lbl}**: **{leader}** ({v_lead:.2f}) deklasuje rywala **{chaser}** ({v_chase:.2f})."
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
        # AUTOMATYCZNY SILNIK RAPORTOWY AI (TACTICAL INSIGHTS)
        # =========================================================
        st.markdown("---")
        st.subheader(" Automated Tactical Scouting Report (AI Insights)" if selected_lang == "EN" else " Automatyczny Raport Taktyczny AI (Analiza Anomalii i Przewag)")
        st.caption(
            "Algorithmic anomaly detection based on League Z-Scores (|σ| ≥ 1.0) and direct stylistic clashes."
            if selected_lang == "EN"
            else "Algorytmiczny system wykrywania anomalii względem ligi (|σ| ≥ 1.0) oraz bezpośrednich dysproporcji stylów obu zespołów."
        )

        # Konfiguracja metryk do analizatora: (PL, EN, kolumna, czy_mniej_znaczy_lepiej)
        ai_metrics_pool = [
            ("Gole Strzelone", "Goals Scored", "Gole_na_mecz", False),
            ("Gole Stracone", "Goals Conceded", "Gole_stracone_na_mecz", True),
            ("Wykreowane xG", "Created xG", "xG_na_mecz", False),
            ("Dopuszczone xGA", "Conceded xGA", "xGA_na_mecz", True),
            ("xG z Gry Otwartej", "Open Play xG", "xG_OP_na_mecz", False),
            ("Strzały z Szesnastki", "Box Shots", "Strzaly_z_pola_karnego", False),
            ("Posiadanie Piłki (%)", "Ball Possession (%)", "Posiadanie", False),
            ("Długie Piłki", "Long Balls", "Long_Balls_Mean", False),
            ("Podania na Połowie Rywala", "Opponent Half Passes", "Passes_Opp_Half_Mean", False),
            ("Wygrane Pojedynki", "Duels Won", "Pojedynki_Wygrane", False)
        ]

        ins_a, ins_b, clashes = generate_tactical_ai_insights(
            team_stats, team_a, team_b, ai_metrics_pool, lang="EN" if selected_lang == "EN" else "PL"
        )

        col_ai_a, col_ai_b = st.columns(2)

        with col_ai_a:
            st.markdown(f"####  {team_a} vs Liga")
            if ins_a:
                for text, kind in ins_a:
                    if kind == "strength":
                        st.success(text)
                    else:
                        st.error(text)
            else:
                st.info("Drużyna porusza się w granicach ligowej średniej we wszystkich kluczowych metrykach." if selected_lang == "PL" else "The team operates strictly within league average boundaries.")

        with col_ai_b:
            st.markdown(f"####  {team_b} vs Liga")
            if ins_b:
                for text, kind in ins_b:
                    if kind == "strength":
                        st.success(text)
                    else:
                        st.error(text)
            else:
                st.info("Drużyna porusza się w granicach ligowej średniej we wszystkich kluczowych metrykach." if selected_lang == "PL" else "The team operates strictly within league average boundaries.")

        # Sekcja bezpośredniego starcia stylów
        if clashes:
            st.markdown("####  Główne Różnice Stylistyczne w tym Meczu" if selected_lang == "PL" else "####  Critical Stylistic Clashes in this Matchup")
            for c in clashes:
                st.warning(c)



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