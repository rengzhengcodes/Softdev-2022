# how-to :: Provision L(inux)A(pache)M(ySQL)P(ython) on a Droplet
---
## Overview
This will allow us to host web apps for softdev on the cloud.

### Estimated Time Cost: ??? Hours

### Prerequisites:

- A digital ocean VPS (Droplet).
Getting Discounts + Account Setup:
	0. The GitHub Edu Pack Discount (Optional)
		a. Register for the [GitHub EduPack](https://education.github.com/pack) here.
		b. Go to [here](https://education.github.com/pack/offers) and scroll down until you see DigitalOcean. There will be a link to use your offer code. Save that for now, we'll need it later.
	1. Create a DigitalOcean account tied to your GitHub [here](https://cloud.digitalocean.com/registrations/new).
	2. Verify your identity with a credit card or PayPal.
		a. You will NOT be charged if you use a credit/debit card.
		b. You will be charged at least $5 if you use PayPal.
	3. Once you are registered, go to the billing tab and enter your promo code that you got from GitHub. Make sure you click apply, a popup will show up once you do it successfully (Optional).
Provisioning a Droplet (a Virtual Private Server (VPS)):
	4. Then go to the Droplets tab.
		a. For distributions, choose Ubuntu 20.04 LTS x64 as that is what we use in class.
		b. For plans, choose Shared CPU (Basic).
		c. For CPU options, choose Regular Intel with SSD for the cheapest plan (this is good enough for our uses).
		d. Choose the $5 plan. It comes with 1GB of RAM, 1 CPU core, 25 GB of SSD storage, and 1000 GB of outbound transfers.
		e. Ignore the "Add block storage" section. That's for more HDD space. We do not need that.
		f. For choose datacenter region, choose NY and one of the 3 available datacenters. We really don't care which, we just need one and NY is the closest to NYC.
		g. Ignore the additional options. Advanced user stuff. You may want monitoring though, it doesn't cost extra.
		f. Authentication
			a. Don't go with password. This is a publically facing utility. If you use a password you will have it brute forced eventually. Choose SSH key.
			b. Create a new key pair (if needed).
				i. Open a terminal and run the command ```$ ssh-keygen```
				ii. Save the name and key under /Users/USER/.ssh/id_rsa or another pathway. The default pathway is the above provided.
				iii. You will then be prompted for a passphrase, if you want one. DigitalOcean highly recommends it.
				iv. This will generate 2 files, called id_rsa and id_rsa.pub by default.
				v. Add the public key by copy pasting the contents of the .pub file into the SSH key content field when you click new key.
				vi. Add your own key by following the section under add your ssh private key to the ssh-agent [here](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent).
				vii. Done!
		g. Enter the tags you want to be associated for the droplet, along with its name.
		f. Enable backups if you want, but remember it comes at a cost!
Installing apache2
	1. Open your VPS console (whether through the website or through sshing)
	2. Run ```$ sudo apt install apache2```
	3. Wait for it to finish and answer yes to the prompt when it asks you to install.
	4. Wait for install...
	5. Done!
Installing MySQL
	1. We are using SQLite3 for this class, so we're installing that instead. Run ```$ sudo apt install sqlite3```
Installing Python
	1. Run ```$ sudo apt install python3```
	2. When it is done, you are done!

### Resources
* All resources are linked above!

---

Accurate as of (last update): 2022-01-12

#### Contributors:  
Renggeng Zheng, pd 1  
