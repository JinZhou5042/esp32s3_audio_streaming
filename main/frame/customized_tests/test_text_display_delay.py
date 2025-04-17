import asyncio
import time
from frameutils import Bluetooth
from frame_sdk import Frame
from frame_sdk.display import PaletteColors, Alignment

async def main():
    async with Frame() as frame:
        b = Bluetooth()
        
        lyrics = [
            "Never gonna give you up",
            "Never gonna let you down",
            "Never gonna run around and desert you",
            "Never gonna make you cry",
            "Never gonna say goodbye",
            "Never gonna tell a lie and hurt you",
            "Never gonna stop",
            "Never gonna give you up",
            "Never gonna let you down",
            "Never gonna run around and desert you",
            "Never gonna make you cry",
            "Never gonna say goodbye",
            "Never gonna tell a lie and hurt you"
        ]

        print("开始逐行刷新，每0.5s一次")

        for line in lyrics:
            # Capture the current time (send time)
            start_time = time.time()

            # Display the text
            await frame.display.show_text(line, color=PaletteColors.YELLOW)

            # Capture the time when the text is shown
            end_time = time.time()

            # Calculate the delay in seconds
            delay = end_time - start_time
            print(f"发送: {line}")
            print(f"延迟: {delay:.4f} 秒")

            # Wait for 0.5 seconds before showing the next line
            await asyncio.sleep(0.5)
        
        print("逐行刷新完成")

# Run the main function
asyncio.run(main())

