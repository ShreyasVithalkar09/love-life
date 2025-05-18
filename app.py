import streamlit as st
import pandas as pd
import random
import time
import plotly.express as px

st.set_page_config(page_title="Love and Life", layout="centered")
st.title("❤️ Life and Love vs Time 📈")

custom_message = "No matter how the life gets, My love will always grow ❤️"

if st.button("Start Graphs"):
        life_data = []
        love_data = []
        time_data = []

        life_val = 0
        love_val = 0.0

        graph_placeholder = st.empty()
        start_time = time.time()

        while time.time() - start_time < 60:
            current_time = round(time.time() - start_time)

            life_val = random.randint(1, 10)
            love_val = round(love_val + 0.2, 2)

            time_data.append(current_time)
            life_data.append(life_val)
            love_data.append(love_val)

            df = pd.DataFrame({
            "Time (s)": time_data,
            "Life": life_data,
            "Love": love_data
            })

            # graphs
            # fig = px.line(df, x="Time (s)", y=["Life", "Love"], title="Life & Love Over Time", markers=True)
            import plotly.graph_objects as go

            fig = go.Figure()

            # Life trace (default color or blue)
            fig.add_trace(go.Scatter(
                x=time_data,
                y=life_data,
                mode='lines+markers',
                name='Life',
                line=dict(color='blue'),
                marker=dict(color='blue')
            ))

            # Love trace (purple)
            fig.add_trace(go.Scatter(
                x=time_data,
                y=love_data,
                mode='lines+markers',
                name='Love',
                line=dict(color='purple'),
                marker=dict(color='purple')
            ))

            fig.update_layout(
                title='Life & Love Over Time',
                xaxis_title='Time (s)',
                yaxis_title='Value',
                yaxis=dict(range=[0, max(10, max(love_data))])
            )


            fig.update_layout(yaxis_range=[0, max(10, max(love_data))])

            graph_placeholder.plotly_chart(fig, use_container_width=True)

            time.sleep(1)

        st.success(f"📢 {custom_message}")


