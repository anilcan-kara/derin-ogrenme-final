import pandas as pd


# Create a simple structure for draw.io compatible XML nodes and edges
def create_drawio_data():
    nodes = []
    edges = []
    node_id = 1  # Start node IDs at 1

    # Layer and node configuration
    layer_sizes = [4, 32, 32, 1]
    x_spacing = 200  # Horizontal spacing for draw.io
    y_spacing = 50  # Vertical spacing

    # Create nodes and positions
    positions = []
    for layer_idx, nodes_in_layer in enumerate(layer_sizes):
        x = layer_idx * x_spacing
        y_start = -(nodes_in_layer - 1) * y_spacing / 2
        layer_positions = []
        for i in range(nodes_in_layer):
            y = y_start + i * y_spacing
            nodes.append(
                {
                    "id": f"n{node_id}",
                    "label": f"Layer-{layer_idx+1}-Node-{i+1}",
                    "x": x,
                    "y": y,
                }
            )
            layer_positions.append(f"n{node_id}")
            node_id += 1
        positions.append(layer_positions)

    # Create edges between nodes in adjacent layers
    edge_id = 1
    for layer_idx in range(len(positions) - 1):
        for src_node in positions[layer_idx]:
            for dst_node in positions[layer_idx + 1]:
                edges.append(
                    {"id": f"e{edge_id}", "source": src_node, "target": dst_node}
                )
                edge_id += 1

    return nodes, edges


# Export as XML
def export_drawio_xml(nodes, edges, filename):
    xml_header = """<?xml version="1.0" encoding="UTF-8"?>
<mxfile host="app.diagrams.net">
  <diagram name="Neural Network Graph">
    <mxGraphModel dx="800" dy="800" grid="1" gridSize="10" guides="1" tooltips="1" connect="1" arrows="1" fold="1" page="1" pageScale="1" pageWidth="827" pageHeight="1169" math="0" shadow="0">
      <root>
        <mxCell id="0" />
        <mxCell id="1" parent="0" />"""
    xml_footer = """      </root>
    </mxGraphModel>
  </diagram>
</mxfile>"""

    xml_body = ""
    for node in nodes:
        xml_body += f"""
        <mxCell id="{node['id']}" value="{node['label']}" style="ellipse;whiteSpace=wrap;html=1;fillColor=#DAE8FC;strokeColor=#6C8EBF;" vertex="1" parent="1">
          <mxGeometry x="{node['x']}" y="{node['y']}" width="60" height="60" as="geometry" />
        </mxCell>"""

    for edge in edges:
        xml_body += f"""
        <mxCell id="{edge['id']}" style="edgeStyle=elbowEdgeStyle;elbow=horizontal;rounded=0;orthogonalLoop=1;jettySize=auto;html=1;exitX=0.5;exitY=0;exitDx=0;exitDy=0;entryX=0.5;entryY=1;entryDx=0;entryDy=0;" edge="1" source="{edge['source']}" target="{edge['target']}" parent="1">
          <mxGeometry relative="1" as="geometry" />
        </mxCell>"""

    # Combine into a single XML file
    drawio_xml = xml_header + xml_body + xml_footer

    # Save the file
    with open(filename, "w") as file:
        file.write(drawio_xml)


# Generate data
nodes, edges = create_drawio_data()

# Save the draw.io XML file
output_filename = "./fixed_neural_network_graph.drawio"
export_drawio_xml(nodes, edges, output_filename)
output_filename
