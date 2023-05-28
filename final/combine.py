import streamlit as st
from youtube import youmain
from speech import spmain
from pdfsummerizer import pdfsummerizermain
def main():
    st.title("Combined Streamlit App")

    # Sidebar for app selection
    app_selection = st.sidebar.radio("Select App", ["App 1", "App 2","App 3"])

    # Display App 1
    if app_selection == "App 1":
        youmain()

    # Display App 2
    elif app_selection == "App 2":
        spmain()
    # Display App 3
    elif app_selection == "App 3":
        pdfsummerizermain()

if __name__ == "__main__":
    main()
