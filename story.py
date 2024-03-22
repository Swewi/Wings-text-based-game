# Wings Game Story Description
# The dictionary, 'wings_text', contains the narrative steps and
# choices for the text-based adventure game 'Wings'. It provides the
# story line, options, and outcomes for the player's journey in the game.

wings_text = {
            "start": {
                "step_text": """
**--------------------------------------------------------------------------**
        After a nice clean takeoff, you are on your way home.
        It has been a tough couple of weeks getting things finished
        before your final assessment, and this is your last check flight!
        You know there is weather coming but you should miss it.
        As you fly your mind wanders food and dinner, you realise you haven't
        been paying attention to your surroundings, it comes as a bit of a
        surprise when you see the massive weather front ahead, realising you
        can't get through, or over it, you'll have to go around it instead.

        Which direction are you going to choose?

**--------------------------------------------------------------------------**
        Option 1: Turn East.
        Option 2: Turn West.
**--------------------------------------------------------------------------**
                     """,
                "options": {
                    "option_1": "east",
                    "option_2": "west"
                }
            },

            "east": {
                "step_text": """
**--------------------------------------------------------------------------**
        Upon turning east, you face navigation problems, your compass
        begins to behave erratically and the GPS screen shows random
        locations.  Now you are in trouble, if you can't rely on your
        instruments all your navigational abilities are for nothing,
        this could end very badlly.

        You must choose between sticking with your current radio code
        or switching to an emergency frequency.

        Are you going to change codes?

**--------------------------------------------------------------------------**
        Option 1: Don't change the code.
        Option 2: Change the code.
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "no_change",
                    "option_2": "change"
                }
            },

            "no_change": {
                "step_text": """
**--------------------------------------------------------------------------**
        As you fly on you use the radio to contact air traffic control they
        inform you that you are close to land, but you can't see it.

        Do you keep heading east and trust air traffic control?

**--------------------------------------------------------------------------**
        Option 1: Do you continue east and trust ATC?
        Option 2: Do you change direction?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "atc_east",
                    "option_2": "turn_away"
                }
            },

            "atc_east": {
                "step_text": """
**--------------------------------------------------------------------------**
        Despite your confusion, you maintain radio contact with air traffic
        control, who continue to assure you that you're over land,
        despite your view of nothing but ocean.

        As the time ticks on you realise that your fuel is running out,
        even though you had plenty to get home and a healthy reserve
        the tanks are nearly empty.

        Upon realizing your fuel is critically low, you're compelled to
        try a risky ocean landing, reminiscent of Captain Sully's
        famous maneuver...
                """,
                "options": {},
                "outcome": "failure"

            },

            "turn_away": {
                "step_text": """
**--------------------------------------------------------------------------**
        Trusting your instincts, you decide to alter your course,
        and quickly realise you made a good choice, despite some cloud still
        floating about you can see land ahead.

        As relief sweeps over you, the altimeter warns you that you are low
        and losing height rapidly, you're going to have to land out.
        Thankfully you seem to be over fields, after a quick assessment
        you pick one that looks flat and cow free!

        You must decide between an immediate landing or conducting a
        brief fly-by for assessment.

**--------------------------------------------------------------------------**
        Option 1: Do you land immediately?
        Option 2: Do you perform a quick fly over to check conditions?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "land_now",
                    "option_2": "fly_past"
                }
            },

            "land_now": {
                "step_text": """
**--------------------------------------------------------------------------**
        Just as you pass over the boundary fence of the field you catch
        a sudden wind shift, it catches a wing, you swear a lot...
                """,
                "options": {},
                "outcome": "failure"
            },

            "fly_past": {
                "step_text": """
**--------------------------------------------------------------------------**
        Your cautious approach proves successful!

        You identify a couple of potential hazards and execute a safe landing.
                """,
                "options": {},
                "outcome": "success"
            },

            "change": {
                "step_text": """
**--------------------------------------------------------------------------**
        You reach over to change radio codes, suddenly you have a
        brain fart and can't remember the right frequency.
        You know it starts with a 7 and has 4 digits.

        The sticker on the dashboard has 3 codes which one do pick?

**--------------------------------------------------------------------------**
        Option 1: Do you choose '7700'?
        Option 2: Or one of the other codes?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "right_code",
                    "option_2": "other_code"
                }
            },

            "right_code": {
                "step_text": """
**--------------------------------------------------------------------------**
        Success!

        Air Traffic Control contact you, realising that something is
        really wrong they send up an aircraft to find you and escort
        you to the nearest airfield...
                """,
                "options": {},
                "outcome": "success"
            },

            "other_code": {
                "step_text": """
**--------------------------------------------------------------------------**
        You didn't think it was '7700' so that left two options.

**--------------------------------------------------------------------------**
        Option 1: Do you choose '7500'?
        Option 2: Or '7200'?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "wrong_code",
                    "option_2": "alt_code"
                }
            },

            "wrong_code": {
                "step_text": """
**--------------------------------------------------------------------------**
        Almost immediately you realise that was the wrong code to use,
        suddenly there are weird lights all around you, you feel weightless,
        and trapped all at the same time!

        The aliens had finally got you…
                """,
                "options": {},
                "outcome": "failure"
            },

            "alt_code": {
                "step_text": """
**--------------------------------------------------------------------------**
        You change the code to '7200' nothing changes, it might be
        time to decide to turn back.

        Do you turn back?

**--------------------------------------------------------------------------**
        Option 1: Do you turn back?
        Option 2: Or do you continue on?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "turn_back",
                    "option_2": "keep_going"
                }
            },

            "west": {
                "step_text": """
**--------------------------------------------------------------------------**
        Although turning west takes you away from your destination
        it looks like the weather is beter in that direction,
        and you have plenty of fuel.

        After awhile you notice a break in the weather, it looks a bit
        like a valley!

        Do you take a chance and fly through the weather valley?

**--------------------------------------------------------------------------**
        Option 1: Do you risk it?
        Option 2: Or do you continue on?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "risk_it",
                    "option_2": "going_on"
                }
            },

            "risk_it": {
                "step_text": """
**--------------------------------------------------------------------------**
        As you approach the weather valley you admire the texture of
        the clouds, it looks amazing from the outside, lets hope it's
        a good choice.

        The weather valley proved to be a great option it was so smooth
        you make quick passage.

        Once you are clear you need to choose a direction again.

**--------------------------------------------------------------------------**
        Option 1: Turn West again?
        Option 2: Or turn East this time?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "west_again",
                    "option_2": "east_again"
                }
            },

            "west_again": {
                "step_text": """
**--------------------------------------------------------------------------**
        Looking west you realise you can just make out the coast!

        Not only is it the coast, but it is part of the coast you recognise,
        you grew up around here and know where the local airfield is!

        Touching down safely is the best feeling!
                """,
                "options": {},
                "outcome": "success"
            },

            "east_again": {
                "step_text": """
**--------------------------------------------------------------------------**
        You can see lights off in the distance, that must be land?
        Turning east you fly on, mile upon mile of ocean flow under
        your wings slowly draining your concentration and focus.

        You slowly realise that you don't seem to be getting closer
        to the lights.

        Do you change direction or continue on towards the lights?

**--------------------------------------------------------------------------**
        Option 1: Do you change direction?
        Option 2: Or continue towards the lights?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "turn_away",
                    "option_2": "the_lights"
                }
            },

            "the_lights": {
                "step_text": """
**--------------------------------------------------------------------------**
        Oh dang it!

        You realise way too late, you should have turned sooner,
        eventually you turn but too late...

        You run out of fuel...
                """,
                "options": {},
                "outcome": "failure"
            },

            "going_on": {
                "step_text": """
**--------------------------------------------------------------------------**
        You can see lights in the distance and decide to continue on
        towards them thinking it's the coast.

        As the miles role by you realise the lights are a lot further away,
        you have to decide when or if to turn back.
        Finding an alternative route might be your best option.

        You let a few more miles role on before you make the decision.

**--------------------------------------------------------------------------**
        Option 1: Do you continue flying towards the lights?
        Option 2: Or do you turn towards back?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "turn_back",
                    "option_2": "alt_lights"
                }
            },

            "alt_lights": {
                "step_text": """
**--------------------------------------------------------------------------**
        Well that was a mistake!

        Aliens finally caught up with you...
                """,
                "options": {},
                "outcome": "failure"
            },

            "turn_back": {
                "step_text": """
**--------------------------------------------------------------------------**
        Having turned back you are conscious of your fuel consumption,
        and potential range remaining.
        You are starting to panic a little!

        Working hard to focus on the situation and reverting to
        basic principles of scanning and looking, you refocus,
        it helps you realise that things aren't going well,
        your fuel is getting low, your flying hours are running out
        and night is coming in.

        The storm front has well and truly passed by now,
        it has made the air clear and visibility is much higher now,

        You can just about make out land off to your left.
        Do you turn towards it?

**--------------------------------------------------------------------------**
        Option 1: Do turn towards the possibility of land?
        Option 2: Or do you continue on?
**--------------------------------------------------------------------------**
                """,
                "options": {
                    "option_1": "turn_land",
                    "option_2": "flying_on"
                }
            },

            "flying_on": {
                "step_text": """
**--------------------------------------------------------------------------**
        After a lot more miles you realise you made a massive mistake.

        Your fuel gauge hits empty,
        the engine splutters,
        you do your best to maintain a sensible glide path.

        Maybe you can survive this...
                """,
                "options": {},
                "outcome": "failure"
            },

            "turn_land": {
                "step_text": """
**--------------------------------------------------------------------------**
        You turn towards the possibility of land, the chance of a safe
        landing and survival.

        As you get closer the shadow resolves into land!

        Although the area is unknown to you, flying over land is a huge relief,
        in the distance you can see a large open area that you can land in,
        it looks like a small airfield.

        The relief you feel as you touchdown, amazing...
                """,
                "options": {},
                "outcome": "success"
            }
}
