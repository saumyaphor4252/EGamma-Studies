# HLT Efficiency Plotting Script

A robust and flexible script for generating efficiency plots for HLT (High-Level Trigger) analysis.

## 🚀 Key Improvements

### 1. **Object-Oriented Design**
- `PlotConfig`: Configuration management using dataclasses
- `HistogramGenerator`: Dedicated class for histogram name generation
- `PlotProcessor`: Main processing logic with error handling

### 2. **Command Line Interface**
```bash
# Basic usage
python plotHist.py

# Dry run to see what would be processed
python plotHist.py --dry-run

# Limit number of plots
python plotHist.py --max-plots 10

# Generate only specific plot types
python plotHist.py --plot-types pt eta

# Custom output directory
python plotHist.py --output-dir my_plots

# Verbose logging
python plotHist.py --verbose

# Custom denominator filter
python plotHist.py --denominator HLTEle32WPTightL1Seeded
```

### 3. **Enhanced Error Handling**
- File validation before processing
- Graceful error recovery
- Detailed error logging
- Progress tracking

### 4. **Better Logging**
- File and console logging
- Progress indicators
- Error summaries
- Configurable log levels

### 5. **Configuration Management**
- YAML configuration file support
- Command line argument parsing
- Default configurations
- Flexible parameter overrides

## 📁 File Structure

```
PlotHists/
├── plotHist.py          # Main plotting script
├── plotter.py           # EfficiencyPlotter class
├── config.py            # Plot styling configuration
├── filter_configs.py    # HLT filter definitions
├── Inputs.py           # Input file configurations
├── plot_config.yaml    # YAML configuration file
├── README.md           # This file
└── plotting.log        # Generated log file
```

## 🎯 Usage Examples

### Basic Plotting
```bash
python plotHist.py
```

### Testing Configuration
```bash
python plotHist.py --dry-run --verbose
```

### Limited Processing
```bash
python plotHist.py --max-plots 5 --plot-types pt
```

### Custom Configuration
```bash
python plotHist.py --output-dir custom_plots --denominator HLTEle32WPTightL1Seeded
```

## 🔧 Configuration

### YAML Configuration
Edit `plot_config.yaml` to modify default settings:

```yaml
plot_types:
  - pt
  - eta
  - phi

denominator_filter: "HLTEle26WP70L1Seeded"
output_dir: "plots"
```

### Command Line Options
- `--dry-run`: Show what would be processed without plotting
- `--max-plots N`: Limit number of plots to process
- `--output-dir DIR`: Specify output directory
- `--plot-types TYPE1 TYPE2`: Specify plot types to generate
- `--denominator FILTER`: Specify denominator filter
- `--verbose`: Enable verbose logging

## 📊 Output

The script generates:
- Efficiency plots in PNG format
- Detailed log file (`plotting.log`)
- Progress indicators and summaries
- Error reports for failed plots

## 🛠️ Error Handling

The script includes robust error handling:
- File validation before processing
- Individual plot error recovery
- Detailed error logging
- Graceful interruption handling

## 🔄 Extensibility

The modular design makes it easy to extend:
- Add new plot types in `HistogramGenerator`
- Modify plotting logic in `PlotProcessor`
- Add new configuration options
- Integrate with different input formats

## 📈 Performance Features

- Progress tracking with counters
- Configurable plot limits
- Dry run mode for testing
- Efficient histogram name generation
- Memory-conscious file handling

## 🎨 Customization

### Adding New Plot Types
1. Modify `HistogramGenerator.generate_histogram_names()`
2. Update `PlotProcessor.process_plot_type()`
3. Add to command line arguments if needed

### Custom Styling
1. Edit `config.py` for plot styling
2. Modify `plot_config.yaml` for defaults
3. Use command line arguments for overrides

## 🐛 Troubleshooting

### Common Issues
1. **File not found**: Check input file paths in `Inputs.py`
2. **Permission errors**: Ensure write access to output directory
3. **Memory issues**: Use `--max-plots` to limit processing
4. **ROOT errors**: Verify ROOT installation and file formats

### Debug Mode
```bash
python plotHist.py --verbose --dry-run
```

## 📝 Logging

The script creates detailed logs:
- File: `plotting.log`
- Console: Real-time progress
- Levels: INFO, DEBUG, ERROR, WARNING

## 🤝 Contributing

To contribute improvements:
1. Follow the existing code structure
2. Add appropriate error handling
3. Update documentation
4. Test with different configurations
5. Add logging for new features

## 📄 License

This script is part of the CMS HLT analysis framework. 