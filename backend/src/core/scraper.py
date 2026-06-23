import logging
from playwright.async_api import BrowserContext, async_playwright
from .config import settings

logger = logging.getLogger("ScraperProvider")

class ScraperException(Exception):
    """Custom exception raised when scraping process fails."""
    pass

class ScraperProvider:
    """Factory class for Playwright browser context."""
    
    @staticmethod
    async def get_context(playwright, storage_state=None, viewport=None) -> BrowserContext:
        """
        Initializes and returns a Playwright BrowserContext based on the environment.
        In LOCAL_DEV, uses standard headless Playwright.
        In CLOUD_PROD, implements proxy support and prepares stealth usage.
        """
        try:
            launch_args = {"headless": True, "args": ["--start-maximized"]}
            
            if settings.is_cloud and settings.proxy_url:
                logger.info("Configuring scraper with third-party proxy for CLOUD_PROD.")
                launch_args["proxy"] = {"server": settings.proxy_url}
            else:
                logger.info("Configuring standard scraper for LOCAL_DEV.")
            
            browser = await playwright.chromium.launch(**launch_args)
            context_args = {}
            if storage_state:
                context_args["storage_state"] = storage_state
            if viewport:
                context_args["viewport"] = viewport
                
            context = await browser.new_context(**context_args)
            # Store browser on context to keep track of it if needed
            context.browser = browser
            
            return context
        except Exception as e:
            logger.error(f"Browser initialization failed: {str(e)}")
            raise ScraperException(f"Browser-Init-Failure: {str(e)}")

    @staticmethod
    async def create_page(context: BrowserContext):
        """Creates a new page, applying stealth if in CLOUD_PROD."""
        try:
            page = await context.new_page()
            if settings.is_cloud:
                from playwright_stealth import stealth_async
                await stealth_async(page)
                logger.info("Stealth wrapper applied to page.")
            return page
        except Exception as e:
            logger.error(f"Page creation failed: {str(e)}")
            raise ScraperException(f"Page-Creation-Failure: {str(e)}")
