# streamlit_app.py
import json
import time

import numpy as np
import streamlit as st
import websockets

# ---------------- Config ----------------

FASTAPI_WS_URL = "ws://localhost:8000/ws/telemetry"

st.set_page_config(page_title="Organism Cockpit", layout="wide")
st.title("🧬 Organism Cockpit — FastAPI + Streamlit")

status_placeholder = st.empty()
placeholder = st.empty()

# ---------------- Telemetry loop ----------------

async def telemetry_loop():
    async with websockets.connect(FASTAPI_WS_URL) as ws:
        status_placeholder.success("Connected to FastAPI telemetry WebSocket")

        while True:
            msg = await ws.recv()
            out = json.loads(msg)

            with placeholder.container():
                col1, col2, col3 = st.columns(3)

                # Physics
                with col1:
                    st.subheader("⚙️ Physics")
                    st.write({
                        "lagrangian": out.get("lagrangian"),
                        "energy": out.get("energy"),
                        "density": out.get("density"),
                    })

                # Attention
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

                # Decision
                with col3:
                    st.subheader("🧭 Decision")
                    st.write(out.get("decision"))

                # Symbolic
                st.subheader("🔣 Symbolic Cortex")
                st.write(out.get("symbolic"))

                # STDP
                st.subheader("⚡ STDP")
                st.write(out.get("stdp"))

            time.sleep(0.05)

# ---------------- Run async from Streamlit ----------------

import asyncio

if "loop_started" not in st.session_state:
    st.session_state["loop_started"] = True
    asyncio.run(telemetry_loop())