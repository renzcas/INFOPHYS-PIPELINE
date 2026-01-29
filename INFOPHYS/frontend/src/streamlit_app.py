import json
import time

import numpy as np
import streamlit as st
import websockets
import asyncio

FASTAPI_WS_URL = "ws://localhost:8000/ws/telemetry"

st.set_page_config(page_title="Organism Cockpit", layout="wide")
st.title("🧬 Organism Cockpit — FastAPI + Streamlit")

status_placeholder = st.empty()
placeholder = st.empty()

async def telemetry_loop():
    async with websockets.connect(FASTAPI_WS_URL) as ws:
        status_placeholder.success("Connected to FastAPI telemetry WebSocket")

        while True:
            msg = await ws.recv()
            out = json.loads(msg)

            with placeholder.container():
                col1, col2, col3 = st.columns(3)

                with col1:
                    st.subheader("⚙️ Physics")
                    st.write({
                        "lagrangian": out.get("lagrangian"),
                        "energy": out.get("energy"),
                        "density": out.get("density"),
                    })

                with col2:
                    st.subheader("🎯 Attention")
                    att = out.get("attention", {})
                    vec = att.get("attention_vector", [])
                    if vec:
                        st.line_chart(vec)
                    st.write({
                        "density": att.get("density"),
                        "energy": att.get("energy"),
                    })

                with col3:
                    st.subheader("🧭 Decision")
                    st.write(out.get("decision"))

                st.subheader("🔣 Symbolic Cortex")
                st.write(out.get("symbolic"))

                st.subheader("⚡ STDP")
                st.write(out.get("stdp"))

            time.sleep(0.05)

async def start():
    await telemetry_loop()

if "loop_started" not in st.session_state:
    st.session_state["loop_started"] = True
    asyncio.create_task(start())