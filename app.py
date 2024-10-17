import streamlit as st
import pandas as pd

# Coefficients from your model
coefficients = {
    "Peer Pressure Influence": 0.1148,
    "Family Influence": 0.0574,
    "Curiosity Influence": 0.0739,
    "Addiction Influence": 0.0439,
    "Marketing Influence": 0.1233,
    "Availability Influence": 0.1239,
    "Stress Influence": 0.0406,
    "Media Influence": 0.0268,
}

# Explanations for each influence
explanations = {
    "Peer Pressure Influence": "A unit increase in peer pressure results in an increase in vapes per day.",
    "Family Influence": "Family influence can drive higher usage, increasing the number of vapes per day.",
    "Curiosity Influence": "Curiosity has a significant positive impact, leading to more vapes per day.",
    "Addiction Influence": "Addiction directly increases the frequency of vaping.",
    "Marketing Influence": "Marketing influence increasess the chances of more frequent vaping.",
    "Availability Influence": "More availability increases the chances of more frequent vaping.",
    "Stress Influence": "Stress causes a slight increase in vapes per day.",
    "Media Influence": "Media has a small positive impact on vaping behavior."
}

# Streamlit App
st.title("Impact of Influences on Predicted Vapes/Cigarettes per Day")

# Sidebar sliders for influence values
peer_pressure = st.sidebar.slider("Peer Pressure Influence", 0, 5, 1)
family_influence = st.sidebar.slider("Family Influence", 0, 5, 1)
curiosity_influence = st.sidebar.slider("Curiosity Influence", 0, 5, 1)
addiction_influence = st.sidebar.slider("Addiction Influence", 0,5, 1)
marketing_influence = st.sidebar.slider("Marketing Influence", 0, 5, 1)
availability_influence = st.sidebar.slider("Availability Influence", 0, 5, 1)
stress_influence = st.sidebar.slider("Stress Influence", 0, 5, 1)
media_influence = st.sidebar.slider("Media Influence", 0, 5, 1)

# Function to calculate the predicted vapes per day
def calculate_vapes_per_day():
    vapes_per_day = (
        peer_pressure * coefficients["Peer Pressure Influence"]
        + family_influence * coefficients["Family Influence"]
        + curiosity_influence * coefficients["Curiosity Influence"]
        + addiction_influence * coefficients["Addiction Influence"]
        + marketing_influence * coefficients["Marketing Influence"]
        + availability_influence * coefficients["Availability Influence"]
        + stress_influence * coefficients["Stress Influence"]
        + media_influence * coefficients["Media Influence"]
        + 2.0  # intercept
    )
    return vapes_per_day

# Calculate the predicted vapes per day
predicted_vapes_per_day = calculate_vapes_per_day()

# Display the predicted vapes per day with a progress bar
st.write(f"### Predicted Vapes/Cigarettes per Day: {predicted_vapes_per_day:.2f}")

# Progress bar to represent vapes per day
st.progress(min(max(predicted_vapes_per_day / 10, 0), 1))  # normalized between 0 and 1 for the progress bar

# Create a DataFrame to show the table of influences, coefficients, and explanations
influence_data = {
    "Influence": list(coefficients.keys()),
    "Coefficient": list(coefficients.values()),
    "Explanation": [explanations[key] for key in coefficients.keys()],
    "Formula Contribution": [
        f"{influence} * {coeff:.4f}" for influence, coeff in coefficients.items()
    ]
}

df_influences = pd.DataFrame(influence_data)

# Display the table
st.write("### Table of Influences, Coefficients, and Explanations")
st.dataframe(df_influences)

# Display explanation for how vapes per day is calculated
st.write("""
#### How the Prediction is Calculated:
The number of vapes per day is calculated as the weighted sum of the different influences based on their coefficients.
The formula for this is:

$$
Vapes\ per\ Day = (Peer\ Pressure\ Influence  \\times 0.1148) + (Family\ Influence \\times 0.0574) 
+ (Curiosity\ Influence \\times 0.0739) + (Addiction\ Influence \\times 0.0439) + (Marketing\ Influence \\times -0.1233) 
+ (Availability\ Influence \\times 0.1239) + (Stress\ Influence \times 0.0406) + (Media\ Influence \\times 0.0268)
$$

Each influence either increases or decreases the predicted vapes per day depending on whether its coefficient is positive or negative. 
For example, increasing Peer Pressure Influence will lead to a higher prediction, while increasing Marketing Influence will decrease the predicted vapes per day.
""")

# Detailed explanation of the influences
st.write("""
### Detailed Explanation of Each Influence:
- **Peer Pressure Influence**: Higher peer pressure is associated with more frequent vaping, increasing the number of vapes per day.
- **Family Influence**: If family members are involved or influencing, this tends to push vaping behavior higher.
- **Curiosity Influence**: A higher level of curiosity often drives individuals to vape more frequently.
- **Addiction Influence**: Addiction has a direct positive effect on vaping behavior.
- **Availability Influence**: When vapes are more available, the frequency of usage increases.
- **Stress Influence**: Stress leads to a moderate increase in vaping frequency.
- **Media Influence**: Media exposure has a small positive effect, slightly increasing the number of vapes per day.
""")
