from playwright.sync_api import sync_playwright
import time
import random
import pyautogui
EMAIL_TEXT = "phanindragangadhara@gmail.com"
SEARCH_QUERY = "hiring python developer"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.linkedin.com")
    print("Login manually within 30 seconds")
    page.wait_for_timeout(30000)

    page.goto(f"https://www.linkedin.com/search/results/content/?keywords={SEARCH_QUERY}")
    page.wait_for_timeout(5000)

    posts = page.locator("div.feed-shared-update-v2")
    count = posts.count()
    print("Posts found:", count)

    for i in range(min(count, 5)):
        post = posts.nth(i)

        try:
            post.scroll_into_view_if_needed()
            time.sleep(2)


            comment_btn = post.locator("button:has-text('Comment')").first
            comment_btn.wait_for(state="visible", timeout=5000)
            comment_btn.click(force=True)

            # Wait for textbox
            textbox = post.locator("div[role='textbox']")
            textbox.wait_for(state="visible", timeout=5000)
            textbox.click()

            # Type slowly
            for char in EMAIL_TEXT:
                textbox.type(char, delay=random.randint(50, 120))

            pyautogui.locateCenterOnScreen('comment.png')
            time.sleep(2)
            pyautogui.click()
        

        except Exception as e:
            print(f"⚠️ Skipped post {i+1}:", e)

    browser.close()
