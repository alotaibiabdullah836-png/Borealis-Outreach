from pathlib import Path

from contact_form_filler import fill_contact_form


BASIC_FORM_HTML = """
<html><body>
<h1>Contact Northwind Colocation</h1>
<form>
  <input type="text" name="full_name" placeholder="Your name" />
  <input type="email" name="email" placeholder="Your email" />
  <input type="text" name="company" placeholder="Company" />
  <input type="password" name="password" placeholder="Not a real field on a contact form" />
  <textarea name="message" placeholder="How can we help?"></textarea>
  <button type="submit">Send</button>
</form>
</body></html>
"""

NO_FORM_HTML = """
<html><body>
<h1>Northwind Colocation</h1>
<p>We build data centers. No contact form or link here.</p>
</body></html>
"""

HOMEPAGE_WITH_CONTACT_LINK_HTML = """
<html><body>
<h1>Northwind Colocation</h1>
<p>We build data centers.</p>
<a href="{target}">Contact Us</a>
</body></html>
"""


def write_html(tmp_path: Path, name: str, content: str) -> str:
    path = tmp_path / name
    path.write_text(content, encoding="utf-8")
    return f"file://{path}"


def test_fill_contact_form_matches_fields_without_submitting(tmp_path):
    url = write_html(tmp_path, "contact.html", BASIC_FORM_HTML)
    result = fill_contact_form(
        url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="We'd like to discuss cooling for your next buildout.",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert result.success is True
    assert result.submitted is False
    assert set(result.matched_fields.keys()) == {"name", "email", "company", "message"}
    assert Path(result.screenshot_path).exists()


def test_fill_contact_form_never_fills_password_field(tmp_path):
    url = write_html(tmp_path, "contact.html", BASIC_FORM_HTML)
    result = fill_contact_form(
        url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="We'd like to discuss cooling for your next buildout.",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert "password" not in result.matched_fields
    assert all("password" not in sig for sig in result.matched_fields.values())


def test_fill_contact_form_submits_only_when_requested(tmp_path):
    url = write_html(tmp_path, "contact.html", BASIC_FORM_HTML)
    dry = fill_contact_form(
        url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="Hello",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert dry.submitted is False

    live = fill_contact_form(
        url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="Hello",
        submit=True,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert live.submitted is True


def test_fill_contact_form_follows_contact_link_when_homepage_has_no_form(tmp_path):
    contact_url = write_html(tmp_path, "contact.html", BASIC_FORM_HTML)
    home_url = write_html(
        tmp_path, "index.html", HOMEPAGE_WITH_CONTACT_LINK_HTML.format(target=contact_url)
    )
    result = fill_contact_form(
        home_url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="Hello",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert result.success is True
    assert set(result.matched_fields.keys()) == {"name", "email", "company", "message"}


def test_fill_contact_form_reports_no_form_found(tmp_path):
    url = write_html(tmp_path, "index.html", NO_FORM_HTML)
    result = fill_contact_form(
        url,
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="Hello",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert result.success is False
    assert result.error == "no_contact_form_fields_found"


def test_fill_contact_form_reports_navigation_failure(tmp_path):
    result = fill_contact_form(
        "file:///nonexistent/path/does-not-exist.html",
        sender_name="Jordan Blake",
        sender_company="Borealis",
        sender_email="jordan@borealis.cool",
        message="Hello",
        submit=False,
        screenshot_dir=tmp_path / "screenshots",
    )
    assert result.success is False
    assert result.error.startswith("navigation_failed")
