import dash_mantine_components as dmc
from dash import callback  # no-prism
from dash import html, Output, Input

component = html.Div(
    [
        dmc.RadioGroup(
            id="radiogroup",
            data=[
                {"value": "react", "label": "React"},
                {"value": "ng", "label": "Angular"},
                {"value": "svelte", "label": "Svelte"},
                {"value": "vue", "label": "Vue"},
            ],
            value="react",
            label="Select your favorite framework/library",
        ),
        dmc.Space(h=10),  # no-prism
        dmc.Text(id="radio-output"),
    ]
)


@callback(Output("radio-output", "children"), Input("radiogroup", "value"))
def choose_framework(value):
    return value