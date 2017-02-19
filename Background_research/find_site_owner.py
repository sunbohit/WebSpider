# -*- coding: utf-8 -*-

#寻找网站所有者
import whois
print whois.whois("bilibili.com")
'''
{
  "domain_name": "BILIBILI.COM",
  "dnssec": "Unsigned",
  "address": "PO Box 1769",
  "registrar": "Name.com, Inc.",
  "updated_date": [
    "2014-09-23 00:00:00",
    "2014-09-23 05:10:04"
  ],
  "creation_date": [
    "2004-10-21 00:00:00",
    "2004-10-21 11:37:37"
  ],
  "state": "CO",
  "referral_url": "http://www.name.com",
  "country": "US",
  "zipcode": "80201",
  "status": [
    "clientTransferProhibited https://icann.org/epp#clientTransferProhibited",
    "clientTransferProhibited"
  ],
  "name_servers": [
    "NS1.HDSLB.NET",
    "NS2.HDSLB.NET",
    "ns1.hdslb.net",
    "ns2.hdslb.net"
  ],
  "name": "Whois Agent",
  "org": "Domain Protection Services, Inc.",
  "expiration_date": [
    "2020-10-21 00:00:00",
    "2020-10-21 11:37:37"
  ],
  "city": "Denver",
  "emails": [
    "bilibili.com@protecteddomainservices.com",
    "abuse@name.com"
  ],
  "whois_server": "whois.name.com"
}

'''
