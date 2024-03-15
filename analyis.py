import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Load the corrected CSV data to create various plots
df = pd.read_csv("results_data.csv")

# Set style
sns.set_style("whitegrid")
palette = sns.color_palette("tab10")

# Convert 'x' to 1 and '-' to 0 for pass@1 columns
df['pass@1 3.5 num'] = df['pass@1 3.5'].apply(lambda x: 1 if x == 'x' else 0)
df['pass@1 4.0 num'] = df['pass@1 4.0'].apply(lambda x: 1 if x == 'x' else 0)

# Plotting pass@1 for 3.5 and 4.0 against difficulty
plt.figure(figsize=(14, 6))

# Plot for 3.5
plt.plot(1, 2, 1)
sns.barplot(data=df, x='Difficulty', y='pass@1 3.5 num', ci=None, palette=palette)
plt.title('pass@1 ChatGPT 3.5 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('pass@1 3.5 (Pass Rate)')
plt.ylim(0, 1.0)  # Grenzen der y-Achse festlegen

# Plot for 4.0
plt.plot(1, 2, 2)
sns.barplot(data=df, x='Difficulty', y='pass@1 4.0 num', ci=None, palette=palette)
plt.title('pass@1 ChatGPT 4.0 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('pass@1 4.0 (Pass Rate)')
plt.ylim(0, 1.0)  # Grenzen der y-Achse festlegen

plt.tight_layout()
plt.show()

# Nochmal der Graph nur mit code req. met

df['code req. met 3.5 num'] = df['code req. met 3.5'].apply(lambda x: 1 if x == 'x' else 0)
df['code req. met 4.0 num'] = df['code req. met 4.0'].apply(lambda x: 1 if x == 'x' else 0)
plt.figure(figsize=(14, 6))

# Plot for 3.5
plt.subplot(1, 2, 1)
sns.barplot(data=df, x='Difficulty', y='code req. met 3.5 num', ci=None, palette=palette)
plt.title('Anforderungen erfüllt ChatGPT 3.5 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('Anforderungen erfüllt (Rate)')
plt.ylim(0, 1.0)  # Grenzen der y-Achse festlegen

# Plot for 4.0
plt.subplot(1, 2, 2)
sns.barplot(data=df, x='Difficulty', y='code req. met 4.0 num', ci=None, palette=palette)
plt.title('Anforderungen erfüllt ChatGPT 4.0 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('Anforderungen erfüllt (Rate)')
plt.ylim(0, 1.0)  # Grenzen der y-Achse festlegen

plt.tight_layout()
plt.show()

# Um den Unterschied zwischen LOCpars 3.5/4.0 und LOCpars der Sample Solution zu visualisieren,
# berechnen wir die Differenz zwischen diesen Werten und plotten diese Differenzen.

df['LOCpars sample solution num'] = pd.to_numeric(df['LOCpars sample solution'], errors='coerce').fillna(0)

# Berechnung der Differenz
df_3_5_filtered = df_filtered = df[(df['LOCpars sample solution'] != '-') & (df['code req. met 3.5'] != '-')]
df['Diff LOCpars 3.5 - Sample'] = df_3_5_filtered['LOCpars 3.5'] - df_3_5_filtered['LOCpars sample solution num']
df_4_0_filtered = df_filtered = df[(df['LOCpars sample solution'] != '-') & (df['code req. met 4.0'] != '-')]
df['Diff LOCpars 4.0 - Sample'] = df_4_0_filtered['LOCpars 4.0'] - df_4_0_filtered['LOCpars sample solution num']

# Plotten der Differenzen
plt.figure(figsize=(14, 6))

# Differenz für Version 3.5
plt.subplot(1, 2, 1)
sns.histplot(df['Diff LOCpars 3.5 - Sample'], kde=True, color='blue')
plt.title('Differenz LOCpars zwischen Sample Solution und ChatGPT 3.5')
plt.xlabel('Unterschied von LOCpars 3.5 zur Musterlösung')
plt.ylabel('Frequenz')

# Differenz für Version 4.0
plt.subplot(1, 2, 2)
sns.histplot(df['Diff LOCpars 4.0 - Sample'], kde=True, color='green')
plt.title('Differenz LOCpars zwischen Sample Solution und ChatGPT 4.0')
plt.xlabel('Unterschied von LOCpars 4.0 zur Musterlösung')
plt.ylabel('Frequenz')

plt.tight_layout()
plt.show()

# Cyclomatic complexity

# Konvertiere 'cyclomatic complexity' und 'cycl. compl. of sample solution' in numerische Werte,
# wobei nicht-numerische Werte mit 'coerce' zu NaN werden und dann mit 0 ersetzt werden.
df['cyclomatic complexity'] = pd.to_numeric(df['cyclomatic complexity'], errors='coerce').fillna(0)
df['cycl. compl. of sample solution'] = pd.to_numeric(df['cycl. compl. of sample solution'], errors='coerce').fillna(0)

# Filtere Zeilen, wo 'code req. met 3.5' oder 'cycl. compl. of sample solution' gleich '-' sind.
df_filtered = df[(df['code req. met 3.5'] != '-') & (df['cycl. compl. of sample solution'] != '-')]

# Gruppieren nach 'Difficulty' und Summen berechnen
cc_sum_by_difficulty = df_filtered.groupby('Difficulty')['cyclomatic complexity'].sum().reset_index()
cc_sample_sum_by_difficulty = df_filtered.groupby('Difficulty')['cycl. compl. of sample solution'].sum().reset_index()

# Plotte beide Summen nebeneinander für jede Schwierigkeitsstufe
cc_sum_by_difficulty['Type'] = 'ChatGPT 3.5'
cc_sample_sum_by_difficulty['Type'] = 'Sample Solution'
cc_combined = pd.concat([
    cc_sum_by_difficulty.rename(columns={'cyclomatic complexity': 'CC Sum'}),
    cc_sample_sum_by_difficulty.rename(columns={'cycl. compl. of sample solution': 'CC Sum'})
])

# Erstelle das Balkendiagramm mit nebeneinanderliegenden Balken
plt.figure(figsize=(14, 6))
difficulty_order = ['easy', 'medium', 'hard']
# Dann benutze diese Reihenfolge im sns.barplot Befehl
plt.subplot(1, 2, 1)
sns.barplot(data=cc_combined, x='Difficulty', y='CC Sum', hue='Type', order=difficulty_order)
plt.ylabel('Summe der Cyclomatic Complexity')
plt.title('Cyclomatic Complexity nach Schwierigkeit: ChatGPT 3.5 vs Musterlösung')
plt.legend()



# Konvertiere 'cyclomatic complexity' und 'cycl. compl. of sample solution' in numerische Werte,
# wobei nicht-numerische Werte mit 'coerce' zu NaN werden und dann mit 0 ersetzt werden.
df['cc 4.0'] = pd.to_numeric(df['cc 4.0'], errors='coerce').fillna(0)
df['cycl. compl. of sample solution'] = pd.to_numeric(df['cycl. compl. of sample solution'], errors='coerce').fillna(0)

# Filtere Zeilen, wo 'code req. met 4.0' oder 'cycl. compl. of sample solution' gleich '-' sind.
df_filtered = df[(df['code req. met 4.0'] != '-') & (df['cycl. compl. of sample solution'] != '-')]

# Gruppieren nach 'Difficulty' und Summen berechnen
cc_sum_by_difficulty = df_filtered.groupby('Difficulty')['cyclomatic complexity'].sum().reset_index()
cc_sample_sum_by_difficulty = df_filtered.groupby('Difficulty')['cycl. compl. of sample solution'].sum().reset_index()

# Plotte beide Summen nebeneinander für jede Schwierigkeitsstufe
cc_sum_by_difficulty['Type'] = 'ChatGPT 4.0'
cc_sample_sum_by_difficulty['Type'] = 'Sample Solution'
cc_combined = pd.concat([
    cc_sum_by_difficulty.rename(columns={'cyclomatic complexity': 'CC Sum'}),
    cc_sample_sum_by_difficulty.rename(columns={'cycl. compl. of sample solution': 'CC Sum'})
])

# Erstelle das Balkendiagramm mit nebeneinanderliegenden Balken
difficulty_order = ['easy', 'medium', 'hard']
# Dann benutze diese Reihenfolge im sns.barplot Befehl
plt.subplot(1, 2, 2)
sns.barplot(data=cc_combined, x='Difficulty', y='CC Sum', hue='Type', order=difficulty_order)
plt.ylabel('Summe der Cyclomatic Complexity')
plt.title('Cyclomatic Complexity nach Schwierigkeit: ChatGPT 4.0 vs Musterlösung')
plt.legend()

plt.tight_layout()
plt.show()