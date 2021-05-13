# this file is to test offline visualization capabilities

#import chart_studio.plotly as py
import plotly.graph_objects as go
#from plotly.offline import iplot
import chart_studio
#from chart_studio.plotly import plot, iplot

chart_studio.tools.set_config_file(world_readable=False,
                             sharing='private')


def offline_plots_test_1(data, predicted, y):
    trace = go.Scatter3d(
        x=data['meas_lat'],
        y=data['meas_lon'],
        z=predicted - y,
        mode='markers',
        marker=dict(
            size=data['time_diff'],
            color=data['meas_time'],
            opacity=0.99,
            colorscale='Viridis',
            colorbar=dict(title='Measurement time'),
            line=dict(color='rgb(140, 140, 170)')
        ),
        #text=df_gridsearch.Text,
        hoverinfo='text'
    )

    data = [trace]
    layout = go.Layout(
        title='3D visualization of the grid search results',
        margin=dict(
            l=30,
            r=30,
            b=30,
            t=30
        ),
        #     height=600,
        #     width=960,
        scene=dict(
            xaxis=dict(
                title='meas_lat',
                nticks=10
            ),
            yaxis=dict(
                title='meas_lon',
            ),
            zaxis=dict(
                title='residuals',

            ),
        ),

    )
    trace.update(dict(x=['A', 'B', 'C'], y=['Cat', 'Dog', 'Bird'], z = ['100', '200', '300']))
    fig = go.Figure(data=data, layout=layout)

    fig.show()
    #iplot(fig)