[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/ehCBajNl)

Els requeriments de hardware en quant a GPU son els següents, per lo que no sería factible executar aquesta IA amb el portàtil del institut
- Minimum: NVIDIA RTX 3070 (8GB VRAM)
- Recommended: NVIDIA RTX 3090 (24GB VRAM)
- Optimal: 2x NVIDIA A100 (80GB VRAM)

Per això he decidit utilitzar la versió més lleugera de [GPT2](https://huggingface.co/openai-community/gpt2), pero al ser un mòdel bastant lleuger no està entrenat per aquesta classe de tasques, per lo que retorna un missatge sense cap sentit

![imagen](https://github.com/user-attachments/assets/dfa80d1c-403c-482f-8b2d-d1a1dc1139bd)

La solució seria probarlo en un equip en una gràfica dedicada amb suficient potencia per a poder executar aquest tipus de inteligencies artificials sense problemes
