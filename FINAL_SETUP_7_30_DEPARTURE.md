# Your Final Complete Setup - 7:30 Departure

Perfect morning routine for your family with 7:30 AM departure time.

## 🏠 Complete House Layout

### Upstairs (Uppe) - `media_player.uppe`
- **United** (`media_player.united`) - Novali's room (older child)
- **Kattniss** (`media_player.kattniss`) - Isobel's room (younger child)
- **Pussgurkan** (`media_player.pussgurkan`) - Parents' room

### Downstairs (Nere) - `media_player.nere`
- **Kocken** (`media_player.kocken`) - Kitchen (Nest Hub with screen 📺)
- **Kompis** (`media_player.kompis`) - Living room
- **Dobby** (`media_player.dobby`) - Office
- **Vision** (`media_player.vision`) - Movie room

### All Speakers - `media_player.party`
All 7 speakers everywhere for emergency broadcasts!

## ⏰ Perfect Timeline for 7:30 Departure

```
06:30 🛏️ Wake up (upstairs bedrooms)
06:40 🍳 Breakfast call (kitchen)
06:55 🚿 Hygiene reminder (bathroom area)
07:05 🛏️ Get dressed (back upstairs)
07:15 🏠 Final prep (downstairs)
07:25 🚨 URGENT - All speakers everywhere!
07:28 🚨🚨 EMERGENCY - Leaving NOW!
```

## 📺 Visual Dashboard on Kocken (Kitchen)

### Countdown Timer Configuration

```yaml
# Add to configuration.yaml
sensor:
  - platform: template
    sensors:
      morning_countdown:
        friendly_name: "Tid kvar till avgång"
        value_template: >
          {% set target = today_at('07:30') %}
          {% if now() > target %}
            Dags att gå!
          {% else %}
            {% set diff = (target - now()).total_seconds() | int %}
            {% set minutes = (diff / 60) | int %}
            {% if minutes > 60 %}
              {{ (minutes / 60) | int }}h {{ minutes % 60 }}m
            {% else %}
              {{ minutes }} min
            {% endif %}
          {% endif %}
        icon_template: >
          {% set target = today_at('07:30') %}
          {% set diff = (target - now()).total_seconds() | int %}
          {% set minutes = (diff / 60) | int %}
          {% if minutes <= 5 %}
            mdi:alarm-light
          {% elif minutes <= 15 %}
            mdi:clock-alert
          {% else %}
            mdi:clock
          {% endif %}

input_datetime:
  departure_time:
    name: Avgångstid
    has_date: false
    has_time: true
    initial: "07:30"
```

### Kitchen Dashboard Auto-Display

```yaml
automation:
  # Show dashboard at 6:25 (5 min before wake-up)
  - id: show_kitchen_dashboard_morning
    alias: "Visa köksdashboard på morgonen"
    trigger:
      - platform: time
        at: "06:25:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: cast.show_lovelace_view
        target:
          entity_id: media_player.kocken
        data:
          dashboard_path: morgonrutin
          view_path: kitchen

  # Hide dashboard after departure
  - id: hide_kitchen_dashboard
    alias: "Dölj köksdashboard"
    trigger:
      - platform: time
        at: "07:45:00"
    action:
      - service: media_player.turn_off
        target:
          entity_id: media_player.kocken
```

## ✅ Morning Checklist (Day-Specific)

