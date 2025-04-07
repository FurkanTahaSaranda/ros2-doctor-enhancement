# Collect diagnostic information using ROS 2 Doctor CLI
from subprocess import check_output

try:
    # Run the ros2 doctor command and capture the output
    output = check_output(['ros2', 'doctor'])

    # Save the result to a text file
    with open('diagnostic_report.txt', 'w') as f:
        f.write(output.decode())

    print("✅ Diagnostic report saved to diagnostic_report.txt")

except FileNotFoundError:
    print("❌ ROS 2 CLI not found. Make sure ROS 2 is sourced and installed.")
except Exception as e:
    print(f"❌ Error while running ros2 doctor: {e}")
