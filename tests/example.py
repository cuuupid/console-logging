# Old features
from console_logging import console
console.log("This should show up as a log.")
console.error("This should show up as an error.")
console.success("This should show up as a success.")
console.info("This should show up as an info.")

# New features
from console_logging.console import Console
console=Console()
console.log("This should show up as a log.")
console.error("This should show up as an error.")
console.success("This should show up as a success.")
console.info("This should show up as an info.")
console.secure("Test","This should not show up.")
console.setVerbosity(5)
console.log("This should show up as a log.")
console.error("This should show up as an error.")
console.success("This should show up as a success.")
console.info("This should show up as an info.")
console.secure("Test","This should show up.")
console.mute()
console.log("This log should not show up.")
console.error("This error should not show up.")
console.success("This success should not show up.")
console.info("This info should not show up.")
console.secure("Test","This should not show up.")
