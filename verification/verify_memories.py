from playwright.sync_api import sync_playwright

def verify_memories():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        try:
            # 1. Login
            print("Navigating to login page...")
            page.goto("http://localhost:5000/login")
            page.fill("input[name='username']", "love")
            page.fill("input[name='password']", "you")
            page.click("button[type='submit']")

            # 2. Check redirect to profiles
            print("Checking for redirection...")
            page.wait_for_url("**/profiles")

            # 3. Navigate to Browse
            print("Navigating to /browse...")
            page.goto("http://localhost:5000/browse")

            # Scroll to the memories section
            header = page.locator("h3:has-text('Because You Watched \"Our Story\"')")
            header.scroll_into_view_if_needed()

            # Screenshot of the memories row
            page.screenshot(path="verification/memories_row.png")
            print("Screenshot saved to verification/memories_row.png")

            # 4. Open Video Overlay
            print("Clicking first memory card...")
            cards = page.locator(".memory-card")
            first_card = cards.first

            # Hover to show details (might be tricky in static screenshot but good to try)
            first_card.hover()
            page.screenshot(path="verification/card_hover.png")

            first_card.click()

            # Check video overlay visibility
            video_overlay = page.locator("#videoOverlay")
            video_overlay.wait_for(state="visible", timeout=2000)

            # Screenshot of the overlay
            page.screenshot(path="verification/video_overlay.png")
            print("Screenshot saved to verification/video_overlay.png")

            # 5. Close Video
            print("Closing video...")
            close_btn = page.locator("#closeVideoBtn")
            close_btn.click()

            video_overlay.wait_for(state="hidden", timeout=2000)

            print("Verification Successful!")

        except Exception as e:
            print(f"Verification Failed: {e}")
            raise e
        finally:
            browser.close()

if __name__ == "__main__":
    verify_memories()
