import ROOT

# Open the ROOT file in update mode
file = ROOT.TFile("file.root", "UPDATE")

# Retrieve the histograms from the file or from other sources
hist1 = file.Get("histogram1_name")  # Replace with actual histogram name
hist2 = file.Get("histogram2_name")  # Replace with actual histogram name

# Error checking for histograms
if not hist1 or not hist2:
    print("Error: One or both histograms do not exist!")
    file.Close()
    exit()

# Check if the histogram_sum_name already exists
hist_sum = file.Get("histogram_sum_name")

if hist_sum:
    if hist_sum.GetEntries() == 0:
        print("Histogram exists but is blank. Reusing it.")
    else:
        print("Histogram exists and is not blank. Resetting it.")
        hist_sum.Reset()  # Reset the contents if not blank
else:
    print("Histogram does not exist. Creating a new one.")
    hist_sum = hist1.Clone("histogram_sum_name")  # Clone hist1 as base
    hist_sum.Reset()  # Reset it to ensure it's empty

# Now proceed to add hist1 and hist2 to hist_sum
hist_sum.Add(hist1)
hist_sum.Add(hist2)

# Write the summed histogram back into the file
hist_sum.Write(hist_sum.GetName(), ROOT.TObject.kOverwrite)

# Close the file
file.Close()

print("Summed histogram has been successfully written to the file.")

