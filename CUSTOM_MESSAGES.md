# Custom Voice Messages Guide

How to add your own custom messages to the time reminder automations.

## Simple Custom Messages

You can add ANY custom message you want! Here are examples:

### Method 1: Add to Existing Time Announcements

Edit your automation and add extra TTS calls:

```yaml
automation:
  - id: morning_reminder_swedish_0730
    alias: "Morgonpåminnelse - 07:30"
    trigger:
      - platform: time
        at: "07:30:00"
    condition:
      - condition: time
        weekday:
          - mon
          - tue
          - wed
          - thu
          - fri
    action:
      # Announce the time
      - service: script.announce_time_and_countdown_swedish
        data:
          speaker: media_player.living_room_speaker
          target_time: "08:00"

      # Wait a moment
      - delay:
          seconds: 3

      # ADD YOUR CUSTOM MESSAGE HERE
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "Kom ihåg att borsta tänderna och packa matlådan!"
```

### Method 2: Create Separate Custom Reminders

Add completely new automations for specific tasks:

```yaml
# Breakfast reminder
automation:
  - id: breakfast_reminder
    alias: "Frukoståminnelse"
    trigger:
      - platform: time
        at: "07:10:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kitchen_mini
        data:
          message: "Dags för frukost! Kom till köket nu."

# Brush teeth reminder
  - id: brush_teeth_reminder
    alias: "Borsta tänderna påminnelse"
    trigger:
      - platform: time
        at: "07:20:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.bathroom_speaker
        data:
          message: "Glöm inte att borsta tänderna ordentligt!"

# Get dressed reminder
  - id: get_dressed_reminder
    alias: "Klä på dig påminnelse"
    trigger:
      - platform: time
        at: "07:35:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "Dags att klä på sig och ta på skorna!"

# Final departure warning
  - id: final_departure_reminder
    alias: "Sista avgångspåminnelse"
    trigger:
      - platform: time
        at: "07:57:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "Tre minuter kvar! Ta din jacka och skolväska och kom till dörren nu!"
```

## Common Custom Message Ideas

### Morning Routine Tasks

```yaml
# Wake up gently
message: "God morgon älskling! Dags att vakna och börja dagen."

# Breakfast
message: "Frukosten är klar! Kom till köket nu."

# Hygiene
message: "Tvättar du ansiktet och borstar tänderna?"

# Getting dressed
message: "Glöm inte att ta på dig sockar och skor!"

# Pack bag
message: "Är din skolväska packad? Kolla att du har allt!"

# Lunch box
message: "Kom ihåg matlådan i kylskåpet!"

# Weather reminder
message: "Det regnar idag, glöm inte regnkläder!"

# Jacket
message: "Är du klädd? Glöm inte jackan!"
```

### Motivational Messages

```yaml
message: "Du hinner! Bara lugn och gör en sak i taget."

message: "Bra jobbat hittills! Fortsätt så!"

message: "Du är nästan klar! Bara några saker kvar."

message: "Fantastiskt! Nu är det bara att ta på skorna och gå!"
```

### Fun/Encouraging Messages

```yaml
message: "Hej hej! Dags att vakna, sover du fortfarande?"

message: "Bing bong! Frukostklockan ringer!"

message: "Turbo-tid! Vi måste skynda oss lite nu!"

message: "Superspeedy-läge aktiverat! 10 minuter kvar!"
```

### Specific Kid Names

```yaml
message: "Emma! Dags att vakna!"

message: "Oskar, har du packat din skolväska?"

message: "Lisa och Emil, kom till köket för frukost!"
```

## Advanced: Different Messages for Different Kids

Use different speakers in different rooms:

```yaml
# Emma's room (Google Mini)
automation:
  - id: emma_wake_up
    alias: "Emma - Väck upp"
    trigger:
      - platform: time
        at: "07:00:00"
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.emmas_room_mini
        data:
          message: "God morgon Emma! Dags att vakna."

# Oskar's room (Google Mini)
  - id: oskar_wake_up
    alias: "Oskar - Väck upp"
    trigger:
      - platform: time
        at: "07:05:00"  # Oskar gets 5 extra minutes
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.oskars_room_mini
        data:
          message: "God morgon Oskar! Upp ur sängen nu!"
```

## Advanced: Announce to Multiple Speakers at Once

Make the same announcement in multiple rooms:

```yaml
action:
  - service: tts.openai_say
    target:
      entity_id:
        - media_player.kids_room_mini
        - media_player.kitchen_speaker
        - media_player.bathroom_mini
    data:
      message: "5 minuter kvar! Alla till hallen!"
```

## Advanced: Random Variety Messages

Keep it fresh so kids don't tune out:

```yaml
action:
  - service: tts.openai_say
    target:
      entity_id: media_player.kids_room_mini
    data:
      message: >
        {% set messages = [
          "God morgon! Dags att vakna och börja dagen!",
          "Hej där! Har du sovit gott? Nu är det dags att gå upp!",
          "Godmorgon godmorgon! Solen är uppe och det är dags för dig med!",
          "Vakna vakna! En ny dag väntar!"
        ] %}
        {{ messages | random }}
```

## Advanced: Weather-Based Messages

Announce different things based on weather:

