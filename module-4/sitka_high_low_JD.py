import csv
from datetime import datetime
import sys

from matplotlib import pyplot as plt

# ---------------------------------------------------------
# High / Low Temperatures Program - Customized for Jordan Dardar (JD)
#   - Reads daily weather data from sitka_weather_2018_simple.csv
#   - User may choose HIGH temps, LOW temps, or EXIT
#   - Loops until user decides to exit
# ---------------------------------------------------------

filename = 'sitka_weather_2018_simple.csv'

# Read the CSV file once and store dates, highs, and lows
dates_JD, highs_JD, lows_JD = [], [], []

with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for row in reader:
        try:
            current_date = datetime.strptime(row[2], '%Y-%m-%d')
            high = int(row[5])
            low = int(row[6])
        except ValueError:
            # Skip rows with missing data
            continue

        dates_JD.append(current_date)
        highs_JD.append(high)
        lows_JD.append(low)


# ---------------------------------------------------------
# JD Graphing Functions
# ---------------------------------------------------------

def jd_plot_highs():
    """Plot Jordan's high temperature graph."""
    fig, ax = plt.subplots()
    ax.plot(dates_JD, highs_JD, c='red')

    plt.title("Jordan Dardar - Daily High Temperatures (2018)", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


def jd_plot_lows():
    """Plot Jordan's low temperature graph."""
    fig, ax = plt.subplots()
    ax.plot(dates_JD, lows_JD, c='blue')

    plt.title("Jordan Dardar - Daily Low Temperatures (2018)", fontsize=24)
    plt.xlabel("", fontsize=16)
    fig.autofmt_xdate()
    plt.ylabel("Temperature (F)", fontsize=16)
    plt.tick_params(axis='both', which='major', labelsize=16)

    plt.show()


# ---------------------------------------------------------
# JD Menu Display Function
# ---------------------------------------------------------

def jd_show_menu():
    """Display the main JD menu instructions."""
    print("\n===============================================")
    print("   High / Low Temperature Viewer - JD Edition")
    print("   Created by Jordan Dardar")
    print("===============================================")
    print("Choose an option below:")
    print("  H - View HIGH temperatures")
    print("  L - View LOW temperatures")
    print("  E - Exit program")


# ---------------------------------------------------------
# JD Main Loop
# ---------------------------------------------------------

def jd_main():
    """Main interactive loop for Jordan's program."""
    while True:
        jd_show_menu()
        choice = input("\nEnter your choice (H/L/E): ").strip().lower()

        if choice == "h":
            print("\nLoading Jordan's HIGH temperature graph...")
            jd_plot_highs()
        elif choice == "l":
            print("\nLoading Jordan's LOW temperature graph...")
            jd_plot_lows()
        elif choice == "e":
            print("\nThank you for using Jordan Dardar's High/Low Temp Viewer! Goodbye!")
            sys.exit(0)
        else:
            print("\nInvalid option. Please type H, L, or E.")


if __name__ == "__main__":
    jd_main()
