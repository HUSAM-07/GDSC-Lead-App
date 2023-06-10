import streamlit as st

st.set_page_config(layout="wide")
st.markdown("[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=space+grotesk&pause=800&color=1C4C8F&width=435&lines=Hello+There!;I+am+HUSAM%2C+The+Marketing+Lead+%26+Technical+Executive+at+Google+DSC+BPDC)](https://git.io/typing-svg)")
def display_marketing_contributions():
    st.title("Marketing Contributions")
    
    marketing_contributions = [
        "1. Created engaging email content and social media posts for events, resulting in a good increase in open rates and click-through rates compared to normal marketing campaign( This number is with respect to my experience in other clubs )",
"2. Main Role: Designing Event Posts ( Instagram Visuals & Illustrations )",
"3. Directed marketing activities and campaigns, ensuring alignment with organizational goals and brand guidelines. Achieved 95% consistency in brand messaging across all marketing channels."
"4. Represented GDSC as the Marketing Team Representative at two physical inter-university GDSC Hackathons.(Only 2 were conducted this year)",
"5. Developed visually appealing GDSC BPDC branding logos that received positive feedback from of GDSC members.",
"6. Established and maintained the GDSC LinkTree page, achieving a good user satisfaction rating for ease of navigation and access to relevant content.",
"7. Managed the GDSC Instagram page, increasing follower count by 200%(1st Year so Pretty Obvious, No Reference Point 😅) and achieving an average engagement rate of 63% through compelling visuals and interactive posts. ( These Numbers are calculated with the help of Instagram's Professional Tools Dashboard )",
"8. Initiated discussions with Instagram to implement GDSC BPDC Verified stickers, aiming for a 15% increase in brand authenticity and trust next year.( In-Progress ) & ( Personal Initiative )",
"9. Created and optimized GDSC email templates, which will result in a drastic increase in email engagement and conversion rates through A/B testing and data-driven improvements. ( Personal Initiative )",
 "   1. Currently testing it ( Please Find the Demo Email Templates in the Drive Folder )",
"10. Led the design and production of GDSC merchandise, including bottles, caps, hoodies, and mugs, to promote brand visibility and foster a sense of community. ( Personal Initiative )",
"11. Designed GDSC Council Hoodie designs that received positive feedback from 95% of council members ( In-Progress )",
"12. Produced video teasers for Technofest GDSC BPDC Events, generating 200+ views and a 15% increase in event registrations.",
"13. Successfully marketed 13 out of 15 events( Was directly responsible for Marketing Them As a Marketing Manager Initially ), achieving an average event registration rate of 37% and receiving positive feedback on event promotion."
    ]
    
    for contribution in marketing_contributions:
        st.markdown(f"- {contribution}")

def display_technical_contributions():
    st.title("Technical Contributions")
    
    technical_contributions = [
        "Conducted an informative workshop on app design and branding with a focus on UI, UX, and Google's Material UI guidelines, receiving a 95% participant satisfaction rating.",
        "- Designed an App during the Workshop as a Design Tutorial.",
        "Developed a comprehensive live page for App Design workshop resources, receiving 98% positive feedback on organization and usability.",
        "- [App Design Workshop Resources](https://www.notion.so/App-Design-Workshop-Resources-5b998b35a2df48ffaeaf8ef1b02ead85?pvs=21)"
    ]
    
    for contribution in technical_contributions:
        st.markdown(f"- {contribution}")

def display_documentation():
    st.title("Documentation")
    
    documentation_contributions = [
        "Utilized web scraping techniques to gather accurate email IDs of 4th-year and 2nd-year students for targeted communication and outreach efforts.",
        "- This Data Is Now Available in the GDSC Main Dashboard",
        "Analyzed the Dashboard and Verified the Column Dependencies."
    ]
    
    for contribution in documentation_contributions:
        st.markdown(f"- {contribution}")

def display_pending_commitments():
    st.title("Pending Commitments")
    
    pending_commitments = [
        "Currently handling the marketing of GDSC council applications through a comprehensive recruitment campaign.",
        "Other Recruitment Activities"
    ]
    
    for contribution in pending_commitments:
        st.markdown(f"- {contribution}")

activities = [
    "Marketing",
    "Technical",
    "Documentation",
    "Pending Commitments"
]

# Sidebar navigation
st.sidebar.title("Navigation")
selected_activity = st.sidebar.radio("Go to", activities)

if selected_activity == "Marketing":
    display_marketing_contributions()
elif selected_activity == "Technical":
    display_technical_contributions()
elif selected_activity == "Documentation":
    display_documentation()
elif selected_activity == "Pending Commitments":
    display_pending_commitments()

st.markdown("[![Typing SVG](https://readme-typing-svg.herokuapp.com?font=space+grotesk&pause=800&color=1C4C8F&width=435&lines=Hello+There!;I+am+HUSAM%2C+The+Marketing+Lead+%26+Technical+Executive+at+Google+DSC+BPDC)](https://git.io/typing-svg)")