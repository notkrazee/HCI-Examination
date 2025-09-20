def gps_tracker():
    # Starting position
    x, y = 0, 0
    print("Starting position: (0, 0)")
    print("Enter N, S, E, W to move. Type STOP to end session.")

    while True:
        command = input("Enter direction: ").strip().lower()

        if command == "stop":
            break
        elif command in ["n", "north"]:
            y += 1
        elif command in ["s", "south"]:
            y -= 1
        elif command in ["e", "east"]:
            x += 1
        elif command in ["w", "west"]:
            x -= 1
        else:
            print("Invalid input! Use N, S, E, W or STOP.")
            continue

        print(f"Current position: ({x}, {y})")

    # Final results
    print("\nSession ended.")
    print(f"Final position: ({x}, {y})")

    if (x, y) == (0, 0):
        print("You returned to the origin (0, 0).")
    else:
        print("You did not return to the origin.")


# Run the program
if __name__ == "__main__":
    gps_tracker()
