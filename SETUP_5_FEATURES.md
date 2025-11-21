# Setup Guide: 5 User-Friendly Features

Complete setup for features 1-5 to make the system easy for everyone.

---

## Feature 1: Dedicated Phone Dashboard (10 minutes)

### Step 1: Create Master On/Off Toggle

1. **Settings** → **Devices & Services** → **Helpers** tab
2. Click **+ Create Helper**
3. Choose **Toggle**
4. **Name:** `Morgonpåminnelser aktiverade`
5. **Icon:** `mdi:alarm`
6. Click **Create**

### Step 2: Create Custom Message Input

1. Still in **Helpers**, click **+ Create Helper**
2. Choose **Text**
3. **Name:** `Eget morgonmeddelande`
4. **Max length:** 200
5. Click **Create**

### Step 3: Create New Dashboard

1. Click **Settings** → **Dashboards**
2. Click **+ Add Dashboard** (bottom right)
3. **Title:** `Morgonrutin`
4. **Icon:** `mdi:alarm`
5. **Show in sidebar:** Check YES
6. Click **Create**

### Step 4: Add Complete Control Panel

1. Click **Morgonrutin** in the sidebar (left menu)
2. You'll see empty dashboard
3. Click **+ Add Card** (bottom right)
4. Scroll down and click **Manual**
5. **Delete everything** in the box
6. **Copy and paste this entire thing:**

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      # 🌅 Morgonrutin
      **Avgång: 7:30**

  - type: entities
    title: 🎚️ Huvudkontroll
    entities:
      - entity: input_boolean.morgonpaminnelser_aktiverade
        name: Alla morgonpåminnelser
    show_header_toggle: false

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

  - type: markdown
    content: |
      ## ✏️ Eget Meddelande

  - type: entities
    entities:
      - entity: input_text.eget_morgonmeddelande
        name: Skriv meddelande här

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
            message: "{{ states('input_text.eget_morgonmeddelande') }}"
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
            message: "{{ states('input_text.eget_morgonmeddelande') }}"
            language: sv

  - type: button
    name: Säg ÖVERALLT
    icon: mdi:bullhorn
    tap_action:
      action: call-service
      service: tts.google_translate_say
      service_data:
        entity_id: media_player.party
        message: "{{ states('input_text.eget_morgonmeddelande') }}"
        language: sv
```

7. Click **Save**
8. Click **Done** (top right)

### Step 5: Test It!

1. You should now see the complete dashboard
2. Try tapping **"Novali"** button
3. United should speak!
4. Try typing in "Eget Meddelande" box: "Test!"
5. Tap "Säg ÖVERALLT"
6. All 7 speakers should speak!

**✅ Feature 1 Complete!**

---

## Feature 2: Interactive Kitchen Dashboard (15 minutes)

### Step 1: Create Checklist Helpers

For each item, create a toggle:

1. **Settings** → **Devices & Services** → **Helpers**
2. Click **+ Create Helper** → **Toggle**
3. Create these (one at a time):

**Daily items:**
- Name: `Ätit frukost`, Icon: `mdi:food-apple`
- Name: `Borstat tänderna`, Icon: `mdi:tooth`
- Name: `Klädda`, Icon: `mdi:tshirt-crew`
- Name: `Packat skolväskan`, Icon: `mdi:bag-personal`
- Name: `Skor på`, Icon: `mdi:shoe-formal`
- Name: `Jacka på`, Icon: `mdi:coat-rack`

**Special items:**
- Name: `Glasögon (Isobel)`, Icon: `mdi:glasses`
- Name: `Frukt med`, Icon: `mdi:fruit-grapes`
- Name: `Idrottskläder (Tisdag)`, Icon: `mdi:weight-lifter`
- Name: `Simkläder (Torsdag)`, Icon: `mdi:swim`

### Step 2: Create Kitchen Dashboard

1. **Settings** → **Dashboards** → **+ Add Dashboard**
2. **Title:** `Kök Morgon`
3. **Icon:** `mdi:coffee`
4. **Show in sidebar:** Check YES
5. Click **Create**
6. Open the new dashboard from sidebar
7. Click **+ Add Card** → **Manual**
8. Paste:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      <div style="text-align: center; font-size: 48px; padding: 20px; background: #1976d2; color: white; border-radius: 10px;">
      🌅 MORGONRUTIN
      </div>

  - type: markdown
    content: |
      <div style="text-align: center; font-size: 36px; padding: 10px;">
      Avgång: <b>7:30</b>
      </div>

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

  - type: entities
    title: Extra att komma ihåg
    show_header_toggle: false
    entities:
      - input_boolean.glasogon_isobel
      - input_boolean.frukt_med
      - input_boolean.idrottskläder_tisdag
      - input_boolean.simkläder_torsdag

  - type: markdown
    content: |
      ## 📢 Kalla på barnen

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
            message: "Novali, kom ner till köket!"
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
            message: "Isobel, kom ner till köket!"
            language: sv
```