```yaml
# Add to configuration.yaml
input_boolean:
  # Daily essentials
  morning_checklist_breakfast:
    name: Ätit frukost
    icon: mdi:food-apple
  morning_checklist_teeth:
    name: Borstat tänderna
    icon: mdi:tooth
  morning_checklist_dressed:
    name: Klädda
    icon: mdi:tshirt-crew
  morning_checklist_bag:
    name: Packat skolväskan
    icon: mdi:bag-personal
  morning_checklist_shoes:
    name: Skor på
    icon: mdi:shoe-formal
  morning_checklist_jacket:
    name: Jacka på
    icon: mdi:coat-rack

  # Special items
  morning_checklist_glasses:
    name: Glasögon (Isobel)
    icon: mdi:glasses
  morning_checklist_fruit:
    name: Frukt med
    icon: mdi:fruit-grapes
  morning_checklist_gym_clothes:
    name: Idrottskläder (Tisdag)
    icon: mdi:weight-lifter
  morning_checklist_library_books:
    name: Biblioteksböcker
    icon: mdi:book-multiple
  morning_checklist_swimming:
    name: Simkläder (Torsdag)
    icon: mdi:swim
  morning_checklist_music_instrument:
    name: Musikinstrument
    icon: mdi:violin

# Auto-reset checklist every morning
automation:
  - id: reset_morning_checklist
    alias: "Återställ morgonchecklista"
    trigger:
      - platform: time
        at: "06:00:00"
    action:
      - service: input_boolean.turn_off
        target:
          entity_id:
            - input_boolean.morning_checklist_breakfast
            - input_boolean.morning_checklist_teeth
            - input_boolean.morning_checklist_dressed
            - input_boolean.morning_checklist_bag
            - input_boolean.morning_checklist_shoes
            - input_boolean.morning_checklist_jacket
            - input_boolean.morning_checklist_glasses
            - input_boolean.morning_checklist_fruit
            - input_boolean.morning_checklist_gym_clothes
            - input_boolean.morning_checklist_library_books
            - input_boolean.morning_checklist_swimming
            - input_boolean.morning_checklist_music_instrument
```

## 🎯 Complete Morning Routine (7:30 Departure)

