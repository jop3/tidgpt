# Your Complete Speaker Setup & Morning Routine

Based on your actual room layout and speakers.

## 🏠 Your House Layout

### Upstairs (Uppe)
- **Kattniss** (`media_player.kattniss`) - Isobel's room (younger child)
- **United** (`media_player.united`) - Novali's room (older child)
- **Pussgurkan** (`media_player.pussgurkan`) - Parents' room
- **Group**: `media_player.uppe`

### Downstairs (Nere)
- **Kompis** (`media_player.kompis`) - Living room
- **Kocken** (`media_player.kocken`) - Kitchen (Nest Hub with screen! 📺)
- **Group**: `media_player.nere`

### Other Speakers
- **Dobby** - Where is this? (Bathroom? Hall?)
- **Vision** - Where is this? (Bathroom? Hall?)

### Groups
- **Party** (`media_player.party`) - ALL speakers everywhere

## 🎯 Perfect Morning Flow

Based on typical movement through your house:

```
07:00 🛏️ Upstairs bedrooms    Wake up (Novali & Isobel)
07:10 🍳 Kitchen              Breakfast call (Kocken)
07:25 🛁 Bathroom             Brush teeth (Dobby/Vision?)
07:35 🛏️ Back upstairs        Get dressed (Uppe)
07:45 🏠 Living room/Kitchen  Final prep (Nere)
07:55 🚨 EVERYWHERE           Emergency (Party group!)
```

## 📺 Visual Countdown Timer for Kocken (Kitchen)

Since Kocken is a Nest Hub with screen, create a visual dashboard!

### Step 1: Create Countdown Sensor

Add to `configuration.yaml`:

```yaml
# Countdown sensor - shows time remaining until departure
sensor:
  - platform: template
    sensors:
      morning_countdown:
        friendly_name: "Tid kvar till avgång"
        value_template: >
          {% set target = today_at('08:00') %}
          {% if now() > target %}
            Ingen avgång idag
          {% else %}
            {% set diff = (target - now()).total_seconds() | int %}
            {% set hours = (diff / 3600) | int %}
            {% set minutes = ((diff % 3600) / 60) | int %}
            {% if hours > 0 %}
              {{ hours }}h {{ minutes }}m
            {% else %}
              {{ minutes }} minuter
            {% endif %}
          {% endif %}
        icon_template: mdi:clock-alert

      morning_countdown_progress:
        friendly_name: "Morgonrutin framsteg"
        unit_of_measurement: '%'
        value_template: >
          {% set start = today_at('07:00') %}
          {% set end = today_at('08:00') %}
          {% set now_time = now() %}
          {% if now_time < start %}
            0
          {% elif now_time > end %}
            100
          {% else %}
            {{ (((now_time - start).total_seconds() / (end - start).total_seconds()) * 100) | int }}
          {% endif %}

# Input for setting departure time
input_datetime:
  departure_time:
    name: Avgångstid
    has_date: false
    has_time: true
    initial: "08:00"

# Update countdown to use configurable time
sensor:
  - platform: template
    sensors:
      time_until_departure:
        friendly_name: "Tid kvar"
        value_template: >
          {% set target_time = states('input_datetime.departure_time') %}
          {% set target = today_at(target_time) %}
          {% if now() > target %}
            "Dags att gå!"
          {% else %}
            {% set diff = (target - now()).total_seconds() | int %}
            {% set minutes = (diff / 60) | int %}
            {{ minutes }} min
          {% endif %}
```

### Step 2: Create Kitchen Dashboard for Kocken

This shows on the Nest Hub screen in the kitchen:

