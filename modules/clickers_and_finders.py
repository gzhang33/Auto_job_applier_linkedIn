'''
Author:     Sai Vignesh Golla
LinkedIn:   https://www.linkedin.com/in/saivigneshgolla/

Copyright (C) 2024 Sai Vignesh Golla

License:    GNU Affero General Public License
            https://www.gnu.org/licenses/agpl-3.0.en.html
            
GitHub:     https://github.com/GodsScion/Auto_job_applier_linkedIn

version:    24.12.29.12.30
'''

from config.settings import click_gap, smooth_scroll
from modules.helpers import buffer, print_lg, sleep
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException

# Click Functions
def find_button_in_modal(modal: WebElement, button_text: str, timeout: float = 5.0, 
                         click: bool = True, scroll: bool = True, 
                         scrollTop: bool = False, fallback_xpaths: list[str] | None = None,
                         driver: WebDriver | None = None) -> WebElement | bool:
    """
    Specialized function for finding and clicking buttons within Easy Apply modal.
    Provides enhanced error handling, retry logic, and modal-specific optimizations.
    
    Args:
        modal: Easy Apply modal WebElement (jobs-easy-apply-modal)
        button_text: Button text to find (e.g., "Review", "Submit application", "Done", "Next")
        timeout: Maximum wait time in seconds
        click: Whether to click the button after finding it
        scroll: Whether to scroll to the element
        scrollTop: Whether to scroll element to top of viewport
        fallback_xpaths: Optional list of alternative XPath expressions to try if primary search fails
        driver: Optional WebDriver instance (required if scroll=True, auto-detected from modal if not provided)
        
    Returns:
        WebElement if found and clickable, False if not found
        
    Example:
        # Simple usage
        find_button_in_modal(modal, "Review", timeout=3)
        
        # With fallback strategies
        find_button_in_modal(modal, "Next", fallback_xpaths=[
            './/button[contains(span, "Next")]',
            './/button[@data-easy-apply-next-button]'
        ])
    """
    if not button_text:
        return False
    
    # Primary XPath strategy
    primary_xpath = f'.//span[normalize-space(.)="{button_text}"]'
    xpath_strategies = [primary_xpath]
    
    # Add fallback XPaths if provided
    if fallback_xpaths:
        xpath_strategies.extend(fallback_xpaths)
    
    # Try each XPath strategy
    for xpath in xpath_strategies:
        try:
            button = WebDriverWait(modal, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            
            if scroll:
                # Get driver from modal if not provided
                if driver is None:
                    driver = modal._parent
                scroll_to_view(driver, button, scrollTop)
            
            if click:
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        button.click()
                        buffer(click_gap)
                        return button
                    except Exception as click_error:
                        error_str = str(click_error).lower()
                        
                        # Handle stale element reference
                        if "stale element" in error_str and attempt < max_retries - 1:
                            try:
                                button = WebDriverWait(modal, 2).until(
                                    EC.element_to_be_clickable((By.XPATH, xpath))
                                )
                                continue
                            except:
                                break
                        
                        # Handle click intercepted (element covered by another element)
                        elif "click intercepted" in error_str or isinstance(click_error, ElementClickInterceptedException):
                            # For modal buttons, this might indicate the button is not ready
                            if attempt < max_retries - 1:
                                sleep(0.5)
                                continue
                            else:
                                raise
                        else:
                            raise
            
            return button
            
        except (NoSuchElementException, TimeoutException):
            # Try next XPath strategy
            continue
        except ElementClickInterceptedException:
            # This is expected in some cases (e.g., modal animations)
            print_lg(f"Button '{button_text}' click intercepted, may need manual intervention")
            return False
        except Exception as e:
            # Log unexpected errors but continue to next strategy
            if xpath == primary_xpath:  # Only log for primary strategy to avoid spam
                print_lg(f"Unexpected error finding button '{button_text}' in modal: {e}")
            continue
    
    # All strategies failed
    print_lg(f"Failed to find button '{button_text}' in modal after trying {len(xpath_strategies)} strategy(ies)")
    return False


def wait_span_click(driver: WebDriver, text: str, time: float=5.0, click: bool=True, scroll: bool=True, scrollTop: bool=False) -> WebElement | bool:
    '''
    Finds the span element with the given `text`.
    - Returns `WebElement` if found, else `False` if not found.
    - Clicks on it if `click = True`.
    - Will spend a max of `time` seconds in searching for each element.
    - Will scroll to the element if `scroll = True`.
    - Will scroll to the top if `scrollTop = True`.
    '''
    if text:
        try:
            # 使用更稳定的等待条件，避免 stale element 问题
            button = WebDriverWait(driver, time).until(
                EC.element_to_be_clickable((By.XPATH, './/span[normalize-space(.)="'+text+'"]'))
            )
            if scroll:  
                scroll_to_view(driver, button, scrollTop)
            if click:
                # 添加重试机制处理 stale element
                max_retries = 3
                for attempt in range(max_retries):
                    try:
                        button.click()
                        buffer(click_gap)
                        break
                    except Exception as stale_error:
                        if "stale element" in str(stale_error).lower() and attempt < max_retries - 1:
                            # 重新定位元素
                            button = WebDriverWait(driver, 2).until(
                                EC.element_to_be_clickable((By.XPATH, './/span[normalize-space(.)="'+text+'"]'))
                            )
                            continue
                        else:
                            raise stale_error
            return button
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)
            return False

