## Over-The-Wire -writeup-
### Bandit6 (bandit6@bandit.labs.overthewire.org)

---
#### Etape 1

Il nous est demandé de chercher un fichier dans tout le serveur, qui répond à ces critères:
- Appartenant à l'utilisateur *bandit7*
- Appartenant au groupe *bandit6*
- Taille: 33bytes

On va donc utiliser encore une fois `find` et ses arguments pour trouver le fichier en question:  
`find / -user bandit7 -group bandit6 -size 33c` va chercher exactement cela.
<details>
<summary>/Voir le log/</summary>
find: ‘/run/lvm’: Permission denied
find: ‘/run/screen/S-bandit24’: Permission denied
find: ‘/run/screen/S-bandit1’: Permission denied
find: ‘/run/screen/S-bandit0’: Permission denied
find: ‘/run/screen/S-bandit5’: Permission denied
find: ‘/run/screen/S-bandit9’: Permission denied
find: ‘/run/screen/S-bandit25’: Permission denied
find: ‘/run/screen/S-bandit2’: Permission denied
find: ‘/run/screen/S-bandit12’: Permission denied
find: ‘/run/screen/S-bandit11’: Permission denied
find: ‘/run/screen/S-bandit30’: Permission denied
find: ‘/run/screen/S-bandit29’: Permission denied
find: ‘/run/screen/S-bandit7’: Permission denied
find: ‘/run/screen/S-bandit14’: Permission denied
find: ‘/run/screen/S-bandit16’: Permission denied
find: ‘/run/screen/S-bandit26’: Permission denied
find: ‘/run/screen/S-bandit15’: Permission denied
find: ‘/run/screen/S-bandit13’: Permission denied
find: ‘/run/screen/S-bandit33’: Permission denied
find: ‘/run/screen/S-bandit4’: Permission denied
find: ‘/run/screen/S-bandit28’: Permission denied
find: ‘/run/screen/S-bandit10’: Permission denied
find: ‘/run/screen/S-bandit8’: Permission denied
find: ‘/run/screen/S-bandit27’: Permission denied
find: ‘/run/screen/S-bandit18’: Permission denied
find: ‘/run/screen/S-bandit22’: Permission denied
find: ‘/run/screen/S-bandit31’: Permission denied
find: ‘/run/screen/S-bandit19’: Permission denied
find: ‘/run/screen/S-bandit21’: Permission denied
find: ‘/run/screen/S-bandit23’: Permission denied
find: ‘/run/screen/S-bandit20’: Permission denied
find: ‘/run/shm’: Permission denied
find: ‘/run/lock/lvm’: Permission denied
find: ‘/var/spool/rsyslog’: Permission denied
find: ‘/var/spool/cron/crontabs’: Permission denied
find: ‘/var/log’: Permission denied
find: ‘/var/tmp’: Permission denied
find: ‘/var/cache/ldconfig’: Permission denied
find: ‘/var/cache/apt/archives/partial’: Permission denied
/var/lib/dpkg/info/bandit7.password
find: ‘/var/lib/apt/lists/partial’: Permission denied
find: ‘/var/lib/polkit-1’: Permission denied
find: ‘/cgroup2/csessions’: Permission denied
find: ‘/home/bandit28-git’: Permission denied
find: ‘/home/bandit30-git’: Permission denied
find: ‘/home/bandit31-git’: Permission denied
find: ‘/home/bandit5/inhere’: Permission denied
find: ‘/home/bandit27-git’: Permission denied
find: ‘/home/bandit29-git’: Permission denied
find: ‘/tmp’: Permission denied
find: ‘/lost+found’: Permission denied
find: ‘/root’: Permission denied
find: ‘/etc/ssl/private’: Permission denied
find: ‘/etc/lvm/backup’: Permission denied
find: ‘/etc/lvm/archive’: Permission denied
find: ‘/etc/polkit-1/localauthority’: Permission denied
find: ‘/sys/fs/pstore’: Permission denied
find: ‘/proc/tty/driver’: Permission denied
find: ‘/proc/15724/task/15724/fd/6’: No such file or directory
find: ‘/proc/15724/task/15724/fdinfo/6’: No such file or directory
find: ‘/proc/15724/fd/5’: No such file or directory
find: ‘/proc/15724/fdinfo/5’: No such file or directory
find: ‘/boot/lost+found’: Permission denied
</details>

**Cependant on a également les messages d'erreurs comme "Permission denied", ou "No such file or directory".**  

---
#### Etape 2

Les trier rendrait notre output plus visible, pour cela j'utilise `grep -v` qui va retourner l'inverse de nos arguments.  
`grep -v -e "Permission denied" -e "No such file or directory"` va renvoyer chaque ligne **qui ne contiennent pas ces phrases.**

On fusionne donc les deux commandes, et on obient `find / -user bandit7 -group bandit6 -size 33c 2>&1 |grep -v -e "Permission denied" -e "No such file or directory"`, qui nous renvoie:
> /var/lib/dpkg/info/bandit7.password

---
#### Etape 3

Il ne nous reste plus qu'à observer le contenu de ce fichier:
> bandit6@bandit:~$ cat /var/lib/dpkg/info/bandit7.password  
> HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs

---
Mot de passe: **HKBPTKQnIay4Fw76bEy8PVxKEDQRKTzs**
