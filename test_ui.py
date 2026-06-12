import time
from playwright.sync_api import sync_playwright

def test_ui():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Intercept GitHub API to avoid network/token issues
        page.route("**/api.github.com/**", lambda route: route.fulfill(
            status=200,
            content_type="application/json",
            body='{"sha":"dummy","content":"e30="}' # 'e30=' is '{}' in base64
        ))

        # Mock GitHub token to prevent token screen block
        page.add_init_script("window.localStorage.setItem('scouts_gh_token', 'dummy_token');")

        page.goto("http://localhost:8080/index.html")

        # Wait for rendering
        page.wait_for_selector(".sc")

        # Check token button
        token_button = page.locator('button[title="Cambiar token de acceso"]')
        assert token_button.count() > 0
        assert token_button.first.get_attribute("aria-label") == "Cambiar token de acceso"
        print("Token button aria-label verified.")

        # Check EdCard
        ed_cards = page.locator('.sc[style*="cursor: pointer"]')
        assert ed_cards.count() > 0
        first_card_div = ed_cards.first.locator('div[role="button"]')
        assert first_card_div.count() > 0
        assert first_card_div.first.get_attribute("tabindex") == "0"
        print("EdCard role and tabIndex verified.")

        # Check EdCard delete button
        del_button = ed_cards.first.locator('button[title="Eliminar"]')
        assert del_button.count() > 0
        assert del_button.first.get_attribute("aria-label") == "Eliminar"
        print("EdCard delete button aria-label verified.")

        # Click a card to enter profile view
        first_card_div.first.click()
        page.wait_for_selector('text=Competencias esenciales')

        # Check CRow
        crows = page.locator('.crow div[role="button"]')
        assert crows.count() > 0
        assert crows.first.get_attribute("tabindex") == "0"
        print("CRow role and tabIndex verified.")

        browser.close()

if __name__ == "__main__":
    test_ui()
