from playwright.sync_api import sync_playwright
from datetime import datetime
import os


class PlaywrightAutomation:

    def __init__(self):

        self.screenshot_dir = "screenshots"

        os.makedirs(self.screenshot_dir, exist_ok=True)

    def log(self, message):

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print(f"[{timestamp}] {message}")

    def take_screenshot(self, page, name):

        path = f"{self.screenshot_dir}/{name}.png"

        page.screenshot(path=path)

        self.log(f"Screenshot saved: {path}")

    def verify_title(self, page, expected_title):

        actual_title = page.title()

        self.log(f"Expected Title : {expected_title}")
        self.log(f"Actual Title   : {actual_title}")

        assert expected_title in actual_title

        self.log("Title Verification Passed")

    def verify_element(self, page, locator):

        element = page.locator(locator)

        assert element.count() > 0

        self.log(f"Element Found: {locator}")

    def run(self):

        with sync_playwright() as p:

            browser = p.chromium.launch(
                headless=False
            )

            page = browser.new_page()

            try:

                self.log("Opening Website")

                page.goto(
                    "https://example.com",
                    timeout=30000
                )

                self.verify_title(
                    page,
                    "Example Domain"
                )

                self.verify_element(
                    page,
                    "h1"
                )

                heading = page.locator(
                    "h1"
                ).text_content()

                self.log(
                    f"Heading Text: {heading}"
                )

                self.take_screenshot(
                    page,
                    "example_homepage"
                )

                self.log(
                    "Automation Execution Successful"
                )

            except Exception as error:

                self.log(
                    f"Execution Failed: {error}"
                )

                self.take_screenshot(
                    page,
                    "failure_capture"
                )

            finally:

                browser.close()

                self.log(
                    "Browser Closed"
                )


if __name__ == "__main__":

    automation = PlaywrightAutomation()

    automation.run()
