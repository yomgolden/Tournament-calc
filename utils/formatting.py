"""
Bot Text Formatting
"""


def home_text():

    return (
        "<b>🏆 Tournament Manager</b>\n\n"

        "Create and manage Battle Royale tournaments directly from Telegram.\n\n"

        "Select an option below."
    )


def setup_header(step, total=5):

    return (

        "<b>🏆 Tournament Setup</b>\n\n"

        f"Step {step} / {total}\n\n"

    )


def tournament_dashboard(
    name,
    mode,
    status
):

    return (

        f"<b>🏆 {name}</b>\n\n"

        f"Mode\n"

        f"{mode}\n\n"

        f"Status\n"

        f"🟢 {status}"

    )
