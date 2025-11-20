# Simple Deployment with Piper TTS (Free)

Step-by-step guide to deploy your morning routine using free Piper TTS.

## Step 1: Install Piper Add-on (2 minutes)

1. Open Home Assistant web interface
2. Click **Settings** (bottom left sidebar)
3. Click **Add-ons**
4. Click **Add-on Store** (bottom right)
5. Search for "**Piper**"
6. Click **Piper** (should be "Piper - Text to speech")
7. Click **Install** (wait 1-2 minutes)
8. Click **Start**
9. Enable **Start on boot**
10. Enable **Show in sidebar** (optional)

## Step 2: Configure Piper for Swedish

1. Still in the Piper add-on page, click **Configuration** tab
2. In the configuration, you should see options for language/voice
3. Or we'll configure it in Home Assistant directly (next step)

## Step 3: Add Piper to Home Assistant Configuration

### Using File Editor:

1. In sidebar, click **Settings** → **Add-ons**
2. If you don't have File Editor:
   - **Add-on Store** → Search "**File editor**"
   - Install → Start → Enable "Show in sidebar"
3. Click **File editor** in sidebar
4. Open **configuration.yaml**
5. Scroll to bottom and add:

```yaml
# Piper TTS - Free Swedish text-to-speech
tts:
  - platform: tts.piper
    language: sv_SE
    voice: sv_SE-nst-medium
```

6. Click **💾 Save** (top right)

### Restart Home Assistant:

1. **Settings** → **System**
2. Click three dots (**⋮**) top right → **Restart**
3. Click **Restart Home Assistant**
4. Wait 2 minutes

## Step 4: Test Piper TTS

1. Click **Developer Tools** (bottom left)
2. Click **Services** tab
3. Service: `tts.speak`
4. Target: Click **Choose entity** → select `media_player.kocken`
5. In **Service data**, paste:

```yaml
message: "Test från köket! Hör ni mig?"
media_player_entity_id: media_player.kocken
```

6. Click **Call Service**

**You should hear it from Kocken!** 🔊

### Test All Speakers:

```yaml
message: "Test från alla högtalare i huset!"
media_player_entity_id: media_player.party
```

## Step 5: Create Morning Automations

### Wake Up Novali (6:30 AM)

1. **Settings** → **Automations & Scenes**
2. Click **+ Create Automation** (bottom right)
3. Click **Create new automation**
4. Click three dots (**⋮**) → **Edit in YAML**
5. Delete everything and paste:

```yaml
alias: "06:30 - Novali vakna"
description: Wake up Novali at 6:30
trigger:
  - platform: time
    at: "06:30:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id: media_player.united
    data:
      volume_level: 0.3
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "God morgon Novali! Dags att vakna. En timme tills vi måste gå."
      media_player_entity_id: media_player.united
mode: single
```

6. Click **Save**
7. Name it: `06:30 - Novali vakna`

### Wake Up Isobel (6:35 AM)

Repeat the process with:

```yaml
alias: "06:35 - Isobel vakna"
description: Wake up Isobel at 6:35
trigger:
  - platform: time
    at: "06:35:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id:
        - media_player.kattniss
        - media_player.pussgurkan
    data:
      volume_level: 0.3
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "God morgon Isobel! Dags att vakna sötnos. 55 minuter tills vi måste gå."
      media_player_entity_id:
        - media_player.kattniss
        - media_player.pussgurkan
mode: single
```

### Breakfast Call (6:40 AM)

```yaml
alias: "06:40 - Frukost"
description: Breakfast announcement
trigger:
  - platform: time
    at: "06:40:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id:
        - media_player.kocken
        - media_player.kompis
    data:
      volume_level: 0.4
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "Frukost! Kom ner till köket nu."
      media_player_entity_id:
        - media_player.kocken
        - media_player.kompis
mode: single
```

### Get Dressed (7:05 AM)

```yaml
alias: "07:05 - Klä på er"
description: Get dressed reminder
trigger:
  - platform: time
    at: "07:05:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "25 minuter kvar! Upp till rummen och klä på er."
      media_player_entity_id: media_player.uppe
mode: single
```

### Final Prep (7:15 AM)

```yaml
alias: "07:15 - Sista förberedelser"
description: Final preparations
trigger:
  - platform: time
    at: "07:15:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id: media_player.nere
    data:
      volume_level: 0.5
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "15 minuter kvar! Ta på skor och jacka."
      media_player_entity_id: media_player.nere
mode: single
```

### 5 Minute Warning (7:25 AM) - ALL SPEAKERS