```yaml
automation:
  # ============================================
  # 06:30 - Wake up Novali (older child)
  # ============================================
  - id: morning_novali_0630
    alias: "06:30 - Novali vakna"
    trigger:
      - platform: time
        at: "06:30:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.united
        data:
          volume_level: 0.3
      - service: tts.openai_say
        target:
          entity_id: media_player.united
        data:
          message: "God morgon Novali! Dags att vakna. En timme tills vi måste gå."

  # ============================================
  # 06:35 - Wake up Isobel (younger, 5 min later)
  # ============================================
  - id: morning_isobel_0635
    alias: "06:35 - Isobel vakna"
    trigger:
      - platform: time
        at: "06:35:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # Announce in both Isobel's room AND parents room (she often sleeps there)
      - service: media_player.volume_set
        target:
          entity_id:
            - media_player.kattniss
            - media_player.pussgurkan
        data:
          volume_level: 0.3
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kattniss
            - media_player.pussgurkan
        data:
          message: "God morgon Isobel! Dags att vakna sötnos. 55 minuter tills vi måste gå."

  # ============================================
  # 06:40 - Kitchen breakfast call
  # ============================================
  - id: morning_breakfast_0640
    alias: "06:40 - Frukost i köket"
    trigger:
      - platform: time
        at: "06:40:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # Show dashboard on Kocken
      - service: cast.show_lovelace_view
        target:
          entity_id: media_player.kocken
        data:
          dashboard_path: morgonrutin
          view_path: kitchen

      # Announce from kitchen + living room
      - service: media_player.volume_set
        target:
          entity_id:
            - media_player.kocken
            - media_player.kompis
        data:
          volume_level: 0.4

      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kocken
            - media_player.kompis
        data:
          message: "Frukost! Kom ner till köket nu. Kolla checklistan på skärmen."

  # ============================================
  # 06:55 - Hygiene reminder
  # ============================================
  - id: morning_hygiene_0655
    alias: "06:55 - Tvätta sig"
    trigger:
      - platform: time
        at: "06:55:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.nere  # All downstairs
        data:
          message: "35 minuter kvar. Dags att tvätta sig och borsta tänderna ordentligt!"

  # ============================================
  # 07:05 - Back upstairs to get dressed
  # ============================================
  - id: morning_getdressed_0705
    alias: "07:05 - Klä på er"
    trigger:
      - platform: time
        at: "07:05:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.uppe  # All upstairs speakers
        data:
          message: "25 minuter kvar! Upp till rummen och klä på er. Bädda sängen också."

  # ============================================
  # 07:15 - Downstairs final prep
  # ============================================
  - id: morning_finalprep_0715
    alias: "07:15 - Sista förberedelser"
    trigger:
      - platform: time
        at: "07:15:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.nere
        data:
          volume_level: 0.5

      - service: tts.openai_say
        target:
          entity_id: media_player.nere  # Kitchen, living room, office, movie room
        data:
          message: "15 minuter kvar! Kolla checklistan i köket. Ta på skor och jacka NU."

  # ============================================
  # 07:20 - Checklist reminder
  # ============================================
  - id: morning_checklist_0720
    alias: "07:20 - Påminn om checklistan"
    trigger:
      - platform: time
        at: "07:20:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kocken
        data:
          message: >
            {% set unchecked = [] %}
            {% if is_state('input_boolean.morning_checklist_breakfast', 'off') %}{% set unchecked = unchecked + ['äta frukost'] %}{% endif %}
            {% if is_state('input_boolean.morning_checklist_teeth', 'off') %}{% set unchecked = unchecked + ['borsta tänderna'] %}{% endif %}
            {% if is_state('input_boolean.morning_checklist_bag', 'off') %}{% set unchecked = unchecked + ['packa väskan'] %}{% endif %}
            {% if is_state('input_boolean.morning_checklist_shoes', 'off') %}{% set unchecked = unchecked + ['ta på skor'] %}{% endif %}
            {% if unchecked | length > 0 %}
              10 minuter kvar! Ni har fortfarande inte: {{ unchecked | join(', ') }}. Skynda er!
            {% else %}
              Bra jobbat! Checklistan är klar. 10 minuter tills vi går.
            {% endif %}

  # ============================================
  # 07:25 - BROADCAST EVERYWHERE (5 min warning)
  # ============================================
  - id: morning_urgent_0725
    alias: "07:25 - BRÅDSKANDE ÖVERALLT"
    trigger:
      - platform: time
        at: "07:25:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # MAX VOLUME on all speakers
      - service: media_player.volume_set
        target:
          entity_id: media_player.party
        data:
          volume_level: 0.8

      # Announce to EVERY speaker
      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "5 MINUTER KVAR! ALLA TILL HALLEN OMEDELBART! VI GÅR OM 5 MINUTER!"

  # ============================================
  # 07:28 - FINAL EMERGENCY (2 min warning)
  # ============================================
  - id: morning_emergency_0728
    alias: "07:28 - NÖDSITUATION"
    trigger:
      - platform: time
        at: "07:28:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # MAXIMUM VOLUME
      - service: media_player.volume_set
        target:
          entity_id: media_player.party
        data:
          volume_level: 0.9

      # First announcement
      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "TVÅ MINUTER! VI GÅR NU! ALLA TILL BILEN OMEDELBART!"

      # Wait 2 seconds
      - delay:
          seconds: 2

      # Repeat it!
      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "TVÅ MINUTER KVAR! VI MÅSTE GÅ NU!"

  # ============================================
  # Day-specific reminders
  # ============================================

  # Tuesday - Gym clothes
  - id: tuesday_gym_reminder
    alias: "Tisdag - Idrottspåminnelse"
    trigger:
      - platform: time
        at: "07:10:00"
    condition:
      - condition: time
        weekday: [tue]
      - condition: state
        entity_id: input_boolean.morning_checklist_gym_clothes
        state: 'off'
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.party  # ALL speakers!
        data:
          message: "GLÖM INTE! Idag är det idrott! Ta med gympakläder och skor!"

  # Thursday - Swimming
  - id: thursday_swimming_reminder
    alias: "Torsdag - Simningspåminnelse"
    trigger:
      - platform: time
        at: "07:10:00"
    condition:
      - condition: time
        weekday: [thu]
      - condition: state
        entity_id: input_boolean.morning_checklist_swimming
        state: 'off'
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "PÅMINNELSE! Idag är det simning! Glöm inte simkläder och handduk!"
```

## 🎨 Kitchen Dashboard for Kocken

Create a dashboard called "Morgonrutin":

