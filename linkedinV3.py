from playwright.sync_api import sync_playwright
import time
import help 
import random
EMAIL_TEXT = input("Enter the comment text you want to post: ")
SEARCH_QUERY = input("Enter your LinkedIn search query: ")

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()

    page.goto("https://www.linkedin.com")
    print("Do manual login")
    page.wait_for_timeout(30000)
    
    page.goto(f"https://www.linkedin.com/search/results/content/?keywords={SEARCH_QUERY}")
    time.sleep(random.randint(3, 6))

    #custom help functions

    help.helperSort()

    time.sleep(random.randint(3, 6))

    help.findlatest()

    time.sleep(random.randint(3, 6))

    help.showres()

    time.sleep(random.randint(3, 6))

    posts = page.locator("div.feed-shared-update-v2").all()

    print(f"Found {len(posts)} posts")

    for post in posts[:5]:
        try:
            comment_button = post.locator("button[aria-label*='Comment']")
            if comment_button.count() > 0:
                comment_button.click()
                time.sleep(2)

                comment_box = post.locator("div[role='textbox']")
                comment_box.click()
                comment_box.fill(EMAIL_TEXT)
                
                print("commented")
                time.sleep(2)

                help.helper()

                print("Posted")
                time.sleep(10) 

        except Exception as e:
            print("Skipped one post:", e)

    browser.close()