import matplotlib.pyplot as plt


def draw_neural_network():
    # Define the layers
    layer_sizes = [4, 32, 32, 1]  # 4 input, 2x 32 hidden, 1 output

    # Define spacing and node properties
    x_spacing = 2.0  # Horizontal spacing between layers
    y_spacing = 0.6  # Vertical spacing between nodes
    node_radius = 0.1  # Node size

    # Set up the figure and axes
    fig, ax = plt.subplots(figsize=(12, 8))
    ax.axis("off")  # Turn off axes
    ax.set_aspect("equal")  # Ensure equal scaling

    # Calculate positions for each layer
    positions = []
    for layer_idx, nodes in enumerate(layer_sizes):
        x_position = layer_idx * x_spacing
        y_positions = [-(i - (nodes - 1) / 2) * y_spacing for i in range(nodes)]
        positions.append([(x_position, y) for y in y_positions])

    # Draw nodes
    for layer in positions:
        for x, y in layer:
            circle = plt.Circle(
                (x, y), node_radius, color="skyblue", ec="black", lw=1.5
            )
            ax.add_patch(circle)

    # Draw arrows between nodes
    for layer_idx in range(len(positions) - 1):
        for x1, y1 in positions[layer_idx]:
            for x2, y2 in positions[layer_idx + 1]:
                ax.annotate(
                    "",
                    xy=(x2, y2),
                    xytext=(x1, y1),
                    arrowprops=dict(arrowstyle="->", lw=0.2, color="gray"),
                )

    # Adjust plot limits for better visibility
    ax.set_xlim(-1, len(layer_sizes) * x_spacing)
    ax.set_ylim(-17, 17)  # Adjust this depending on node density

    # Title
    plt.title(
        "4-Input, 32-Hidden, 32-Hidden, 1-Output Neural Network Visualization",
        fontsize=14,
    )

    # Display
    plt.show()


# Call the function to draw the neural network
draw_neural_network()
