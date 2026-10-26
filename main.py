from pyscript import document


grade7_members = {
    "Jose Madrid",
    "Jaden Cortez",
    "Laine Capistrano ",
    "Christina Nicholas"
}

grade8_members = {
    "Bea Domingo",
    "Lexa Delos Santos",
    "Joe Kerr"
}

grade9_members = {
    "Chloe Adlawan",
    "Inno Pena",
    "Sophia Gascon",
    "Zoey Adlawan"
}

grade10_members = {
    "Cianna Del Prado",
    "Mateo Salacup",
    "Mandy Cajanding"
}


all_members = grade7_members | grade8_members | grade9_members | grade10_members


def display_members():
   
    members_list = "<br>".join(sorted(all_members))

   
    total_members = len(all_members)

    
    document.getElementById("result").innerHTML = f"""
        <h2>ALL MEMBERS:</h2>
        {members_list}
        <br>
        TOTAL MEMBERS: {total_members}
    """


def add_member(event):
   
    first_name = document.getElementById("first_name").value.strip()
    last_name = document.getElementById("last_name").value.strip()

   
    full_name = first_name.title() + " " + last_name.title()

    
    global all_members
    all_members = all_members | {full_name}

   
    display_members()

    
    document.getElementById("first_name").value = ""
    document.getElementById("last_name").value = ""


display_members()