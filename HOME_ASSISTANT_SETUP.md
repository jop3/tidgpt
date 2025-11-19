# Home Assistant Time Reminder Setup

This guide will help you set up automated time announcements on your Google Home speakers using Home Assistant.

## Features

- Announces current time at scheduled intervals
- Provides countdown reminders ("15 minutes until 8:00 AM")
- Weekday-only scheduling (won't disturb weekends)
- Customizable times and target deadlines
- Works with any Google Home or Chromecast speaker
- **Easy on/off control from your phone** - See [MOBILE_CONTROL_GUIDE.md](MOBILE_CONTROL_GUIDE.md)

## Prerequisites

- Home Assistant installed and running
- Google Home speaker(s) already connected to Home Assistant
- File Editor add-on (or SSH access) to edit configuration files

## Step 1: Find Your Speaker Entity ID

1. Open Home Assistant
2. Go to **Settings** → **Devices & Services** → **Entities**
3. Search for your Google Home speaker name
4. Copy the **entity_id** (it will look like `media_player.living_room_speaker` or `media_player.kitchen_display`)

Example entity IDs:
- `media_player.living_room_speaker`
- `media_player.bedroom_speaker`
- `media_player.kitchen_display`

## Step 2: Add the Configuration

You have two options for adding the automations:

### Option A: Using File Editor (Recommended)

1. Install the **File Editor** add-on if you haven't already:
   - Go to **Settings** → **Add-ons** → **Add-on Store**
   - Search for "File Editor" and install it

2. Open File Editor from the sidebar

3. Open `configuration.yaml`

4. Add this line if it doesn't already exist:
   ```yaml
   script: !include scripts.yaml
   automation: !include automations.yaml
   ```

5. Open `scripts.yaml` and add the script from `home_assistant_automations.yaml` (the `script:` section)

6. Open `automations.yaml` and add the automations from `home_assistant_automations.yaml` (the `automation:` section)

7. **Important**: In each automation, change `media_player.living_room_speaker` to your actual speaker entity ID

### Option B: Using UI Automation Editor

For each time you want an announcement:

1. Go to **Settings** → **Automations & Scenes**
2. Click **Create Automation** → **Create new automation**
3. Click the three dots → **Edit in YAML**
4. Copy one automation from `home_assistant_automations.yaml`
5. Replace `media_player.living_room_speaker` with your speaker
6. Save

## Step 3: Customize the Schedule

Edit the times to match your needs:

**Default schedule (weekday mornings)**:
- 7:00 AM - "The time is 7 AM. One hour until 8 AM."
- 7:15 AM - "The time is 7:15 AM. 45 minutes until 8 AM."
- 7:30 AM - "The time is 7:30 AM. 30 minutes until 8 AM."
- 7:45 AM - "The time is 7:45 AM. 15 minutes until 8 AM."
- 7:55 AM - "Only 5 minutes until 8 AM!"

**To change announcement times:**
```yaml
trigger:
  - platform: time
    at: "07:00:00"  # Change this to your desired time
```

**To change the target time:**
```yaml
data:
  target_time: "08:00"  # Change this to your departure time
```

**To change which days:**
```yaml
condition:
  - condition: time
    weekday:
      - mon  # Remove or add: mon, tue, wed, thu, fri, sat, sun
      - tue
      - wed
      - thu
      - fri
```

## Step 4: Reload and Test

1. **Check Configuration**:
   - Go to **Developer Tools** → **YAML**
   - Click **Check Configuration**
   - Fix any errors if they appear

2. **Reload**:
   - Click **Reload Automations** (or restart Home Assistant)

3. **Test**:
   - Go to **Settings** → **Automations & Scenes**
   - Find "Morning Reminder - 7:00 AM"
   - Click the three dots → **Run**
   - Your speaker should announce the time!

## Advanced Customization

### Announce to Multiple Speakers

Change:
```yaml
entity_id: media_player.living_room_speaker
```

To:
```yaml
entity_id:
  - media_player.living_room_speaker
  - media_player.kids_room_speaker
  - media_player.kitchen_speaker
```

### Different Target Times

If your kids need to leave at different times, create separate automations for each child's room:

```yaml
# Kid 1 - leaves at 7:45
- service: script.announce_time_and_countdown
  data:
    speaker: media_player.kid1_room
    target_time: "07:45"

# Kid 2 - leaves at 8:00
- service: script.announce_time_and_countdown
  data:
    speaker: media_player.kid2_room
    target_time: "08:00"
```

### Custom Messages

For special announcements, use direct TTS:

```yaml
- service: tts.google_translate_say
  target:
    entity_id: media_player.living_room_speaker
  data:
    message: "Don't forget your lunch!"
```

### Volume Control

Set volume before announcements:

```yaml
action:
  - service: media_player.volume_set
    target:
      entity_id: media_player.living_room_speaker
    data:
      volume_level: 0.5  # 0.0 to 1.0
  - service: script.announce_time_and_countdown
    data:
      speaker: media_player.living_room_speaker
      target_time: "08:00"
```

### Gradual Wake-Up

Start quiet and get louder:

```yaml
# 7:00 - Quiet
- service: media_player.volume_set
  data:
    volume_level: 0.3

# 7:30 - Medium
- service: media_player.volume_set
  data:
    volume_level: 0.5

# 7:55 - Loud
- service: media_player.volume_set
  data:
    volume_level: 0.7
```

## Troubleshooting

### Speaker Not Found

- Make sure your Google Home is connected to Home Assistant
- Check **Settings** → **Devices & Services** → **Google Cast**
- Try disconnecting and reconnecting the speaker

### No Sound

- Check speaker volume in Home Assistant
- Make sure the speaker isn't playing something else
- Try a manual TTS test in **Developer Tools** → **Services**:
  ```yaml
  service: tts.google_translate_say
  target:
    entity_id: media_player.living_room_speaker
  data:
    message: "Test message"
  ```

### Automations Not Running

- Check **Settings** → **Automations & Scenes** - make sure they're enabled (not grayed out)
- Verify the time condition matches your timezone
- Check **Settings** → **System** → **Logs** for errors

### Wrong Time Announced

- Check your Home Assistant timezone: **Settings** → **System** → **General**
- The time announcements use your Home Assistant's system time

## Tips for Kids

- Start with more frequent announcements and reduce over time
- Use consistent target times so kids internalize the schedule
- Consider visual cues too (smart lights that change color)
- Combine with other automations (lights turning on, music playing)

## Example Complete Setup

Here's a full morning routine automation:

```yaml
- id: complete_morning_routine
  alias: "Complete Morning Routine - 7:00 AM"
  trigger:
    - platform: time
      at: "07:00:00"
  condition:
    - condition: time
      weekday: [mon, tue, wed, thu, fri]
  action:
    # Turn on bedroom lights
    - service: light.turn_on
      target:
        entity_id: light.kids_bedroom
      data:
        brightness_pct: 50

    # Wait a moment
    - delay:
        seconds: 5

    # Announce time
    - service: script.announce_time_and_countdown
      data:
        speaker: media_player.kids_room
        target_time: "08:00"

    # Play morning music after 2 minutes
    - delay:
        minutes: 2
    - service: media_player.play_media
      target:
        entity_id: media_player.kids_room
      data:
        media_content_id: "your_spotify_playlist_uri"
        media_content_type: "playlist"
```

## Need Help?

- Check the [Home Assistant Community Forums](https://community.home-assistant.io/)
- Search for "TTS automation" or "Google Home announcements"
- Post your configuration (with entity IDs removed) for help

## Alternative: Simple Manual Announcements

If you just want to test or use it occasionally without full automation:

1. Go to **Developer Tools** → **Services**
2. Select `tts.google_translate_say`
3. Fill in:
   ```yaml
   entity_id: media_player.living_room_speaker
   message: "It's time to get ready for school!"
   ```
4. Click **Call Service**

You can also create a dashboard button for manual announcements!