```yaml
# Create a new dashboard called "Morgonrutin"
# Settings → Dashboards → Add Dashboard

title: Morgonrutin
views:
  - title: Kök
    path: kitchen
    badges: []
    cards:
      # BIG COUNTDOWN TIMER
      - type: entity
        entity: sensor.time_until_departure
        name: 🕐 TID KVAR
        icon: mdi:clock-alert
        style: |
          ha-card {
            font-size: 48px;
            text-align: center;
            background:
              {% if states('sensor.time_until_departure') | int < 5 %}
                red
              {% elif states('sensor.time_until_departure') | int < 15 %}
                orange
              {% else %}
                green
              {% endif %};
            color: white;
          }

      # Progress bar
      - type: gauge
        entity: sensor.morning_countdown_progress
        name: Morgonrutin framsteg
        min: 0
        max: 100
        severity:
          green: 0
          yellow: 50
          red: 80

      # Set departure time
      - type: entities
        entities:
          - entity: input_datetime.departure_time
            name: Avgångstid idag
        title: Inställningar

      # MORNING CHECKLIST (see below)
```

### Step 3: Cast Dashboard to Kocken Automatically

Auto-show the kitchen dashboard on Kocken during morning hours:

```yaml
automation:
  - id: show_kitchen_dashboard_morning
    alias: "Visa köksdashboard på morgonen"
    trigger:
      - platform: time
        at: "06:55:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # Cast the dashboard to Kocken
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
        at: "08:15:00"
    action:
      - service: media_player.turn_off
        target:
          entity_id: media_player.kocken
```

## ✅ Morning Checklists (Day-Specific!)

Create customizable checklists that show on Kocken.

### Step 1: Create Checklist Items

Add to `configuration.yaml`:

```yaml
# Daily checklist items
input_boolean:
  # Basic daily tasks
  morning_checklist_dressed:
    name: Klädda
    icon: mdi:tshirt-crew
  morning_checklist_teeth:
    name: Borstat tänderna
    icon: mdi:tooth
  morning_checklist_breakfast:
    name: Ätit frukost
    icon: mdi:food-apple
  morning_checklist_bag:
    name: Packat skolväskan
    icon: mdi:bag-personal
  morning_checklist_shoes:
    name: Skor på
    icon: mdi:shoe-formal
  morning_checklist_jacket:
    name: Jacka på
    icon: mdi:coat-rack

  # Day-specific items
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
    name: Biblioteksböcker (Onsdag)
    icon: mdi:book-multiple
  morning_checklist_swimming:
    name: Simkläder (Torsdag)
    icon: mdi:swim

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
            - input_boolean.morning_checklist_dressed
            - input_boolean.morning_checklist_teeth
            - input_boolean.morning_checklist_breakfast
            - input_boolean.morning_checklist_bag
            - input_boolean.morning_checklist_shoes
            - input_boolean.morning_checklist_jacket
            - input_boolean.morning_checklist_glasses
            - input_boolean.morning_checklist_fruit
            - input_boolean.morning_checklist_gym_clothes
            - input_boolean.morning_checklist_library_books
            - input_boolean.morning_checklist_swimming
```

### Step 2: Add Checklist to Kitchen Dashboard

Add this card to the Kocken dashboard:

