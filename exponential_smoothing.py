# import random
#
#
# def exponential_smoothing(alpha, data_stream):
#     smoothed_data = []
#     prev_smoothed = data_stream[0]  # Initial value for the first data point
#
#     for data_point in data_stream:
#         smoothed = alpha * data_point + (1 - alpha) * prev_smoothed
#         smoothed_data.append(smoothed)
#         prev_smoothed = smoothed
#
#     return smoothed_data
#
#
# # Generate a random stream of data points
# random.seed(42)  # For reproducibility
# data_stream = [random.randint(1, 100) for _ in range(10)]
#
# # Define the smoothing parameter (alpha)
# alpha = 0.2
#
# # Apply exponential smoothing to the data
# smoothed_data = exponential_smoothing(alpha, data_stream)
#
# # Print the original data and the smoothed data
# print("Original data:", data_stream)
# print("Smoothed data:", smoothed_data)

# import queue
#
# class HighPassFilter:
#
#     def __init__(self, cutoff_frequency):
#         self.cutoff_frequency = cutoff_frequency
#         self.queue = queue.Queue()
#
#     def filter(self, sample):
#         if sample > self.cutoff_frequency:
#             self.queue.put(sample)
#             return sample
#     def get_filtered_samples(self):
#         filtered_samples = []
#         while not self.queue.empty():
#             filtered_samples.append(self.queue.get())
#         return filtered_samples
#
# def main():
#     filter = HighPassFilter(20)
#     samples = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
#     for sample in samples:
#         a=filter.filter(sample)
#         print(a)
#     filtered_samples = filter.get_filtered_samples()
#     print(filtered_samples)
#
# if __name__ == "__main__":
#     main()
import numpy as np
import matplotlib as plt
def moving_average(signal, window_size):
    # Pad the signal to handle the edges
    padded_signal = np.pad(signal, (window_size // 2, window_size // 2), mode='edge')

    # Compute the moving average using convolution
    window = np.ones(window_size) / window_size
    smoothed_signal = np.convolve(padded_signal, window, mode='valid')

    return smoothed_signal


# Sample data for demonstration purposes
# Replace this with your actual filtered signal
time = np.linspace(0, 1, 1000)  # Time vector
filtered_signal = np.sin(2 * np.pi * 5 * time) + 0.5 * np.sin(2 * np.pi * 50 * time)

# Define moving average window size
window_size = 10

# Apply moving average to the filtered signal
smoothed_signal = moving_average(filtered_signal, window_size)

# Plot the filtered and smoothed signals
# plt.figure(figsize=(10, 6))
# plt.plot(time, filtered_signal, label='Filtered Signal')
plt.plot(time[window_size // 2:-window_size // 2], smoothed_signal, label='Smoothed Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.legend()
plt.grid(True)
plt.show()