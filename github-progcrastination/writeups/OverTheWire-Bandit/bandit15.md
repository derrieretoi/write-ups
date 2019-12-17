## Over-The-Wire -writeup-
### Bandit15 (bandit15@bandit.labs.overthewire.org)

---
#### Etape 1

Dans ce niveau il faut envoyer le mot de passe du niveau actuel, mais cette fois ci **avec une encryption SSL, sur localhost au port 30001**.

L'encryption SSL réfère à l'utilisation d'**OpenSSL**. Pour se connecter, on utilise la commande `openssl s_client -connect [host]:[port]`.

Ici, la commande à éxecuter est: `ssl s_client -connect localhost:30001`, qui nous renvoie ensuite tout les détails de la connection:
<detais>
<summary>/Voir le log/</summary>

```console
 bandit15@bandit:~$ openssl s_client -connect localhost:30001
 CONNECTED(00000003)
 depth=0 CN = localhost
 verify error:num=18:self signed certificate
 verify return:1
 depth=0 CN = localhost
 verify return:1
 ---
 Certificate chain
  0 s:/CN=localhost
    i:/CN=localhost
 ---
 Server certificate
 -----BEGIN CERTIFICATE-----
 MIICBjCCAW+gAwIBAgIEfkeLojANBgkqhkiG9w0BAQUFADAUMRIwEAYDVQQDDAls
 b2NhbGhvc3QwHhcNMTkwODAzMDc0OTMxWhcNMjAwODAyMDc0OTMxWjAUMRIwEAYD
 VQQDDAlsb2NhbGhvc3QwgZ8wDQYJKoZIhvcNAQEBBQADgY0AMIGJAoGBAMDGwHmT
 GntqHvPYiM0wm4Dsmhlmiywaj0CGZKW1Cx6ze9pH+iWXEvcnWga4Kfevqh0LJLeS
 jmgE6hFRK9rTwq+q6UE0hADazxb7r8jpthnHwKyRGEtFmsFTv/JqJDk+V5cngA4Y
 m4scTjF+r1Y7jQA5VkUPHy+eYoNoqRqGh7JhAgMBAAGjZTBjMBQGA1UdEQQNMAuC
 CWxvY2FsaG9zdDBLBglghkgBhvhCAQ0EPhY8QXV0b21hdGljYWxseSBnZW5lcmF0
 ZWQgYnkgTmNhdC4gU2VlIGh0dHBzOi8vbm1hcC5vcmcvbmNhdC8uMA0GCSqGSIb3
 DQEBBQUAA4GBAEICbhntCy/wyg56HQpox3nt8YtTkr6g21P4akxso7m08u6FuyiY
 t/8yd+iph6qlRDHQ+D8T4TcpflsV8YKPXIgMoJQtGkuVgqHeCfgBEJcx+T52F8aX
 84l5d7tEr9XEuCPKIlf4/GL8wOQLww2a2+sjlSwa8S1XlkbC61JzPyS3
 -----END CERTIFICATE-----
 subject=/CN=localhost
 issuer=/CN=localhost
 ---
 No client certificate CA names sent
 Peer signing digest: SHA512
 Server Temp Key: X25519, 253 bits
 ---
 SSL handshake has read 1019 bytes and written 269 bytes
 Verification error: self signed certificate
 ---
 New, TLSv1.2, Cipher is ECDHE-RSA-AES256-GCM-SHA384
 Server public key is 1024 bit
 Secure Renegotiation IS supported
 Compression: NONE
 Expansion: NONE
 No ALPN negotiated
 SSL-Session:
     Protocol  : TLSv1.2
     Cipher    : ECDHE-RSA-AES256-GCM-SHA384
     Session-ID: B69A139E8F7E3227A1FC65CC14FA5DD835CD7CCBFDB23062379AA988B39B1CB2
     Session-ID-ctx: 
     Master-Key: 752E17123F079818836DCCDBFCE03461F4FC5BB360FA6D232E1AD40AEE91D38F2EF9A075FBED20A660AAFB8BDC6A784B
     PSK identity: None
     PSK identity hint: None
     SRP username: None
     TLS session ticket lifetime hint: 7200 (seconds)
     TLS session ticket:
     0000 - 6a 32 a6 c7 27 26 f0 c8-b4 75 99 96 41 ed a8 13   j2..'&...u..A...
     0010 - 8e 71 1d 65 da 2f 5c 55-7e 27 24 fd 42 18 3d 79   .q.e./\U~'$.B.=y
     0020 - 6e df 9d 12 03 65 e0 d5-48 b5 7f d0 b4 f2 cb 25   n....e..H......%
     0030 - 6d ae 99 4a e8 5e 55 08-11 db ad a1 fa 57 b0 6a   m..J.^U......W.j
     0040 - 46 6f 40 4d 87 8b 4e 2c-fe 20 d1 39 d4 d6 3b 56   Fo@M..N,. .9..;V
     0050 - 47 fd 70 06 36 b3 19 57-d6 6f 31 3d fa 4a 83 44   G.p.6..W.o1=.J.D
     0060 - c5 21 a4 43 75 3e 3b 61-37 bb 33 1c 96 e0 d3 e1   .!.Cu>;a7.3.....
     0070 - 88 05 fb 62 93 b8 67 b1-b9 cf e5 34 10 eb 8a ea   ...b..g....4....
     0080 - eb d6 17 2a ac ea 9b 57-ea f6 3b 99 90 41 b0 dd   ...*...W..;..A..
     0090 - 5f 8b e8 a5 70 7c 49 2c-96 e2 61 e6 7d a6 2c ac   _...p|I,..a.}.,.

     Start Time: 1576542326
     Timeout   : 7200 (sec)
     Verify return code: 18 (self signed certificate)
     Extended master secret: yes
 ---
 ```
</details>
