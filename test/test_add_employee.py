Record









Target:

Library


25
    page2 = context.new_page()
26
    page2.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewEmployeeList")
27
    page2.close()
28
    page1.get_by_role("textbox", name="Type for hints...").first.click()
29
    page1.get_by_role("textbox", name="Type for hints...").first.press("ControlOrMeta+ر")
30
    page1.get_by_role("textbox", name="Type for hints...").first.click()
31
    page1.get_by_role("textbox", name="Type for hints...").first.fill("Test")
32
    page1.get_by_role("textbox").nth(2).click()
33
    page1.get_by_role("button", name=" Add").click()
34
    page1.get_by_role("button", name="Reload").click()
35
    page1.get_by_role("textbox", name="Username").click()
36
    page1.get_by_role("textbox", name="Username").fill("Admin")
37
    page1.locator("div").filter(has_text=re.compile(r"^Password$")).nth(1).click()
38
    page1.get_by_role("textbox", name="Password").fill("admin123")
39
    page1.get_by_role("textbox", name="Password").press("Enter")
40
    page1.get_by_role("button", name="Login").click()
41
    page1.get_by_role("textbox", name="First Name").click()
42
    page1.get_by_role("textbox", name="First Name").fill("Test")
43
    page1.get_by_role("textbox", name="Last Name").click()
44
    page1.get_by_role("textbox", name="Last Name").fill("User")
45
    page1.get_by_role("button", name="Save").click()
46
    page1.goto("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/167")
47
​
48
    # ---------------------
49
    context.close()
50
    browser.close()
51
​
52
​
53
with sync_playwright() as playwright:
54
    run(playwright)
55
​

