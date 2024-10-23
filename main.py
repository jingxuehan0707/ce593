import plotly.figure_factory as ff

# Define project tasks and details
tasks = [
    dict(Task="Cleaning the data", Start='2024-10-22', Finish='2024-10-29', Resource='Harvey'),
    dict(Task="Visualize the speed contour diagram", Start='2024-10-22', Finish='2024-10-29', Resource='Xinyang and Nolan'),
    dict(Task="Visualize the fundamental diagram", Start='2024-10-22', Finish='2024-10-29', Resource='Xinyang and Nolan'),
    dict(Task="Model optimization", Start='2024-10-22', Finish='2024-10-29', Resource='Harvey'),
    dict(Task="Write PPT presentation", Start='2024-10-30', Finish='2024-11-05', Resource='Team')
]

# Create the Gantt chart
fig = ff.create_gantt(tasks, index_col='Resource', show_colorbar=True, group_tasks=True, showgrid_x=True, showgrid_y=True)

# Show the Gantt chart
fig.show()