```yaml
# In your kitchen dashboard
cards:
  - type: markdown
    content: |
      # ✅ MORGONCHECKLISTA
      {% set day = now().weekday() %}
      {% if day == 0 %}**MÅNDAG**
      {% elif day == 1 %}**TISDAG - Glöm inte idrott!** 🏃
      {% elif day == 2 %}**ONSDAG**
      {% elif day == 3 %}**TORSDAG - Simkläder!** 🏊
      {% elif day == 4 %}**FREDAG - Snart helg!** 🎉
      {% endif %}

  # Daily checklist (always shown)
  - type: entities
    title: Varje dag
    entities:
      - input_boolean.morning_checklist_breakfast
      - input_boolean.morning_checklist_teeth
      - input_boolean.morning_checklist_dressed
      - input_boolean.morning_checklist_bag
      - input_boolean.morning_checklist_shoes
      - input_boolean.morning_checklist_jacket

  # Conditional checklist based on day
  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'monday'
    card:
      type: entities
      title: Extra idag (Måndag)
      entities:
        - input_boolean.morning_checklist_glasses
        - input_boolean.morning_checklist_fruit

  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'tuesday'
    card:
      type: entities
      title: Extra idag (Tisdag - IDROTT)
      entities:
        - input_boolean.morning_checklist_gym_clothes
        - input_boolean.morning_checklist_fruit

  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'wednesday'
    card:
      type: entities
      title: Extra idag (Onsdag)
      entities:
        - input_boolean.morning_checklist_library_books
        - input_boolean.morning_checklist_fruit

  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'thursday'
    card:
      type: entities
      title: Extra idag (Torsdag - SIMNING)
      entities:
        - input_boolean.morning_checklist_swimming
        - input_boolean.morning_checklist_fruit

  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'friday'
    card:
      type: entities
      title: Extra idag (Fredag)
      entities:
        - input_boolean.morning_checklist_fruit
```

### Step 3: Voice Announcements for Checklist

Announce forgotten items:

```yaml
automation:
  # 7:50 - Remind about unchecked items
  - id: checklist_reminder_0750
    alias: "Påminn om checklista 07:50"
    trigger:
      - platform: time
        at: "07:50:00"
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
            {% if is_state('input_boolean.morning_checklist_breakfast', 'off') %}{% set unchecked = unchecked + ['frukost'] %}{% endif %}
            {% if is_state('input_boolean.morning_checklist_teeth', 'off') %}{% set unchecked = unchecked + ['borsta tänderna'] %}{% endif %}
            {% if is_state('input_boolean.morning_checklist_bag', 'off') %}{% set unchecked = unchecked + ['packa väskan'] %}{% endif %}
            {% if unchecked | length > 0 %}
              Kolla checklistan! Ni har inte gjort: {{ unchecked | join(', ') }}.
            {% else %}
              Bra jobbat! Allt på checklistan är klart!
            {% endif %}

  # Tuesday - Gym reminder
  - id: gym_reminder_tuesday
    alias: "Påminn om idrott (Tisdag)"
    trigger:
      - platform: time
        at: "07:45:00"
    condition:
      - condition: time
        weekday: [tue]
      - condition: state
        entity_id: input_boolean.morning_checklist_gym_clothes
        state: 'off'
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.party  # Announce everywhere!
        data:
          message: "GLÖM INTE! Idag är det idrott! Ta med gympakläder!"
```

## 🎯 Complete Morning Routine (Your Exact Setup)

```yaml
automation:
  # ============================================
  # 07:00 - Wake up kids in their rooms
  # ============================================
  - id: morning_novali_0700
    alias: "07:00 - Novali vakna"
    trigger:
      - platform: time
        at: "07:00:00"
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

  - id: morning_isobel_0705
    alias: "07:05 - Isobel vakna"
    trigger:
      - platform: time
        at: "07:05:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # Isobel often sleeps in parents room, so announce there too
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
          message: "God morgon Isobel! Dags att vakna sötnos."

  # ============================================
  # 07:10 - Kitchen breakfast call
  # ============================================
  - id: morning_breakfast_0710
    alias: "07:10 - Frukost i köket"
    trigger:
      - platform: time
        at: "07:10:00"
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

      # Announce from kitchen
      - service: tts.openai_say
        target:
          entity_id: media_player.kocken
        data:
          message: "Frukost! Kom ner till köket. Kolla checklistan på skärmen."

  # ============================================
  # 07:30 - Back upstairs to get dressed
  # ============================================
  - id: morning_getdressed_0730
    alias: "07:30 - Klä på er"
    trigger:
      - platform: time
        at: "07:30:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.uppe  # All upstairs speakers
        data:
          message: "30 minuter kvar! Upp till rummen och klä på er. Bädda sängen också."

  # ============================================
  # 07:45 - Downstairs final prep
  # ============================================
  - id: morning_finalprep_0745
    alias: "07:45 - Sista förberedelser"
    trigger:
      - platform: time
        at: "07:45:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.nere  # Kitchen + Living room
        data:
          message: "15 minuter kvar! Kolla checklistan i köket. Ta på skor och jacka."

  # ============================================
  # 07:55 - BROADCAST EVERYWHERE
  # ============================================
  - id: morning_urgent_0755
    alias: "07:55 - BRÅDSKANDE"
    trigger:
      - platform: time
        at: "07:55:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.party  # ALL speakers!
        data:
          volume_level: 0.8

      - service: tts.openai_say
        target:
          entity_id: media_player.party
        data:
          message: "5 MINUTER KVAR! ALLA TILL HALLEN OMEDELBART!"
```

