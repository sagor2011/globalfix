# GlobalFix

GlobalFix is a Python-based utility designed to track and display detailed task information and system usage statistics on Windows systems. It provides insights into CPU and memory usage by active processes, helping users manage their system resources more efficiently.

## Features

- Lists all running tasks with details like PID, name, user, CPU, and memory usage.
- Displays overall system usage statistics, including CPU, memory, and disk usage.
- Refreshes the displayed information upon user request.

## Requirements

- Python 3.x
- `psutil` library

## Installation

1. Make sure you have Python installed on your system.
2. Install the `psutil` library if you haven't already:

   ```sh
   pip install psutil
   ```

## Usage

1. Clone the repository or download the `globalfix.py` file.
2. Run the script using Python:

   ```sh
   python globalfix.py
   ```

3. The program will display current task information and system usage statistics in the console.
4. Press Enter to refresh the information.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Acknowledgements

- Built with the `psutil` library for accessing system and process information.

## Contact

For any questions or suggestions, please open an issue on the GitHub repository.