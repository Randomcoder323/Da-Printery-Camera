# Da printery Camera


## What and Why?
Thsi is a cmaera timelapse project for my A1 mini to be able to take timelapse. Its powred by an esp32 which a limit switch connected to my computer, and a camera, powered by python code to take pcitrues on each layer! I made this camera timelapse module to be able to take cool timelapse of my prints with a way better camera than the 0.5 fps 240 quality camera on the a1 mini. I can also remotely monitor my print as an added bonus!

## How will I assemble this? 
I will print the limt siwtch mount and screw the switch in, then put it on the printer. Before this  I will solder the wires to the esp32. I will put the camera on the table so its stable and both the cmaera and esp32 to my computer. I will lastly run my code and adjust the printer gcode.

## Pictures and Assembly 
<p align="center">
  <img width="964" height="552" alt="image" src="https://github.com/user-attachments/assets/ec45c9e2-f04f-4fa1-b18f-5ee92acd2259" /><br><br>
  <img width="982" height="745" alt="Screenshot 2026-03-20 074557" src="https://github.com/user-attachments/assets/a44520ba-96b7-4021-ba55-a9405be804c0" /><br><br>
  <img width="1005" height="768" alt="Screenshot 2026-03-19 181841" src="https://github.com/user-attachments/assets/fa2c88db-164e-4870-b08b-ed97d85e9e4a" /><br><br>
  <img width="475" height="509" alt="Screenshot 2026-03-19 181812" src="https://github.com/user-attachments/assets/09c46d57-8f92-4d31-a1f1-656d92e6808b" /><br><br>
  <img width="1005" height="681" alt="Screenshot 2026-03-19 174410" src="https://github.com/user-attachments/assets/50bbe6d1-c20a-4774-830b-6af65548aac5" /><br><br>
  <img width="614" height="398" alt="Screenshot 2026-03-19 174123" src="https://github.com/user-attachments/assets/917b95ba-6acb-42c3-b1fb-753c05f00a54" />
</p>

## Why?

I made this camera timelapse module to be able to take cool timelapse of my prints with a way better camera than the 0.5 fps 240 quality camera on the a1 mini. I can also remotely monitor my print as an added bonus!

## BOM

| Item                      | Qty | Price | Link |
|---------------------------|-----|-------|------|
| ESP32 CH340C              | 1   | $3.32 | [Buy](https://www.aliexpress.us/item/3256804290552594.html) |
| Arced 21mm limit switch   | 1   | $1.59 | [Buy](https://www.aliexpress.us/item/3256808047511109.html) |
| Camera module             | 1   | $11.11| [Buy](https://www.aliexpress.us/item/3256810425121893.html) |
| 3D printed parts          | 1   | N/A   | Self printed |
| 64GB MicroSD card         | 1   | $5.08 | [Buy](https://www.aliexpress.us/item/3256802611588453.html) |

**Total (after coupons): ~$21**

## Wiring and Code
The limit siwtch is goind to be connected to the esp 32 gpio pin and ground. The esp 32 will be connected to my computer, which will also be conencted to the camera as an external camera. Everything is going to be soldered and then wrapped in electric tape to give it a clean look. I really like how everything is clean and simple, as I made moutn for the limit switch and a box for the esp32 with e wires.

<p align="center">
  <img width="961" height="544" alt="image" src="https://github.com/user-attachments/assets/35707a21-5dae-45b8-8010-1f1f731a1680" />
</p>

Code can be found under **[Capture.py](PC_Camera_Capture/capture.py)**

Look at  **[Timelapse.gcode](PC_Camera_Capture/Timelapse.gcode)** to make the timelapse work in the slicer.

