import streamlit as st

def set_space_grotesk_font_style():
    st.markdown(
        """
        <style>
        @import url('https://fonts.googleapis.com/css2?family=Space+Grotesk&display=swap');

        .space-grotesk {
            font-family: 'Space Grotesk', sans-serif;
        }
        </style>
        """,
        unsafe_allow_html=True
    )

def main():
    set_space_grotesk_font_style()

    st.markdown('<h1 class="space-grotesk">Hello, Space Grotesk!</h1>', unsafe_allow_html=True)
    st.markdown('<p class="space-grotesk">This is a text styled with Space Grotesk font.</p>', unsafe_allow_html=True)

if __name__ == "__main__":
    main()
