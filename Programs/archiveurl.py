import waybackpy


# Capturing a new archive on Wayback machine.

def archive(Host):

    target_url = waybackpy.Url(Host)
    archived_url = target_url.save()
    print(archived_url)