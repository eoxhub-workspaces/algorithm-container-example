import datetime
import os

# Define the output directory and ensure it exists
output_dir = "/app/output"
os.makedirs(output_dir, exist_ok=True)

# Generate simulated output
timestamp = datetime.datetime.now().isoformat()
file_path = os.path.join(output_dir, "observation_result.txt")

with open(file_path, "w") as file:
    file.write("Algorithm executed successfully.\n")
    file.write(f"Timestamp: {timestamp}\n")
    file.write("Status: Nominal\n")

print(f"Process complete. Data written to {file_path}")