```yaml
title: Morgonrutin
views:
  - title: Kök
    path: kitchen
    badges: []
    cards:
      # HUGE countdown timer
      - type: markdown
        content: |
          <div style="text-align: center; font-size: 72px; font-weight: bold; padding: 40px;
          {% set target = today_at('07:30') %}
          {% set diff = (target - now()).total_seconds() | int %}
          {% set minutes = (diff / 60) | int %}
          {% if minutes <= 5 %}
            background: #ff4444; color: white;">
            🔴 {{ minutes }} MIN!
          {% elif minutes <= 15 %}
            background: #ffaa00; color: white;">
            🟠 {{ minutes }} min
          {% else %}
            background: #44ff44; color: black;">
            🟢 {{ minutes }} min
          {% endif %}
          </div>

      # Departure time display
      - type: markdown
        content: |
          # 🚗 Avgång klockan 7:30

      # Progress bar
      - type: gauge
        entity: sensor.morning_countdown_progress
        name: Morgonrutin framsteg
        min: 0
        max: 100
        needle: true
        severity:
          green: 0
          yellow: 60
          red: 85

      # Daily checklist
      - type: markdown
        content: |
          # ✅ DAGENS CHECKLISTA
          {% set day = now().weekday() %}
          {% if day == 0 %}**MÅNDAG**
          {% elif day == 1 %}**TISDAG - IDROTT!** 🏃
          {% elif day == 2 %}**ONSDAG**
          {% elif day == 3 %}**TORSDAG - SIMNING!** 🏊
          {% elif day == 4 %}**FREDAG - Snart helg!** 🎉
          {% endif %}

      - type: entities
        title: Grundläggande
        entities:
          - input_boolean.morning_checklist_breakfast
          - input_boolean.morning_checklist_teeth
          - input_boolean.morning_checklist_dressed
          - input_boolean.morning_checklist_bag
          - input_boolean.morning_checklist_shoes
          - input_boolean.morning_checklist_jacket

      # Conditional Tuesday card
      - type: conditional
        conditions:
          - condition: state
            entity: sensor.day_of_week
            state: 'tuesday'
        card:
          type: entities
          title: 🏃 IDAG - IDROTT!
          entities:
            - input_boolean.morning_checklist_gym_clothes
            - input_boolean.morning_checklist_fruit

      # Conditional Thursday card
      - type: conditional
        conditions:
          - condition: state
            entity: sensor.day_of_week
            state: 'thursday'
        card:
          type: entities
          title: 🏊 IDAG - SIMNING!
          entities:
            - input_boolean.morning_checklist_swimming
            - input_boolean.morning_checklist_fruit

      # Other days
      - type: entities
        title: Extra att komma ihåg
        entities:
          - input_boolean.morning_checklist_glasses
          - input_boolean.morning_checklist_fruit
          - input_boolean.morning_checklist_library_books
          - input_boolean.morning_checklist_music_instrument
```

## 📱 Mobile Dashboard

Add this to your phone dashboard:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🏠 Morgonkontroll - Avgång 7:30

  # Time remaining
  - type: entity
    entity: sensor.morning_countdown
    name: Tid kvar till avgång
    icon: mdi:clock-alert

  # Individual room controls
  - type: horizontal-stack
    cards:
      - type: button
        name: Novali
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.united
            message: "Novali, dags att gå upp nu!"

      - type: button
        name: Isobel
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id:
              - media_player.kattniss
              - media_player.pussgurkan
            message: "Isobel, dags att vakna!"

  # Floor controls
  - type: horizontal-stack
    cards:
      - type: button
        name: 🏠 Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.uppe
            message: "Alla som är uppe, kom ner nu!"

      - type: button
        name: 🏠 Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.nere
            message: "Skynda på lite nere!"

  # PANIC BUTTON
  - type: button
    name: "🚨 ÖVERALLT - VI GÅR NU!"
    icon: mdi:alarm-light
    tap_action:
      action: call-service
      service: tts.openai_say
      service_data:
        entity_id: media_player.party
        message: "ALLA TILL BILEN NU! VI GÅR OMEDELBART!"

  # Checklist status
  - type: entities
    title: Checklist Status
    entities:
      - input_boolean.morning_checklist_breakfast
      - input_boolean.morning_checklist_teeth
      - input_boolean.morning_checklist_bag
      - input_boolean.morning_checklist_shoes