9. Click **Save** → **Done**

### Step 3: Auto-Display on Kocken

Make this dashboard show automatically on Kocken at 6:25 AM:

1. **Settings** → **Automations & Scenes** → **+ Create Automation**
2. Three dots → **Edit in YAML**
3. Paste:

```yaml
alias: "Visa köksdashboard på morgonen"
description: Show kitchen dashboard on Kocken
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

### Step 4: Auto-Reset Checklist Daily

Reset all checkboxes at 6:00 AM:

1. **Settings** → **Automations & Scenes** → **+ Create Automation**
2. Three dots → **Edit in YAML**
3. Paste:

```yaml
alias: "Återställ checklista varje morgon"
description: Reset checklist at 6 AM
trigger:
  - platform: time
    at: "06:00:00"
action:
  - service: input_boolean.turn_off
    target:
      entity_id:
        - input_boolean.atit_frukost
        - input_boolean.borstat_tanderna
        - input_boolean.kladda
        - input_boolean.packat_skolvaskan
        - input_boolean.skor_pa
        - input_boolean.jacka_pa
        - input_boolean.glasogon_isobel
        - input_boolean.frukt_med
        - input_boolean.idrottskläder_tisdag
        - input_boolean.simkläder_torsdag
mode: single
```

4. Click **Save**

**✅ Feature 2 Complete!**

---

## Feature 3: One-Tap Scenes (5 minutes)

### Scene 1: Normal Morgon (All ON)

1. **Settings** → **Scenes** → **+ Add Scene** (bottom right)
2. **Name:** `Normal Morgon`
3. **Icon:** `mdi:alarm-check`
4. Click **+ Add Entity**
5. Add: `input_boolean.morgonpaminnelser_aktiverade`
6. Toggle it **ON** (blue)
7. Click **Save**

### Scene 2: Lov/Helg (All OFF)

1. **Settings** → **Scenes** → **+ Add Scene**
2. **Name:** `Lov och Helg`
3. **Icon:** `mdi:palm-tree`
4. Click **+ Add Entity**
5. Add: `input_boolean.morgonpaminnelser_aktiverade`
6. Toggle it **OFF** (grey)
7. Click **Save**

### Scene 3: Sen Morgon

1. **Settings** → **Scenes** → **+ Add Scene**
2. **Name:** `Sen Morgon`
3. **Icon:** `mdi:alarm-snooze`
4. Click **+ Add Entity**
5. Find all your morning automations (0630, 0635, 0640, etc.)
6. Turn OFF: 0630, 0635, 0640, 0655, 0705
7. Turn ON: 0715, 0725, 0728
8. Click **Save**

### Add Scene Buttons to Phone Dashboard

1. Go to **Morgonrutin** dashboard
2. Click three dots → **Edit Dashboard**
3. Click **+ Add Card** → **Manual**
4. Paste:

```yaml
type: horizontal-stack
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
        entity_id: scene.lov_och_helg

  - type: button
    name: Sen Morgon
    icon: mdi:alarm-snooze
    tap_action:
      action: call-service
      service: scene.turn_on
      target:
        entity_id: scene.sen_morgon
```

5. Click **Save** → **Done**

**✅ Feature 3 Complete!**

---

## Feature 4: Pre-Made Message Buttons (3 minutes)

Add common phrase buttons to your phone dashboard:

1. Go to **Morgonrutin** dashboard
2. Three dots → **Edit Dashboard**
3. Click **+ Add Card** → **Manual**
4. Paste:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 💬 Färdiga Meddelanden

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
        name: Matlåda!
        icon: mdi:lunch-box
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.kocken
            message: "Kom ihåg matlådan i kylskåpet!"
            language: sv

  - type: horizontal-stack
    cards:
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

      - type: button
        name: Skynda på!
        icon: mdi:run-fast
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.nere
            message: "Skynda på lite nu! Vi har bråttom!"
            language: sv

  - type: horizontal-stack
    cards:
      - type: button
        name: Bra jobbat!
        icon: mdi:thumb-up
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.party
            message: "Bra jobbat! Ni är nästan klara!"
            language: sv

      - type: button
        name: Kom hit!
        icon: mdi:hand-wave
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.party
            message: "Jag behöver er hjälp här! Kom hit nu!"
            language: sv
```

