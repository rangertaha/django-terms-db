"""A Django app providing a database of terms to look up."""

__version_info__ = {
    "major": 0,
    "minor": 0,
    "micro": 1,
    "releaselevel": "final",
    "serial": 1,
}


def get_version(short=False):
    assert __version_info__["releaselevel"] in ("alpha", "beta", "final")
    vers = [f"{__version_info__['major']}.{__version_info__['minor']}"]
    if __version_info__["micro"]:
        vers.append(f".{__version_info__['micro']}")
    if __version_info__["releaselevel"] != "final" and not short:
        vers.append(
            f"{__version_info__['releaselevel'][0]}{__version_info__['serial']}"
        )
    return "".join(vers)


__version__ = get_version()
