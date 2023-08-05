#
#
#   Page 2
#
#

import random
import gradio as gr


def random_response(message, history):
    return random.choice(["Yes", "No"])


app = gr.ChatInterface(
    random_response,
    title="Page 2"
)
