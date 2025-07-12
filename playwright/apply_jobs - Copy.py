import sys
import time
from playwright.sync_api import sync_playwright

# CLI args or defaults
job_title = sys.argv[1] if len(sys.argv) > 1 else "Tally"
location = sys.argv[2] if len(sys.argv) > 2 else "Pune"
email = sys.argv[3] if len(sys.argv) > 3 else "default_email@example.com"
password = sys.argv[4] if len(sys.argv) > 4 else "default_password"
experience = "fresher"
max_applications = 20
RESUME_PATH = "C:/Users/Lucky/Downloads/Documents/Murtuza_Resume_D.pdf"

def test_click_on_job_card():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ── LOGIN ──
        # ── LOGIN ──
        page.goto("https://www.naukri.com/", timeout=60000)
        page.click("a#login_Layer", timeout=10000)

        try:
            # ✅ Wait for login modal
            page.wait_for_selector("input[type='text']", timeout=15000)

            # ✅ Fill email and password using JS-path (CSS selector form)
            page.fill("div.drawer-wrapper input[type='text']", email)
            page.fill("div.drawer-wrapper input[type='password']", password)

            # ✅ Click the Login button inside drawer-wrapper
            page.click("div.drawer-wrapper button:has-text('Login')")

            print("✅ Login submitted")

        except Exception as e:
            print("❌ Login fields not found:", str(e))



if __name__ == "__main__":
    test_click_on_job_card()
