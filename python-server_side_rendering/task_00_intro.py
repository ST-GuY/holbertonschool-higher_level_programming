import os


def generate_invitations(template, attendees):
    # Vérifier types
    if not isinstance(template, str) or not isinstance(attendees, list):
        print(f"Invalid input types: template is {type(template)}, attendees is {type(attendees)}")
        return

    # Vérifier contenu du template
    if template == "":
        print("Template is empty, no output files generated.")
        return

    # Vérifier liste d'attendees
    if len(attendees) == 0:
        print("No data provided, no output files generated.")
        return

    # Vérifier que tous les éléments de la liste sont des dicts
    if not all(isinstance(item, dict) for item in attendees):
        print("Invalid input types: attendees must be a list of dictionaries.")
        return

    # Pour chaque participant
    for idx, attendee in enumerate(attendees, start=1):
        # Récupérer les valeurs, remplacer None ou absence par "N/A"
        name = attendee.get("name") if attendee.get("name") is not None else "N/A"
        event_title = attendee.get("event_title") if attendee.get("event_title") is not None else "N/A"
        event_date = attendee.get("event_date") if attendee.get("event_date") is not None else "N/A"
        event_location = attendee.get("event_location") if attendee.get("event_location") is not None else "N/A"

        # Créer le texte final via remplacement simple
        content = template.replace("{name}", str(name))
        content = content.replace("{event_title}", str(event_title))
        content = content.replace("{event_date}", str(event_date))
        content = content.replace("{event_location}", str(event_location))

        # Nom du fichier de sortie
        filename = f"output_{idx}.txt"

        try:
            if os.path.exists(filename):
                pass

            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
        except Exception as e:
            print(f"Error writing file {filename}: {e}")
            # On continue les autres fichiers même si un échoue

    print(f"{len(attendees)} invitation(s) generated.")
