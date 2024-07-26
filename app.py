import streamlit as st

# Title of the app
st.title("Cool and Relevant Emojis")

# Emojis for different categories
smileys = [
    ":grinning:", ":smiley:", ":smile:", ":grin:", ":laughing:", ":sweat_smile:", ":joy:", "::", ":relaxed:", ":blush:",
    ":innocent:", ":slightly_smiling_face:", ":upside_down_face:", ":wink:", ":relieved:", ":heart_eyes:", "::",
    ":kissing_heart:", ":kissing:", ":kissing_smiling_eyes:", ":kissing_closed_eyes:", ":yum:", ":stuck_out_tongue:",
    ":stuck_out_tongue_winking_eye:", ":zany_face:", ":stuck_out_tongue_closed_eyes:", ":money_mouth_face:"
]

animals = [
    ":dog:", ":cat:", ":mouse:", ":hamster:", ":rabbit:", ":fox_face:", ":bear:", ":panda_face:", ":koala:", ":tiger:",
    "::", ":cow:", ":pig:", ":frog:", ":monkey_face:"
]

foods = [
    ":green_apple:", ":apple:", ":pear:", ":tangerine:", ":lemon:", ":banana:", ":watermelon:", ":grapes:", ":strawberry:",
    ":blueberries:", ":melon:", ":cherries:", ":peach:", ":mango:", ":pineapple:", ":coconut:", "::", ":tomato:",
    ":eggplant:", ":avocado:", ":broccoli:", ":cucumber:", ":hot_pepper:", ":bell_pepper:", ":corn:", ":carrot:",
    ":garlic:", ":onion:", ":potato:", ":sweet_potato:"
]

activities = [
    ":soccer:", ":basketball:", ":football:", ":baseball:", ":softball:", ":tennis:", ":volleyball:", ":rugby_football:",
    ":8ball:",":goal_net:", ":dart:", ":bowling:", ":video_game:", ":slot_machine:"
]

# Function to display emojis
def display_emojis(category, emojis):
    st.write(f"### {category}")
    st.write(' '.join([f"{e}" for e in emojis]))

# Displaying emojis by categories
display_emojis("Smileys and Emotions", smileys)
display_emojis("Animals and Nature", animals)
display_emojis("Food and Drink", foods)
display_emojis("Activities", activities)

# Combining all emojis
st.write("### All Emojis Combined")
all_emojis = smileys + animals + foods + activities
st.write(' '.join([f"{e}" for e in all_emojis]))
