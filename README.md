# Time Reminder App for Google Home

Announces the time and countdowns to your Google Home speakers, perfect for helping kids stay on track during morning routines.

## 🏠 Have Home Assistant? Use That Instead!

If you already have Home Assistant, use the **[Home Assistant automations](HOME_ASSISTANT_SETUP.md)** instead - they're simpler and more integrated. This Python app is for standalone use or if you don't have Home Assistant.

**Quick Links**:
- **[Home Assistant Setup](HOME_ASSISTANT_SETUP.md)** - For Home Assistant users (recommended)
- **[Quick Start Guide](QUICKSTART.md)** - Compare both options
- **Python App Setup** - Continue reading below

---

## Features

- Announces current time to Google Home speakers
- Provides countdown reminders ("15 minutes until 8:00 AM")
- Configurable schedule via YAML file
- Automatic discovery of Google Home/Chromecast devices
- Can run continuously or as individual announcements
- Easy to automate with cron or systemd

## Requirements

- Python 3.7 or higher
- Google Home or Chromecast-enabled speaker on the same network
- Linux, macOS, or Windows

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

Or install manually:
```bash
pip install pychromecast PyYAML
```

### 2. Find Your Speaker

List all available Google Home/Chromecast devices:

```bash
python time_reminder.py --list-devices
```

This will show all devices on your network. Note the exact name of your speaker.

### 3. Create Configuration

Copy the example configuration:

```bash
cp config.example.yaml config.yaml
```

Edit `config.yaml` and update the speaker name to match your device:

```yaml
speaker_name: "Your Speaker Name"  # Must match exactly!
```

### 4. Test the Connection

Test that everything works:

```bash
python time_reminder.py --test
```

You should hear "Time reminder app is working correctly!" from your speaker.

### 5. Try a Time Announcement

```bash
python time_reminder.py --announce-time
```

### 6. Try a Countdown

```bash
python time_reminder.py --countdown 08:00
```

This will announce how many minutes until 8:00 AM.

## Configuration

Edit `config.yaml` to set up your morning routine schedule:

```yaml
speaker_name: "Kitchen speaker"

schedule:
  # 7:00 AM - First announcement
  - time: "07:00"
    announce_time: true
    countdowns:
      - "08:00"  # School departure time

  # 7:30 AM - Half hour warning
  - time: "07:30"
    announce_time: true
    countdowns:
      - "08:00"

  # 7:45 AM - 15 minute warning
  - time: "07:45"
    announce_time: true
    countdowns:
      - "08:00"
```

### Configuration Options

- `speaker_name`: Exact name of your Google Home speaker (case-sensitive)
- `schedule`: List of scheduled announcements
  - `time`: When to make the announcement (24-hour format HH:MM)
  - `announce_time`: Whether to announce the current time (true/false)
  - `countdowns`: List of target times to count down to (24-hour format)

## Running the App

### Run Scheduled Announcements

This runs continuously and makes announcements based on your schedule:

```bash
python time_reminder.py
```

The app will keep running and make announcements at the scheduled times. Press Ctrl+C to stop.

### One-Time Commands

Announce the current time:
```bash
python time_reminder.py --announce-time
```

Announce countdown to a specific time:
```bash
python time_reminder.py --countdown 08:00
```

## Automation

### Option 1: Run at Startup (Recommended)

Create a systemd service (Linux):

```bash
# Copy the example service file
sudo cp time-reminder.service /etc/systemd/system/

# Edit the service file to set the correct paths
sudo nano /etc/systemd/system/time-reminder.service

# Enable and start the service
sudo systemctl enable time-reminder
sudo systemctl start time-reminder

# Check status
sudo systemctl status time-reminder
```

### Option 2: Cron Job

Run only during specific hours (e.g., 7-8 AM on weekdays):

```bash
crontab -e
```

Add this line:
```
0 7 * * 1-5 cd /path/to/tidgpt && timeout 1h python time_reminder.py
```

This starts the app at 7:00 AM on weekdays and runs for 1 hour.

### Option 3: Manual Run

Simply start it manually when needed:

```bash
python time_reminder.py
```

## Troubleshooting

### Speaker Not Found

1. Make sure your computer and Google Home are on the same network
2. Run `python time_reminder.py --list-devices` to see available devices
3. Ensure the speaker name in `config.yaml` matches exactly (case-sensitive)
4. Check that your firewall isn't blocking mDNS/multicast traffic

### No Sound

1. Make sure the speaker volume is turned up
2. Try the test command: `python time_reminder.py --test`
3. Check if the speaker is already playing something else

### Connection Issues

- The app needs to be on the same local network as your Google Home
- Some guest networks block device discovery
- Try disabling VPN if you're using one

### Python Version

Make sure you're using Python 3.7+:
```bash
python --version
```

## Command Line Options

```
python time_reminder.py [OPTIONS]

Options:
  --config FILE        Use alternate config file (default: config.yaml)
  --list-devices       List all Chromecast devices and exit
  --test              Test connection and speak a message
  --announce-time      Announce current time once and exit
  --countdown HH:MM    Announce countdown to specific time and exit
  -h, --help          Show help message
```

## Tips for Kids

- Set up a visual schedule alongside the voice reminders
- Use consistent target times so kids learn the routine
- Start with more frequent reminders and reduce as they adapt
- Consider different schedules for weekdays vs weekends

## Example Schedules

### Minimal (just a few key reminders)
```yaml
schedule:
  - time: "07:30"
    announce_time: true
    countdowns: ["08:00"]
  - time: "07:50"
    announce_time: false
    countdowns: ["08:00"]
```

### Detailed (every 15 minutes)
```yaml
schedule:
  - time: "07:00"
    announce_time: true
    countdowns: ["08:00"]
  - time: "07:15"
    announce_time: true
    countdowns: ["08:00"]
  - time: "07:30"
    announce_time: true
    countdowns: ["08:00"]
  - time: "07:45"
    announce_time: true
    countdowns: ["08:00"]
  - time: "07:55"
    announce_time: false
    countdowns: ["08:00"]
```

### Multiple Target Times
```yaml
schedule:
  - time: "07:30"
    announce_time: true
    countdowns:
      - "08:00"  # Leave for school
      - "08:30"  # Bus arrives
```

## License

MIT License - Feel free to use and modify as needed.

## Contributing

Issues and pull requests welcome!
