import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("=== RUNNING INDUSTRIAL ENGINEERING THESIS PLOTTER ===")
print("Project Case Study: PT. Boga Dimsum Indonesia (Bakpao Packaging Design)\n")

# Data riil distribusi gender responden (Tabel 4.4)
gender_counts = {
    'Gender': ['Male', 'Female'],
    'Total_Respondents': [50, 50]
}
df_gender = pd.DataFrame(gender_counts)

# Data riil Importance Level hasil Conjoint Analysis (Tabel 4.8)
conjoint_results = {
    'Attributes': [
        'Bentuk Wadah (Container Shape)', 
        'Bentuk Kemasan (Packaging Shape)',
        'Material Kemasan (Material)', 
        'Banyak Isi (Quantity)', 
        'Varian Rasa (Flavor Variant)',
        'Bentuk Bakpao (Bun Motif)',
        'Pembuka Kemasan (Tear Notch)'
    ],
    'Importance_Value_Pct': [26.17, 17.83, 15.15, 13.03, 11.59, 9.11, 7.03]
}
df_importance = pd.DataFrame(conjoint_results)

# Setup visualisasi grafik menggunakan Seaborn
sns.set_theme(style="whitegrid")
fig, axes = plt.subplots(1, 2, figsize=(13, 5))

# Plot 1: Grafik Demografi Gender Responden
sns.barplot(x='Gender', y='Total_Respondents', data=df_gender, ax=axes, color='lightsteelblue')
axes.set_title('Respondent Gender Distribution (N=100)')
axes.set_ylabel('Total Count')

# Plot 2: Grafik Atribut Terpenting Berdasarkan Analisis Konjoin
sns.barplot(x='Importance_Value_Pct', y='Attributes', data=df_importance, ax=axes, color='coral')
axes.set_title('Conjoint Analysis: Relative Attribute Importance (%)')
axes.set_xlabel('Percentage (%)')
axes.set_xlim(0, 100)

plt.tight_layout()

# Menyimpan hasil chart visualisasi otomatis ke folder
plt.savefig('thesis_conjoint_results.png', dpi=300)
print("[SUCCESS] Academic charts successfully generated and saved as 'thesis_conjoint_results.png'")
