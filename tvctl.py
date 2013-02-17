import serial

class NEC:
  def __init__(self,tty=0):
    self.serial = serial.Serial(tty)

  def on(self):
    self.serial.write('\x30\x30\x21\x0D')

  def off(self):
    self.serial.write('\x30\x30\x21\x0D')

  def vid1(self):
    self.serial.write('\x30\x30\x5F\x76\x31\x0D')

  def vid2(self):
    self.serial.write('\x30\x30\x5F\x76\x34\x0D')

  def svid(self):
    self.serial.write('\x30\x30\x5F\x76\x33\x0D')

  def hd1(self):
    self.serial.write('\x30\x30\x5F\x76\x32\x0D')

  def hd2(self):
    self.serial.write('\x30\x30\x5F\x76\x35\x0D')

  def vga(self):
    self.serial.write('\x30\x30\x5F\x72\x32\x0D')

  def rgb(self):
    self.serial.write('\x30\x30\x5F\x72\x33\x0D')

  def dvi(self):
    self.serial.write('\x30\x30\x5F\x72\x31\x0D')