def multi_sel(driver: WebDriver, texts: list, time: float=5.0) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that text.
    - Will spend a max of `time` seconds in searching for each element.
    '''
    for text in texts:
        ##> ------ Dheeraj Deshwal : dheeraj20194@iiitd.ac.in/dheerajdeshwal9811@gmail.com - Bug fix ------
        wait_span_click(driver, text, time, False)
        ##<
        try:
            button = WebDriverWait(driver,time).until(EC.presence_of_element_located((By.XPATH, './/span[normalize-space(.)="'+text+'"]')))
            scroll_to_view(driver, button)
            button.click()
            buffer(click_gap)
        except Exception as e:
            print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)

def multi_sel_noWait(driver: WebDriver, texts: list, actions: ActionChains = None) -> None:
    '''
    - For each text in the `texts`, tries to find and click `span` element with that class.
    - If `actions` is provided, bot tries to search and Add the `text` to this filters list section.
    - Won't wait to search for each element, assumes that element is rendered.
    '''
    for text in texts:
        try:
            button = driver.find_element(By.XPATH, './/span[normalize-space(.)="'+text+'"]')
            scroll_to_view(driver, button)
            button.click()
            buffer(click_gap)
        except Exception as e:
            if actions: company_search_click(driver,actions,text)
            else:   print_lg("Click Failed! Didn't find '"+text+"'")
            # print_lg(e)

def boolean_button_click(driver: WebDriver, actions: ActionChains, text: str) -> None:
    '''
    Tries to click on the boolean button with the given `text` text.
    '''
    try:
        list_container = driver.find_element(By.XPATH, './/h3[normalize-space()="'+text+'"]/ancestor::fieldset')
        button = list_container.find_element(By.XPATH, './/input[@role="switch"]')
        scroll_to_view(driver, button)
        actions.move_to_element(button).click().perform()
        buffer(click_gap)
    except Exception as e:
        print_lg("Click Failed! Didn't find '"+text+"'")
        # print_lg(e)

# Find functions
def find_by_class(driver: WebDriver, class_name: str, time: float=5.0) -> WebElement | Exception:
    '''
    Waits for a max of `time` seconds for element to be found, and returns `WebElement` if found, else `Exception` if not found.
    '''
    return WebDriverWait(driver, time).until(EC.presence_of_element_located((By.CLASS_NAME, class_name)))

# Scroll functions
def scroll_to_view(driver: WebDriver, element: WebElement, top: bool = False, smooth_scroll: bool = smooth_scroll) -> None:
    '''
    Scrolls the `element` to view.
    - `smooth_scroll` will scroll with smooth behavior.
    - `top` will scroll to the `element` to top of the view.
    '''
    if top:
        return driver.execute_script('arguments[0].scrollIntoView();', element)
    behavior = "smooth" if smooth_scroll else "instant"
    return driver.execute_script('arguments[0].scrollIntoView({block: "center", behavior: "'+behavior+'" });', element)

# Enter input text functions
def text_input_by_ID(driver: WebDriver, id: str, value: str, time: float=5.0) -> None | Exception:
    '''
    Enters `value` into the input field with the given `id` if found, else throws NotFoundException.
    - `time` is the max time to wait for the element to be found.
    '''
    username_field = WebDriverWait(driver, time).until(EC.presence_of_element_located((By.ID, id)))
    username_field.send_keys(Keys.CONTROL + "a")
    username_field.send_keys(value)

def try_xp(driver: WebDriver, xpath: str, click: bool=True, timeout: float=5.0) -> WebElement | bool:
    """
    改进版：添加显式等待机制，提高定位稳定性
    """
    try:
        if click:
            element = WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )
            element.click()
            return True
        else:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            return element
    except Exception as e:
        return False

def try_linkText(driver: WebDriver, linkText: str) -> WebElement | bool:
    try:    return driver.find_element(By.LINK_TEXT, linkText)
    except:  return False

def try_find_by_classes(driver: WebDriver, classes: list[str], timeout: float=5.0) -> WebElement | ValueError:
    """
    改进版：添加显式等待，提高定位成功率
    """
    for cla in classes:
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((By.CLASS_NAME, cla))
            )
            return element
        except Exception:
            continue
    raise ValueError("Failed to find an element with given classes")

def company_search_click(driver: WebDriver, actions: ActionChains, companyName: str) -> None:
    '''
    Tries to search and Add the company to company filters list.
    '''
    wait_span_click(driver,"Add a company",1)
    search = driver.find_element(By.XPATH,"(.//input[@placeholder='Add a company'])[1]")
    search.send_keys(Keys.CONTROL + "a")
    search.send_keys(companyName)
    buffer(3)
    actions.send_keys(Keys.DOWN).perform()
    actions.send_keys(Keys.ENTER).perform()
    print_lg(f'Tried searching and adding "{companyName}"')

def text_input(actions: ActionChains, textInputEle: WebElement | bool, value: str, textFieldName: str = "Text") -> None | Exception:
    if textInputEle:
        sleep(1)
        # actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
        textInputEle.clear()
        textInputEle.send_keys(value.strip())
        sleep(2)
        actions.send_keys(Keys.ENTER).perform()
    else:
        print_lg(f'{textFieldName} input was not given!')