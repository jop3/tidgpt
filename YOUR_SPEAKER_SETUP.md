# Your Custom Speaker Configuration

Based on your Google Cast devices, here are your exact speaker entity IDs.

## Your Speakers

### Individual Speakers (7 total)
- **Dobby** - `media_player.dobby` (Google Nest Mini)
- **Kattniss** - `media_player.kattniss` (Google Nest Mini)
- **Kocken** - `media_player.kocken` (Google Nest Hub - has screen!)
- **Kompis** - `media_player.kompis` (Google Nest Mini)
- **Pussgurkan** - `media_player.pussgurkan` (Google Home Mini)
- **United** - `media_player.united` (Google Nest Mini)
- **Vision** - `media_player.vision` (Google Nest Mini)

### Pre-Made Groups (4 total)
- **Nere** - `media_player.nere` (Downstairs group)
- **Uppe** - `media_player.uppe` (Upstairs group)
- **Tjejernas Rum** - `media_player.tjejernas_rum` (Girls' room group)
- **Party** - `media_player.party` (Party mode group)

### Other Cast Devices (Not for voice)
- SHIELD Android TV (not useful for announcements)
- Tv i Vardagsrum (Chromecast HD - not useful for voice)

## Perfect Setup for Morning Routine!

Your groups make this SUPER easy! You already have "Uppe" and "Nere" which is perfect for escalation.

## Broadcast Everywhere Script (Copy-Paste Ready)

Add this to your `scripts.yaml`:

```yaml
# Broadcast to ALL speakers in house
announce_everywhere:
  alias: "Meddela överallt"
  description: "Skicka meddelande till ALLA högtalare i huset"
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
          - media_player.dobby
          - media_player.kattniss
          - media_player.kocken
          - media_player.kompis
          - media_player.pussgurkan
          - media_player.united
          - media_player.vision
      data:
        volume_level: "{{ volume | default(0.7) }}"

    # Announce to all speakers
    - service: tts.openai_say
      target:
        entity_id:
          - media_player.dobby
          - media_player.kattniss
          - media_player.kocken
          - media_player.kompis
          - media_player.pussgurkan
          - media_player.united
          - media_player.vision
      data:
        message: "{{ message }}"

# URGENT broadcast - MAX VOLUME, repeats twice
announce_everywhere_urgent:
  alias: "BRÅDSKANDE - Meddela överallt"
  description: "Brådskande meddelande till alla högtalare, högt och upprepas"
  fields:
    message:
      description: "Meddelandet att skicka"
      example: "ALLA TILL HALLEN NU!"
  sequence:
    # MAX VOLUME
    - service: media_player.volume_set
      target:
        entity_id:
          - media_player.dobby
          - media_player.kattniss
          - media_player.kocken
          - media_player.kompis
          - media_player.pussgurkan
          - media_player.united
          - media_player.vision
      data:
        volume_level: 0.8

    # First announcement
    - service: tts.openai_say
      target:
        entity_id:
          - media_player.dobby
          - media_player.kattniss
          - media_player.kocken
          - media_player.kompis
          - media_player.pussgurkan
          - media_player.united
          - media_player.vision
      data:
        message: "UPPMÄRKSAMHET! {{ message }}"

    # Wait 3 seconds
    - delay:
        seconds: 3

    # Repeat it!
    - service: tts.openai_say
      target:
        entity_id:
          - media_player.dobby
          - media_player.kattniss
          - media_player.kocken
          - media_player.kompis
          - media_player.pussgurkan
          - media_player.united
          - media_player.vision
      data:
        message: "{{ message }}"

# Use your existing GROUPS for easier targeting
announce_upstairs:
  alias: "Meddela uppe"
  description: "Skicka till alla högtalare på övervåningen"
  fields:
    message:
      description: "Meddelandet"
  sequence:
    - service: tts.openai_say
      target:
        entity_id: media_player.uppe
      data:
        message: "{{ message }}"

announce_downstairs:
  alias: "Meddela nere"
  description: "Skicka till alla högtalare på nedervåningen"
  fields:
    message:
      description: "Meddelandet"
  sequence:
    - service: tts.openai_say
      target:
        entity_id: media_player.nere
      data:
        message: "{{ message }}"

announce_girls_room:
  alias: "Meddela tjejernas rum"
  description: "Skicka till tjejernas rum"
  fields:
    message:
      description: "Meddelandet"
  sequence:
    - service: tts.openai_say
      target:
        entity_id: media_player.tjejernas_rum
      data:
        message: "{{ message }}"
```

## Smart Escalation Using Your Groups

Use your existing groups for progressive escalation:

```yaml
automation:
  # 7:00 - Just girls' room (quiet wake-up)
  - id: morning_girls_room_0700
    alias: "Morgon - Tjejernas rum 07:00"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.tjejernas_rum
        data:
          volume_level: 0.3
      - service: tts.openai_say
        target:
          entity_id: media_player.tjejernas_rum
        data:
          message: "God morgon! Dags att vakna. En timme tills vi måste gå."

  # 7:30 - Upstairs only (where bedrooms probably are)
  - id: morning_upstairs_0730
    alias: "Morgon - Uppe 07:30"
    trigger:
      - platform: time
        at: "07:30:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.uppe
        data:
          message: "30 minuter kvar! Klä på er och kom ner till köket."

  # 7:45 - Downstairs (kitchen/hall area)
  - id: morning_downstairs_0745
    alias: "Morgon - Nere 07:45"
    trigger:
      - platform: time
        at: "07:45:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.nere
        data:
          message: "15 minuter kvar! Kolla att ni har allt packat."

  # 7:55 - EVERYWHERE! (all speakers)
  - id: morning_broadcast_0755
    alias: "Morgon - ÖVERALLT 07:55"
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
```

## Dashboard Panic Buttons (Your Speakers)

Add to your dashboard:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🚨 Snabbmeddelanden
      Skicka till olika delar av huset

  # Quick location buttons
  - type: horizontal-stack
    cards:
      - type: button
        name: Tjejernas rum
        icon: mdi:home-account
        tap_action:
          action: call-service
          service: script.announce_girls_room
          service_data:
            message: "Dags att gå upp nu!"

      - type: button
        name: Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: script.announce_upstairs
          service_data:
            message: "Kom ner till köket!"

      - type: button
        name: Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: script.announce_downstairs
          service_data:
            message: "Skynda på lite!"

  # EMERGENCY buttons
  - type: horizontal-stack
    cards:
      - type: button
        name: "🚨 ALLA TILL HALLEN"
        icon: mdi:alarm-light
        tap_action:
          action: call-service
          service: script.announce_everywhere_urgent
          service_data:
            message: "ALLA TILL HALLEN OMEDELBART!"

      - type: button
        name: "🚨 VI GÅR NU"
        icon: mdi:run-fast
        tap_action:
          action: call-service
          service: script.announce_everywhere_urgent
          service_data:
            message: "VI GÅR NU! ALLA TILL BILEN!"

  # Fun "where are you" buttons
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
```

## Suggested Room-Based Routine

Based on typical Swedish house layout (educated guess!):

**Guess at your layout:**
- **Uppe (Upstairs)**: Bedrooms including "Tjejernas rum"
- **Nere (Downstairs)**: Kitchen, living room, hall

**Suggested speakers for each area** (you tell me if I'm wrong!):
- **Tjejernas rum** (Girls' room): Uses the group `media_player.tjejernas_rum`
- **Kitchen** (Köket): Maybe `media_player.kocken` (the Nest Hub with screen)?
- **Living room/Hall**: Maybe `media_player.dobby`, `media_player.united`, or others?
- **Bathroom**: Maybe `media_player.kompis` or `media_player.vision`?

## Smart Morning Flow Using Your Setup

```yaml
# 7:00 - Girls' room wake-up (gentle, quiet)
entity_id: media_player.tjejernas_rum
volume: 0.3
message: "God morgon! Dags att vakna."

# 7:10 - Kitchen call (pull them downstairs)
entity_id: media_player.kocken  # If this is in kitchen
message: "Frukost! Kom ner till köket."

# 7:30 - Upstairs reminder (back to rooms to get dressed)
entity_id: media_player.uppe
message: "30 minuter kvar. Klä på er och gör i ordning."

# 7:45 - Downstairs (final prep area)
entity_id: media_player.nere
message: "15 minuter! Kolla väskan och ta på skorna."

# 7:55 - EVERYWHERE (can't miss this)
entity_id: ALL 7 speakers
volume: 0.8
message: "5 MINUTER! ALLA TILL HALLEN!"
```

## Cool Feature: Use "Kocken" (Nest Hub)

Since Kocken is a Nest Hub with a **screen**, you could also:
- Show visual timers
- Display checklists
- Show pictures ("This is what a made bed looks like!")

But voice announcements work great on it too!

## Questions for Perfect Setup

To customize your routine perfectly, tell me:

1. **Where is each speaker located?**
   - Example: "Dobby = hall, Kattniss = bathroom, Kocken = kitchen"

2. **What's in the "Tjejernas rum" group?**
   - Is this multiple speakers or one room with multiple kids?

3. **Which areas are "Uppe" and "Nere"?**
   - Upstairs bedrooms / Downstairs common areas?

4. **What time do you need to leave?**
   - 8:00? 8:15? I'll adjust the schedule

## Testing Your Setup

Test each speaker works:

```yaml
# Test individual speakers
service: tts.openai_say
data:
  entity_id: media_player.dobby
  message: "Test från Dobby"

# Test groups
service: tts.openai_say
data:
  entity_id: media_player.uppe
  message: "Test från alla högtalare uppe"

# Test broadcast all
service: script.announce_everywhere
data:
  message: "Test från ALLA högtalare"
  volume: 0.5
```

## Your Groups Are Perfect!

You already have the groups set up, which makes this SO much easier:
- ✅ **media_player.uppe** - Upstairs announcements
- ✅ **media_player.nere** - Downstairs announcements
- ✅ **media_player.tjejernas_rum** - Direct to girls' room
- ✅ **media_player.party** - Fun for parties! (play music everywhere)

Most people have to create these manually. You're already ahead!

Want me to create the complete morning routine once you tell me which speaker is in which room?
