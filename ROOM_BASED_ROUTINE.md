# Room-Based Morning Routine

Smart announcements that follow your kids through their morning routine,
speaking in the room they're likely to be in at each time.

## The Concept

Instead of announcing everything to one speaker, we track the typical morning
flow and speak to different rooms:

**Typical Morning Flow:**
1. **Bedroom** (7:00-7:10) - Wake up, get out of bed
2. **Kitchen** (7:10-7:25) - Breakfast
3. **Bathroom** (7:25-7:35) - Wash face, brush teeth
4. **Bedroom** (7:35-7:45) - Get dressed, make bed
5. **Living Room/Hall** (7:45-8:00) - Shoes, jacket, bag, final checks

## Setup Requirements

You'll need Google Home speakers in different rooms. Common setup:
- **Bedroom Mini** - `media_player.kids_room_mini` or separate for each kid
- **Kitchen Speaker** - `media_player.kitchen_speaker`
- **Bathroom Mini** - `media_player.bathroom_mini` (optional but helpful!)
- **Living Room Speaker** - `media_player.living_room_speaker`

Don't have speakers in every room? No problem - we'll announce to nearby rooms.

## Complete Room-Based Routine

Here's a full morning routine that follows kids through the house:

```yaml
automation:
  # ============================================
  # BEDROOM - Wake Up Phase (7:00-7:10)
  # ============================================

  - id: bedroom_wake_up_0700
    alias: "🛏️ Sovrum - Väckning 07:00"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # Gentle volume for wake-up
      - service: media_player.volume_set
        target:
          entity_id: media_player.kids_room_mini
        data:
          volume_level: 0.3

      # Wake up announcement
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "God morgon! Dags att vakna. Klockan är 7, en timme tills vi måste gå."

  - id: bedroom_get_up_0705
    alias: "🛏️ Sovrum - Gå upp 07:05"
    trigger:
      - platform: time
        at: "07:05:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "Dags att gå upp ur sängen nu. Frukosten väntar om 5 minuter!"

  # ============================================
  # KITCHEN - Breakfast Phase (7:10-7:25)
  # ============================================

  - id: kitchen_breakfast_0710
    alias: "🍳 Kök - Frukost 07:10"
    trigger:
      - platform: time
        at: "07:10:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.kitchen_speaker
        data:
          volume_level: 0.4

      - service: tts.openai_say
        target:
          entity_id: media_player.kitchen_speaker
        data:
          message: "Frukostdags! Kom till köket och sätt dig vid bordet. 50 minuter kvar."

  - id: kitchen_eat_up_0720
    alias: "🍳 Kök - Ät upp 07:20"
    trigger:
      - platform: time
        at: "07:20:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kitchen_speaker
        data:
          message: "Ät upp så att du hinner bli klar. 40 minuter kvar. Snart dags att borsta tänderna."

  # ============================================
  # BATHROOM - Hygiene Phase (7:25-7:35)
  # ============================================

  - id: bathroom_teeth_0725
    alias: "🚿 Badrum - Tänder 07:25"
    trigger:
      - platform: time
        at: "07:25:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      # If you have bathroom speaker
      - service: tts.openai_say
        target:
          entity_id: media_player.bathroom_mini  # or kitchen if no bathroom speaker
        data:
          message: "Dags att gå till badrummet. Tvätta ansiktet och borsta tänderna ordentligt!"

  - id: bathroom_finish_up_0732
    alias: "🚿 Badrum - Gör klart 07:32"
    trigger:
      - platform: time
        at: "07:32:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.bathroom_mini
        data:
          message: "Är du klar? Dags att gå och klä på dig nu!"

  # ============================================
  # BEDROOM - Getting Dressed Phase (7:35-7:45)
  # ============================================

  - id: bedroom_get_dressed_0735
    alias: "🛏️ Sovrum - Klä på dig 07:35"
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
          message: "Tillbaka till sovrummet! Klä på dig och gör i ordning. 25 minuter kvar."

  - id: bedroom_make_bed_0742
    alias: "🛏️ Sovrum - Bädda 07:42"
    trigger:
      - platform: time
        at: "07:42:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "Glöm inte att bädda sängen! Sedan går du till hallen."

  # ============================================
  # LIVING ROOM/HALL - Final Prep (7:45-8:00)
  # ============================================

  - id: hall_prep_0745
    alias: "🚪 Hall - Förberedelser 07:45"
    trigger:
      - platform: time
        at: "07:45:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: media_player.volume_set
        target:
          entity_id: media_player.living_room_speaker
        data:
          volume_level: 0.5

      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "15 minuter kvar! Kom till hallen. Ta på dig skor och jacka. Kolla att skolväskan är packad."

  - id: hall_check_bag_0750
    alias: "🚪 Hall - Kolla väskan 07:50"
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
          message: "10 minuter! Har du allt? Böcker, matlåda, vattenflaska? Kolla igenom nu!"

  - id: hall_final_warning_0755
    alias: "🚪 Hall - Sista varningen 07:55"
    trigger:
      - platform: time
        at: "07:55:00"
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
          message: "5 MINUTER KVAR! Alla ska vara vid dörren med jacka och skor på NU!"

  - id: hall_departure_0758
    alias: "🚪 Hall - Avgång 07:58"
    trigger:
      - platform: time
        at: "07:58:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "TVÅ MINUTER! Vi går nu! Till bilen/dörren omedelbart!"
```

