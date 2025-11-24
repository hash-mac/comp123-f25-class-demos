"""
Generated using Gemini through a series of prompts in cut_images.prompts
"""

import customtkinter as ctk
from PIL import Image, ImageTk
import requests
import io
import threading
import time
import tkinter as tk  # Needed for widget state constants

# Set the CustomTkinter appearance mode and theme
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue", "dark-blue", "green"


class CatApp:
    """A CustomTkinter application to display random cat images from an API."""

    def __init__(self, master):
        self.master = master
        master.title("Random Cat Viewer 🐈")

        self.original_pil_image = None
        self.tk_image = None

        # --- Configure Grid Layout for Main Window ---
        # Row 0: Image area (expands)
        master.grid_rowconfigure(0, weight=1)
        # Row 1: Button row (fixed height)
        master.grid_rowconfigure(1, weight=0)
        # Column 0: Only one column, expands
        master.grid_columnconfigure(0, weight=1)

        # --- GUI Elements ---

        # 1. Image Label (CTkLabel) - Row 0
        self.image_label = ctk.CTkLabel(
            master,
            text="Click 'Get Cat' or press ENTER to start...",
            font=ctk.CTkFont(size=20)
        )
        # sticky="nsew" makes it fill the available space
        self.image_label.grid(row=0, column=0, padx=20, pady=(20, 10), sticky="nsew")

        # 2. Button (CTkButton) - Row 1
        self.cat_button = ctk.CTkButton(
            master,
            text="Get a New Cat!",
            command=self.load_cat_image,
            fg_color="green"
        )
        # sticky="ew" makes it stretch horizontally
        self.cat_button.grid(row=1, column=0, pady=(0, 20), padx=20, sticky="ew")

        # 3. Bind the window resize event (<Configure>)
        self.master.bind('<Configure>', self._on_resize)

        # 4. Bind the ENTER key event (<Return>)
        self.master.bind('<Return>', self.load_cat_image_event)

        # Initial call to load an image when the app starts
        self.load_cat_image()

    # ------------------------------------
    # --- Loading Indicator Control ---
    # ------------------------------------

    def _set_button_loading_state(self):
        """Changes the button to a disabled loading state."""
        self.cat_button.configure(
            text="Loading...",
            state=tk.DISABLED,  # Disable button during load
            fg_color="gray"  # Change color for visual loading feedback
        )

    def _set_button_ready_state(self):
        """Resets the button to the active, ready state."""
        self.cat_button.configure(
            text="Get a New Cat!",
            state=tk.NORMAL,  # Enable button
            fg_color="green"
        )

    # ------------------------------------
    # --- Image Fetching and Display Logic ---
    # ------------------------------------

    def load_cat_image_event(self, event):
        """Wrapper function to handle the event object passed by the <Return> bind."""
        # Only proceed if the button is not currently disabled (i.e., not already loading)
        if self.cat_button.cget("state") == tk.NORMAL:
            self.load_cat_image()

    def load_cat_image(self):
        """Starts the loading status and the image fetching thread."""
        self._set_button_loading_state()
        # Start the network request in a separate thread to keep the UI responsive
        threading.Thread(target=self._fetch_and_process_image, daemon=True).start()

    def _fetch_and_process_image(self):
        """Fetches the image data from the API. Runs in a worker thread."""
        api_url = "https://cataas.com/cat"

        # Simulate a network delay to easily see the loading state
        time.sleep(0.5)

        try:
            # 1. Fetch image data
            response = requests.get(api_url, stream=True)
            response.raise_for_status()
            image_data = response.content
            pil_image = Image.open(io.BytesIO(image_data))

            # 2. Safely call update function in the main thread
            self.master.after(0, self._update_gui, pil_image)

        except requests.RequestException as e:
            self.master.after(0, lambda: self._update_gui_error(f"Error fetching image: {e}"))
        except Exception as e:
            self.master.after(0, lambda: self._update_gui_error(f"An unexpected error occurred: {e}"))

    def _update_gui(self, new_pil_image):
        """Updates the image and resets the button. Runs in the main thread."""

        self.original_pil_image = new_pil_image

        # Get current label size to resize the image appropriately
        label_width = self.image_label.winfo_width()
        label_height = self.image_label.winfo_height()
        self._display_resized_image(label_width, label_height)

        self._set_button_ready_state()

    def _update_gui_error(self, message):
        """Handles updating the GUI in case of an error."""
        self._set_button_ready_state()
        self.cat_button.configure(text="Try Again", fg_color="red")

        self.original_pil_image = None
        self.image_label.configure(text=message, image=None, text_color="red")

    # ------------------------------------
    # --- Resizing and Display Logic ---
    # ------------------------------------

    def _on_resize(self, event):
        """Resizes the currently loaded image to fit the label size when the window changes."""
        # Check if the event came from the root window (not a child widget)
        if str(event.widget) == str(self.master):
            if self.original_pil_image:
                label_width = self.image_label.winfo_width()
                label_height = self.image_label.winfo_height()
                self._display_resized_image(label_width, label_height)

    def _display_resized_image(self, container_width, container_height):
        """Scales the self.original_pil_image to fit the given dimensions."""
        if not self.original_pil_image or container_width <= 0 or container_height <= 0:
            return

        img_copy = self.original_pil_image.copy()
        original_width, original_height = img_copy.size

        # Calculate scaling ratio
        width_ratio = container_width / original_width
        height_ratio = container_height / original_height
        fit_ratio = min(width_ratio, height_ratio)

        # Apply scaling
        if fit_ratio < 1:
            new_width = int(original_width * fit_ratio)
            new_height = int(original_height * fit_ratio)
        else:
            new_width = original_width
            new_height = original_height

        if new_width > 0 and new_height > 0:
            # Resize using a high-quality filter
            resized_image = img_copy.resize((new_width, new_height), Image.LANCZOS)

            # Convert to Tkinter PhotoImage for display
            self.tk_image = ImageTk.PhotoImage(resized_image)
            self.image_label.configure(image=self.tk_image, text="")


# ------------------------------------
# --- Main Execution Block ---
# ------------------------------------

if __name__ == "__main__":
    # Create the main CustomTkinter window instance
    root = ctk.CTk()

    # Set initial and minimum size for usability
    root.geometry("600x500")
    root.minsize(300, 250)

    # Initialize and run the application
    app = CatApp(root)
    root.mainloop()
