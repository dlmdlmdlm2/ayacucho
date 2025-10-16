# batalla_ayacucho_app.py
# App informativa sobre la Batalla de Ayacucho (Perú, 1824)

import streamlit as st

st.set_page_config(page_title="Batalla de Ayacucho", page_icon="🇵🇪", layout="centered")

st.title("⚔️ Batalla de Ayacucho (1824)")
st.subheader("Datos Generales — Perú")

st.markdown("""
**Fecha:** 9 de diciembre de 1824  
**Lugar:** Pampas de la Quinua, distrito de Quinua, región Ayacucho, Perú  
**Altitud:** Aproximadamente 3,400 metros sobre el nivel del mar
""")

st.divider()

st.markdown("### 👥 Comandantes Principales")
st.write("- **Patriotas:** Antonio José de Sucre")
st.write("- **Realistas:** José de La Serna (Virrey) y José de Canterac")

st.divider()

st.markdown("### 🏁 Resultado y Consecuencias")
st.write("**Resultado:** Victoria del Ejército Unido Libertador")
st.write("**Consecuencia:** Rendición del ejército realista mediante la Capitulación de Ayacucho")

st.divider()

st.markdown("### 📜 Importancia Histórica")
st.write("- Selló la independencia del Perú.")
st.write("- Marcó el fin del dominio español en Sudamérica.")
st.write("- Es considerada la última gran batalla por la independencia de América del Sur.")

st.divider()

st.markdown("### 🏞️ Patrimonio y Monumentos")
st.write("- **Santuario Histórico:** La Pampa de Ayacucho fue declarada Santuario Histórico Nacional.")
st.write("- **Monumento:** Obelisco de la Pampa de la Quinua (44 m de altura), inaugurado en 1974 para el 150.º aniversario.")

st.divider()

st.caption("Fuente: [Bicentenario del Perú](https://bicentenario.gob.pe), [Gob.pe](https://www.gob.pe), [Wikipedia](https://es.wikipedia.org/wiki/Batalla_de_Ayacucho)")

