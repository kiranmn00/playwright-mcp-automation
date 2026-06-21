from playwright.sync_api import sync_playwright

def test_example_site():
with sync_playwright() as p:

```
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()

    page.goto("https://example.com")

    title = page.title()

    print(f"Page Title: {title}")

    assert "Example Domain" in title

    heading = page.locator("h1").text_content()

    print(f"Heading: {heading}")

    assert heading == "Example Domain"

    page.screenshot(path="example_page.png")

    print("Validation Successful")

    browser.close()
```

if **name** == "**main**":
test_example_site()
