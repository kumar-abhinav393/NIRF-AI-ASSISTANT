# Spinner state
spinner_running = False
spinner_frames = [
    "⏳ Connecting to Gemini   ",
    "⏳ Connecting to Gemini.  ",
    "⏳ Connecting to Gemini.. ",
    "⏳ Connecting to Gemini...",
]

def start_spinner(root, output_text):
    global spinner_running
    spinner_running = True

    def animate(i=0):
        if not spinner_running:
            return
        output_text.delete("1.0", "end")
        output_text.insert("1.0", spinner_frames[i % len(spinner_frames)])
        root.after(300, animate, i + 1)

    animate()

def stop_spinner():
    global spinner_running
    spinner_running = False