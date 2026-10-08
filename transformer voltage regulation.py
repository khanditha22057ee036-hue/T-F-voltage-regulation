# Transformer Voltage Regulation Calculation
# Formula: %VR = ((VNL - VFL) / VFL) * 100

VNL = float(input("Enter no-load voltage (V): "))
VFL = float(input("Enter full-load voltage (V): "))

if VNL < 0 or VFL <= 0:
    print("Enter valid voltage values.")
else:
    voltage_regulation = ((VNL - VFL) / VFL) * 100

    print("Transformer Voltage Regulation =",
          round(voltage_regulation, 2), "%")
