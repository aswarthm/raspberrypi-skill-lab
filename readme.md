
# Raspberry Pi 4 Setup Guide

## Step 1: Download and Install Raspberry Pi Imager

1. Visit the [Raspberry Pi Downloads page](https://www.raspberrypi.org/software/).
2. Download the Raspberry Pi Imager for your operating system (Windows/MacOS/Linux).
3. Install the Raspberry Pi Imager by following the on-screen instructions.

## Step 2: Write OS to microSD Card

1. Insert your microSD card into your computer.
2. Open Raspberry Pi Imager.
3. Click on `CHOOSE DEVICE` and select `Raspberry Pi 4`.
4. Click on `CHOOSE OS` and select `Raspberry Pi OS (64-bit)`.
5. Click on `CHOOSE STORAGE` and select your microSD card.
6. Press `Ctrl` + `Shift` + `X` to open the advanced options menu.
- In the advanced options menu:
  - **Set Hostname:** Ensure the hostname is set to `raspberrypi.local`.
  - **Set username and password:** Set the username as `pi` and password as `12345678`.
  - **Configure WiFi:** Enter your WiFi network's SSID and password.
  - **Enable SSH:** Switch to `Services` tab and check the `Enable SSH` option. Choose `Use password authentication`
  - **Save the changes:** Click on `SAVE` to apply the changes

7. Click on `WRITE` and wait for the process to complete.


## Step 4: Boot Raspberry Pi

1. Eject the microSD card from your computer and insert it into your Raspberry Pi.
2. Connect your Raspberry Pi to power and to your network via Ethernet or previously configured WiFi settings.
3. Wait for the Raspberry Pi to boot up.
> Use [Fing](https://www.fing.com/fing-desktop/) to check whether the Raspberry Pi has booted

## Connect via SSH Using Terminal

1. Open a new Terminal/CMD prompt
2. Enter the following command
```bash
ssh pi@raspberrypi.local
```
3. Accept the security prompt by typing `yes` and enter the password when prompted

## Connect via SSH Using Visual Studio Code

1. Install [Visual Studio Code](https://code.visualstudio.com/download) on your computer
2. Install the "Remote - SSH" extension from the VS Code marketplace.
3. Open VS Code, then open the Command Palette (`Ctrl+Shift+P`).
4. Type `Remote-SSH: Connect to Host...` and press Enter.
5. Type `ssh pi@raspberrypi.local` in the prompt and press enter.
6. Follow the prompts to authenticate and connect.

## Connect via VNC Viewer

### Step 1: Enable VNC Server on Raspberry Pi

1. **Access Terminal on Raspberry Pi:** You can do this via SSH using CMD or VS Code.

2. **Enable VNC Server:** Run the following command in the terminal:

   ```bash
   sudo raspi-config
   ```

3. **Navigate to Interfacing Options:** Use the arrow keys to navigate to `Interfacing Options`, press Enter.

4. **Enable VNC:** Find the VNC option, select it, and then choose `Yes` to enable.

5. **Exit raspi-config:** Select `Finish` and reboot your Raspberry Pi if prompted.

### Step 2: Install VNC Viewer on Your Computer

1. **Download VNC Viewer:** Go to the [RealVNC website](https://www.realvnc.com/en/connect/download/viewer/) and download VNC Viewer for your operating system.

2. **Install VNC Viewer:** Follow the installation instructions specific to your OS.

### Step 3: Connect to Your Raspberry Pi

1. **Open VNC Viewer:** Launch the VNC Viewer application on your computer.

2. **Enter Raspberry Pi's IP Address:** In the top bar, enter the IP address of your Raspberry Pi. If you're unsure of the IP, you can find it using your router's admin interface or a network scanning tool like [Fing](https://www.fing.com/fing-desktop/).

   - The format should be `raspberrypi.local` or the IP address directly, such as `192.168.1.X`.

3. **Authenticate:** When prompted, enter the username (`pi` by default) and password for your Raspberry Pi.

4. **Start Using Raspberry Pi Desktop:** You should now see your Raspberry Pi's desktop environment and be able to control it remotely.

Connecting via VNC Viewer allows you to use the Raspberry Pi's graphical desktop environment from another computer, making it ideal for setups where you don't have access to an additional monitor or keyboard.

# Clone the project

```bash
git clone https://github.com/aswarthm/raspberrypi-skill-lab.git
```