```yaml
alias: "07:25 - BRÅDSKANDE"
description: 5 minute urgent warning
trigger:
  - platform: time
    at: "07:25:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id: media_player.party
    data:
      volume_level: 0.8
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "5 MINUTER KVAR! ALLA TILL HALLEN OMEDELBART!"
      media_player_entity_id: media_player.party
mode: single
```

### 2 Minute Emergency (7:28 AM) - ALL SPEAKERS

```yaml
alias: "07:28 - NÖDSITUATION"
description: 2 minute emergency warning
trigger:
  - platform: time
    at: "07:28:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: media_player.volume_set
    target:
      entity_id: media_player.party
    data:
      volume_level: 0.9
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "TVÅ MINUTER! VI GÅR NU! ALLA TILL BILEN OMEDELBART!"
      media_player_entity_id: media_player.party
  - delay:
      seconds: 3
  - service: tts.speak
    target:
      entity_id: tts.piper
    data:
      message: "TVÅ MINUTER KVAR! VI MÅSTE GÅ NU!"
      media_player_entity_id: media_player.party
mode: single
```

## Step 6: Create Phone Dashboard

1. Click **Overview** (top left)
2. Click three dots (**⋮**) → **Edit Dashboard**
3. Click **+ Add Card**
4. Scroll down → **Manual**
5. Paste:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🏠 Morgonkontroll

  - type: horizontal-stack
    cards:
      - type: button
        name: Novali
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.speak
          target:
            entity_id: tts.piper
          service_data:
            message: "Novali, dags att gå upp!"
            media_player_entity_id: media_player.united

      - type: button
        name: Isobel
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.speak
          target:
            entity_id: tts.piper
          service_data:
            message: "Isobel, dags att vakna!"
            media_player_entity_id:
              - media_player.kattniss
              - media_player.pussgurkan

  - type: horizontal-stack
    cards:
      - type: button
        name: Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: tts.speak
          target:
            entity_id: tts.piper
          service_data:
            message: "Alla uppe, kom ner!"
            media_player_entity_id: media_player.uppe

      - type: button
        name: Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: tts.speak
          target:
            entity_id: tts.piper
          service_data:
            message: "Skynda på!"
            media_player_entity_id: media_player.nere

  - type: button
    name: "🚨 ÖVERALLT"
    icon: mdi:alarm-light
    tap_action:
      action: call-service
      service: tts.speak
      target:
        entity_id: tts.piper
      service_data:
        message: "ALLA TILL HALLEN! VI GÅR NU!"
        media_player_entity_id: media_player.party
```

6. Click **Save** → **Done**

## Step 7: Test Tomorrow Morning!

All automations are now active. They'll run automatically on weekdays.

### Manual Test Now:

1. **Settings** → **Automations & Scenes**
2. Find any automation
3. Click three dots (**⋮**) → **Run**

## Piper Voice Options

If you don't like the default voice, try others:

In **configuration.yaml**, change the voice:

```yaml
tts:
  - platform: tts.piper
    language: sv_SE
    voice: sv_SE-nst-medium  # Current choice
    # Try these alternatives:
    # voice: sv_SE-nst-low     # Faster, lower quality
```

Unfortunately, Piper only has 2 Swedish voices currently. If you want more variety, that's when OpenAI becomes worth it (6 different voices to choose from).

## Troubleshooting

**"Service not found: tts.speak"**
- Piper add-on isn't running
- Go to Settings → Add-ons → Piper → Start

**"Entity not found"**
- Check speaker names are correct
- Settings → Devices & Services → Entities → search "media_player"

**No sound:**
- Check speaker volume
- Try test in Developer Tools first
- Make sure speaker isn't playing something else

**Robotic/bad quality:**
- This is the trade-off for free TTS
- If kids don't respond well, switch to OpenAI (~1 SEK/month)

## Next Steps

After testing Piper for a few days:

**If it works great:** You're done! Free forever! 🎉

**If voice quality isn't good enough:**
- Switch to OpenAI TTS (just change service calls)
- I can give you the updated config
- Costs ~1 SEK/month for much better voices

## Quick Reference

**Test command:**
```yaml
service: tts.speak
target:
  entity_id: tts.piper
data:
  message: "Your message here"
  media_player_entity_id: media_player.party
```

**All your speakers:**
- `media_player.united` - Novali's room
- `media_player.kattniss` - Isobel's room
- `media_player.pussgurkan` - Parents' room
- `media_player.kocken` - Kitchen
- `media_player.kompis` - Living room
- `media_player.dobby` - Office
- `media_player.vision` - Movie room
- `media_player.uppe` - All upstairs
- `media_player.nere` - All downstairs
- `media_player.party` - ALL 7 speakers!

That's it! Your free morning routine is ready! 🎉
