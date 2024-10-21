import ROOT

# Open the ROOT file in update mode (so you can write back to it)
input_file = ROOT.TFile("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2023_Samples/CMSSW_13_0_14/src/EGTools/TrigTools/test/Efficiency_Modified_2023_3million.root", "READ")
#input_file = ROOT.TFile("/afs/cern.ch/work/s/ssaumya/private/Egamma/Run3Winter24_Efficiency/2024_Samples/CMSSW_13_3_3/src/EGTools/TrigTools/test/Efficiency_Modified_2024_3million.root", "READ")

# Get the two histograms from the ROOT file
hist1_num = input_file.Get("EfficiencyCalculator/num_ele_pt_EB")  # Replace with actual histogram name
hist2_num = input_file.Get("EfficiencyCalculator/num_ele_pt_EE")  # Replace with actual histogram name
hist1_den = input_file.Get("EfficiencyCalculator/den_ele_pt")

# Create a new histogram to store the sum
#hist_sum = file.Get("EfficiencyCalculator/num_ele_pt")
#hist_sum = hist1.Clone("EfficiencyCalculator/num_ele_pt_EB")  # Clone the first histogram as a template
#hist_sum.SetTitle("EfficiencyCalculator/num_ele_pt")  # Set a new title for the summed histogram
#hist_sum.Reset()  # Reset the contents of the cloned histogram

# Check if the histograms exist
if not hist1_num or not hist2_num:
    print("Error: One or both histograms not found in the file.")
else:
    # Add the two histograms
    hist_sum = hist1_num.Clone("num_ele_pt")  # Clone hist1 to keep the same binning and properties
    hist_sum.Add(hist2_num)
    hist_den = hist1_den.Clone("den_ele_pt")
    # Open a new ROOT file to save the result
    output_file = ROOT.TFile.Open("output_file2023.root", "RECREATE")

    # Write the summed histogram to the new file
    hist_sum.Write()
    hist_den.Write()

    print("hist_sum entries:", hist_sum.GetEntries())
    print("hist_den entries:", hist_den.GetEntries())

    # Close the files
    output_file.Close()


# Add the two histograms
#hist_sum.Add(hist1) 
#hist_sum.Add(hist2)

print("hist1 entries:", hist1_num.GetEntries())
print("hist2 entries:", hist2_num.GetEntries())
#print("hist_sum entries:", hist_sum.GetEntries())

# Write the summed histogram to the ROOT file
#hist_sum.Write("EfficiencyCalculator/num_ele_pt",ROOT.TObject.kOverwrite)

# Close the file to save changes
input_file.Close()
