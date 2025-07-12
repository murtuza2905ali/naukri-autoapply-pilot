import sys
import time
from playwright.sync_api import sync_playwright

# CLI args or defaults
job_title = sys.argv[1] if len(sys.argv) > 1 else "Tally"
location = sys.argv[2] if len(sys.argv) > 2 else "Pune"
email = sys.argv[3] if len(sys.argv) > 3 else "default_email@example.com"
password = sys.argv[4] if len(sys.argv) > 4 else "default_password"
experience = "Fresher"
max_applications = 20
RESUME_PATH = "C:/Users/Lucky/Downloads/Documents/Murtuza_Resume_D.pdf"

def test_click_on_job_card():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()

        # ── LOGIN ──
        page.goto("https://www.naukri.com/", timeout=60000)
        page.click("a#login_Layer", timeout=10000)

        try:
            # Wait for login drawer to appear
            page.wait_for_selector("div.drawer-wrapper input[placeholder='Enter your active Email ID / Username']", timeout=15000)

            # Fill email and password
            page.fill("div.drawer-wrapper input[placeholder='Enter your active Email ID / Username']", email)
            page.fill("div.drawer-wrapper input[placeholder='Enter your password']", password)

            # Click the Login button (inside drawer)
            page.click("div.drawer-wrapper button:has-text('Login')")

            print("✅ Login submitted")

        except Exception as e:
            print("❌ Login fields not found:", str(e))


        time.sleep(5)





        page.wait_for_selector("button.nI-gNb-sb__icon-wrapper", timeout=10000)

        # Scroll and force click the button
        search_btn = page.locator("button.nI-gNb-sb__icon-wrapper")
        search_btn.scroll_into_view_if_needed()
        search_btn.click(force=True)

        print("✅ Search button clicked")
        job_type_selected = False
        try:
            page.click("input#jobType", timeout=3000)
            page.click("text='Job'", timeout=3000)
            job_type_selected = True
            print("✅ Job type selected")
        except:
            print("⚠️ Job type not available")

        # ── Fill job title and location ──
        page.fill("input[placeholder*='keyword']", job_title)
        page.fill("input[placeholder*='location']", location)

        # ── If Job Type NOT selected, fill experience ──
        if not job_type_selected:
            try:
                page.click("input#experienceDD", timeout=3000)
                page.fill("input#experienceDD", "Fresher")
                page.keyboard.press("Enter")
                print("✅ Experience filled and selected")

            except:
                print("⚠️ Experience field failed")

        time.sleep(2)

        # ── Finally, press Enter to search ──
        page.click(".nI-gNb-sb__icon-wrapper")
        print("✅ Search button clicked")




        # ── COLLECT LINKS ──
                # ── Wait for job listings to appear ──
        # ── WAIT FOR JOB CARDS TO LOAD ──
        try:
            page.wait_for_selector("div.cust-job-tuple a.title", timeout=15000)
        except:
            print("⚠️ Timed out waiting for job listings to appear")

        # ── COLLECT JOB LINKS ──
        job_links = page.locator("div.cust-job-tuple a.title")
        count = job_links.count()
        total = min(count, max_applications)
        print(f"🔍 Found {count} jobs, applying to {total}.")


        for i in range(total):
            # open job
            job_links.nth(i).scroll_into_view_if_needed()
            with context.expect_page() as info:
                job_links.nth(i).click()
            job_page = info.value
            job_page.wait_for_load_state()
            time.sleep(2)

            # ── CLICK APPLY ──
            applied = False
            for sel in ("button#apply-button","button:has-text('Apply')","xpath=//button[contains(., 'Apply')]"):
                try:
                    btn = job_page.locator(sel).first
                    if btn.is_visible(timeout=3000):
                        btn.scroll_into_view_if_needed()
                        btn.click(force=True)
                        print(f"✅ Clicked Apply using: {sel}")
                        applied = True
                        break
                except:
                    continue

            # fallback “I’m Interested”
            if not applied:
                try:
                    btn = job_page.locator("button#imInterested").first
                    if btn.is_visible(timeout=2000):
                        btn.click()
                        print("✅ Clicked on I'm Interested.")
                        applied = True
                except:
                    pass

            # fallback company site
            if not applied:
                try:
                    btn = job_page.locator("button#company-site-button").first
                    if btn.is_visible(timeout=2000):
                        with context.expect_page() as comp_info:
                            btn.click()
                        comp_tab = comp_info.value
                        print("🌐 Opened company site.")
                        time.sleep(5)
                        comp_tab.close()
                        print("🔙 Closed company site tab.")
                        applied = True
                except:
                    pass

            # ── WAIT FOR EITHER SIDEBAR OR SUCCESS ──# ── WAIT FOR EITHER SIDEBAR OR SUCCESS ──
            if applied:
                try:
                    job_page.wait_for_timeout(1000)

                    # 1️⃣ Check for success message
                    if job_page.locator("text=You have successfully applied to").is_visible(timeout=5000):
                        print("🎉 Application successful!")
                        job_page.close()

                    # 2️⃣ Check for sidebar presence using provided code
                    elif job_page.locator("div.chatbot_Nav").is_visible(timeout=3000):
                        print("💬 Sidebar detected — leaving tab open for manual resume input.")
                        # Do not close the tab

                    else:
                        print("❓ No clear response — closing tab.")
                        job_page.close()

                except Exception as e:
                    print(f"⚠️ Timeout or unexpected error: {e}")
                    job_page.close()
            else:
                print("❌ No apply option found.")
                job_page.close()


            # cleanup
            page.bring_to_front()
            time.sleep(2)

        print("✅ Loop complete.")
        input("Press Enter to close browser…")
        browser.close()

if __name__ == "__main__":
    test_click_on_job_card()