```yaml
# Requires weather integration in Home Assistant
action:
  - service: tts.openai_say
    target:
      entity_id: media_player.living_room_speaker
    data:
      message: >
        {% if states('weather.home') == 'rainy' %}
          Det regnar idag! Glöm inte regnkläder och paraply!
        {% elif states('weather.home') == 'snowy' %}
          Det snöar! Ta på dig varma kläder och vinterjacka!
        {% elif state_attr('weather.home', 'temperature') < 0 %}
          Det är kallt ute! Kom ihåg mössa och vantar!
        {% else %}
          Vädret är fint idag! Ha en bra dag!
        {% endif %}
```

## Advanced: Day-Specific Messages

Different messages for different days:

```yaml
action:
  - service: tts.openai_say
    target:
      entity_id: media_player.kids_room_mini
    data:
      message: >
        {% set day = now().weekday() %}
        {% if day == 0 %}
          God morgon! Det är måndag, ny vecka börjar!
        {% elif day == 1 %}
          Tisdag idag! Glöm inte att ni har idrott!
        {% elif day == 2 %}
          Onsdag, halvvägs genom veckan!
        {% elif day == 3 %}
          Torsdag! Snart är det helg!
        {% elif day == 4 %}
          Fredag! Sista dagen innan helgen!
        {% endif %}

# Or specific reminders for specific days
  - id: tuesday_gym_reminder
    alias: "Tisdagspåminnelse - Idrott"
    trigger:
      - platform: time
        at: "07:20:00"
    condition:
      - condition: time
        weekday: [tue]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "Idag är det idrott! Glöm inte gympapåsen!"
```

## Testing Custom Messages

Test any message instantly from your phone:

1. Open Home Assistant app
2. Go to **Developer Tools** → **Services**
3. Select `tts.openai_say`
4. Fill in:
```yaml
entity_id: media_player.your_mini_speaker
message: "Din egen text här!"
```
5. Click **Call Service**

## Tips for Good Messages

### DO:
- Keep messages short and clear
- Use specific instructions ("Take your bag" not "Get ready")
- Match the urgency to the time (calm early, urgent late)
- Use positive, encouraging language
- Test the timing - kids need time to do what you ask

### DON'T:
- Make messages too long (kids will tune out)
- Use complicated words
- Give multiple instructions in one message
- Nag too much (they'll start ignoring it)

## Volume Control

Set different volumes for different times:

```yaml
action:
  # Quiet wake-up at 7:00
  - service: media_player.volume_set
    target:
      entity_id: media_player.kids_room_mini
    data:
      volume_level: 0.3  # 30% volume

  - service: tts.openai_say
    target:
      entity_id: media_player.kids_room_mini
    data:
      message: "God morgon, dags att vakna..."

  # Louder urgent reminder at 7:55
  - service: media_player.volume_set
    target:
      entity_id: media_player.living_room_speaker
    data:
      volume_level: 0.7  # 70% volume

  - service: tts.openai_say
    target:
      entity_id: media_player.living_room_speaker
    data:
      message: "5 minuter kvar! Alla till dörren NU!"
```

## Examples: Complete Morning Routine

Here's a full example with custom messages at each step:

```yaml
automation:
  # 7:00 - Gentle wake up
  - id: wake_up_0700
    alias: "07:00 - Väck upp"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.kids_room_mini
        data:
          volume_level: 0.3
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "God morgon! Dags att vakna. Du har en timme på dig."

  # 7:10 - Breakfast call
  - id: breakfast_0710
    alias: "07:10 - Frukost"
    trigger:
      - platform: time
        at: "07:10:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kitchen_speaker
        data:
          message: "Frukost! Kom till köket nu så att ni hinner äta ordentligt."

  # 7:25 - Get dressed
  - id: get_dressed_0725
    alias: "07:25 - Klä på dig"
    trigger:
      - platform: time
        at: "07:25:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "Klä på dig nu! Skor och jacka också. 35 minuter kvar."

  # 7:40 - Brush teeth
  - id: brush_teeth_0740
    alias: "07:40 - Tänder"
    trigger:
      - platform: time
        at: "07:40:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.bathroom_mini
        data:
          message: "Borsta tänderna ordentligt! Minst 2 minuter."

  # 7:50 - Final check
  - id: final_check_0750
    alias: "07:50 - Kolla väskan"
    trigger:
      - platform: time
        at: "07:50:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "Kolla att du har allt! Skolväska, matlåda, jacka, mössa. 10 minuter kvar!"

  # 7:57 - Last call
  - id: last_call_0757
    alias: "07:57 - Sista varningen"
    trigger:
      - platform: time
        at: "07:57:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.living_room_speaker
        data:
          volume_level: 0.7
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "TRE MINUTER! Alla till hallen NU! Vi måste gå om tre minuter!"
```

## Quick Examples You Can Copy/Paste

Just change the `entity_id` and `message`:

```yaml
# Simple custom reminder
- service: tts.openai_say
  target:
    entity_id: media_player.your_mini_speaker
  data:
    message: "Your message here in Swedish!"

# With volume control
- service: media_player.volume_set
  target:
    entity_id: media_player.your_mini_speaker
  data:
    volume_level: 0.5
- service: tts.openai_say
  target:
    entity_id: media_player.your_mini_speaker
  data:
    message: "Your message here!"

# Multiple speakers
- service: tts.openai_say
  target:
    entity_id:
      - media_player.kitchen_mini
      - media_player.kids_room_mini
  data:
    message: "Same message to multiple rooms!"
```

## How to Add Your Custom Messages

1. Edit the automation file in Home Assistant
2. Find the time you want to add a message to
3. Add the TTS service call (see examples above)
4. Test it using Developer Tools → Services
5. Save and reload automations

That's it! You can add as many custom messages as you want.