5. Click **Save** → **Done**

**✅ Feature 4 Complete!**

---

## Feature 5: Voice Control (10 minutes)

### Step 1: Setup Google Assistant Integration

1. **Settings** → **Devices & Services**
2. Click **+ Add Integration** (bottom right)
3. Search for "**Google Assistant**"
4. Click **Google Assistant**
5. Follow the setup wizard:
   - Sign in with your Google account
   - Grant permissions
   - Select which entities to expose

### Step 2: Expose Morning Controls

In the Google Assistant setup:
1. Check the box for: `input_boolean.morgonpaminnelser_aktiverade`
2. Check boxes for your automations if you want individual control
3. Click **Submit**

### Step 3: Sync with Google

1. Open **Google Home app** on your phone
2. Tap your profile icon
3. Tap **Assistant settings**
4. Tap **Home control**
5. Tap **Home Assistant** (should appear in list)
6. Tap the sync icon (↻) if needed

### Step 4: Test Voice Commands

Say to your Google Home:
- "Hey Google, turn on morgonpåminnelser aktiverade"
- "Hey Google, turn off morgonpåminnelser aktiverade"

Or in English:
- "Hey Google, turn on morning reminders enabled"
- "Hey Google, turn off morning reminders enabled"

### Step 5: Create Voice Routines (Optional)

Make it easier by creating Google Assistant routines:

1. Open **Google Home app**
2. Tap **Automations** (bottom)
3. Tap **+** → **New routine**
4. **When:** Add starter phrase: "Turn on morning mode"
5. **Then:** Add action → **Adjust Home devices**
6. Select `input_boolean.morgonpaminnelser_aktiverade` → Turn **ON**
7. Save

Now you can say:
- "Hey Google, turn on morning mode" (enables all reminders)
- "Hey Google, turn off morning mode" (disables all reminders)

**✅ Feature 5 Complete!**

---

## Summary: What You Can Do Now

### From Phone (Morgonrutin Dashboard):
✅ Master ON/OFF toggle
✅ Quick buttons: Novali, Isobel, Uppe, Nere
✅ Panic button (all speakers)
✅ Type custom messages
✅ Pre-made message buttons (Frukt, Matlåda, Idrott, etc.)
✅ Scene buttons (Normal, Lov/Helg, Sen Morgon)

### From Kitchen (Kocken Screen):
✅ Visual checklist (auto-displays at 6:25 AM)
✅ Tap to check off tasks
✅ Call buttons for kids
✅ Auto-resets at 6:00 AM

### By Voice:
✅ "Hey Google, turn on morning mode"
✅ "Hey Google, turn off morning mode"

---

## Test Everything!

### Test Phone Dashboard:
1. Open Home Assistant app
2. Tap **Morgonrutin** in menu
3. Tap each button
4. Type message in text box → tap "Säg ÖVERALLT"
5. Tap scene buttons

### Test Kitchen Dashboard:
1. Go to kitchen
2. Open **Kök Morgon** dashboard
3. Tap checkboxes
4. Tap kid buttons

### Test Voice:
Say: "Hey Google, turn off morning mode"

---

## Quick Reference for Your Wife:

Print this:

```
📱 MORGONRUTIN APP

ÖPPna appen:
- Tryck "Morgonrutin" i menyn

KALLA PÅ BARNEN:
- Tryck [Novali] eller [Isobel]

SKICKA EGET MEDDELANDE:
- Skriv i textrutan
- Tryck "Säg ÖVERALLT"

FÄRDIGA MEDDELANDEN:
- [Frukt idag!]
- [Matlåda!]
- [Idrott idag!]
- [Skynda på!]

NÖDLÄGE:
- Tryck [ALLA TILL HALLEN NU!]

STÄNG AV FÖR HELGEN:
- Tryck [Lov/Helg]

STARTA IGEN:
- Tryck [Normal Morgon]

MED RÖST:
"Hey Google, turn off morning mode"
```

---

That's it! All 5 features are now set up! 🎉