## 📱 Dashboard Control Panel

Add to your phone dashboard:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🏠 Morgonkontroll

  # Quick room announcements
  - type: horizontal-stack
    cards:
      - type: button
        name: Novali's rum
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.united
            message: "Novali, dags att gå upp!"

      - type: button
        name: Isobel's rum
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id:
              - media_player.kattniss
              - media_player.pussgurkan
            message: "Isobel, dags att vakna!"

  - type: horizontal-stack
    cards:
      - type: button
        name: Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.uppe
            message: "Alla uppe, kom ner!"

      - type: button
        name: Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: tts.openai_say
          service_data:
            entity_id: media_player.nere
            message: "Skynda på lite!"

  # PANIC BUTTON
  - type: button
    name: "🚨 ÖVERALLT - ALLA TILL HALLEN!"
    icon: mdi:alarm-light
    tap_action:
      action: call-service
      service: tts.openai_say
      service_data:
        entity_id: media_player.party
        message: "ALLA TILL HALLEN OMEDELBART! VI GÅR NU!"

  # Checklist status
  - type: entities
    title: Checklista status
    entities:
      - sensor.time_until_departure
      - input_boolean.morning_checklist_breakfast
      - input_boolean.morning_checklist_teeth
      - input_boolean.morning_checklist_bag
```

## 🎨 Color-Coded Countdown on Kocken

Make the countdown change color as time runs out:

```yaml
# In kitchen dashboard
- type: custom:mushroom-template-card  # Or use entity card
  entity: sensor.time_until_departure
  primary: |
    {% set mins = states('sensor.time_until_departure') | int %}
    {% if mins <= 5 %}
      🔴 {{ mins }} MINUTER KVAR!
    {% elif mins <= 15 %}
      🟠 {{ mins }} minuter kvar
    {% else %}
      🟢 {{ mins }} minuter kvar
    {% endif %}
  icon: |
    {% set mins = states('sensor.time_until_departure') | int %}
    {% if mins <= 5 %}
      mdi:alarm-light
    {% elif mins <= 15 %}
      mdi:clock-alert
    {% else %}
      mdi:clock
    {% endif %}
  icon_color: |
    {% set mins = states('sensor.time_until_departure') | int %}
    {% if mins <= 5 %}
      red
    {% elif mins <= 15 %}
      orange
    {% else %}
      green
    {% endif %}
```

## 🤔 Still Need to Know

Where are these speakers?
- **Dobby** - Bathroom? Hall? Upstairs or downstairs?
- **Vision** - Bathroom? Hall?

Let me know and I'll add them to the perfect spots!

## 🎯 Summary

Your complete setup:
1. ✅ **Voice announcements** following kids through the house
2. ✅ **Visual countdown timer** on Kocken (kitchen Nest Hub)
3. ✅ **Daily checklists** with day-specific items
4. ✅ **Smart escalation** (rooms → floors → EVERYWHERE)
5. ✅ **Panic button** broadcasts to all speakers
6. ✅ **Personalized messages** (Novali vs Isobel, handles Isobel sleeping in parents room)

Everything is ready to copy-paste into your Home Assistant!
