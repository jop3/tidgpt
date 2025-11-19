# Quick Start Guide

Choose the method that works best for you:

## ⭐ Recommended: Home Assistant with OpenAI TTS (Swedish)

**Best option if you need Swedish language and better voice quality**

**Pros**: Natural-sounding Swedish voices, kids will actually listen, very affordable (~1 SEK/month)
**Setup Time**: 10 minutes

1. Get OpenAI API key (takes 5 minutes, see guide)
2. Add OpenAI TTS to Home Assistant configuration
3. Copy Swedish automations from `home_assistant_automations_openai_swedish.yaml`
4. Replace `media_player.living_room_speaker` with your speaker

**See**: [OPENAI_TTS_SETUP.md](OPENAI_TTS_SETUP.md) for detailed instructions

**Voice samples**: Try voices like `nova` (calm), `echo` (friendly), `fable` (energetic)

---

## Option 1: Home Assistant with Google Translate (Basic)

**Free option with robotic English voice**

**Pros**: Simple, integrated, visual interface, completely free
**Setup Time**: 5-10 minutes
**Cons**: Robotic voice, English only (or poor Swedish)

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

| Feature | HA + OpenAI TTS | HA + Google TTS | Python App |
|---------|----------------|-----------------|------------|
| Setup Complexity | Easy | Easy | Medium |
| Voice Quality | ⭐⭐⭐⭐⭐ Natural | ⭐⭐ Robotic | ⭐⭐ Robotic |
| Swedish Support | ✅ Excellent | ⚠️ Poor | ⚠️ Poor |
| Cost | ~1 SEK/month | Free | Free |
| Visual Interface | ✅ Yes | ✅ Yes | ❌ No |
| Multiple Speakers | ✅ Easy | ✅ Easy | ✅ Possible |
| Works Offline | ❌ No | ⚠️ Limited | ⚠️ Limited |
| Kids Will Listen | ✅ Yes | ⚠️ Maybe | ⚠️ Maybe |

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

### Test OpenAI TTS (Swedish)
1. Go to **Developer Tools** → **Services**
2. Select `tts.openai_say`
3. Fill in:
   ```yaml
   entity_id: media_player.your_speaker
   message: "Klockan är nu 7. En timme kvar till klockan 8."
   ```
4. Click **Call Service**

### Test Google TTS (English)
1. Go to **Developer Tools** → **Services**
2. Select `tts.google_translate_say`
3. Fill in:
   ```yaml
   entity_id: media_player.your_speaker
   message: "The time is now 7 AM"
   ```
4. Click **Call Service**
