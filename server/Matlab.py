import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Create the figure and axis
fig, ax = plt.subplots(figsize=(8, 6))
ax.axis('off')

# Draw components
def draw_box(x, y, text, width=2.8, height=1.2, color='lightblue'):
    rect = patches.FancyBboxPatch((x, y), width, height,
                                   boxstyle="round,pad=0.02",
                                   edgecolor='black', facecolor=color)
    ax.add_patch(rect)
    ax.text(x + width / 2, y + height / 2, text, ha='center', va='center', fontsize=10)

# Components
draw_box(1, 6, "Synthea Dataset\n(FHIR/JSON)", color='lightgreen')
draw_box(5, 6, "MCP Server (FastAPI)\n• Patient API\n• Medication Analysis", color='orange')
draw_box(3, 4.5, "Data Loader\n(JSON -> Python)", color='lightgrey')
draw_box(1, 2.5, "AI Assistant Client\n(Python Script)", color='lightblue')
draw_box(5, 3, "Analysis Layer\n• Interaction Rules\n• Logic Engine", color='wheat')
draw_box(3, 1, "Output:\n• Patient Summary\n• Warnings\n• Recommendations", color='lightyellow')

# Arrows
def draw_arrow(start, end):
    ax.annotate("", xy=end, xytext=start,
                arrowprops=dict(arrowstyle="->", lw=2))

draw_arrow((2.4, 6.6), (3, 6.6))      # Data -> Server
draw_arrow((6.4, 6), (6.4, 4.2))      # Server -> Analysis
draw_arrow((6.4, 4.2), (6.4, 3))      # to Analysis Layer
draw_arrow((6.4, 3), (5.2, 3))        # to Analysis Box
draw_arrow((4.4, 6), (4.4, 4.5))      # Server -> Loader
draw_arrow((4.4, 4.5), (4.4, 3))      # Loader -> Analysis
draw_arrow((2.5, 2.5), (5, 2.5))      # Client -> Server
draw_arrow((4.5, 3), (4.5, 1.8))      # Analysis -> Output

plt.title("Architecture: AI Physician’s Assistant with MCP Server", fontsize=14, weight='bold')

plt.subplots_adjust(left=0.05, right=0.95, top=0.95, bottom=0.05)
plt.show()