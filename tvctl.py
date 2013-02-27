import serial

class NEC:
  def __init__(self,tty=0):
    self.serial = serial.Serial(tty)

  def on(self):
    self.serial.write('\x30\x30\x21\x0D')
    return "Turned TV On (pls wait 1m before doing this again)"

  def off(self):
    self.serial.write('\x30\x30\x21\x0D')
    return "Turned TV Off (pls wait 1m before doing this again)"

  def vid1(self):
    self.serial.write('\x30\x30\x5F\x76\x31\x0D')
    return "Switched Input to Video1"

  def vid2(self):
    self.serial.write('\x30\x30\x5F\x76\x34\x0D')
    return "Switched Input to Video2"

  def svid(self):
    self.serial.write('\x30\x30\x5F\x76\x33\x0D')
    return "Switched Input to SVideo"

  def hd1(self):
    self.serial.write('\x30\x30\x5F\x76\x32\x0D')
    return "Switched Input to HD1"

  def hd2(self):
    self.serial.write('\x30\x30\x5F\x76\x35\x0D')
    return "Switched Input to HD2"

  def vga(self):
    self.serial.write('\x30\x30\x5F\x72\x32\x0D')
    return "Switched Input to VGA"

  def rgb(self):
    self.serial.write('\x30\x30\x5F\x72\x33\x0D')
    return "Switched Input to Component??"

  def dvi(self):
    self.serial.write('\x30\x30\x5F\x72\x31\x0D')
    return "Switched Input to DVI"
