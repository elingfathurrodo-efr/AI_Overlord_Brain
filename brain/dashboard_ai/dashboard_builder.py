import os

dashboard_file="../../dashboard/index.html"

def add_panel(panel_name):

    panel_code=f"""

<div class="card">
<h2>{panel_name}</h2>
<p id="{panel_name.lower()}">loading...</p>
</div>

"""

    with open(dashboard_file,"r") as f:
        html=f.read()

    insert_point=html.find("</div>")

    new_html=html[:insert_point]+panel_code+html[insert_point:]

    with open(dashboard_file,"w") as f:
        f.write(new_html)

    print("Dashboard updated with panel:",panel_name)