## Visual Timeline

```
07:00  🛏️ Bedroom    "God morgon! Dags att vakna"
07:05  🛏️ Bedroom    "Gå upp ur sängen"
07:10  🍳 Kitchen    "Frukostdags! Kom till köket"
07:20  🍳 Kitchen    "Ät upp, snart dags för tänderna"
07:25  🚿 Bathroom   "Tvätta ansiktet och borsta tänderna"
07:32  🚿 Bathroom   "Gör klart, dags att klä på dig"
07:35  🛏️ Bedroom    "Klä på dig och gör i ordning"
07:42  🛏️ Bedroom    "Bädda sängen, sedan till hallen"
07:45  🚪 Hall       "Ta på skor och jacka, kolla väskan"
07:50  🚪 Hall       "Har du allt? Kolla igenom!"
07:55  🚪 Hall       "5 MINUTER KVAR!"
07:58  🚪 Hall       "TVÅ MINUTER! Vi går nu!"
```

## Multiple Kids in Different Rooms

If you have kids in separate bedrooms:

```yaml
# Emma's room (older, leaves at 8:00)
automation:
  - id: emma_wake_up
    alias: "Emma - Väckning"
    trigger:
      - platform: time
        at: "07:00:00"
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.emmas_room_mini
        data:
          message: "God morgon Emma! Dags att vakna."

# Oskar's room (younger, leaves at 8:15)
  - id: oskar_wake_up
    alias: "Oskar - Väckning"
    trigger:
      - platform: time
        at: "07:10:00"  # Sleeps 10 min longer
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.oskars_room_mini
        data:
          message: "God morgon Oskar! Upp och hoppa nu!"

# Then both get kitchen announcements
  - id: breakfast_both
    alias: "Frukost - Båda"
    trigger:
      - platform: time
        at: "07:20:00"
    action:
      - service: tts.openai_say
        target:
          entity_id:
            - media_player.kitchen_speaker
            - media_player.emmas_room_mini
            - media_player.oskars_room_mini
        data:
          message: "Alla till köket för frukost nu!"
```

## Smart Escalation

Get progressively louder and more urgent as time runs out:

```yaml
# 7:00 - Very quiet, gentle wake-up (bedroom only)
volume_level: 0.3
message: "God morgon..." (soft)

# 7:30 - Normal volume (current room)
volume_level: 0.4
message: "30 minuter kvar" (normal)

# 7:45 - Louder (hall/common area)
volume_level: 0.5
message: "15 minuter kvar!" (firm)

# 7:55 - LOUD (all speakers!)
volume_level: 0.7
entity_id: [all speakers]
message: "5 MINUTER! ALLA TILL HALLEN!" (urgent)
```

## Don't Have Speakers in Every Room?

**No bathroom speaker?** Announce from kitchen or bedroom:
```yaml
# Before bathroom time
- service: tts.openai_say
  target:
    entity_id: media_player.kitchen_speaker
  data:
    message: "Dags att gå till badrummet nu!"
```

**Only have 2-3 speakers?** Use strategic placement:
- **Bedroom** - Wake up, get dressed
- **Kitchen/Living** - All other announcements
- **Add bathroom later** - It's surprisingly useful!

## Advanced: Add Time References