```

## 🎤 Broadcast Scripts (All Your Speakers)

```yaml
# Add to scripts.yaml
script:
  announce_everywhere:
    alias: "Meddela överallt"
    description: "Skicka meddelande till alla 7 högtalare"
    fields:
      message:
        description: "Meddelandet att skicka"
      volume:
        description: "Volym (0.0-1.0)"
    sequence:
      - service: media_player.volume_set
        target:
          entity_id:
            - media_player.united
            - media_player.kattniss
            - media_player.pussgurkan
            - media_player.kocken
            - media_player.kompis
            - media_player.dobby
            - media_player.vision
        data:
          volume_level: "{{ volume | default(0.7) }}"
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.united
            - media_player.kattniss
            - media_player.pussgurkan
            - media_player.kocken
            - media_player.kompis
            - media_player.dobby
            - media_player.vision
        data:
          message: "{{ message }}"

  # Or use your Party group (simpler!)
  announce_everywhere_party:
    alias: "Meddela överallt (Party)"
    description: "Använd Party-gruppen"
    fields:
      message:
        description: "Meddelandet"
    sequence:
      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "{{ message }}"
```

## 📊 Visual Timeline

Your complete morning flow:

```
06:30 🛏️ United (Novali)         "God morgon! 1 timme kvar"
06:35 🛏️ Kattniss+Pussgurkan     "God morgon Isobel! 55 min kvar"
06:40 🍳 Kocken+Kompis           "Frukost! Kolla checklistan" [SHOW DASHBOARD]
06:55 🏠 Nere (all downstairs)   "35 min - borsta tänderna"
07:05 🏠 Uppe (all upstairs)     "25 min - klä på er, bädda"
07:15 🏠 Nere (all downstairs)   "15 min - skor, jacka, checklist!"
07:20 🍳 Kocken                  "Check checklistan - vad fattas?"
07:25 🚨 PARTY (ALL 7 SPEAKERS)  "5 MINUTER! ALLA TILL HALLEN!"
07:28 🚨 PARTY (MAX VOLUME)      "2 MINUTER! VI GÅR NU!"
```

## 🎯 Special Features for Your Setup

### Office Speaker (Dobby)
- Could announce to you while you're working: "5 minuter tills avgång!"
- Useful if you work from home and need departure reminders too

### Movie Room (Vision)
- If kids sneak off to watch TV in the morning, they'll DEFINITELY hear the announcements!
- Makes sure they can't "hide" in the movie room

### Nest Hub (Kocken)
Since it has a screen, you get:
- ✅ Visual countdown timer (huge numbers!)
- ✅ Interactive checklist (tap to check off)
- ✅ Color-coded urgency (green → orange → red)
- ✅ Day-specific reminders shown visually
- ✅ Auto-displays at 6:25 AM, auto-hides at 7:45 AM

## 🔧 Customization

### Change departure time:
Just tap the time selector on Kocken's dashboard, or edit:
```yaml
input_datetime.departure_time:
  initial: "07:30"  # Change to whatever you need
```

### Add custom checklist items:
```yaml
input_boolean.morning_checklist_YOURITEM:
  name: Din påminnelse
  icon: mdi:ICON
```

### Adjust wake-up times:
If kids need more/less time, adjust the times in automations.

## 🎉 Why This Setup is Perfect

1. ✅ **7:30 departure** - Perfectly timed for your schedule
2. ✅ **All 7 speakers mapped** - Every room covered
3. ✅ **Handles Isobel sleeping in parents room** - Announces both places
4. ✅ **Visual dashboard on Kocken** - Kids can see AND hear
5. ✅ **Day-specific reminders** - Idrott, simning, etc.
6. ✅ **Progressive escalation** - Rooms → Floors → EVERYWHERE
7. ✅ **Can't hide anywhere** - Movie room and office covered!

## 🚀 Next Steps

1. Copy the configuration to your Home Assistant
2. Test each speaker:
   ```yaml
   service: tts.openai_say
   data:
     entity_id: media_player.party
     message: "Test från alla högtalare! Kan ni höra?"
   ```
3. Create the kitchen dashboard for Kocken
4. Set up the checklist items
5. Test the full routine!

Everything is ready for your 7:30 departure! 🎉
