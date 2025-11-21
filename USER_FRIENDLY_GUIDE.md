# User-Friendly Setup Guide
## Making Everything Easy for Non-Technical Users

Complete guide to make the morning routine system easy for everyone to use and customize.

---

## 🎯 Goal: Your Wife Can Control Everything from Her Phone

No coding, no configuration files - just tap buttons!

---

## Part 1: Phone Dashboard (Primary Control Center)

### Create a Dedicated "Morgonrutin" Dashboard

This gives you a separate dashboard just for morning control - clean and simple.

#### Step 1: Create New Dashboard

1. Click **Settings** → **Dashboards**
2. Click **+ Add Dashboard** (bottom right)
3. **Name:** `Morgonrutin`
4. **Icon:** `mdi:alarm`
5. **Show in sidebar:** YES
6. Click **Create**

#### Step 2: Add Complete Control Panel

1. Click the new **Morgonrutin** in sidebar
2. Click **+ Add Card**
3. Choose **Manual**
4. Paste this complete dashboard:

```yaml
type: vertical-stack
cards:
  # Header
  - type: markdown
    content: |
      # 🌅 Morgonrutin
      **Avgång: 7:30**

  # Quick status
  - type: horizontal-stack
    cards:
      - type: entity
        entity: sensor.time
        name: Tid nu
        icon: mdi:clock

  # ON/OFF Master Control
  - type: entities
    title: 🎚️ Huvudkontroll
    entities:
      - entity: input_boolean.morning_reminders_enabled
        name: Alla morgonpåminnelser
    show_header_toggle: false

  # Individual automation toggles
  - type: entities
    title: ⏰ Schema
    entities:
      - entity: automation.0630_novali_vakna
        name: "06:30 - Novali"
      - entity: automation.0635_isobel_vakna
        name: "06:35 - Isobel"
      - entity: automation.0640_frukost
        name: "06:40 - Frukost"
      - entity: automation.0655_tvatta_sig
        name: "06:55 - Tvätta"
      - entity: automation.0705_kla_pa_er
        name: "07:05 - Klä på"
      - entity: automation.0715_sista_forberedelser
        name: "07:15 - Förbered"
      - entity: automation.0725_bradskande_overallt
        name: "07:25 - 5 min!"
      - entity: automation.0728_nodsituation
        name: "07:28 - 2 min!"

  # Quick announcement buttons
  - type: markdown
    content: |
      ## 📢 Snabbmeddelanden

  - type: horizontal-stack
    cards:
      - type: button
        name: Novali
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.united
            message: "Novali, kom!"
            language: sv

      - type: button
        name: Isobel
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id:
              - media_player.kattniss
              - media_player.pussgurkan
            message: "Isobel, kom!"
            language: sv

  - type: horizontal-stack
    cards:
      - type: button
        name: Alla Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.uppe
            message: "Alla uppe, kom ner!"
            language: sv

      - type: button
        name: Alla Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.nere
            message: "Kom hit nu!"
            language: sv

  # Emergency buttons
  - type: markdown
    content: |
      ## 🚨 Nödsituation

  - type: button
    name: ALLA TILL HALLEN NU!
    icon: mdi:alarm-light
    tap_action:
      action: call-service
      service: tts.google_translate_say
      service_data:
        entity_id: media_player.party
        message: "ALLA TILL HALLEN OMEDELBART! VI GÅR NU!"
        language: sv
    hold_action:
      action: none

  # Custom message input
  - type: markdown
    content: |
      ## ✏️ Eget Meddelande

  - type: entities
    entities:
      - entity: input_text.custom_morning_message
        name: Skriv meddelande

  - type: horizontal-stack
    cards:
      - type: button
        name: Säg till Novali
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.united
            message: "{{ states('input_text.custom_morning_message') }}"
            language: sv

      - type: button
        name: Säg till Isobel
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id:
              - media_player.kattniss
              - media_player.pussgurkan
            message: "{{ states('input_text.custom_morning_message') }}"
            language: sv

  - type: button
    name: Säg ÖVERALLT
    icon: mdi:bullhorn
    tap_action:
      action: call-service
      service: tts.google_translate_say
      service_data:
        entity_id: media_player.party
        message: "{{ states('input_text.custom_morning_message') }}"
        language: sv
```

5. Click **Save**

---

## Part 2: Visual Dashboard on Kocken (Kitchen Nest Hub)

Interactive touchscreen dashboard that shows on Kocken's screen!

### Features:
- ✅ Big countdown timer
- ✅ Tap to check off tasks
- ✅ Day-specific reminders
- ✅ Easy to customize

### Step 1: Create Helper for Custom Message

1. **Settings** → **Devices & Services** → **Helpers** tab
2. Click **+ Create Helper**
3. Choose **Text**
4. Name: `Eget morgonmeddelande`
5. Max length: 200
6. Click **Create**

### Step 2: Create Master On/Off Toggle

1. **Settings** → **Devices & Services** → **Helpers** tab
2. Click **+ Create Helper**
3. Choose **Toggle**
4. Name: `Morgonpåminnelser aktiverade`
5. Icon: `mdi:alarm`
6. Click **Create**

