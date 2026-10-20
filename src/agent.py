import os
import signal
import sys
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.conversational_ai.conversation import Conversation
from elevenlabs.conversational_ai.default_audio_interface import DefaultAudioInterface

# Load environment variables
load_dotenv()

api_key = os.getenv("ELEVENLABS_API_KEY")
agent_id = os.getenv("AGENT_ID")

if not api_key or not agent_id:
    print("❌ Error: Missing ELEVENLABS_API_KEY or AGENT_ID in your .env file.")
    sys.exit(1)

def main():
    print("🚀 Initializing Isolated ElevenLabs Voice Agent...")
    
    # Initialize the client
    client = ElevenLabs(api_key=api_key)

    # Set up local audio interface (mic & speaker)
    audio_interface = DefaultAudioInterface()

    # Create the conversation session with real-time callbacks
    conversation = Conversation(
        client=client,
        agent_id=agent_id,
        requires_auth=True,
        audio_interface=audio_interface,
        callback_agent_response=lambda response: print(f"\n🤖 Agent: {response}"),
        callback_user_transcript=lambda transcript: print(f"👤 User: {transcript}"),
        callback_latency_measurement=lambda latency: print(f"⚡ [Latency: {latency}ms]")
    )

    # Handle graceful exit on Ctrl+C
    def shutdown_handler(sig, frame):
        print("\n🛑 Shutting down conversation session...")
        conversation.end_session()
        sys.exit(0)

    signal.signal(signal.SIGINT, shutdown_handler)

    print("\n🎙️ Voice session active! Speak into your microphone (Press Ctrl+C to exit)...\n")
    conversation.start_session()

    # Keep session alive
    session_id = conversation.wait_for_session_end()
    print(f"\n📁 Session ended. Conversation ID: {session_id}")

if __name__ == "__main__":
    main()