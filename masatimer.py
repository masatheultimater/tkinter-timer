from tkinter import *
from tkinter import ttk # Tk themed widgets for beautiful UI
from tkinter import messagebox
import time

class MasaTimer(Frame):
  def __init__(self, master):
    # super().__init__(master)
    # self.pack()
    
    Frame.__init__(self, master)
    self.master.title('Masa Timer')
    self.master.geometry('300x150')

    self.secs = IntVar(value=0)
    self.mins = IntVar(value=0)
    self.total_secs = 0
    self.is_running = False

    self.entry1 = ttk.Entry(self, width=2, textvariable=self.mins, font='Arial, 30')
    self.label1 = ttk.Label(self, text=u'分', font='Arial, 30')
    self.entry2 = ttk.Entry(self, width=2, textvariable=self.secs, font='Arial, 30')
    self.label2 = ttk.Label(self, text=u'秒', font='Arial, 30')
    self.time_left_clock = ttk.Label(self, text=u'00:00', font='Arial, 40')
    self.start_button = ttk.Button(
      self,
      text='START',
      command=self.start
    )
    self.stop_button = ttk.Button(
      self,
      text='STOP',
      command=self.stop
    )
    self.reset_button = ttk.Button(
      self,
      text='RESET',
      command=self.reset_timer
    )
    
    self.entry1.pack(side=LEFT)
    self.label1.pack(side=LEFT)
    self.entry2.pack(side=LEFT)
    self.label2.pack(side=LEFT)

    self.start_button.pack(side=LEFT)
    self.stop_button.pack(side=LEFT)
    self.reset_button.pack(side=LEFT)

    self.time_left_clock.pack()
  
  def calculate_time_rest(self):
    print('calculate_time_rest begins.')
    if self.is_running:
      time_rest = self.finish_time - time.time()
      if time_rest < 0:
        self.time_left_clock.config(text='Time Up!!!')
        messagebox.showwarning('時間切れのお知らせ', 'Time Is Up!!!! \n お疲れさまでした')
      else:
        self.time_left_clock.config(text='%02d:%02d'%(time_rest/60,time_rest%60))
        self.after(1000, self.calculate_time_rest)

  # for computing length of target time
  # turn the input mins/secs into total secs only
  def target_time_in_secs(self):
    print('target_time_in_secs begins.')
    # total_secs as Int
    self.total_secs = self.mins.get() * 60 + self.secs.get()
    print('total_secs:' + str(self.total_secs))

  def start(self):
    print('start begins.')
    if self.is_running:
      pass
    else:
      self.is_running = True
      self.target_time_in_secs()
      # finish_time as float
      self.finish_time = time.time() + float(self.total_secs)
      print(time.time())
      print(self.total_secs)
      print(self.finish_time)
      print(time.time())
      self.calculate_time_rest()
    
  def stop(self):
    if not self.is_running:
      pass
    else:
      is_running = False
      # TODO ストップさせたときの処理
    
  def reset_timer(self):
    if self.is_running:
      pass
    else:
      self.time_left_clock.config(text='00:00')

# for exec as script
if __name__ == '__main__':
    root = Tk()
    app = MasaTimer(master=root)
    app.pack()
    app.mainloop()

# Global Window Settings
# root = Tk()
# root.title('Masa Timer')
# root.geometry('300x150')

# Variables
# secs = IntVar(value=0)
# mins = IntVar(value=0)
# finish_time = 0.0
# total_secs = 0
# is_running = False

# Widgets
# frame1 = ttk.Frame(root)
# frame2 = ttk.Frame(root)
# frame3 = ttk.Frame(root)

# entry1 = ttk.Entry(frame1, width=2, textvariable=mins, font='Arial, 30')
# label1 = ttk.Label(frame1, text=u'分', font='Arial, 30')
# entry2 = ttk.Entry(frame1, width=2, textvariable=secs, font='Arial, 30')
# label2 = ttk.Label(frame1, text=u'秒', font='Arial, 30')
# time_left_clock = ttk.Label(frame3, text=u'00:00', font='Arial, 40')

# start_button = ttk.Button(
#   frame2,
#   text='START',
#   command=start()
# )
# stop_button = ttk.Button(
#   frame2,
#   text='STOP',
#   command=stop()
# )
# reset_button = ttk.Button(
#   frame2,
#   text='RESET',
#   command=reset_timer()
# )

# def calculate_time_rest():
#   print('calculate_time_rest begins.')
#   global is_running,time_rest,finish_time,time_left_clock
#   if is_running:
#     time_rest = finish_time - time.time()
#     if time_rest < 0:
#       time_left_clock.config(text='Time Up!!!')
#       # TODO ダイアログボックスでお知らせ
#     else:
#       time_left_clock.config(text='%02d:%02d'%(time_rest/60,time_rest%60))
#       frame3.after(1000, calculate_time_rest)

# # for computing length of target time
# # turn the input mins/secs into total secs only
# def target_time_in_secs():
#   print('target_time_in_secs begins.')
#   global is_running,mins,secs,total_secs
#   # total_secs as Int
#   total_secs = mins.get() * 60 + secs.get()
#   print('total_secs:' + str(total_secs))

# def start():
#   print('start begins.')
#   global is_running,finish_time
#   is_running = True
#   target_time_in_secs()
#   # finish_time as float
#   finish_time = time.time() + total_secs
#   calculate_time_rest()
  
# def stop():
#   global is_running
#   if not is_running:
#     pass
#   else:
#     is_running = False
#     # TODO ストップさせたときの処理
  
# def reset_timer():
#   global is_running,time_left_clock
#   if is_running:
#     pass
#   else:
#     time_left_clock.config(text='00:00')

# Layout
# frame1.pack()
# entry1.pack(side=LEFT)
# label1.pack(side=LEFT)
# entry2.pack(side=LEFT)
# label2.pack(side=LEFT)

# frame2.pack()
# start_button.pack(side=LEFT)
# stop_button.pack(side=LEFT)
# reset_button.pack(side=LEFT)

# frame3.pack()
# time_left_clock.pack()

# Start
# root.mainloop()

