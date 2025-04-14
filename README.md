# Email Scheduler

This project is an email scheduler that sends beautifully crafted HTML emails wishing recipients a good morning, good afternoon, good noon, good evening, or good night at specific times of the day. The project is organized in a way that makes it easy to understand and use.

## Project Structure

```
email-scheduler
├── src
│   ├── scheduler.py          # Main logic for scheduling email sending
│   ├── email_sender.py       # Handles email sending functionality
│   ├── config.py             # Configuration settings and environment variable loading
│   ├── templates             # Contains HTML templates for different greetings
│   │   ├── good_morning.html
│   │   ├── good_afternoon.html
│   │   ├── good_noon.html
│   │   ├── good_evening.html
│   │   └── good_night.html
├── requirements.txt          # Lists project dependencies
├── README.md                 # Documentation for the project
└── .env                      # Stores environment variables for sensitive information
```

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/yourusername/email-scheduler.git
   cd email-scheduler
   ```

2. **Create a virtual environment** (optional but recommended):
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:
   ```
   pip install -r requirements.txt
   ```

4. **Configure your email settings**:
   - Create a `.env` file in the root directory and add your email credentials and other configuration settings.

5. **Design your HTML templates**:
   - Customize the HTML files located in the `src/templates` directory to create your desired email designs.

## Usage

To start the email scheduler, run the following command:

```
python src/scheduler.py
```

The scheduler will automatically send emails at the specified times based on the configured greetings.

## Examples

- Good Morning emails will be sent at 8:00 AM.
- Good Afternoon emails will be sent at 12:00 PM.
- Good Noon emails will be sent at 1:00 PM.
- Good Evening emails will be sent at 6:00 PM.
- Good Night emails will be sent at 9:00 PM.

## Contributing

Feel free to submit issues or pull requests if you have suggestions or improvements for the project.

## License

This project is licensed under the MIT License. See the LICENSE file for details.