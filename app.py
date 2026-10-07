import streamlit as st
import streamlit.components.v1 as components
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px
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
        
        # Moduły Obrony
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

        # Moduły Podań
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
        
        # Moduły Obrony
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

        # Moduły Podań
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

st.set_page_config(page_title="Football Team Analytics", layout="wide")

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
        Wygrana=("Wygrana", "sum"),
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

def render_dark_table_html(df, title, is_xg=False, lang="PL"):
    """Renderuje kompaktową tabelę w ciemnym stylu z dynamicznym językiem (PL / EN)."""
    
    # Dobór etykiet kolumn w zależności od języka i trybu (Real vs xG)
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

def render_metric_bar_and_paper(df, col_name, title_chart, title_paper, value_header, color_scale="Greens", sort_asc=False):
    """Tworzy zsynchronizowany widok 2-kolumnowy wspierający ujemne wartości."""
    sorted_df = df.sort_values(by=col_name, ascending=sort_asc).copy().reset_index(drop=True)
    avg_val = sorted_df[col_name].mean()
    
    # Wykres słupkowy
    fig = go.Figure()
    fig.add_trace(go.Bar(
        x=sorted_df[col_name],
        y=sorted_df["Team"],
        orientation='h',
        text=[
            f"{v:+.2f}" if ("Gole - xG" in value_header or "Gole - xGA" in value_header)
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
        annotation_text=f"Średnia: {avg_val:.2f}", 
        annotation_position="bottom right" if avg_val >= 0 else "bottom left",
        annotation_font=dict(size=10, color="#475569")
    )
    
    x_min, x_max = sorted_df[col_name].min(), sorted_df[col_name].max()
    x_range = [x_min * 1.3 if x_min < 0 else 0, x_max * 1.25 if x_max > 0 else 0]
    
    fig.update_layout(
        height=620,
        template="simple_white",
        paper_bgcolor="#FFFFFF",
        plot_bgcolor="#F8FAFC",
        title=dict(
            text=f"<b>{title_chart}</b>",
            x=0.04, y=0.96,
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
            tickfont=dict(size=11, color="#0F172A", family="Arial, sans-serif")
        ),
        margin=dict(l=120, r=40, t=50, b=50)
    )
    
    # Generowanie ciemnej tabeli HTML
    rows_html = ""
    for idx, row in sorted_df.iterrows():
        rank = idx + 1
        team = row["Team"]
        val = row[col_name]
        matches = int(row["Mecze"]) if "Mecze" in row else len(sorted_df)
        
        if "Gole - xG" in value_header:
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
        
    lang = st.session_state.get("selected_lang", "PL")
    th_bar_team = "Team" if lang == "EN" else "Drużyna"
    th_bar_m = "MP" if lang == "EN" else "M"

    table_html = f"""
    <div style="background-color: #1a1d21; border: 1px solid #2d333b; border-radius: 6px; padding: 14px 18px; font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;">
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
        components.html(table_html, height=620, scrolling=False)


# =========================================================================
# WYBÓR LIGI I DYNAMICZNE WCZYTANIE DANYCH
# =========================================================================
LEAGUES_CONFIG = {
    "PKO BP Ekstraklasa": {"file": "Ekstraklasa 2026-2027.xlsx", "title": "🇵🇱 Ekstraklasa - Zaawansowany Dashboard Analityczny"},
    "Premier League": {"file": "Premier League 2026-2027.xlsx", "title": " Premier League - Zaawansowany Dashboard Analityczny"},
    "La Liga": {"file": "La Liga 26-27.xlsx", "title": "La Liga - Zaawansowany Dashboard Analityczny"},
    "Serie A": {"file": "Serie A 26-27.xlsx", "title": "Serie A - Zaawansowany Dashboard Analityczny"},
    "Bundesliga": {"file": "Bundesliga 26-27.xlsx", "title": "Bundesliga - Zaawansowany Dashboard Analityczny"},
    "Ligue 1": {"file": "Ligue 1 26-27.xlsx", "title": "Ligue 1 - Zaawansowany Dashboard Analityczny"}
}

if "selected_lang" not in st.session_state:
    st.session_state["selected_lang"] = "PL"

def t(key):
    return TRANSLATIONS.get(st.session_state["selected_lang"], {}).get(key, key)

col_league_sel, col_space, col_lang = st.columns([2.6, 0.4, 1.0])

with col_lang:
    st.markdown("<p style='font-size: 12px; font-weight: 600; color: #94A3B8; margin-bottom: 2px;'>🌐 Język / Language:</p>", unsafe_allow_html=True)
    c_fl_pl, c_fl_en = st.columns(2)
    with c_fl_pl:
        is_active_pl = "border: 2px solid #38BDF8;" if st.session_state["selected_lang"] == "PL" else "opacity: 0.5;"
        st.markdown(f"""<div style="display:flex; justify-content:center; margin-bottom: 4px;"><img src="https://flagcdn.com/w40/pl.png" width="28" style="border-radius: 3px; {is_active_pl}"></div>""", unsafe_allow_html=True)
        if st.button("PL", key="btn_lang_pl", use_container_width=True):
            st.session_state["selected_lang"] = "PL"
            st.rerun()

    with c_fl_en:
        is_active_en = "border: 2px solid #38BDF8;" if st.session_state["selected_lang"] == "EN" else "opacity: 0.5;"
        st.markdown(f"""<div style="display:flex; justify-content:center; margin-bottom: 4px;"><img src="https://flagcdn.com/w40/gb.png" width="28" style="border-radius: 3px; {is_active_en}"></div>""", unsafe_allow_html=True)
        if st.button("EN", key="btn_lang_en", use_container_width=True):
            st.session_state["selected_lang"] = "EN"
            st.rerun()

selected_lang = st.session_state["selected_lang"]

with col_league_sel:
    selected_league_name = st.selectbox(
        t("choose_league"),
        list(LEAGUES_CONFIG.keys()),
        index=0,
        key="sb_main_league_selector"
    )

current_league = LEAGUES_CONFIG[selected_league_name]
matches_df, team_stats = load_and_process_team_data(current_league["file"])

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

display_df = team_stats.copy()
float_cols = display_df.select_dtypes(include=["float"]).columns
display_df[float_cols] = display_df[float_cols].round(2)
display_df.columns = [col.replace("_", " ") for col in display_df.columns]

# =========================================================================
# ZAKŁADKI
# =========================================================================
tab_ogolne, tab_ofensywa, tab_defensywa, tab_podania, tab_druzyny, tab_zaleznosci = st.tabs([
    t("tab_general"), t("tab_offense"), t("tab_defense"), t("tab_passing"), t("tab_teams"), t("tab_insights")
]) 

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
# TAB 1: OGÓLNE STATYSTYKI
# =========================================================================
with tab_ogolne:
    ogolne_widok = st.selectbox(
        t("gen_select"), [t("gen_opt1"), t("gen_opt2"), t("gen_opt3")]
    )
    st.markdown("---")

    if ogolne_widok == t("gen_opt1"):
        tab_real = compute_custom_table(matches_df, is_xg=False)
        tab_xg_comp = compute_custom_table(matches_df, is_xg=True)
        col_t1, col_t2 = st.columns(2)
        with col_t1:
            title_real = "Real Standings" if selected_lang == "EN" else "Tabela Realna"
            components.html(render_dark_table_html(tab_real, title_real, is_xg=False, lang=selected_lang), height=590, scrolling=False)
        with col_t2:
            title_xg = "Expected Goals (xG) Table" if selected_lang == "EN" else "Tabela xG"
            components.html(render_dark_table_html(tab_xg_comp, title_xg, is_xg=True, lang=selected_lang), height=590, scrolling=False)

    elif ogolne_widok == t("gen_opt2"):
        home_matches = matches_df[matches_df["Venue"] == "Home"]
        away_matches = matches_df[matches_df["Venue"] == "Away"]
        tab_home = compute_custom_table(home_matches, is_xg=False)
        tab_away = compute_custom_table(away_matches, is_xg=False)
        col_h, col_a = st.columns(2)
        with col_h:
            t_home = "🏠 Home Table" if selected_lang == "EN" else "🏠 Tabela: Mecze u Siebie"
            components.html(render_dark_table_html(tab_home, t_home, is_xg=False, lang=selected_lang), height=590, scrolling=False)
        with col_a:
            t_away = "🚌 Away Table" if selected_lang == "EN" else "🚌 Tabela: Mecze na Wyjeździe"
            components.html(render_dark_table_html(tab_away, t_away, is_xg=False, lang=selected_lang), height=590, scrolling=False)
            
        st.markdown("---")
        st.subheader("Home Advantage Analysis (xG Home vs Away)" if selected_lang == "EN" else "Wpływ Własnego Boiska na Jakość Gry (Expected Goals Dom vs Wyjazd)")
        venue_summary = matches_df.groupby(["Team", "Venue"]).agg(xG_mean=("xG_For", "mean"), xGA_mean=("xG_Against", "mean"), Mecze=("Points", "count")).unstack()
        venue_df = pd.DataFrame({
            "Team": venue_summary.index,
            "xG_Home": venue_summary[("xG_mean", "Home")].round(2),
            "xG_Away": venue_summary[("xG_mean", "Away")].round(2),
            "xGA_Home": venue_summary[("xGA_mean", "Home")].round(2),
            "xGA_Away": venue_summary[("xGA_mean", "Away")].round(2),
        }).reset_index(drop=True)
        venue_df["xG_Diff"] = (venue_df["xG_Home"] - venue_df["xG_Away"]).round(2)
        venue_df["xGA_Diff"] = (venue_df["xGA_Away"] - venue_df["xGA_Home"]).round(2)

        league_home_xg, league_away_xg = venue_df["xG_Home"].mean(), venue_df["xG_Away"].mean()
        league_home_xga, league_away_xga = venue_df["xGA_Home"].mean(), venue_df["xGA_Away"].mean()

        col_k1, col_k2, col_k3 = st.columns(3)
        col_k1.metric("Avg Home xG" if selected_lang == "EN" else "Średnie xG Gospodarzy (Dom)", f"{league_home_xg:.2f}", f"{league_home_xg - league_away_xg:+.2f}")
        col_k2.metric("Avg Away xG" if selected_lang == "EN" else "Średnie xG Gości (Wyjazd)", f"{league_away_xg:.2f}", "Baseline", delta_color="off")
        col_k3.metric("Avg Away xGA Conceded" if selected_lang == "EN" else "Średnie xGA Dopuszczone na Wyjazdach", f"{league_away_xga:.2f}", f"{league_away_xga - league_home_xga:+.2f}", delta_color="inverse")

        pills_opts = ["1. Attack", "2. Defense", "3. Delta"]
        xg_venue_mode = st.pills("Perspective:", pills_opts, default=pills_opts[0])
        
        if xg_venue_mode == pills_opts[0]:
            df_plot = venue_df.sort_values(by="xG_Home", ascending=False).reset_index(drop=True)
            fig_v = go.Figure()
            fig_v.add_trace(go.Bar(name="Home", x=df_plot["Team"], y=df_plot["xG_Home"], marker_color="#38BDF8", text=[f"{v:.2f}" for v in df_plot["xG_Home"]], textposition="outside"))
            fig_v.add_trace(go.Bar(name="Away", x=df_plot["Team"], y=df_plot["xG_Away"], marker_color="#94A3B8", text=[f"{v:.2f}" for v in df_plot["xG_Away"]], textposition="outside"))
            fig_v.update_layout(barmode="group", height=480, template="plotly_dark", xaxis=dict(tickangle=-35))
            st.plotly_chart(fig_v, use_container_width=True)

    elif ogolne_widok == t("gen_opt3"):
        st.subheader("Full Standings & Advanced Metrics" if selected_lang == "EN" else "Pełna Tabela Zbiorcza ze Wszystkimi Wskaźnikami")
        ogolne_cols = ["Team", "Mecze", "Punkty", "Gole Strzelone", "Gole na mecz", "Gole Stracone", "Gole stracone na mecz", "xG na mecz", "xGA na mecz", "Posiadanie", "Podania ogolem", "Podania celne", "Pojedynki Wygrane"]
        st.dataframe(display_df[ogolne_cols], use_container_width=True, hide_index=True, column_config=common_col_config)

# =========================================================================
# TAB 2: STATYSTYKI OFENSYWNE
# =========================================================================
with tab_ofensywa:
    ofensywa_widok = st.selectbox(t("att_select"), [t(f"att_opt{i}") for i in range(1, 21)])
    st.markdown("---")

    if ofensywa_widok == t("att_opt1"):
        ofensywa_cols = ["Team", "Mecze", "Gole Strzelone", "Gole na mecz", "xG na mecz", "xGOT na mecz", "Bilans xG", "Strzaly na mecz", "Celne strzaly", "Big Chances", "Kontakty w polu karnym", "Podania celne", "Posiadanie"]
        st.dataframe(display_df[ofensywa_cols], use_container_width=True, hide_index=True, column_config=common_col_config)

    elif ofensywa_widok == t("att_opt2"):
        render_metric_bar_and_paper(df=team_stats, col_name="xG_na_mecz", title_chart="Total Expected Goals (xG)", title_paper="Total xG Rankings", value_header="xG / 90", color_scale="Blues")
        st.markdown("---")
        team_list = sorted(team_stats["Team"].unique().tolist())
        selected_line_team = st.selectbox("Select team for trend analysis:", team_list, index=0)
        team_matches = matches_df[matches_df["Team"] == selected_line_team].copy().reset_index(drop=True)
        team_matches["Kolejka"] = team_matches.index + 1
        
        fig_trend = go.Figure()
        fig_trend.add_trace(go.Scatter(x=team_matches["Kolejka"], y=team_matches["xG_For"], mode="lines+markers", name="Created xG", line=dict(color="#38BDF8", width=3), marker=dict(size=11, color="#38BDF8")))
        fig_trend.update_layout(height=460, template="plotly_dark")
        st.plotly_chart(fig_trend, use_container_width=True)

    elif ofensywa_widok == t("att_opt3"): render_metric_bar_and_paper(team_stats, "xG_OP_na_mecz", "Open Play xG", "Open Play xG Rankings", "xG OP / 90", "Greens")
    elif ofensywa_widok == t("att_opt4"): render_metric_bar_and_paper(team_stats, "xG_SP_na_mecz", "Set Play xG", "Set Play xG Rankings", "SP xG / 90", "Oranges")
    elif ofensywa_widok == t("att_opt5"): render_metric_bar_and_paper(team_stats, "npxG_na_mecz", "Non-Penalty xG", "npxG Rankings", "npxG / 90", "Purples")
    elif ofensywa_widok == t("att_opt6"): render_metric_bar_and_paper(team_stats, "xGOT_na_mecz", "Expected Goals on Target (xGOT)", "xGOT Rankings", "xGOT / 90", "Tealgrn")
    elif ofensywa_widok == t("att_opt7"): render_metric_bar_and_paper(team_stats, "xG_na_strzal", "Expected Goals per Shot", "xG / Shot Rankings", "xG / Shot", "Viridis")
    elif ofensywa_widok == t("att_opt8"): render_metric_bar_and_paper(team_stats, "xG_na_gola", "xG Needed per Goal", "xG / Goal Rankings", "xG / 1 Goal", "RdYlGn_r")
    elif ofensywa_widok == t("att_opt9"): render_metric_bar_and_paper(team_stats, "Celne_na_gola", "Shots on Target Needed per Goal", "SoT / Goal Rankings", "SoT / Goal", "RdYlGn_r", True)
    elif ofensywa_widok == t("att_opt10"): render_metric_bar_and_paper(team_stats, "Gole_minus_xG", "Finishing Overperformance (Goals - xG)", "Goals - xG Rankings", "Goals - xG", "RdYlGn", False)
    elif ofensywa_widok == t("att_opt11"): render_metric_bar_and_paper(team_stats, "Strzaly_z_pola_karnego", "Shots Inside Box per Match", "Shots Inside Box Rankings", "Box Shots / 90", "Blues")
    elif ofensywa_widok == t("att_opt12"): render_metric_bar_and_paper(team_stats, "Strzaly_zza_pola_karnego", "Shots Outside Box per Match", "Shots Outside Box Rankings", "Outside Shots / 90", "Purples")
    elif ofensywa_widok == t("att_opt14"): render_metric_bar_and_paper(team_stats, "Celnosc_strzalow_proc", "Shot Accuracy %", "Shot Accuracy Rankings", "Accuracy %", "Blues")
    
    elif ofensywa_widok == t("att_opt15"):
        col_bc1, col_bc2 = st.columns(2)
        with col_bc1:
            fig_bc = go.Figure(go.Bar(x=team_stats.sort_values(by="Big_Chances", ascending=False)["Big_Chances"], y=team_stats.sort_values(by="Big_Chances", ascending=False)["Team"], orientation='h', marker_color="#10B981"))
            fig_bc.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_bc, use_container_width=True)
        with col_bc2:
            fig_bcm = go.Figure(go.Bar(x=team_stats.sort_values(by="Big_Chances_Missed", ascending=False)["Big_Chances_Missed"], y=team_stats.sort_values(by="Big_Chances_Missed", ascending=False)["Team"], orientation='h', marker_color="#EF4444"))
            fig_bcm.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_bcm, use_container_width=True)
    
    elif ofensywa_widok == t("att_opt16"):
        fig_matrix = px.scatter(team_stats, x="xG_na_mecz", y="xG_na_gola", text="Team", template="plotly_dark", height=600)
        fig_matrix.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
        st.plotly_chart(fig_matrix, use_container_width=True)
        
    elif ofensywa_widok == t("att_opt19"):
        eff_df = team_stats.sort_values(by="Strzaly_na_gola", ascending=True).reset_index(drop=True)
        fig_eff = go.Figure(go.Bar(x=eff_df["Strzaly_na_gola"], y=eff_df["Team"], orientation='h', marker=dict(color=eff_df["Strzaly_na_gola"], colorscale="RdYlGn_r")))
        fig_eff.update_layout(height=620, template="simple_white", yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_eff, use_container_width=True)
        
    elif ofensywa_widok == t("att_opt20"):
        fig_xgot = px.scatter(team_stats, x="xGOT_Suma", y="Gole_Strzelone", text="Team", template="plotly_dark", height=560)
        fig_xgot.update_traces(textposition="top center", marker=dict(size=12, color="#AF7AC5"))
        st.plotly_chart(fig_xgot, use_container_width=True)

# =========================================================================
# TAB 3: STATYSTYKI DEFENSYWNE
# =========================================================================
with tab_defensywa:
    defensywa_widok = st.selectbox(t("def_select"), [t(f"def_opt{i}") for i in range(1, 21)], key="sb_def_analytics_view")
    st.markdown("---")

    if defensywa_widok == t("def_opt1"):
        defensywa_cols = ["Team", "Mecze", "Gole Stracone", "Gole stracone na mecz", "xGA na mecz", "xAGOT na mecz", "Odbiory", "Przejecia", "Rzuty Rozne", "Pojedynki Wygrane"]
        st.dataframe(display_df[defensywa_cols], use_container_width=True, hide_index=True, column_config=common_col_config)

    elif defensywa_widok == t("def_opt2"): render_metric_bar_and_paper(team_stats, "xGA_na_mecz", "Total xGA Rankings", "Total xGA Rankings", "xGA / 90", "Reds_r", True)
    elif defensywa_widok == t("def_opt3"): render_metric_bar_and_paper(team_stats, "xGA_OP_na_mecz", "Open Play xGA", "Open Play xGA Rankings", "xGA OP / 90", "Reds_r", True)
    elif defensywa_widok == t("def_opt4"): render_metric_bar_and_paper(team_stats, "xGA_SP_na_mecz", "Set Play xGA", "Set Play xGA Rankings", "SP xGA / 90", "Oranges_r", True)
    elif defensywa_widok == t("def_opt5"): render_metric_bar_and_paper(team_stats, "npxGA_na_mecz", "Non-Penalty xGA", "npxGA Rankings", "npxGA / 90", "Purples_r", True)
    elif defensywa_widok == t("def_opt6"): render_metric_bar_and_paper(team_stats, "xAGOT_na_mecz", "Expected Goals on Target Against (xAGOT)", "xAGOT Rankings", "xAGOT / 90", "Reds_r", True)
    elif defensywa_widok == t("def_opt7"): render_metric_bar_and_paper(team_stats, "xGA_na_strzal_rywala", "xGA per Opponent Shot", "xGA / Shot Against", "xGA / Opp Shot", "Reds_r", True)
    elif defensywa_widok == t("def_opt8"): render_metric_bar_and_paper(team_stats, "xGA_na_gola_straconego", "xGA Needed to Score Against", "xGA / Goal Conceded", "xGA / Conceded Goal", "Greens", False)
    elif defensywa_widok == t("def_opt9"): render_metric_bar_and_paper(team_stats, "Celne_rywala_na_gola", "Opponent SoT Needed per Goal", "SoT Against / Goal", "Opp SoT / Goal", "Greens", False)
    elif defensywa_widok == t("def_opt10"): render_metric_bar_and_paper(team_stats, "Gole_stracone_minus_xGA", "Defensive Goals Prevented (xGA - GA)", "Goals Prevented (xGA - GA)", "Prevented (xGA - GA)", "RdYlGn", False)
    elif defensywa_widok == t("def_opt11"): render_metric_bar_and_paper(team_stats, "Box_Shots_Against_Mean", "Opponent Shots Inside Box per Match", "Shots Inside Box Against", "Opp Box Shots / 90", "Reds_r", True)
    elif defensywa_widok == t("def_opt12"): render_metric_bar_and_paper(team_stats, "Outside_Box_Shots_Against_Mean", "Opponent Shots Outside Box per Match", "Shots Outside Box Against", "Opp Long Range / 90", "Purples_r", True)
    elif defensywa_widok == t("def_opt14"): render_metric_bar_and_paper(team_stats, "Celnosc_strzalow_rywala_proc", "Opponent Shot Accuracy %", "Opponent Shot Accuracy", "Opp Accuracy %", "Reds_r", True)
    elif defensywa_widok == t("def_opt15"): render_metric_bar_and_paper(team_stats, "Big_Chances_Against_Mean", "Big Chances Conceded per Match", "Big Chances Conceded", "Conceded BC / 90", "Reds_r", True)
    
    elif defensywa_widok == t("def_opt16"):
        fig_m = px.scatter(team_stats, x="xGA_na_mecz", y="xGA_na_gola_straconego", text="Team", template="plotly_dark", height=600)
        fig_m.update_traces(textposition="top center", marker=dict(size=12, color="#EF4444"))
        fig_m.update_layout(xaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_m, use_container_width=True)

    elif defensywa_widok == t("def_opt17"):
        fig_rel_d = px.scatter(team_stats, x="xGA_na_mecz", y="xAGOT_na_mecz", text="Team", template="plotly_dark", height=580)
        fig_rel_d.update_traces(textposition="top center", marker=dict(size=12, color="#EF4444"))
        st.plotly_chart(fig_rel_d, use_container_width=True)
        
    elif defensywa_widok == t("def_opt18"):
        fig_box_d = px.scatter(team_stats, x="Box_Touches_Against_Mean", y="Box_Shots_Against_Mean", text="Team", template="plotly_dark", height=580)
        fig_box_d.update_traces(textposition="top center", marker=dict(size=12, color="#EF4444"))
        st.plotly_chart(fig_box_d, use_container_width=True)

# =========================================================================
# TAB 4: DYSTRYBUCJA I PODANIA
# =========================================================================
with tab_podania:
    podania_widok = st.selectbox(t("pass_select"), [t(f"pass_opt{i}") for i in range(1, 10)], key="sb_passes_view")
    st.markdown("---")

    if podania_widok == t("pass_opt1"):
        t_cols = ["Team", "Mecze", "Posiadanie", "Podania_ogolem", "Passes_Total_Against_Mean", "Podania_celne", "Passes_Own_Half_Mean", "Passes_Opp_Half_Mean", "Passes_Opp_Half_Against_Mean", "Long_Balls_Mean", "Long_Balls_Against_Mean"]
        st.dataframe(team_stats[t_cols].copy(), use_container_width=True, hide_index=True)
        
    elif podania_widok == t("pass_opt2"): render_metric_bar_and_paper(team_stats, "Posiadanie", "Average Ball Possession (%)", "Possession Rankings", "Possession %", "Blues", False)
    
    elif podania_widok == t("pass_opt3"):
        df_sorted_p = team_stats.sort_values(by="Podania_ogolem", ascending=False).reset_index(drop=True)
        fig_p_tot = go.Figure()
        fig_p_tot.add_trace(go.Bar(y=df_sorted_p["Team"], x=df_sorted_p["Podania_ogolem"], name="Team Passes", orientation='h', marker_color="#38BDF8"))
        fig_p_tot.add_trace(go.Bar(y=df_sorted_p["Team"], x=df_sorted_p["Passes_Total_Against_Mean"], name="Opponent Passes", orientation='h', marker_color="#EF4444"))
        fig_p_tot.update_layout(barmode="group", height=640, template="plotly_dark", yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_p_tot, use_container_width=True)
        
    elif podania_widok == t("pass_opt4"): render_metric_bar_and_paper(team_stats, "Passes_Own_Half_Mean", "Passes in Own Half Rankings", "Own Half Passes", "Own Half / 90", "Teal", False)
    elif podania_widok == t("pass_opt5"): render_metric_bar_and_paper(team_stats, "Passes_Opp_Half_Mean", "Passes in Opposition Half Rankings", "Opposition Half Passes", "Opp Half / 90", "Greens", False)
    
    elif podania_widok == t("pass_opt6"):
        col_lb1, col_lb2 = st.columns(2)
        with col_lb1:
            fig_lb_w = go.Figure(go.Bar(x=team_stats.sort_values(by="Long_Balls_Mean", ascending=False)["Long_Balls_Mean"], y=team_stats.sort_values(by="Long_Balls_Mean", ascending=False)["Team"], orientation='h', marker_color="#F59E0B"))
            fig_lb_w.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_lb_w, use_container_width=True)
        with col_lb2:
            fig_lb_a = go.Figure(go.Bar(x=team_stats.sort_values(by="Long_Balls_Against_Mean", ascending=False)["Long_Balls_Against_Mean"], y=team_stats.sort_values(by="Long_Balls_Against_Mean", ascending=False)["Team"], orientation='h', marker_color="#8B5CF6"))
            fig_lb_a.update_layout(height=520, template="simple_white", yaxis=dict(autorange="reversed"))
            st.plotly_chart(fig_lb_a, use_container_width=True)

    elif podania_widok == t("pass_opt7"): render_metric_bar_and_paper(team_stats, "Podania_na_gola", "Passes per Goal Scored", "Passes / Goal Scored", "Passes / Goal", "Viridis_r", True)
    
    elif podania_widok == t("pass_opt8"):
        fig_p_matrix = px.scatter(team_stats, x="Passes_Opp_Half_Mean", y="Passes_Opp_Half_Against_Mean", text="Team", template="plotly_dark", height=600)
        fig_p_matrix.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
        fig_p_matrix.update_layout(yaxis=dict(autorange="reversed"))
        st.plotly_chart(fig_p_matrix, use_container_width=True)

    elif podania_widok == t("pass_opt9"):
        team_list_pass = sorted(team_stats["Team"].unique().tolist())
        sel_t_pass = st.selectbox("Select Team:", team_list_pass, index=0, key="sb_pass_team_sel")
        t_m_df = matches_df[matches_df["Team"] == sel_t_pass].copy().reset_index(drop=True)
        t_m_df["Kolejka"] = t_m_df.index + 1
        
        fig_p_trend = go.Figure()
        fig_p_trend.add_trace(go.Scatter(x=t_m_df["Kolejka"], y=t_m_df["Passes_Total"], mode="lines+markers", name=f"{sel_t_pass} (Team)", line=dict(color="#38BDF8", width=2.5)))
        fig_p_trend.add_trace(go.Scatter(x=t_m_df["Kolejka"], y=t_m_df["Passes_Total_Against"], mode="lines+markers", name="Opponent", line=dict(color="#EF4444", width=2.5)))
        fig_p_trend.update_layout(height=430, template="plotly_dark")
        st.plotly_chart(fig_p_trend, use_container_width=True)

# =========================================================================
# TAB 5: STATYSTYKI DRUŻYN (Z BOISKIEM)
# =========================================================================
with tab_druzyny:
    team_list_prof = sorted(team_stats["Team"].unique().tolist())
    selected_prof_team = st.selectbox("Select Team:", team_list_prof, index=0, key="sb_team_profile_select")

    team_row = team_stats[team_stats["Team"] == selected_prof_team].iloc[0]
    t_matches = matches_df[matches_df["Team"] == selected_prof_team].copy().reset_index(drop=True)
    t_matches["Kolejka"] = t_matches.index + 1
    m_count = len(t_matches)

    st.markdown("---")
    
    # ---------------------------------------------------------
    # BOISKO OFENSYWNE (MAPA STRZAŁÓW)
    # ---------------------------------------------------------
    col_map_head, col_map_toggle = st.columns([3, 1])
    with col_map_head:
        if selected_lang == "EN":
            st.markdown(f"##### Shot Map Visualization (Simulated): {selected_prof_team}")
        else:
            st.markdown(f"##### Wizualizacja Mapy Strzałów (Symulacja): {selected_prof_team}")
            
    with col_map_toggle:
        mode_opts = ["Suma (Cały Sezon)", "Średnia (Na mecz)"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)"]
        shot_mode = st.radio("Display Mode:", mode_opts, key="radio_shot_map_mode")
        
    is_avg = "Średnia" in shot_mode or "Average" in shot_mode

    if is_avg:
        raw_box, raw_out = t_matches['Box_Shots'].mean(), t_matches['Outside_Box_Shots'].mean()
        dots_box, dots_out = int(round(raw_box)), int(round(raw_out))
        box_label = f"Inside Box ({raw_box:.1f})" if selected_lang == "EN" else f"W polu karnym ({raw_box:.1f})"
        out_label = f"Outside Box ({raw_out:.1f})" if selected_lang == "EN" else f"Zza pola karnego ({raw_out:.1f})"
    else:
        raw_box, raw_out = t_matches['Box_Shots'].sum(), t_matches['Outside_Box_Shots'].sum()
        dots_box, dots_out = int(raw_box), int(raw_out)
        box_label = f"Inside Box ({dots_box})" if selected_lang == "EN" else f"W polu karnym ({dots_box})"
        out_label = f"Outside Box ({dots_out})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out})"

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
        
        # Powiększona wysokość boiska (Krok 2)
        fig_p.update_layout(
            height=580, 
            xaxis=dict(visible=False, range=[-3, 108], fixedrange=True),
            yaxis=dict(visible=False, range=[-3, 71], scaleanchor="x", scaleratio=1, fixedrange=True),
            plot_bgcolor="#0E1117", paper_bgcolor="#0E1117", margin=dict(l=10, r=10, t=30, b=10),
            showlegend=True, legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5, font=dict(color="#FFFFFF"))
        )
        return fig_p

    fig_pitch = draw_dark_pitch()
    seed_val = sum(ord(c) for c in selected_prof_team)

    if dots_box > 0:
        np.random.seed(seed_val)
        box_x = np.random.triangular(88.5, 96.0, 103.0, dots_box)
        box_y = np.random.triangular(18.0, 34.0, 50.0, dots_box)
        fig_pitch.add_trace(go.Scatter(x=box_x, y=box_y, mode="markers", name=box_label, marker=dict(color="#10B981", size=8 if is_avg else 7, line=dict(width=1, color="#0E1117"))))

    if dots_out > 0:
        np.random.seed(seed_val + 1)
        out_x = np.random.triangular(65.0, 85.0, 88.4, dots_out) 
        out_y = np.random.triangular(12.0, 34.0, 56.0, dots_out)
        fig_pitch.add_trace(go.Scatter(x=out_x, y=out_y, mode="markers", name=out_label, marker=dict(color="#38BDF8", size=8 if is_avg else 7, line=dict(width=1, color="#0E1117"))))

    # Poszerzone kolumny dla boiska (Krok 1)
    col_map1, col_map2, col_map3 = st.columns([0.15, 4, 0.15])
    with col_map2:
        st.plotly_chart(fig_pitch, use_container_width=True)

    # ---------------------------------------------------------
    # BOISKO DEFENSYWNE (MAPA STRZAŁÓW DOPUSZCZONYCH)
    # ---------------------------------------------------------
    st.markdown("---")
    col_map_head_def, col_map_toggle_def = st.columns([3, 1])
    
    with col_map_head_def:
        if selected_lang == "EN":
            st.markdown(f"##### Conceded Shot Map (Simulated): {selected_prof_team}")
        else:
            st.markdown(f"##### Wizualizacja Dopuszczonych Strzałów (Symulacja): {selected_prof_team}")
            
    with col_map_toggle_def:
        mode_opts_def = ["Suma (Cały Sezon)", "Średnia (Na mecz)"] if selected_lang == "PL" else ["Total (Full Season)", "Average (Per Match)"]
        shot_mode_def = st.radio("Display Mode:", mode_opts_def, key="radio_shot_map_mode_def")
        
    is_avg_def = "Średnia" in shot_mode_def or "Average" in shot_mode_def

    if is_avg_def:
        raw_box_def, raw_out_def = t_matches['Box_Shots_Against'].mean(), t_matches['Outside_Box_Shots_Against'].mean()
        dots_box_def, dots_out_def = int(round(raw_box_def)), int(round(raw_out_def))
        box_label_def = f"Inside Box ({raw_box_def:.1f})" if selected_lang == "EN" else f"W polu karnym ({raw_box_def:.1f})"
        out_label_def = f"Outside Box ({raw_out_def:.1f})" if selected_lang == "EN" else f"Zza pola karnego ({raw_out_def:.1f})"
    else:
        raw_box_def, raw_out_def = t_matches['Box_Shots_Against'].sum(), t_matches['Outside_Box_Shots_Against'].sum()
        dots_box_def, dots_out_def = int(raw_box_def), int(raw_out_def)
        box_label_def = f"Inside Box ({dots_box_def})" if selected_lang == "EN" else f"W polu karnym ({dots_box_def})"
        out_label_def = f"Outside Box ({dots_out_def})" if selected_lang == "EN" else f"Zza pola karnego ({dots_out_def})"

    fig_pitch_def = draw_dark_pitch()
    seed_val_def = sum(ord(c) for c in selected_prof_team) + 99 

    if dots_box_def > 0:
        np.random.seed(seed_val_def)
        box_x_def = np.random.triangular(2.0, 9.0, 16.5, dots_box_def)
        box_y_def = np.random.triangular(18.0, 34.0, 50.0, dots_box_def)
        fig_pitch_def.add_trace(go.Scatter(x=box_x_def, y=box_y_def, mode="markers", name=box_label_def, marker=dict(color="#EF4444", size=8 if is_avg_def else 7, line=dict(width=1, color="#0E1117"))))

    if dots_out_def > 0:
        np.random.seed(seed_val_def + 1)
        out_x_def = np.random.triangular(16.6, 22.0, 40.0, dots_out_def) 
        out_y_def = np.random.triangular(12.0, 34.0, 56.0, dots_out_def)
        fig_pitch_def.add_trace(go.Scatter(x=out_x_def, y=out_y_def, mode="markers", name=out_label_def, marker=dict(color="#F59E0B", size=8 if is_avg_def else 7, line=dict(width=1, color="#0E1117"))))

    # Poszerzone kolumny dla boiska (Krok 1)
    col_map1_def, col_map2_def, col_map3_def = st.columns([0.15, 4, 0.15])
    with col_map2_def:
        st.plotly_chart(fig_pitch_def, use_container_width=True)


# =========================================================================
# TAB 6: PRACOWNIA ZALEŻNOŚCI
# =========================================================================
with tab_zaleznosci:
    st.header("🔬 Correlation Lab: X vs Y Metrics" if selected_lang == "EN" else "🔬 Zależności: Wybierz osie X i Y")
    
    METRIC_DB = {
        "Punkty": "Punkty", "Gole na mecz": "Gole_na_mecz", "Gole stracone na mecz": "Gole_stracone_na_mecz", 
        "xG na mecz": "xG_na_mecz", "xGA na mecz": "xGA_na_mecz", "Posiadanie": "Posiadanie"
    }

    col_x, col_y, col_team = st.columns([1.2, 1.2, 1.2])
    with col_x: x_choice = st.selectbox("X Axis:", list(METRIC_DB.keys()), index=3, key="sb_custom_x")
    with col_y: y_choice = st.selectbox("Y Axis:", list(METRIC_DB.keys()), index=0, key="sb_custom_y")
    with col_team: selected_team_zal = st.selectbox("Highlight Team:", ["Wszystkie"] + sorted(team_stats["Team"].unique().tolist()), index=0, key="sb_custom_team")

    val_x, val_y = team_stats[METRIC_DB[x_choice]], team_stats[METRIC_DB[y_choice]]
    corr_val = val_x.corr(val_y)

    fig_scatter = px.scatter(team_stats, x=METRIC_DB[x_choice], y=METRIC_DB[y_choice], text="Team", template="plotly_dark", height=620)
    fig_scatter.update_traces(textposition="top center", marker=dict(size=12, color="#38BDF8"))
    st.plotly_chart(fig_scatter, use_container_width=True)