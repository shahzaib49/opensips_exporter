from prometheus_client import Gauge

# Define a gauge for profile call count.
profile_call_count = Gauge(
    'profile_call_count',
    'Call count for each profile from profile_get_size command',
    ['profile_name', 'profile_value']
)

def update_profile_metrics(client):
    """
    Retrieves the list of profiles, and for each profile calls get_profile_size,
    then updates the profile_call_count metric.
    """
    profiles_data = client.list_all_profiles()
    if not profiles_data or "Profiles" not in profiles_data:
        print("No Profiles found in list_all_profiles response.")
        return

    for profile in profiles_data["Profiles"]:
        profile_name = profile.get("name", "unknown")
        profile_size_data = client.get_profile_size(profile_name)
        if profile_size_data and "Profile" in profile_size_data:
            prof = profile_size_data["Profile"]
            prof_name = prof.get("name", "unknown")
            prof_value = prof.get("value")
            if prof_value is None:
                prof_value = "none"
            else:
                prof_value = str(prof_value)
            prof_count = prof.get("count", 0)
            profile_call_count.labels(profile_name=prof_name, profile_value=prof_value).set(prof_count)
        else:
            print(f"No profile data found for {profile_name}.")
