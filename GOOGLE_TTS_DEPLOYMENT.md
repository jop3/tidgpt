# Deploy with Google Translate TTS - Simple Guide

Complete step-by-step deployment using Google Translate TTS (already built-in, free).

## ✅ You Just Tested It Works!

You heard the voice - that means everything is ready. Let's build your morning routine!

## Step 1: Create All Morning Automations

For each automation below:
1. **Settings** → **Automations & Scenes**
2. Click **+ Create Automation** (bottom right)
3. Click **Create new automation**
4. Click three dots (**⋮**) top right → **Edit in YAML**
5. **Delete everything** in the box
6. **Copy and paste** the automation
7. Click **Save**
8. Give it the name shown

---

### Automation 1: Wake Up Novali (6:30 AM)

**Name:** `06:30 - Novali vakna`

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
  - service: tts.google_translate_say
    target:
      entity_id: media_player.united
    data:
      message: "God morgon Novali! Dags att vakna. En timme tills vi måste gå."
      language: sv
mode: single
```

---

### Automation 2: Wake Up Isobel (6:35 AM)

**Name:** `06:35 - Isobel vakna`

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
  - service: tts.google_translate_say
    target:
      entity_id:
        - media_player.kattniss
        - media_player.pussgurkan
    data:
      message: "God morgon Isobel! Dags att vakna sötnos. 55 minuter tills vi måste gå."
      language: sv
mode: single
```

---

### Automation 3: Breakfast (6:40 AM)

**Name:** `06:40 - Frukost`

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
  - service: tts.google_translate_say
    target:
      entity_id:
        - media_player.kocken
        - media_player.kompis
    data:
      message: "Frukost! Kom ner till köket nu."
      language: sv
mode: single
```

---

### Automation 4: Hygiene (6:55 AM)

**Name:** `06:55 - Tvätta sig`

```yaml
alias: "06:55 - Tvätta sig"
description: Hygiene reminder
trigger:
  - platform: time
    at: "06:55:00"
condition:
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
action:
  - service: tts.google_translate_say
    target:
      entity_id: media_player.nere
    data:
      message: "35 minuter kvar. Dags att tvätta sig och borsta tänderna ordentligt!"
      language: sv
mode: single
```

---

### Automation 5: Get Dressed (7:05 AM)

**Name:** `07:05 - Klä på er`

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
  - service: tts.google_translate_say
    target:
      entity_id: media_player.uppe
    data:
      message: "25 minuter kvar! Upp till rummen och klä på er. Bädda sängen också."
      language: sv
mode: single
```

---

### Automation 6: Final Prep (7:15 AM)

**Name:** `07:15 - Sista förberedelser`

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
  - service: tts.google_translate_say
    target:
      entity_id: media_player.nere
    data:
      message: "15 minuter kvar! Ta på skor och jacka. Kolla att ni har allt."
      language: sv
mode: single
```

---

### Automation 7: 5 Minute Warning (7:25 AM) ⚠️ ALL SPEAKERS

**Name:** `07:25 - BRÅDSKANDE ÖVERALLT`

```yaml
alias: "07:25 - BRÅDSKANDE ÖVERALLT"
description: 5 minute urgent warning to all speakers
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
  - service: tts.google_translate_say
    target:
      entity_id: media_player.party
    data:
      message: "5 MINUTER KVAR! ALLA TILL HALLEN OMEDELBART!"
      language: sv
mode: single
```

---

### Automation 8: 2 Minute Emergency (7:28 AM) 🚨 ALL SPEAKERS

**Name:** `07:28 - NÖDSITUATION`

```yaml
alias: "07:28 - NÖDSITUATION"
description: 2 minute emergency warning - repeats twice
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
  - service: tts.google_translate_say
    target:
      entity_id: media_player.party
    data:
      message: "TVÅ MINUTER! VI GÅR NU! ALLA TILL BILEN OMEDELBART!"
      language: sv
  - delay:
      seconds: 3
  - service: tts.google_translate_say
    target:
      entity_id: media_player.party
    data:
      message: "TVÅ MINUTER KVAR! VI MÅSTE GÅ NU!"
      language: sv
