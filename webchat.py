#!/usr/bin/env python
import os

from rasa_addons.webchat import WebChatInput, SocketInputChannel
from rasa_core.agent import Agent

current_path = os.path.dirname(os.path.realpath(__file__))

agent = Agent.load("models/dialogue", "models/default/current")
input_channel = WebChatInput(static_assets_path=os.path.join(current_path, 'static'))
agent.handle_channel(SocketInputChannel(5500, "/", input_channel))
