# scanme
Single IP port recon tool, identifies open ports and services using the [sockets](https://docs.python.org/3/library/socket.html) module.
```
______________¶¶¶
_____________¶¶_¶¶¶¶
____________¶¶____¶¶¶
___________¶¶¶______¶¶
___________¶¶¶_______¶¶
__________¶¶¶¶________¶¶
__________¶_¶¶_________¶¶
__________¶__¶¶_________¶¶____¶¶
__________¶__¶¶__________¶¶¶¶¶¶¶
_________¶¶__¶¶¶______¶¶¶¶¶¶___¶
_________¶¶___¶¶__¶¶¶¶¶¶__¶¶
_______¶¶_¶____¶¶¶¶________¶¶
______¶¶__¶¶___¶¶__________¶¶
_____¶¶____¶¶___¶¶__________¶¶
___¶¶_______¶¶___¶¶_________¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶__¶¶_________¶
_¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶_¶¶________¶¶
¶¶__¶¶¶¶¶¶____¶¶¶¶¶¶¶¶¶______¶¶
¶¶¶¶¶___¶______¶___¶¶¶¶¶_____¶¶
________¶¶¶¶¶¶¶¶______¶¶¶¶¶_¶¶
______¶¶¶¶¶¶¶¶¶¶¶________¶¶¶¶
______¶¶¶¶¶¶¶¶¶¶¶¶
______¶__¶¶_¶¶¶¶¶¶
_____¶¶______¶___¶
_____¶¶_____¶¶___¶
_____¶______¶¶___¶
____¶¶______¶¶___¶¶
____¶¶______¶¶___¶¶
___¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶
__¶¶¶¶¶¶¶¶¶_¶¶¶¶¶¶¶¶
__¶¶________¶¶¶____¶¶
____¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶¶

█▀▀ █▀▀ █▀▀█ █▀▀▄ █▀▄▀█ █▀▀ 
▀▀█ █░░ █▄▄█ █░░█ █░▀░█ █▀▀ 
▀▀▀ ▀▀▀ ▀░░▀ ▀░░▀ ▀░░░▀ ▀▀▀
@𝖆𝖚𝖙𝖍𝖔𝖗: 𝖕𝖗𝖔𝖉𝖘𝖊𝖆𝖓𝖇 (𝖍𝖙𝖙𝖕𝖘://𝖌𝖎𝖙𝖍𝖚𝖇.𝖈𝖔𝖒/𝖕𝖗𝖔𝖉𝖘𝖊𝖆𝖓𝖇/𝖘𝖈𝖆𝖓𝖒𝖊)
```
### Installation
Clone:
```bash
git clone https://github.com/prodseanb/scanme.git
```
Run:
```bash
cd scanme
python3 run.py [target]
```
Examples:
```bash
python3 run.py scanme.nmap.org
python3 run.py 172.16.101.134
```
### Run on Docker
```bash
sudo docker pull prodseanb/scanme
sudo docker run -t -i scanme [target]
```
### Faster, more efficient
Using [threads](https://docs.python.org/3/library/threading.html) to maximize scanning efficiency.
```
Ports = 0-5000
Initial commit (before threads):
[*] Time taken: 0:00:21.249790
This commit (with threads):
[*] Time taken: 0:00:07.769030
```
### Identifies open/listening ports and services
```
[Hit] 172.16.101.134:53 = Open        [*] SERVICE: domain
[Hit] 172.16.101.134:80 = Open        [*] SERVICE: http
[Hit] 172.16.101.134:443 = Open        [*] SERVICE: https
[Hit] 172.16.101.134:1883 = Open        [*] SERVICE: none
```
### Scan more ports
On Linux: `ulimit -n [limit]`.<br />
On Windows, find this line and adjust the value:
```python
main.MAX_ports = 1000
```
### Let's work...
As an open-source advocate, I invite you to work with me on this project. Send me a pull request. 🤘 Want to conduct other business? Send me a message on [LinkedIn](https://www.linkedin.com/in/sean-bachiller-40b63417b/). 
