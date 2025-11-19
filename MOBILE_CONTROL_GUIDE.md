# Controlling Time Reminders from Your Phone

Easy ways to turn the morning reminders on/off from your Home Assistant app.

## Method 1: Built-in Controls (Easiest - No Setup!)

**This works right now without any changes:**

1. Open **Home Assistant app** on your phone
2. Tap **Settings** (gear icon at bottom)
3. Tap **Automations & Scenes**
4. You'll see all your morning reminders:
   - Morgonpåminnelse - 07:00
   - Morgonpåminnelse - 07:15
   - Morgonpåminnelse - 07:30
   - etc.
5. **Tap the toggle** next to any automation to turn it on/off

**Perfect for:**
- Turning off reminders on holidays
- Disabling specific times
- Quick on/off when kids are sick

---

## Method 2: Dashboard Card (Better!)

**Add controls to your main screen for quick access:**

### Step 1: Create the Dashboard Card

1. Open **Home Assistant app**
2. Go to your **Overview** (or any dashboard)
3. Tap the **pencil icon** (top right) to edit
4. Tap **+ Add Card** (bottom right)
5. Scroll down and tap **Manual**
6. **Copy and paste this:**

```yaml
type: entities
title: ⏰ Morgonpåminnelser
entities:
  - entity: automation.morning_reminder_swedish_0700
    name: "Kl 07:00"
  - entity: automation.morning_reminder_swedish_0715
    name: "Kl 07:15"
  - entity: automation.morning_reminder_swedish_0730
    name: "Kl 07:30"
  - entity: automation.morning_reminder_swedish_0745
    name: "Kl 07:45"
  - entity: automation.morning_reminder_swedish_0755
    name: "Kl 07:55"
show_header_toggle: true
```

7. Tap **Save**
8. Tap **Done** (top right)

**Now you have:**
- Quick toggles for each time
- Master "all on/off" toggle at the top
- Always visible on your main screen

---

## Method 3: Master Switch (Most Convenient!)

**One switch to rule them all - turn everything on/off at once.**

### Step 1: Add Master Switch to Configuration

1. In Home Assistant, open **File Editor**
2. Open `configuration.yaml`
3. Add this section:

```yaml
input_boolean:
  morning_reminders_enabled:
    name: Morgonpåminnelser aktiverade
    initial: true
    icon: mdi:alarm
```

4. Save and **restart Home Assistant**

### Step 2: Update Each Automation

For **each** morning reminder automation, add this condition at the top of the `condition:` section:

```yaml
condition:
  - condition: state
    entity_id: input_boolean.morning_reminders_enabled
    state: "on"
  - condition: time
    weekday:
      - mon
      - tue
      - wed
      - thu
      - fri
```

### Step 3: Add Dashboard Control

Add this simple card to your dashboard:

```yaml
type: entities
entities:
  - entity: input_boolean.morning_reminders_enabled
    name: "Morgonpåminnelser"
```

**Now you can:**
- Toggle one switch to enable/disable ALL reminders
- Perfect for vacations, weekends, sick days

---

## Method 4: Quick Actions Widget (iOS/Android)

**Add Home Assistant widgets to your phone's home screen:**

### iOS:
1. Long-press home screen → Add Widget
2. Find **Home Assistant**
3. Choose widget size
4. Edit widget → select your automation toggles

### Android:
1. Long-press home screen → Widgets
2. Find **Home Assistant**
3. Drag widget to home screen
4. Configure to show automation toggles

**Control reminders without even opening the app!**

---

## Method 5: Voice Control (If you have Google Assistant)

If your Home Assistant is connected to Google Assistant:

- "Hey Google, turn off morning reminders"
- "Hey Google, turn on 7:30 alarm automation"

Set this up in Home Assistant → Integrations → Google Assistant

---

## Common Scenarios

### Scenario: School Holiday / Vacation

**Option A (Quick):**
1. Open HA app → Settings → Automations
2. Toggle off all morning reminders

**Option B (If you have master switch):**
1. Open HA app
2. Find "Morgonpåminnelser" switch
3. Turn off

### Scenario: Kids Sleeping In (Sick Day)

**Just disable for today:**
1. Open HA app → Settings → Automations
2. Toggle off each automation
3. They'll automatically turn back on tomorrow (they only run on weekdays anyway)

### Scenario: Different Schedule on Certain Days

**Create a Scene:**
1. Set automations how you want them (some on, some off)
2. Go to Settings → Scenes
3. Create Scene → Save current state
4. Name it (e.g., "Sen morgon")
5. Add scene button to dashboard

Now you can activate "Sen morgon" with one tap!

---

## My Recommendation

**Start with Method 1** (built-in controls) - it works right now, no setup needed.

**Then add Method 2** (dashboard card) when you get comfortable - takes 2 minutes and makes it much more convenient.

**Add Method 3** (master switch) if you find yourself turning all reminders on/off frequently.

---

## Quick Reference

### Turn Off All Reminders (Method 1)
Settings → Automations & Scenes → Toggle each one off

### Turn Off All Reminders (Method 2)
Dashboard → Morgonpåminnelser card → Toggle master switch at top

### Turn Off All Reminders (Method 3)
Dashboard → "Morgonpåminnelser aktiverade" → Toggle off

### Test a Reminder Right Now
Dashboard → Your control card → "Test nu" button

---

## Troubleshooting

**Q: I turned off an automation but it still ran**
- Automations only check their conditions when triggered
- If you turn it off at 7:01, the 7:00 reminder already ran
- Turn it off the night before to prevent morning reminders

**Q: Where do I find my automations in the app?**
- Bottom navigation: Settings (gear icon)
- Or: Sidebar menu → Settings → Automations & Scenes

**Q: Can I schedule automatic on/off?**
- Yes! Create an automation that turns on/off the master switch
- Example: "Turn off morning reminders on Saturdays"

**Q: Can I change times from my phone?**
- Not directly - you need to edit the automation
- In the app: Settings → Automations → Select automation → Edit
- Change the time in the trigger section

---

## Pro Tips

1. **Create a dedicated dashboard** just for morning routines:
   - Add controls for reminders
   - Add manual announcement buttons
   - Add light controls for kids' rooms
   - Name it "Morgonrutin" and add to sidebar

2. **Use notification automation** to remind yourself:
   ```yaml
   automation:
     - trigger:
         - platform: time
           at: "22:00:00"
       action:
         - service: notify.mobile_app_your_phone
           data:
             message: "Kom ihåg att kolla morgonpåminnelserna för imorgon!"
   ```

3. **Weekend auto-disable**:
   ```yaml
   automation:
     - trigger:
         - platform: time
           at: "20:00:00"
       condition:
         - condition: time
           weekday:
             - fri
       action:
         - service: input_boolean.turn_off
           target:
             entity_id: input_boolean.morning_reminders_enabled
   ```

4. **Add to Home Assistant widget** on your phone for instant access without opening the app

---

## See Also

- `mobile_control_panel.yaml` - Full-featured control panel with all options
- `dashboard_card_swedish.yaml` - Swedish dashboard with manual controls
- `home_assistant_automations_openai_swedish.yaml` - The actual automations
