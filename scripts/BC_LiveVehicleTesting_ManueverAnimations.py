import pandas as pd
from matplotlib.animation import FuncAnimation
import matplotlib.pyplot as plt
import os
from datetime import datetime

# Set features to plot for the filtered data
FEATURES_TO_PLOT = ['veh_long_vel_mps', 'veh_accel_mps2', 'veh_jerk_mps3', 'veh_ltrl_vel_mps', 'veh_yaw_rate_radps']


def get_manuever():
    """
    Get a specific manuever from the live vehicle testing data based on user input time.
    """
    # Prompt user for which trip to load
    # Trip from 10:45 to 11:15 --> trip_num = 1 (Ayyan)
    # Trip from 11:50 to 12:30 --> trip_num = 2 (Isabel)
    while True:
        trip_num = input("Enter the trip number (1 [Ayyan] or 2 [Isabel]): ")
        if trip_num in ['1', '2']:
            break
        else:
            print("Invalid trip number. Please try again.")

    if trip_num == '1':
        trip1_df = pd.read_csv('data/trip1_data_mike_Nov15.csv')
    elif trip_num == '2':
        trip1_df = pd.read_csv('data/trip2_data_mike_Nov15.csv')

    
    # Convert 'date_time' to datetime format and remove timezone information
    trip1_df['date_time'] = pd.to_datetime(trip1_df['date_time']).dt.tz_localize(None)
    

    min_time = trip1_df['date_time'].min()
    max_time = trip1_df['date_time'].max()

    # Prompt user for a valid start time
    while True:
        user_time_str = input(f"Enter a start time between {min_time.strftime('%H:%M:%S')} and {max_time.strftime('%H:%M:%S')} (format HH:MM:SS): ")
        try:
            user_time = datetime.strptime(f"2024-11-15 {user_time_str}", '%Y-%m-%d %H:%M:%S')
            if min_time <= user_time <= max_time:
                break
            else:
                print("Time is out of range. Please try again.")
        except ValueError:
            print("Invalid time format or time is out of range. Please try again.")

    # Filter the dataframe based on the user input time
    start_time = user_time

    # Prompt for a valid end time that has to be at least 1 second after the start time
    while True:
        user_time_str = input(f"Enter an end time that is at least 1 second after {start_time.strftime('%H:%M:%S')} and less than {max_time.strftime('%H:%M:%S')} (format HH:MM:SS): ")
        try:
            end_time = datetime.strptime(f"2024-11-15 {user_time_str}", '%Y-%m-%d %H:%M:%S')
            if end_time > start_time and end_time < max_time:
                break
        except ValueError:
            print("Invalid time format or time is out of range. Please try again.")

    # Filter the dataframe based on the user input time
    trip1_df_filtered = trip1_df[(trip1_df['date_time'] >= start_time) & (trip1_df['date_time'] <= end_time)]

    return trip1_df_filtered

if __name__ == '__main__':
    manuever = get_manuever()
    
    # Create a complete time range with 1-second intervals
    min_time = manuever['date_time'].min()
    max_time = manuever['date_time'].max()
    complete_time_range = pd.date_range(start=min_time, end=max_time, freq='100ms')

    # Determine grid size
    num_features = len(FEATURES_TO_PLOT)
    grid_rows = 1
    grid_cols = 5

    # Create a figure and axis
    fig, axes = plt.subplots(grid_rows, grid_cols, figsize=(25, 5))
    fig.set_tight_layout(True)

    # Flatten axes array for easy iteration
    axes = axes.flatten()

    # Initialize lines and fills for each subplot
    lines = []
    fills = []

    for i, feature in enumerate(FEATURES_TO_PLOT):
        ax = axes[i]
        ax.plot(manuever['date_time'], manuever[feature], label=feature)
        line = ax.axvline(x=min_time, color='r', linestyle='--', linewidth=2)
        ax.set_xlim(min_time, max_time)
        ax.set_ylim(manuever[feature].min(), manuever[feature].max())
        ax.set_title(feature, fontsize=14, fontweight='bold')
        ax.set_xlabel('Time')
        ax.set_ylabel(feature, fontsize=12)
        ax.set_xticks([])  # Remove x-axis tickers
        ax.grid(True)  # Enable grid lines
        lines.append(line)
        fills.append((None, None))  # Placeholder for fill_between objects

    # Function to update the plot
    def update(frame):
        # Get the current time from the complete time range
        current_time = complete_time_range[frame]
        
        for i, feature in enumerate(FEATURES_TO_PLOT):
            ax = axes[i]
            line = lines[i]
            line.set_xdata([current_time])
            
            # Clear previous fills
            if fills[i][0] is not None:
                fills[i][0].remove()
            if fills[i][1] is not None:
                fills[i][1].remove()
            
            # Update the fill areas
            fill1 = ax.fill_between(complete_time_range, manuever[feature].min(), manuever[feature].max(), where=(complete_time_range <= current_time), color='green', alpha=0.3)
            fill2 = ax.fill_between(complete_time_range, manuever[feature].min(), manuever[feature].max(), where=(complete_time_range >= current_time), color='gray', alpha=0.3)
            fills[i] = (fill1, fill2)
        
        # Update the label with current time in HH:MM:SS format and bold font
        current_time_str = current_time.strftime('%H:%M:%S')
        fig.suptitle(f'Time: {current_time_str}', fontweight='bold', fontsize=16, color='red')
        return lines

    # Create the animation with 10 fps
    ani = FuncAnimation(fig, update, frames=len(complete_time_range), interval=1000/10)

    # Save the animation as a GIF
    if not os.path.exists('scripts/gifs'):
        os.makedirs('scripts/gifs')
    # Format the file name with the start and end times
    start_time_str = manuever['date_time'].iloc[0].strftime('%Y-%m-%d_%H-%M-%S')
    end_time_str = manuever['date_time'].iloc[-1].strftime('%Y-%m-%d_%H-%M-%S')
    file_name = f'scripts/gifs/vehicle_dynamics_animation_{start_time_str}_{end_time_str}.gif'
    ani.save(file_name, writer='pillow', dpi=100)