Make messages dynamic based on actual time remaining:

```yaml
- service: tts.openai_say
  target:
    entity_id: media_player.kids_room_mini
  data:
    message: >
      {% set target = today_at('08:00') %}
      {% set minutes = ((target - now()).total_seconds() / 60) | int %}
      God morgon! {{ minutes }} minuter tills vi måste gå. Upp ur sängen nu!
```

## Pro Tips

### 1. Follow the Physical Flow
Think about where kids physically move:
- Morning: Bedroom → Kitchen → Bathroom → Bedroom → Hall
- After school: Hall → Kitchen → Bedroom (homework)
- Evening: Living room → Bathroom → Bedroom

### 2. Use Nearby Speakers for Transitions
Before they move to next location, announce from where they're going:
```yaml
# At 7:08, announce from kitchen to pull them there
- entity_id: media_player.kitchen_speaker
  message: "Frukosten är klar! Kom nu!"
```

### 3. Double-Announce Important Things
For critical reminders, announce in current AND next room:
```yaml
entity_id:
  - media_player.kids_room_mini
  - media_player.living_room_speaker
message: "5 minuter kvar! Alla till hallen NU!"
```

### 4. Different Tones for Different Rooms
- **Bedroom** - Gentle, encouraging
- **Kitchen** - Practical, task-focused
- **Bathroom** - Specific instructions
- **Hall** - Urgent, checklist-style

### 5. Weekend Different Routine
Different room flow on weekends:
```yaml
condition:
  - condition: time
    weekday: [sat, sun]
action:
  # Weekend: Stay in bedroom longer, no rush
  - service: tts.openai_say
    target:
      entity_id: media_player.kids_room_mini
    data:
      message: "God morgon! Det är helg, ni kan ta det lugnt idag."
```

## Testing Your Room Flow

Test the sequence manually:

1. **Developer Tools** → **Services**
2. Test each room in order:
```yaml
# Test 1: Bedroom
service: tts.openai_say
data:
  entity_id: media_player.kids_room_mini
  message: "Test sovrumshögtalare"

# Test 2: Kitchen
service: tts.openai_say
data:
  entity_id: media_player.kitchen_speaker
  message: "Test kökshögtalare"

# And so on...
```

3. Walk through your house and verify you can hear each announcement clearly

## Troubleshooting

**Kids don't move to the next room:**
- Add transition announcements 2-3 minutes before
- Make the "pull" message more enticing
- Volume up to grab attention

**Multiple kids, different speeds:**
- Create separate automation sets per kid
- Use their names in messages
- Different speakers for each bedroom

**Can't hear in certain rooms:**
- Add a speaker (minis are cheap!)
- Or increase volume for that room
- Or announce from nearest room

## Example: Complete Morning Flow (Copy-Paste Ready)

Minimal version if you only have 2-3 speakers:

```yaml
automation:
  # Bedroom - Wake up
  - id: morning_bedroom
    alias: "Morgon - Sovrum"
    trigger:
      - platform: time
        at: "07:00:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.kids_room_mini
        data:
          message: "God morgon! Upp och hoppa. Frukosten är klar om 10 minuter."

  # Kitchen - Breakfast
  - id: morning_kitchen
    alias: "Morgon - Kök"
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
          message: "Frukost nu! Ät ordentligt så att du orkar hela dagen."

  # Hall - Final prep
  - id: morning_hall
    alias: "Morgon - Hall"
    trigger:
      - platform: time
        at: "07:45:00"
    condition:
      - condition: time
        weekday: [mon, tue, wed, thu, fri]
    action:
      - service: tts.openai_say
        target:
          entity_id: media_player.living_room_speaker
        data:
          message: "15 minuter! Skor, jacka, skolväska. Kolla att du har allt!"
```

## Customization Template

Replace with your actual speaker names and times:

```yaml
# YOUR MORNING FLOW
# Adjust times based on your routine

07:XX  🛏️ media_player.YOUR_BEDROOM     "YOUR MESSAGE"
07:XX  🍳 media_player.YOUR_KITCHEN      "YOUR MESSAGE"
07:XX  🚿 media_player.YOUR_BATHROOM     "YOUR MESSAGE"
07:XX  🚪 media_player.YOUR_HALL         "YOUR MESSAGE"
```

The key is matching announcements to where kids actually are!