mode: single
```

---

## Step 2: Add Phone Dashboard Controls

1. Click **Overview** (top left)
2. Click three dots (**⋮**) → **Edit Dashboard**
3. Click **+ Add Card** (bottom right)
4. Scroll down → Click **Manual**
5. Paste this:

```yaml
type: vertical-stack
cards:
  - type: markdown
    content: |
      ## 🏠 Morgonkontroll
      Avgång 7:30

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
            message: "Novali, dags att gå upp!"
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
            message: "Isobel, dags att vakna!"
            language: sv

  - type: horizontal-stack
    cards:
      - type: button
        name: Uppe
        icon: mdi:stairs-up
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.uppe
            message: "Alla uppe, kom ner nu!"
            language: sv

      - type: button
        name: Nere
        icon: mdi:stairs-down
        tap_action:
          action: call-service
          service: tts.google_translate_say
          service_data:
            entity_id: media_player.nere
            message: "Skynda på lite!"
            language: sv

  - type: button
    name: "🚨 ÖVERALLT"
    icon: mdi:alarm-light
    tap_action:
      action: call-service
      service: tts.google_translate_say
      service_data:
        entity_id: media_player.party
        message: "ALLA TILL HALLEN! VI GÅR NU!"
        language: sv
```

6. Click **Save**
7. Click **Done**

---

## Step 3: Test Each Automation

1. Go to **Settings** → **Automations & Scenes**
2. Find "06:30 - Novali vakna"
3. Click three dots (**⋮**) → **Run**
4. **United should speak!**

Test each one:
- 06:30 - Should hear in Novali's room
- 06:35 - Should hear in Isobel's room AND parents' room
- 06:40 - Should hear in kitchen and living room
- 07:25 - Should hear EVERYWHERE (all 7 speakers!)

---

## Step 4: Verify All Automations Are Enabled

1. **Settings** → **Automations & Scenes**
2. Make sure ALL your new automations have the toggle **ON** (blue)
3. If any are **OFF** (grey), click to turn them ON

---

## Step 5: You're Done! 🎉

Your morning routine is now active and will run automatically **Monday-Friday** at the scheduled times!

### What Happens Tomorrow Morning:

```
06:30 🛏️ United speaks           "God morgon Novali!"
06:35 🛏️ Kattniss+Pussgurkan     "God morgon Isobel!"
06:40 🍳 Kocken+Kompis           "Frukost! Kom ner till köket"
06:55 🏠 Nere (all downstairs)   "35 min - tvätta sig!"
07:05 🏠 Uppe (all upstairs)     "25 min - klä på er!"
07:15 🏠 Nere (all downstairs)   "15 min - skor och jacka!"
07:25 🚨 PARTY (ALL 7 SPEAKERS!) "5 MINUTER! ALLA TILL HALLEN!"
07:28 🚨 PARTY (MAX VOLUME!)     "2 MINUTER! VI GÅR NU!" (x2)
```

---

## Quick Reference

### Test Any Message Right Now:

1. **Developer Tools** → **Services**
2. Service: `tts.google_translate_say`
3. Service data:
```yaml
entity_id: media_player.party
message: "Test från alla högtalare!"
language: sv
```
4. Click **Call Service**

### Your Speaker Groups:

- **media_player.uppe** = All upstairs (United, Kattniss, Pussgurkan)
- **media_player.nere** = All downstairs (Kocken, Kompis, Dobby, Vision)
- **media_player.party** = ALL 7 speakers everywhere!

### Disable for Weekends/Holidays:

Automations only run Monday-Friday, so weekends are already skipped!

For holidays:
1. **Settings** → **Automations & Scenes**
2. Toggle any automation **OFF** (turns grey)
3. Toggle back **ON** when you want it to resume

---

## Troubleshooting

**Automation didn't run:**
- Check it's enabled (toggle ON)
- Check it's a weekday (Mon-Fri only)
- Check the current time hasn't passed

**No sound:**
- Check speaker volume isn't muted
- Try test in Developer Tools first
- Make sure speaker isn't playing something else

**Wrong language/English voice:**
- Make sure `language: sv` is in the automation
- Some words might still sound English (normal with Google TTS)

---

## Want Better Voice Quality Later?

If the robotic voice bothers you or kids tune it out, you can upgrade to **OpenAI TTS** (~1 SEK/month) for natural-sounding voices.

Just:
1. Get OpenAI API key (5 minutes)
2. Change `tts.google_translate_say` to `tts.openai_say`
3. Remove `language: sv` line
4. That's it!

But test with Google TTS first - it might be perfectly fine! 🎉

---

## Summary

✅ **8 automations created** and enabled
✅ **Phone dashboard** with manual controls
✅ **All 7 speakers** mapped and working
✅ **Runs Monday-Friday** automatically
✅ **7:30 departure** timeline
✅ **FREE** forever!

Your mornings just got a LOT easier! 🌅
