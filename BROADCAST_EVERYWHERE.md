# Broadcast Everywhere - Panic Button

Emergency override that announces to ALL speakers at once when kids
are hiding, not responding, or you need to make sure everyone hears.

## The Problem

Sometimes kids:
- Hide in their room with door closed
- Don't hear announcements
- Are in an unexpected location
- Are playing and tuning out the reminders

**Solution:** BROADCAST TO EVERY SPEAKER IN THE HOUSE!

## Setup: Define Your Speaker Group

First, create a group of all your speakers in `configuration.yaml`:

```yaml
# Add this to configuration.yaml
media_player:
  - platform: group
    name: "All Speakers"
    unique_id: all_house_speakers
    entities:
      - media_player.kids_room_mini
      - media_player.kitchen_speaker
      - media_player.living_room_speaker
      - media_player.bathroom_mini
      - media_player.bedroom_speaker
      # Add ALL your speakers here!
```

**Or** manually list them (no group needed):

```yaml
# Just define them directly in automations
entity_id:
  - media_player.kids_room_mini
  - media_player.kitchen_speaker
  - media_player.living_room_speaker
  - media_player.bathroom_mini
  - media_player.parents_room_speaker
  # Add all your speakers
```

## Script: Broadcast to All Speakers

Create a reusable script:

```yaml
# Add to scripts.yaml
script:
  announce_everywhere:
    alias: "Meddela överallt"
    description: "Skicka meddelande till ALLA högtalare"
    fields:
      message:
        description: "Meddelandet att skicka"
        example: "ALLA TILL HALLEN NU!"
      volume:
        description: "Volym (0.0-1.0)"
        example: 0.7
    sequence:
      # Set volume on all speakers
      - service: media_player.volume_set
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            - media_player.bathroom_mini
            # ADD YOUR SPEAKERS HERE
        data:
          volume_level: "{{ volume | default(0.7) }}"

      # Announce to all speakers
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            - media_player.bathroom_mini
            # ADD YOUR SPEAKERS HERE
        data:
          message: "{{ message }}"

  # Quick urgent broadcast
  announce_everywhere_urgent:
    alias: "BRÅDSKANDE - Meddela överallt"
    description: "Brådskande meddelande till alla högtalare"
    fields:
      message:
        description: "Meddelandet att skicka"
        example: "ALLA TILL HALLEN NU!"
    sequence:
      # MAX VOLUME
      - service: media_player.volume_set
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            # ADD YOUR SPEAKERS HERE
        data:
          volume_level: 0.8

      # Announce with urgency
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            # ADD YOUR SPEAKERS HERE
        data:
          message: "UPPMÄRKSAMHET! {{ message }}"

      # Wait 3 seconds
      - delay:
          seconds: 3

      # Repeat it!
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            # ADD YOUR SPEAKERS HERE
        data:
          message: "{{ message }}"
```

## Dashboard Panic Buttons

Add these to your dashboard for quick access from your phone:

```yaml
# Add to your dashboard
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🚨 Överallt-meddelanden
      Skicka till ALLA högtalare

  - type: horizontal-stack
    cards:
      # Quick urgent messages
      - type: button
        name: "ALLA TILL HALLEN!"
        icon: mdi:alarm-light
        tap_action:
          action: call-service
          service: script.announce_everywhere_urgent
          service_data:
            message: "ALLA TILL HALLEN OMEDELBART!"
        hold_action:
          action: none

      - type: button
        name: "VI GÅR NU!"
        icon: mdi:run-fast
        tap_action:
          action: call-service
          service: script.announce_everywhere_urgent
          service_data:
            message: "VI GÅR NU! ALLA TILL BILEN!"

  - type: horizontal-stack
    cards:
      - type: button
        name: "VAR ÄR NI?"
        icon: mdi:account-question
        tap_action:
          action: call-service
          service: script.announce_everywhere
          service_data:
            message: "Var är ni? Svara mig nu!"
            volume: 0.6

      - type: button
        name: "KOM HIT NU"
        icon: mdi:phone-alert
        tap_action:
          action: call-service
          service: script.announce_everywhere
          service_data:
            message: "Jag har sagt det tre gånger. Kom hit NU!"
            volume: 0.7

  # Custom message input
  - type: entities
    entities:
      - input_text.broadcast_message
    title: Eget meddelande

  - type: button
    name: "Skicka eget meddelande"
    icon: mdi:bullhorn
    tap_action:
      action: call-service
      service: script.announce_everywhere
      service_data:
        message: "{{ states('input_text.broadcast_message') }}"
        volume: 0.7
```

## Input Text for Custom Messages

Add this to `configuration.yaml`:

```yaml
input_text:
  broadcast_message:
    name: Meddelande att skicka överallt
    initial: "Kom hit nu!"
    max: 200
```

Now you can type any message on your phone and broadcast it!

## Automated Broadcast Escalation

Add broadcast to critical time slots:

```yaml
automation:
  # Final 5-minute warning - EVERYWHERE
  - id: broadcast_final_warning
    alias: "🚨 Sista varningen - ÖVERALLT"
    trigger:
      - platform: time
        at: "07:55:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: script.announce_everywhere_urgent
        data:
          message: "5 MINUTER KVAR! ALLA TILL HALLEN OMEDELBART!"

  # 2-minute "we're leaving NOW" - MAX VOLUME EVERYWHERE
  - id: broadcast_leaving_now
    alias: "🚨 Vi åker - ÖVERALLT"
    trigger:
      - platform: time
        at: "07:58:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: all  # Or list all speakers
        data:
          volume_level: 0.9  # LOUD!

      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kids_room_mini
            - media_player.kitchen_speaker
            - media_player.living_room_speaker
            - media_player.bathroom_mini
            # ALL SPEAKERS
        data:
          message: "TVÅ MINUTER! VI GÅR NU! ALLA TILL BILEN OMEDELBART!"
```

