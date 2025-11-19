# Quick Start Guide

Choose the method that works best for you:

## Option 1: Home Assistant (Recommended if you already have it)

**Pros**: Simple, integrated, visual interface, easy automation management
**Setup Time**: 5-10 minutes

1. Find your Google Home speaker entity ID in Home Assistant
2. Copy the automations from `home_assistant_automations.yaml`
3. Replace `media_player.living_room_speaker` with your speaker
4. Add to Home Assistant and reload

**See**: [HOME_ASSISTANT_SETUP.md](HOME_ASSISTANT_SETUP.md) for detailed instructions

---

## Option 2: Standalone Python App

**Pros**: Runs independently, portable, doesn't need Home Assistant
**Setup Time**: 10-15 minutes

1. Install dependencies: `pip install -r requirements.txt`
2. Find your speaker: `python time_reminder.py --list-devices`
3. Create config: `cp config.example.yaml config.yaml`
4. Edit config with your speaker name
5. Run: `python time_reminder.py`

**See**: [README.md](README.md) for detailed instructions

---

## Which Should I Choose?

### Use Home Assistant if:
- You already have Home Assistant running
- You want a visual interface to manage automations
- You want to combine with other smart home actions (lights, music, etc.)
- You prefer point-and-click configuration

### Use Python App if:
- You don't have Home Assistant
- You want something simple and standalone
- You need to run it on a different computer than Home Assistant
- You prefer configuration files over UI

---

## Quick Comparison

| Feature | Home Assistant | Python App |
|---------|---------------|------------|
| Setup Complexity | Easy | Medium |
| Visual Interface | ✅ Yes | ❌ No |
| Runs Independently | ❌ No | ✅ Yes |
| Multiple Speakers | ✅ Easy | ✅ Possible |
| Combine with Lights/Music | ✅ Yes | ❌ No |
| Works without HA | ❌ No | ✅ Yes |
| Can Run on Any Computer | Depends | ✅ Yes |

---

## I Have Home Assistant - Which Approach?

Since you already have Home Assistant running, **use the Home Assistant automations**. They're simpler, more integrated, and give you more flexibility.

The Python app is still useful if you:
- Want to run announcements from a different computer
- Need a portable solution
- Want to learn Python/Chromecast programming

---

## Test Commands (Python App)

```bash
# List all speakers
python time_reminder.py --list-devices

# Test connection
python time_reminder.py --test

# Announce current time
python time_reminder.py --announce-time

# Announce countdown to 8:00 AM
python time_reminder.py --countdown 08:00
```

## Test in Home Assistant

1. Go to **Developer Tools** → **Services**
2. Select `tts.google_translate_say`
3. Fill in:
   ```yaml
   entity_id: media_player.your_speaker
   message: "Test message"
   ```
4. Click **Call Service**