### Step 3: Create Kitchen Dashboard

This is what shows on Kocken's screen!

1. **Settings** → **Dashboards** → **+ Add Dashboard**
2. Name: `Kök - Morgon`
3. Icon: `mdi:coffee`
4. Click **Create**
5. Open the new dashboard
6. Click **+ Add Card** → **Manual**
7. Paste:

```yaml
type: vertical-stack
cards:
  # Big header
  - type: markdown
    content: |
      <div style="text-align: center; font-size: 48px; padding: 20px; background: #1976d2; color: white; border-radius: 10px;">
      🌅 MORGONRUTIN
      </div>

  # Current time
  - type: markdown
    content: |
      <div style="text-align: center; font-size: 36px; padding: 10px;">
      Avgång: <b>7:30</b>
      </div>

  # Today's date and day
  - type: markdown
    content: |
      {% set days = ['Måndag', 'Tisdag', 'Onsdag', 'Torsdag', 'Fredag', 'Lördag', 'Söndag'] %}
      {% set day = days[now().weekday()] %}
      <div style="text-align: center; font-size: 24px; padding: 10px;">
      <b>{{ day }}</b> {{ now().strftime('%d %B') }}
      </div>

  # Daily checklist
  - type: markdown
    content: |
      # ✅ CHECKLISTA

  - type: entities
    title: Grundläggande
    show_header_toggle: false
    entities:
      - input_boolean.atit_frukost
      - input_boolean.borstat_tanderna
      - input_boolean.kladda
      - input_boolean.packat_skolvaskan
      - input_boolean.skor_pa
      - input_boolean.jacka_pa

  # Day specific
  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'tuesday'
    card:
      type: entities
      title: 🏃 IDAG - IDROTT!
      entities:
        - input_boolean.idrottskläder_tisdag
        - input_boolean.frukt_med

  - type: conditional
    conditions:
      - entity: sensor.day_of_week
        state: 'thursday'
    card:
      type: entities
      title: 🏊 IDAG - SIMNING!
      entities:
        - input_boolean.simkläder_torsdag
        - input_boolean.frukt_med

  # Quick buttons
  - type: horizontal-stack
    cards:
      - type: button
        name: Novali
        icon: mdi:account
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.united
            message: "Novali, kom ner!"
            language: sv

      - type: button
        name: Isobel
        icon: mdi:account-child
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id:
              - media_player.kattniss
              - media_player.pussgurkan
            message: "Isobel, kom ner!"
            language: sv
```

8. Click **Save**

### Step 4: Auto-Show Dashboard on Kocken

Make the dashboard automatically appear on Kocken's screen at 6:25 AM:

1. **Settings** → **Automations & Scenes** → **+ Create Automation**
2. Three dots → **Edit in YAML**
3. Paste:

```yaml
alias: "Visa köksdashboard på morgonen"
description: Show kitchen dashboard on Kocken at 6:25 AM
trigger:
  - platform: time
    at: "06:25:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: cast.show_lovelace_view
    target:
      entity_id: media_player.kocken
    data:
      dashboard_path: kok-morgon
      view_path: default
mode: single
```

4. Click **Save**

---

## Part 3: Voice Control via Google Assistant

Your wife can control everything by voice!

### Setup:

1. **Settings** → **Integrations**
2. Search for "**Google Assistant**"
3. Click **Configure**
4. Follow setup (link Google account)

### Once Setup, She Can Say:

- "Hey Google, turn on morning reminders"
- "Hey Google, turn off morning reminders"
- "Hey Google, run Novali wake up"
- "Hey Google, announce to all speakers 'time for breakfast'"

---

## Part 4: Home Screen Widgets (Phone)

Add Home Assistant widgets to phone home screen for instant access!

### iOS:
1. Long-press home screen
2. Tap **+** (top left)
3. Search "**Home Assistant**"
4. Choose widget size
5. Add widget
6. Tap widget → **Edit Widget**
7. Choose entities to show (morning automation toggles)

### Android:
1. Long-press home screen
2. Tap **Widgets**
3. Find **Home Assistant**
4. Drag to home screen
5. Configure to show morning controls

Now she can control from phone home screen without opening app!

---

## Part 5: Simple Customization (No Coding!)

### Change Messages (Easy Way):

Instead of editing automations, use the **custom message input**:

1. Open Morgonrutin dashboard
2. Scroll to "Eget Meddelande"
3. Type: "Kom och ät nu!"
4. Tap which speaker to send to
5. Done!

### Change Schedule Times:

Create a simple helper to adjust wake-up time:

1. **Settings** → **Helpers** → **+ Create Helper**
2. Choose **Time**
3. Name: `Novali väckning`
4. Default: `06:30:00`
5. Create

Add to dashboard:
```yaml
- type: entities
  title: ⏰ Justera tider
  entities:
    - entity: input_datetime.novali_vackning
      name: Novali väcks
    - entity: input_datetime.isobel_vackning
      name: Isobel väcks
```

Then your wife can just change the time on the dashboard!

### Pre-Made Message Buttons:

Add common messages as buttons:

