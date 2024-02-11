CIRCUITPY_CREATOR_ID =  0x0000239A
CIRCUITPY_CREATION_ID = 0x00320004

IDF_TARGET = esp32

CIRCUITPY_ESP_FLASH_MODE = dio
CIRCUITPY_ESP_FLASH_FREQ = 40m
CIRCUITPY_ESP_FLASH_SIZE = 4MB

CIRCUITPY_ESPCAMERA = 0


# Include these Python libraries in firmware.
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_asyncio
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_Ticks
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_NeoPixel
FROZEN_MPY_DIRS += $(TOP)/frozen/Adafruit_CircuitPython_HTTPServer
FROZEN_MPY_DIRS += $(TOP)/frozen/my-stuff


