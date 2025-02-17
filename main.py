import streamlit as st
from streamlit_option_menu import option_menu
import os

#### Page Configuration ####
st.set_page_config(
    page_title = "New Fresha",
    layout = "wide"
)

#### Main App Setup ####

def main():
    
    #### Display Banner and apply menu
    with st.sidebar:
        page_selected = option_menu(
            menu_title = "Navigation Menu",
            options = ["Home", "Calender", "Sales", "Clients", "Catalog", "Online Booking", "Marketing", "Team", "Reports", "Settings"],
            default_index = 0
        )

    #### Dynamic module import and execution ####
    try:
        if page_selected == "Home":
            import home
            home.main()
        elif page_selected == "Calender":
            import calender
            calender.main()
        elif page_selected == "Sales":
            import sales
            sales.main()
        elif page_selected == "Clients":
            import clients
            clients.main()
        elif page_selected == "Catalog":
            import catalog
            catalog.main()
        elif page_selected == "Online Booking":
            import online_booking
            online_booking.main()
        elif page_selected == "Marketing":
            import marketing
            marketing.main()
        elif page_selected == "Team":
            import team
            team.main()
        elif page_selected == "Reports":
            import reports
            reports.main()
        elif page_selected == "Settings":
            import settings
            settings.main()
    except ImportError as e:
        st.error(f"Error loading module: {e}") 
   
    st.title("New Fresha")
    st.write("This is an attempt to make a new AI driven CRM Platform")

if __name__ == "__main__":
    main()