# run level
runlevel 表示当前系统的运行级别, 可以使用``runlevel``命令查询系统的当前运行级别

linux的运行级别为:

| level | name | desc |
|:---:|---|---|
| 0 | Halt | Shut down the system |
| 1 | Single-user mode  | for administrator tasks |
| 2 | Multi-user mode  | does not configure network and does not export network services |
| 3 | Multi-user mode with network  | Start the system normally |
| 4 | Not used/user defined mode | For special purposes |
| 5 | Start the system normally with approprate display manager | Same as level 3 + display manager |
| 6 | Reboot | Reboot the system |
| S | Single user mode|  do not configure network interface or start daemons |

