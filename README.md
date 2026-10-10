# SEETI — simple pressure cooker companion

A one-tap Streamlit prototype for Indian kitchens.

## Run

```bash
pip install -r requirements.txt
streamlit run app.py
```

Choose your food and start a session. The whistle button simulates a hardware event. This is **not** real whistle detection; real detection requires an external sensor and firmware integration. No pressure or food-readiness measurement is performed.

## Next hardware milestone

ESP32 + microphone listens for whistle signatures and sends detected events to the app. Validate false positives and missed detections with different cooker models and background sounds. Keep electronics away from heat and steam.

## Safety

Never leave a lit stove unattended. Do not use this app to decide when it is safe to open a cooker. Follow the cooker's instructions.
