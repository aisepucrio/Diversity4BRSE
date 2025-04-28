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

# Plot simple bar chart
fig, ax = plt.subplots(figsize=(12, 6))
ax.bar(df['Subcategory'], df['Quantity'], color=df['Color'])

ax.margins(x=0.01)

# Labels and title
ax.set_xlabel('Subcategories')
ax.set_ylabel('Quantity')
#ax.set_title('Bias Subcategories Colored by Main Category')

ax.set_xlabel('Subcategories', fontsize=14)
ax.set_ylabel('Quantity',    fontsize=14)

# 5) Ticks com fonte personalizada
ax.tick_params(axis='x', labelsize=12)
ax.tick_params(axis='y', labelsize=12)

# Legend for the 5 categories
legend_handles = [
    plt.Line2D([0], [0], marker='s', color=col, linestyle='')
    for col in colors.values()
]
ax.legend(
    legend_handles, 
    colors.keys(), 
    title='Categories of Bias',
    loc='upper right',
    frameon=True,
    borderpad=0.5
)

plt.xticks(rotation=45, ha='right')
plt.tight_layout()
plt.show()
