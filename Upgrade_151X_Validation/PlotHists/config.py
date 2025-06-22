# Plotting configuration
PAD_GAP = 0.01
X_PAD_RANGE = [0.0, 1.0]
Y_PAD_RANGE = [0.0, 0.30-PAD_GAP, 0.30+PAD_GAP, 1.0]

# Plot styling
PLOT_STYLE = {
    'maximum': 1.3,
    'minimum': 0.2,
    'x_range': [10, 400],
    'y_range': [0.7, 1.3]
}

# Legend configuration
LEGEND_CONFIG = {
    'main': {
        'x1': 0.25,
        'y1': 0.85,
        'x2': 0.95,
        'y2': 0.92,
        'columns': 4,
        'text_size': 0.027
    },
    'ratio': {
        'x1': 0.25,
        'y1': 0.75,
        'x2': 0.95,
        'y2': 0.85,
        'columns': 4,
        'text_size': 0.085
    }
}

# Output configuration
OUTPUT_DIR = "./plots" 