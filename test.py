import curses
import time

def animate_flash(stdscr, text):
    curses.curs_set(0)  # Hide the cursor
    stdscr.clear()  # Clear the screen
    stdscr.addstr(0, 0, text)  # Print the text

    # Animate the flashing effect
    for i in range(10):
        stdscr.addstr(0, 0, text, curses.A_REVERSE)  # Flash the text
        stdscr.refresh()  # Update the screen
        time.sleep(0.1)

        stdscr.addstr(0, 0, text, curses.A_NORMAL)  # Un-flash the text
        stdscr.refresh()  # Update the screen
        time.sleep(0.1)

    curses.curs_set(1)  # Show the cursor again

# Initialize curses
stdscr = curses.initscr()

# Call the animation function
animate_flash(stdscr, "Hello, World!")

# Clean up and exit curses
curses.nocbreak()
stdscr.keypad(False)
curses.echo()
curses.endwin()
