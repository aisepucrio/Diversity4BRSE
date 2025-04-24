import matplotlib.pyplot as plt
import pandas as pd

# Data
data = {
    'Uncertainty': {
        'Unsure': 8,
        'Unconscious': 3
    },
    'Denial': {
        'Not Recognized': 21,
        'Avoided': 2
    },
    'Recognition': {
        'Anti-diversity': 4,
        'General Awareness': 8,
        'Gender': 12,
        'Racial': 10,
        'LGBT': 4,
        'Disability': 2,
        'Age': 1,
        'Religious': 2,
        'Political': 6,
        'Regional': 2
    },
    'Personal Experience': {
        'Work Environment': 6,
        'Upbringing': 1
    },
    'Out of scope': {
        'Out of scope': 5
    }
}

# Flatten data into a DataFrame
rows = []
for category, subs in data.items():
    for subcat, qty in subs.items():
        rows.append({'Category': category, 'Subcategory': subcat, 'Quantity': qty})
df = pd.DataFrame(rows)

# Assign a unique color to each of the 5 main categories
colors = {
    'Uncertainty': '#1f77b4',
    'Denial':        '#ff7f0e',
    'Recognition':       '#2ca02c',
    'Personal Experience': '#d62728',
    'Out of scope':    '#9467bd'
}
df['Color'] = df['Category'].map(colors)

fig, ax = plt.subplots(figsize=(4, 10))

# 1) Plota barras horizontais: Subcategory no eixo y, Quantity no eixo x
ax.barh(df['Subcategory'], df['Quantity'], color=df['Color'])

# 2) Remove margem extra em y
ax.margins(y=0.01)

# 3) Rótulos trocados de lugar
ax.set_ylabel('Subcategories', fontsize=14)
ax.set_xlabel('Quantity',     fontsize=14)

# 4) Ticks com fonte personalizada
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# 5) Legenda dentro do gráfico
legend_handles = [
    plt.Line2D([0], [0], marker='s', color=col, linestyle='')
    for col in colors.values()
]
ax.legend(
    legend_handles,
    colors.keys(),
    title='Categories of Bias',
    fontsize=11,
    title_fontsize=13,
    loc='upper right',
    frameon=True,
    borderpad=0.5
)

plt.tight_layout()
plt.show()
