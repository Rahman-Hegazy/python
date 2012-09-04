#!/usr/bin/python2
# coding=utf8

## 函数接收的参数 local ：是个字典，和 locals() 一样，参见 code.interact
## http://lilydjwg.is-programmer.com/2012/1/9/a-python-debug-function.31673.html
def repl(local, histfile=None, banner=None):
  import readline
  import rlcompleter
  readline.parse_and_bind('tab: complete')
  if histfile is not None and os.path.exists(histfile):
    # avoid duplicate reading
    readline.clear_history()
    readline.set_history_length(10000)
    readline.read_history_file(histfile)
  import code
  ## 默认用 __main__.__dict__ 里边的对象进行补全，而不是 globals()，重新设置 readline 补全函数
  readline.set_completer(rlcompleter.Completer(local).complete)
  code.interact(local=local, banner=banner)
  if histfile is not None:
    readline.write_history_file(histfile)

def foo():
    text = "hello world"
    ## python 内置函数 locals() 可以输出本地变量
    repl(locals())

    #import code
    #pyshell = code.InteractiveConsole(locals=locals())
    #pyshell.interact()

    print text

foo()



