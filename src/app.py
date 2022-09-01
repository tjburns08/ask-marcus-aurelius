from dash import Dash, dcc, html, dash_table, Input, Output, State
import plotly.express as px
import pandas as pd
from sentence_transformers import SentenceTransformer
from scipy.spatial import distance
import re
import textwrap
import base64

app = Dash(__name__)
server = app.server

dat = pd.read_csv('data/meditations_processed.csv')
space = pd.read_csv('data/sentence_embeddings.csv')

# For update function
model_name = 'all-mpnet-base-v2'
model = SentenceTransformer(model_name)

# The image
image_path = 'assets/DALL·E 2022-08-31 21.03.55 - A painting of Marcus Aurelius thinking deeply as a stoic philosopher in ancient Rome.png'

fig = px.scatter()
app.layout = html.Div([
    # TODO make the instructions
    html.A(html.P('Click here for instructions'), href="https://tjburns08.github.io/gwas_app_instructions.html"),
    html.Img(src=image_path, 
        style={'height':'30%', 'width':'30%'}),
    dcc.Textarea(
        placeholder='Ask Marcus Aurelius a question...',
        id = 'user-input',
        value='',
        style={'width': '100%'}
    ),
    html.Button('Submit', id='value-enter'),
    dash_table.DataTable(data = dat.to_dict('records'), style_data={
        'whiteSpace': 'normal',
        'height': 'auto',
    },
        id = 'answer-table',
        fill_width = False,
        columns = [{"name": i, "id": i} for i in dat.columns])
])


@app.callback(
    Output('answer-table', 'data'),
    Input('value-enter', 'n_clicks'),
    State('user-input', 'value'))

def update_table(n_clicks, value):

    if not value or n_clicks == 0:
        return

    text_coord = model.encode(value, show_progress_bar = True)
    out = pd.concat([dat.reset_index(), space], axis = 1)

    cos_dist = []
    embedding_cols = [str(i) for i in range(768)]
    for i in range(0, out.shape[0]):
        curr = out.iloc[i]
        curr = curr[embedding_cols]
        curr_dist = distance.cosine(u = text_coord, v = curr)
        cos_dist.append(curr_dist)

    out['cos_dist'] = cos_dist
    out = out.sort_values('cos_dist')
    out = out.head(10)
    out = out[['book', 'verse', 'text']]

    return out.to_dict('records')


if __name__ == '__main__':
    app.run_server(debug=True)