```yaml
- type: horizontal-stack
  cards:
    - type: button
      name: Frukt idag!
      icon: mdi:fruit-grapes
      tap_action:
        action: call-service
        service: tts.google_translate_say
        service_data:
          entity_id: media_player.party
          message: "Glöm inte att ta med frukt till skolan idag!"
          language: sv

    - type: button
      name: Idrott idag!
      icon: mdi:weight-lifter
      tap_action:
        action: call-service
        service: tts.google_translate_say
        service_data:
          entity_id: media_player.party
          message: "Idag är det idrott! Glöm inte gympapåsen!"
          language: sv
```

---

## Part 6: Quick Scenes for Common Situations

### Create Scenes for One-Tap Control

#### Scene 1: Normal Morning
All automations ON

1. **Settings** → **Scenes** → **+ Add Scene**
2. Name: `Normal morgon`
3. Add entities: All your morning automations → State: ON
4. Save

#### Scene 2: Lov/Helg (Vacation/Weekend)
All automations OFF

1. **Settings** → **Scenes** → **+ Add Scene**
2. Name: `Lov och helg`
3. Add entities: All your morning automations → State: OFF
4. Save

#### Scene 3: Sen morgon (Slow morning)
Only last 2 automations ON (7:25, 7:28)

1. **Settings** → **Scenes** → **+ Add Scene**
2. Name: `Sen morgon`
3. Add early automations → State: OFF
4. Add 7:25 and 7:28 → State: ON
5. Save

### Add Scene Buttons to Dashboard:

```yaml
- type: horizontal-stack
  cards:
    - type: button
      name: Normal Morgon
      icon: mdi:alarm-check
      tap_action:
        action: call-service
        service: scene.turn_on
        target:
          entity_id: scene.normal_morgon

    - type: button
      name: Lov/Helg
      icon: mdi:palm-tree
      tap_action:
        action: call-service
        service: scene.turn_on
        target:
          entity_id: scene.lov_helg

    - type: button
      name: Sen Morgon
      icon: mdi:alarm-snooze
      tap_action:
        action: call-service
        service: scene.turn_on
        target:
          entity_id: scene.sen_morgon
```

Now your wife can tap ONE button to configure the whole morning!

---

## Part 7: Notifications to Your Phones

Get notified on your phones:

### Morning Started Notification:

```yaml
alias: "Notis - Morgonrutin startad"
trigger:
  - platform: time
    at: "06:30:00"
condition:
  - condition: time
    weekday: [mon, tue, wed, thu, fri]
action:
  - service: notify.mobile_app_YOUR_PHONE
    data:
      title: "Morgonrutin startad"
      message: "Novali vaknad klockan 6:30"
```

### Departure Countdown Notification:

```yaml
alias: "Notis - 10 minuter kvar"
trigger:
  - platform: time
    at: "07:20:00"
condition:
  - condition: time
    weekday: [mon, tue, wed, thu, fri]
action:
  - service: notify.mobile_app_YOUR_PHONE
    data:
      title: "⏰ 10 minuter kvar!"
      message: "Dags att börja gå mot bilen"
      data:
        actions:
          - action: ANNOUNCE_ALL
            title: "Säg till alla"
```

---

## Summary: What Your Wife Can Do (No Tech Knowledge Needed)

### From Her Phone:
✅ **One tap** to turn morning reminders on/off
✅ **One tap** to wake Novali or Isobel
✅ **One tap** to announce to specific floors
✅ **One tap PANIC button** (broadcast everywhere)
✅ **Type any message** and send to any speaker
✅ **Toggle individual times** on/off
✅ **Choose scenes** (Normal/Vacation/Slow morning)

### From Kitchen (Kocken Screen):
✅ **See countdown timer** (visual, color-coded)
✅ **Tap checkboxes** for completed tasks
✅ **See day-specific reminders** (gym, swimming)
✅ **Quick buttons** to call kids

### By Voice (Google Assistant):
✅ "Hey Google, turn off morning reminders"
✅ "Hey Google, tell everyone to come to the kitchen"

### No Coding Ever!
✅ All controls are buttons and toggles
✅ Pre-made message buttons
✅ Visual checkboxes
✅ Scene buttons for common situations

---

## Quick Start Checklist for Your Wife:

Print this and stick on fridge:

```
📱 MORGONRUTIN - SNABBGUIDE

FRÅN TELEFONEN (appen):
- Öppna Home Assistant
- Klicka "Morgonrutin" i menyn
- Tryck på knappar för att prata till barnen!

🚨 NÖDLÄGE:
- Tryck röda knappen "ALLA TILL HALLEN NU!"

📺 FRÅN KÖKET (Kocken):
- Skärmen visar nedräkning automatiskt kl 6:25
- Bocka av när saker är klara
- Tryck på barn-knappar för att kalla på dem

🗣️ MED RÖSTEN:
- "Hey Google, turn on morning reminders"
- "Hey Google, turn off morning reminders"

LOV/HELG:
- Öppna Morgonrutin-appen
- Tryck "Lov/Helg" knappen
- Klart! (Tryck "Normal Morgon" när skolan börjar igen)
```

---

Want me to create any specific custom buttons or messages for your family's routine?
