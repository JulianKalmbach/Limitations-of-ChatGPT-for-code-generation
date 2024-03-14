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
plt.subplot(1, 2, 1)
sns.barplot(data=df, x='Difficulty', y='pass@1 3.5 num', ci=None, palette=palette)
plt.title('pass@1 ChatGPT 3.5 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('pass@1 3.5 (Pass Rate)')

# Plot for 4.0
plt.subplot(1, 2, 2)
sns.barplot(data=df, x='Difficulty', y='pass@1 4.0 num', ci=None, palette=palette)
plt.title('pass@1 ChatGPT 3.5 vs. Difficulty')
plt.xlabel('Difficulty')
plt.ylabel('pass@1 4.0 (Pass Rate)')

plt.tight_layout()
plt.show()

# Um den Unterschied zwischen LOCpars 3.5/4.0 und LOCpars der Sample Solution zu visualisieren,
# berechnen wir die Differenz zwischen diesen Werten und plotten diese Differenzen.

df['LOCpars sample solution num'] = pd.to_numeric(df['LOCpars sample solution'], errors='coerce').fillna(0)

# Berechnung der Differenz
df['Diff LOCpars 3.5 - Sample'] = df['LOCpars 3.5'] - df['LOCpars sample solution num']
df['Diff LOCpars 4.0 - Sample'] = df['LOCpars 4.0'] - df['LOCpars sample solution num']

# Plotten der Differenzen
plt.figure(figsize=(14, 6))

# Differenz für Version 3.5
plt.subplot(1, 2, 1)
sns.histplot(df['Diff LOCpars 3.5 - Sample'], kde=True, color='blue')
plt.title('Difference between LOCpars 3.5 and Sample Solution')
plt.xlabel('Difference (LOCpars 3.5 - Sample)')
plt.ylabel('Frequency')

# Differenz für Version 4.0
plt.subplot(1, 2, 2)
sns.histplot(df['Diff LOCpars 4.0 - Sample'], kde=True, color='green')
plt.title('Difference between LOCpars 4.0 and Sample Solution')
plt.xlabel('Difference (LOCpars 4.0 - Sample)')
plt.ylabel('Frequency')

plt.tight_layout()
plt.show()