# Telegram Work Hours Bot

The Telegram Work Hours Bot is a bot designed to help users manage their work hours and determine when they can leave the workplace based on their arrival time and the assumption that the working day, including lunch break, lasts 8 hours and 45 minutes.

## Features

- **Work Hours Calculation**: Users can provide their arrival time to the bot in hours and minutes format, and the bot will calculate and send the estimated time when they can leave work.
- **Convenient Time Format**: The bot ensures that the calculated time is presented in a user-friendly format, making it easy for users to understand their work schedule.
- **Personalized Experience**: The bot provides personalized responses to each user based on their input and keeps track of their work hours individually.
- **User-Friendly Interaction**: The bot is designed to be intuitive and easy to use, allowing users to quickly input their arrival time and receive the corresponding work hours information.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/gecsagen/home_bot.git
   ```

2. Navigate to the project directory:

   ```bash
   cd home_bot
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

4. Set up the environment variables:
   - Rename the `.example.env` file to `.env`.
   - Open the `.env` file and update the values according to your configuration.

5. Start the bot:

   ```bash
   python bot.py
   ```

## Usage

1. Start a conversation with the bot on Telegram by searching for its username: `@home_bot`.

2. Provide your arrival time in the following format: `HH:MM`, where `HH` represents the hours and `MM` represents the minutes.

3. The bot will respond with the estimated time when you can leave work based on the assumed working day duration of 8 hours and 45 minutes.

4. Enjoy managing your work hours conveniently with the Telegram Work Hours Bot!

## Contributing

Contributions to the Telegram Work Hours Bot are welcome! If you have any suggestions, feature requests, or bug reports, please open an issue or submit a pull request.

When contributing to this project, please follow the existing coding style and conventions. Also, ensure that your changes are well-documented and thoroughly tested.

## License

This project is licensed under the [MIT License](LICENSE).

## Contact

If you have any questions, feedback, or inquiries, please feel free to contact the project maintainer:

- Email: [your-email@example.com](mailto:geksbomba@gmail.com)

---

*Note: The Telegram Work Hours Bot is a fictional project created for demonstration purposes. The actual implementation may vary based on your specific needs and requirements.*
