#!/usr/bin/env python3
"""
Time Reminder App for Google Home
Announces time and reminders to help kids track morning routines
"""

import pychromecast
import time
import argparse
import yaml
from datetime import datetime, timedelta
from pathlib import Path
import sys
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class TimeReminder:
    def __init__(self, config_file='config.yaml'):
        """Initialize the Time Reminder app"""
        self.config = self.load_config(config_file)
        self.speaker = None

    def load_config(self, config_file):
        """Load configuration from YAML file"""
        config_path = Path(config_file)
        if not config_path.exists():
            logger.error(f"Config file not found: {config_file}")
            logger.info("Please create a config.yaml file. See config.example.yaml for reference.")
            sys.exit(1)

        with open(config_path, 'r') as f:
            return yaml.safe_load(f)

    def discover_speakers(self):
        """Discover available Google Home/Chromecast devices"""
        logger.info("Discovering Chromecast devices...")
        chromecasts, browser = pychromecast.get_listed_chromecasts(friendly_names=[self.config['speaker_name']])

        if not chromecasts:
            logger.error(f"Could not find speaker: {self.config['speaker_name']}")
            logger.info("Available devices:")
            all_chromecasts, _ = pychromecast.get_chromecasts()
            for cc in all_chromecasts:
                logger.info(f"  - {cc.name}")
            return None

        return chromecasts[0]

    def connect_speaker(self):
        """Connect to the configured Google Home speaker"""
        self.speaker = self.discover_speakers()
        if self.speaker:
            self.speaker.wait()
            logger.info(f"Connected to: {self.speaker.name}")
            return True
        return False

    def speak(self, message, language='en'):
        """Send TTS message to Google Home speaker"""
        if not self.speaker:
            logger.error("No speaker connected")
            return False

        try:
            logger.info(f"Speaking: {message}")
            # Use the default media controller for TTS
            mc = self.speaker.media_controller
            mc.play_media(
                f'http://translate.google.com/translate_tts?ie=UTF-8&total=1&idx=0&textlen=32&client=tw-ob&q={message.replace(" ", "+")}&tl={language}',
                'audio/mp3'
            )
            mc.block_until_active()
            return True
        except Exception as e:
            logger.error(f"Error speaking: {e}")
            return False

    def announce_time(self):
        """Announce the current time"""
        now = datetime.now()
        time_str = now.strftime("%I:%M %p").lstrip('0')
        message = f"The time is now {time_str}"
        self.speak(message)

    def announce_countdown(self, target_time_str):
        """Announce time remaining until target time"""
        now = datetime.now()
        target_time = datetime.strptime(target_time_str, "%H:%M").replace(
            year=now.year, month=now.month, day=now.day
        )

        # If target time has passed today, assume it's for tomorrow
        if target_time < now:
            target_time += timedelta(days=1)

        time_diff = target_time - now
        minutes = int(time_diff.total_seconds() / 60)

        if minutes > 60:
            hours = minutes // 60
            remaining_minutes = minutes % 60
            if remaining_minutes > 0:
                message = f"{hours} hours and {remaining_minutes} minutes until {target_time.strftime('%I:%M %p').lstrip('0')}"
            else:
                message = f"{hours} hours until {target_time.strftime('%I:%M %p').lstrip('0')}"
        else:
            message = f"{minutes} minutes until {target_time.strftime('%I:%M %p').lstrip('0')}"

        self.speak(message)

    def run_schedule(self):
        """Run the scheduled announcements from config"""
        if not self.connect_speaker():
            logger.error("Failed to connect to speaker")
            sys.exit(1)

        logger.info("Starting scheduled announcements...")
        logger.info("Press Ctrl+C to stop")

        try:
            while True:
                now = datetime.now()
                current_time = now.strftime("%H:%M")

                # Check if current time matches any scheduled announcement
                for announcement in self.config.get('schedule', []):
                    if announcement['time'] == current_time:
                        logger.info(f"Triggering announcement at {current_time}")

                        # Announce current time if configured
                        if announcement.get('announce_time', True):
                            self.announce_time()
                            time.sleep(3)  # Pause between announcements

                        # Announce countdowns if configured
                        for countdown in announcement.get('countdowns', []):
                            self.announce_countdown(countdown)
                            time.sleep(3)  # Pause between announcements

                # Sleep until next minute
                time.sleep(60 - now.second)

        except KeyboardInterrupt:
            logger.info("\nStopping announcements...")

    def list_devices(self):
        """List all available Chromecast devices"""
        logger.info("Scanning for all Chromecast devices...")
        chromecasts, browser = pychromecast.get_chromecasts()

        if not chromecasts:
            logger.info("No devices found")
            return

        print("\nAvailable devices:")
        for cc in chromecasts:
            cc.wait()
            print(f"  - Name: {cc.name}")
            print(f"    Model: {cc.model_name}")
            print(f"    UUID: {cc.uuid}")
            print()


def main():
    parser = argparse.ArgumentParser(
        description='Time Reminder App for Google Home'
    )
    parser.add_argument(
        '--config',
        default='config.yaml',
        help='Path to config file (default: config.yaml)'
    )
    parser.add_argument(
        '--list-devices',
        action='store_true',
        help='List all available Chromecast devices'
    )
    parser.add_argument(
        '--test',
        action='store_true',
        help='Test connection and speak a message'
    )
    parser.add_argument(
        '--announce-time',
        action='store_true',
        help='Announce the current time once'
    )
    parser.add_argument(
        '--countdown',
        help='Announce countdown to specific time (format: HH:MM, e.g., 08:00)'
    )

    args = parser.parse_args()

    app = TimeReminder(args.config)

    if args.list_devices:
        app.list_devices()
    elif args.test:
        if app.connect_speaker():
            app.speak("Time reminder app is working correctly!")
    elif args.announce_time:
        if app.connect_speaker():
            app.announce_time()
    elif args.countdown:
        if app.connect_speaker():
            app.announce_countdown(args.countdown)
    else:
        # Run the scheduled announcements
        app.run_schedule()


if __name__ == '__main__':
    main()
