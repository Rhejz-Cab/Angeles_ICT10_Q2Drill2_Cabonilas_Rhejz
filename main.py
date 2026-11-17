
from pyscript import document, when

grade7 = {
    "Ovel Fontanilla",
    "Alexxa Gargallo",
    "Nescza Rose"
}

grade8 = {
    "Anthony Clive",
    "Grace Bernardus",
    "Lhance Evangelista"
}

grade9 = {
    "Liam Estrella",
    "John Vasallo"
}

grade10 = {
    "Cindy Jung"
}

master_members = grade7 | grade8 | grade9 | grade10

def update_display():
    member_list = "<br>".join(sorted(master_members))

    document.querySelector("#output").innerHTML = f"""
        <h5>All Members:</h5>
        {member_list}
        <br><br>
        <strong>Total members: {len(master_members)}</strong>
    """


@when("click", "#submit-btn")
def add_member(event):
    global master_members

    first_name = document.querySelector("#first-name").value.strip().title()
    last_name = document.querySelector("#last-name").value.strip().title()

    full_name = first_name + " " + last_name

    master_members = master_members | {full_name}

    update_display()

    document.querySelector("#first-name").value = ""
    document.querySelector("#last-name").value = ""


update_display()
