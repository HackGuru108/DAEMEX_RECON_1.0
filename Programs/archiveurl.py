import waybackpy

# Capturing a new archive on Wayback machine.

def archive(Host):

    target_url = waybackpy.Url(Host)
    archived_url = target_url.save()
    print("\n====================================================================\n")
    print(f'Following is the Archived Urls of {Host} \n')
    print(archived_url)

    print("\n====================================================================\n")