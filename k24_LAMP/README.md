# how-to :: Provision L(inux)A(pache)M(ySQL)P(ython) on a Droplet
---
## Overview
This will allow us to host web apps for softdev on the cloud for our course.

### Estimated Time Cost: 2 Hours

### Prerequisites:
 - A GitHub Account
 - A GitHub Student Developer Pack
 - A credit card/debit card/PayPal with $5

### Getting Discounts + Digital Ocean Account Setup:  

0. The GitHub Edu Pack Discount (Optional)  
	a. Register for the [GitHub EduPack](https://education.github.com/pack) here.  
	b. Go to [here](https://education.github.com/pack/offers) and scroll down until you see DigitalOcean. There will be a link to use your offer code. Save that for now, we'll need it later.  
1. Create a DigitalOcean account tied to your GitHub   [here](https://cloud.digitalocean.com/registrations/new).
2. Verify your identity with a credit card or PayPal.  
	a. You will NOT be charged if you use a credit/debit card.  
	b. You will be charged at least $5 if you use PayPal.  
3. Once you are registered, go to the billing tab and enter your promo code that you got from GitHub. Make sure you click apply, a popup will show up once you do it successfully (Optional).  

### Provisioning a Droplet (a Virtual Private Server (VPS)):

4. Go to the Droplets tab.  
	a. For distributions, choose Ubuntu 20.04 LTS x64 as that is what we use in class.  
	b. For plans, choose Shared CPU (Basic).  
	c. For CPU options, choose Regular Intel with SSD for the cheapest plan (this is good enough for our uses).  
	d. Choose the $5 plan. It comes with 1GB of RAM, 1 CPU core, 25 GB of SSD storage, and 1000 GB of outbound transfers.  
	e. Ignore the "Add block storage" section. That's for more HDD space. We do not need that.  
	f. For choose datacenter region, choose NY and one of the 3 available datacenters. We really don't care which, we just need one and NY is the closest to NYC.  
	g. Ignore the additional options. Advanced user stuff. You may want monitoring though, it doesn't cost extra.  
	h. Authentication  
		i. Don't go with password. This is a publically facing utility. If you use a password you will have it brute forced eventually. Choose SSH key.  
		ii. Create a new key pair (if needed).  
			1. Open a terminal and run the command ```$ ssh-keygen```  
			2. Save the name and key under /Users/USER/.ssh/id_rsa or another pathway. The default pathway is the above provided.  
			3. You will then be prompted for a passphrase, if you want one. DigitalOcean highly recommends it.  
			4. This will generate 2 files, called id_rsa and id_rsa.pub by default.  
			5. Add the public key by copy pasting the contents of the .pub file into the SSH key content field when you click new key.  
			6. Add your own key by following the section under add your ssh private key to the ssh-agent [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).  
			7. Done!  
	i. Enter the tags you want to be associated for the droplet, along with its name.  
	j. Enable backups if you want, but remember it comes at a cost!  

### Installing apache2

1. Open your VPS console (whether through the website or through sshing)  
2. Run ```$ sudo apt install apache2```  
3. Wait for it to finish and answer yes to the prompt when it asks you to install.  
4. Wait for install...  
5. Done!  

### Installing MySQL

1. We are using SQLite3 for this class, so we're installing that instead. Run ```$ sudo apt install sqlite3```

### Installing Python  

1. Run ```$ sudo apt install python3```  
2. When it is done, you are done!  

### Securing the Boat

1. Create a sudo user so not everyone has root access  
	a. Our Source: [https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart](https://www.digitalocean.com/community/tutorials/how-to-create-a-sudo-user-on-ubuntu-quickstart)  
	b. run ```$ adduser username```  
	c. Enter your desired password.  
	d. Follow the prompts on screen.  
	e. Leave fields blank if you want to.  
	f. run ```$ usermod -aG sudo username``` to add the user to the sudo list.  
	g. use su - username to swap to the new user.  
	f. verify you are a sudouser (instructions in the link above) and you are done!  
2. Enabling this account's ssh login
	a. Shoutout to [this](https://www.digitalocean.com/community/questions/error-permission-denied-publickey-when-i-try-to-ssh) and Qina Liu for figuring out what took me a headscratchingly long time.  
	b. Make sure you have root/su perms.
	c. ```$ sudo nano /etc/ssh/sshd_config```  
	d. Find "PasswordAuthentication" and change it from no to yes.  
	e. Save and exit.  
	f. Run ```$ sudo service sshd reload``` for the new changes to take effect.  
	g. Go to the console on your local machine.  
	h. Run ```$ ssh-copy-id username@dropletip```  
	i. Enter your password. Tada.  
	j. Repeat steps c through f except turn PasswordAuthentication back off.  
2. Disabling root login
	a. Source: [https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner](https://www.digitalocean.com/community/questions/how-can-i-disable-ssh-login-for-a-root-user-i-am-the-account-owner)  
	b. Run ```$ sudo nano /etc/ssh/sshd_config```  
	c. set "PermitRootLogin" to "no"  
	d. Save  
	e. Run ```$ sudo service ssh restart```  

### Adding a Domain
1. Get a domain registered
	a. Many fancy websites do this, from [Google](https://domains.google/), Mykolyk-certified and Stuyvesant preferred [NameCheap](https://www.namecheap.com/), to the ones that come with your GitHub edupack (tech.com, namecheap, and name.com).
		 i. They all have separate application processes with their own documentation, so that's not included here.
	b. Get the digitalocean name servers set up. They have documentation [here](https://docs.digitalocean.com/products/networking/dns/quickstart/)
		i. The gist though is you want to add your domain through the networking tab in digitalocean.
		ii. This tells digital ocean servers, "hey, guys this is the new domain. whenever someone asks for it, you, the name server, give them the IP address associated"
		iii. Then you go to your domain registrar and follow these [general instructions](https://www.digitalocean.com/community/tutorials/how-to-point-to-digitalocean-nameservers-from-common-domain-registrars). Basically, you're telling your registrar "we don't need your name servers anymore, our vps provider does that for us. Tell ICANN (the domain registration people) that whenever a DNS server receives a request for this url, point them to the digital ocean guys for resolution"
		iv. Wait for all of this to propogate (should take about an hour)
		v. Test (whether through pinging or seeing if the ICANN whois registration has properly updated the nameservers [here](https://lookup.icann.org/lookup))
		vi. Done!

### Resources
* All resources are linked above!

---

Accurate as of (last update): 2022-01-12

#### Contributors:  
Renggeng Zheng, pd 1  