## Escalation Strategy

Use room-based announcements normally, then escalate to broadcast:

```yaml
# 7:45 - Normal announcement (hall only)
- service: tts.openai_say
  target:
    entity_id: media_player.living_room_speaker
  data:
    message: "15 minuter kvar. Kom till hallen."

# 7:50 - Still just hall
- service: tts.openai_say
  target:
    entity_id: media_player.living_room_speaker
  data:
    message: "10 minuter! Kom till hallen nu!"

# 7:55 - BROADCAST EVERYWHERE
- service: script.announce_everywhere_urgent
  data:
    message: "5 MINUTER KVAR! ALLA TILL HALLEN NU!"

# 7:58 - BROADCAST EVERYWHERE MAX VOLUME
- service: script.announce_everywhere_urgent
  data:
    message: "VI GÅR NU! ALLA TILL BILEN OMEDELBART!"
```

## Different Urgency Levels

Create multiple broadcast scripts:

```yaml
script:
  # Normal broadcast (60% volume)
  broadcast_normal:
    sequence:
      - service: media_player.volume_set
        target:
          entity_id: all
        data:
          volume_level: 0.6
      - service: tts.openai_say
        target:
          entity_id: [all speakers]
        data:
          message: "{{ message }}"

  # Urgent broadcast (70% volume)
  broadcast_urgent:
    sequence:
      - service: media_player.volume_set
        target:
          entity_id: all
        data:
          volume_level: 0.7
      - service: tts.openai_say
        target:
          entity_id: [all speakers]
        data:
          message: "UPPMÄRKSAMHET! {{ message }}"

  # EMERGENCY broadcast (90% volume, repeats twice)
  broadcast_emergency:
    sequence:
      - service: media_player.volume_set
        target:
          entity_id: all
        data:
          volume_level: 0.9
      - service: tts.openai_say
        target:
          entity_id: [all speakers]
        data:
          message: "BRÅDSKANDE! {{ message }}"
      - delay:
          seconds: 3
      - service: tts.openai_say
        target:
          entity_id: [all speakers]
        data:
          message: "{{ message }}"
```

## Phone Widget Quick Actions

Add to your Home Assistant phone widget:

1. "Broadcast: Alla till hallen"
2. "Broadcast: Vi går nu"
3. "Broadcast: Var är ni?"

Tap from your lock screen!

## Voice Control

If you have Google Assistant connected to HA:

"Hey Google, run broadcast urgent message"
"Hey Google, tell everyone to come to the hall"

## Example Use Cases

### Hiding in bedroom
```yaml
message: "Jag vet att ni är där inne! Kom ut NU!"
```

### Not responding
```yaml
message: "Jag har sagt det tre gånger. Om ni inte kommer om 30 sekunder blir det inga dataspel ikväll!"
```

### Playing outside/headphones on
```yaml
volume: 0.9
message: "KAN NI HÖRA MIG? ALLA IN I HUSET NU!"
```

### Emergency
```yaml
message: "NÖDSITUATION! Alla till köket OMEDELBART!"
```

## Testing Your Speaker List

Test that all speakers work:

```yaml
service: script.announce_everywhere
data:
  message: "Test. Kan ni höra detta i alla rum?"
  volume: 0.5
```

Walk around your house and verify you hear it everywhere.

## Pro Tips

### 1. Progressive Escalation
Start with room-specific, escalate to broadcast:
- 7:45: Hall speaker only
- 7:50: Hall + nearby speakers
- 7:55: ALL SPEAKERS

### 2. Different Messages for Different Situations
- **Can't find kids**: "Var är ni? Kom fram nu!"
- **Running late**: "VI ÄR SENA! ALLA TILL BILEN NU!"
- **Not listening**: "Jag har sagt det tre gånger. Kom hit NU!"

### 3. Visual + Audio
Combine with lights flashing:
```yaml
- service: light.turn_on
  target:
    entity_id: light.kids_room
  data:
    flash: long
- service: script.announce_everywhere_urgent
  data:
    message: "ALLA TILL HALLEN!"
```

### 4. Repeat Important Messages
For critical announcements, say it twice:
```yaml
- service: script.announce_everywhere
  data:
    message: "5 minuter kvar!"
- delay:
    seconds: 3
- service: script.announce_everywhere
  data:
    message: "Jag sa 5 minuter kvar! Alla till hallen!"
```

### 5. Don't Overuse It
Keep broadcast for:
- Final urgent reminders (last 5 min)
- Emergency situations
- When kids aren't responding
- When you can't find them

If you broadcast everything, kids tune it out!

## Finding Your Speakers

To get YOUR actual speaker entity IDs, do this:

1. Open Home Assistant app
2. Go to **Developer Tools** → **States**
3. Type "media_player" in the filter
4. You'll see all your speakers like:
   - `media_player.sovrum_mini`
   - `media_player.kok_speaker`
   - `media_player.vardagsrum`

5. Copy those exact names into the scripts above

Or just tell me what Google Home devices you have and where they are, and I'll write the exact configuration for you!

## Quick Copy-Paste Template

Replace `media_player.YOURNAME` with your actual speakers:

```yaml
# Your speakers list - update this once, use everywhere
script:
  broadcast_all:
    sequence:
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.SPEAKER1
            - media_player.SPEAKER2
            - media_player.SPEAKER3
            - media_player.SPEAKER4
        data:
          message: "{{ message }}"
          volume: "{{ volume | default(0.7) }}"
```

Want me to create the exact configuration once you send me your speaker names?
