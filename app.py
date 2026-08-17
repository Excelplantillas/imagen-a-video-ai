import gradio as gr


def generar_video(imagen, instrucciones):
    if imagen is None:
        return None, "Debes subir una imagen."

    if not instrucciones.strip():
        return None, "Debes escribir una instrucción."

    return None, f"Imagen recibida. Instrucción: {instrucciones}"


with gr.Blocks(title="Imagen a Video AI") as demo:

    gr.Markdown(
        """
        # 🎬 Imagen → Video AI

        Sube una imagen y escribe qué movimiento quieres generar.
        """
    )

    with gr.Row():

        with gr.Column():

            imagen = gr.Image(
                type="filepath",
                label="📷 Sube una imagen"
            )

            instrucciones = gr.Textbox(
                label="✍️ ¿Qué quieres que haga?",
                placeholder=(
                    "Ejemplo: Haz que la mujer salte y sonría "
                    "mientras mueve los brazos."
                ),
                lines=5
            )

            boton = gr.Button(
                "🎬 GENERAR VIDEO",
                variant="primary"
            )

        with gr.Column():

            video = gr.Video(
                label="🎥 Video generado"
            )

            estado = gr.Textbox(
                label="Estado"
            )

    boton.click(
        fn=generar_video,
        inputs=[imagen, instrucciones],
        outputs=[video, estado]
    )


demo.launch()
