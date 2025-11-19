# OpenAI TTS Setup for Home Assistant (Swedish)

This guide shows you how to upgrade from Google Translate TTS to OpenAI's much better sounding voices with Swedish language support.

## Why OpenAI TTS?

- **Much better sound quality** - Natural voices that don't sound robotic
- **Excellent Swedish support** - Native Swedish pronunciation
- **Very affordable** - ~$0.015 per 1000 characters (about $0.30/month for daily morning reminders)
- **Easy to set up** - Takes about 10 minutes

## Cost Breakdown

For daily morning reminders (5 announcements per day on weekdays):
- Average message: ~50 characters
- Per day: 5 messages × 50 chars = 250 characters
- Per month: 250 × 22 weekdays = 5,500 characters
- **Cost: About $0.08-0.10 per month** (less than 1 SEK!)

You get $5 in free credits when you sign up, which lasts months.

## Step 1: Get OpenAI API Key (5 minutes)

1. Go to https://platform.openai.com/
2. Sign up or log in
3. Click your profile icon (top right) → **View API Keys**
4. Click **Create new secret key**
5. Give it a name like "Home Assistant TTS"
6. **Copy the key immediately** (you can't see it again!)
7. Save it somewhere safe (you'll need it in a moment)

### Add Payment Method (Required)

OpenAI requires a payment method even for the free tier:

1. Go to https://platform.openai.com/settings/organization/billing/overview
2. Click **Add payment method**
3. Add a credit/debit card
4. Set a usage limit if you want (e.g., $5/month maximum)

Don't worry - with morning reminders, you'll spend less than 1 SEK per month!

## Step 2: Add OpenAI TTS to Home Assistant (3 minutes)

### Option A: Using File Editor (Easiest)

1. Open **File Editor** in Home Assistant
2. Open `configuration.yaml`
3. Add this section (or update existing `tts:` section):

```yaml
tts:
  - platform: openai_tts
    api_key: sk-proj-xxxxxxxxxxxxxxxxxxxxx  # Your API key here
    voice: nova  # See voice options below
```

4. **Save the file**

### Option B: Using YAML Editor

1. Go to **Settings** → **Add-ons** → **File Editor**
2. Edit `configuration.yaml`
3. Add the TTS configuration above
4. Save

## Step 3: Choose a Voice

OpenAI has 6 voices. All support Swedish! Try each to find one your kids like:

- **`alloy`** - Neutral, clear
- **`echo`** - Warm, friendly (good for kids)
- **`fable`** - Upbeat, energetic
- **`nova`** - Calm, soothing (recommended for mornings)
- **`onyx`** - Deep, authoritative
- **`shimmer`** - Bright, enthusiastic

**Start with `nova` or `echo`** - they work great for morning routines.

To change voices later, just edit `configuration.yaml` and restart Home Assistant.

## Step 4: Restart Home Assistant

1. Go to **Settings** → **System**
2. Click **Restart** (top right)
3. Wait for Home Assistant to come back online (~1 minute)

## Step 5: Test It!

1. Go to **Developer Tools** → **Services**
2. Select `tts.openai_say`
3. Fill in:
   ```yaml
   entity_id: media_player.your_speaker_name
   message: "Klockan är nu 7. En timme kvar till klockan 8."
   ```
4. Click **Call Service**

You should hear the message in Swedish with a much better voice!

## Step 6: Add the Swedish Automations

Now use the Swedish automations from `home_assistant_automations_openai_swedish.yaml`:

1. Copy the `script:` section to your `scripts.yaml`
2. Copy the `automation:` section to your `automations.yaml`
3. **Change `media_player.living_room_speaker`** to your actual speaker
4. Reload scripts and automations (or restart HA)

## What the Automations Will Say (in Swedish)

- **7:00**: "Klockan är nu 7. En timme kvar till klockan 8."
- **7:15**: "Klockan är nu 7. 45 minuter kvar till klockan 8."
- **7:30**: "Klockan är nu 7 och 30. 30 minuter kvar till klockan 8."
- **7:45**: "Klockan är nu 7 och 45. 15 minuter kvar till klockan 8."
- **7:55**: "Uppmärksamhet! Bara 5 minuter kvar till klockan 8. Dags att göra klart och göra dig redo!"

## Customization Tips

### Try Different Voices

Let your kids help choose! Test each voice:

```yaml
service: tts.openai_say
data:
  entity_id: media_player.your_speaker
  message: "Hej! Jag är rösten Nova. Tycker ni om hur jag låter?"
```

Change `voice: nova` in `configuration.yaml` to try others.

### Custom Messages

Add specific reminders your kids need:

```yaml
# Borsta tänderna
- service: tts.openai_say
  data:
    entity_id: media_player.kids_room
    message: "Glöm inte att borsta tänderna!"

# Packa skolväskan
- service: tts.openai_say
  data:
    entity_id: media_player.kids_room
    message: "Kom ihåg att packa din skolväska och ta med matlådan!"

# Frukostpåminnelse
- service: tts.openai_say
  data:
    entity_id: media_player.kitchen
    message: "Dags för frukost nu!"
```

### Adjust Volume

Set volume before announcements so they're not too loud in the morning:

```yaml
action:
  # Set comfortable morning volume
  - service: media_player.volume_set
    target:
      entity_id: media_player.kids_room
    data:
      volume_level: 0.4  # 40% volume

  # Then announce
  - service: tts.openai_say
    target:
      entity_id: media_player.kids_room
    data:
      message: "Klockan är nu 7. Dags att vakna!"
```

## Troubleshooting

### "Invalid API Key" Error

- Make sure you copied the entire key including `sk-proj-` prefix
- Check for extra spaces before/after the key
- Generate a new key if needed

### No Sound

- Test with Developer Tools first to isolate the issue
- Check speaker volume
- Make sure speaker isn't already playing something

### Wrong Language / English Instead of Swedish

OpenAI automatically detects language from the message. If your messages are in Swedish, it will speak Swedish. If you're hearing English, check that your messages are actually in Swedish in the automation.

### "Platform not found" Error

Make sure you:
1. Have `openai_tts` (not `openai`) as the platform
2. Restarted Home Assistant after editing configuration.yaml
3. Have the correct indentation in YAML

### Cost Concerns

Set a usage limit in OpenAI dashboard:
1. Go to https://platform.openai.com/settings/organization/limits
2. Set a monthly budget (e.g., $2)
3. You'll get email alerts if you approach the limit

## Monitoring Usage

Check your usage:
1. Go to https://platform.openai.com/usage
2. See how much you've used
3. For TTS, look under "Audio generation"

Most users spend $0.05-0.15 per month for daily morning announcements.

## Alternative: Mix Languages

If you want some messages in English and some in Swedish, just change the message language:

```yaml
# Swedish
message: "Klockan är nu 7."

# English
message: "The time is now 7 o'clock."
```

OpenAI automatically switches pronunciation!

## Next Steps

1. Let it run for a week and see how your kids respond
2. Adjust times/messages based on what works
3. Try different voices to see which one they listen to best
4. Add more automations as needed (bedtime reminders, homework time, etc.)

## Funny Ideas to Try

Since AI voices are more flexible:

```yaml
# Extra enthusiastic Monday morning
- service: tts.openai_say
  data:
    message: "God morgon! Det är måndag! Ny vecka, nya möjligheter! Dags att vakna!"

# Friday celebration
- service: tts.openai_say
  data:
    message: "Det är fredag! Sista dagen innan helgen! Men först måste vi hinna till skolan!"

# Gentle wake-up with countdown
- service: tts.openai_say
  data:
    message: "God morgon sötnos. Klockan är 7. Du har en hel timme på dig innan vi måste gå."
```

Different voices can make different announcements more fun!
