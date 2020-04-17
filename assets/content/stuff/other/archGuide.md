# Oversimplified Arch install guide with 2^7+1 lines

[Way better official guide that describes stuff more and better](https://wiki.archlinux.org/index.php/Installation_guide). If you run into any errors during this guide, I recommend deleting all disks you have interacted whith and follow the steps on the official guide

## Download Live Arch

1. Get iso file and its checksum from [Arch download page](https://archlinux.org/download)

### Checksum

1. run `gpg --keyserver-options auto-key-retrieve --verify archlinux-version-x86_64.iso.sig` to verify your downloaded iso.

### Put live Arch on usb

1. [Balena Etcher](https://balena.io/etcher)

## Boot it

1. Plug in the usb
1. Reboot computer
1. Boot into the usb

## Setup disk

1. Identify target disk with `lsblk` (by size of the disk)
1. fdisk /dev/sdX
  1. `d` to delete partition(s)
  1. `i` to print info about partitions
    - if there are no partitions it prints an error -> you deleted all partitions -> good
  1. `n` to create new partition
    - Partition number leave default
    - First sector leave default
    - Last sector leave default
    - If it asks, yes, remove signature
  1. `w` to write changes and exit
1. `mkfs.ext4 /dev/sdX1` to make file system on the new partition
1. `mount /dev/sdX1 /mnt` to mount the disk to /mnt

## Install Arch

1. `pacstrap /mnt base linux linux-firmware`
  - `pacstrap` - Package installing thing
  - `/mnt` - where to install the packages
  - `base linux linux-firmware` - what packages to install
1. `genfstab -U /mnt >> /mnt/etc/fstab` - generates file with info about the partitions on `/mnt`. (Is needed by other programs I guess)
  - `cat /mnt/etc/fstab`
    - check that:
      - the file exists
      - is not empty
      - does not contain word "error" (case insensitive)
    - if everything is good, you can continue
1. `arch-chroot /mnt` - change root
  - move into the installed arch on your disk (/mnt)
1. I recommand installing neovim or other text editor now (`pacman -S neovim`)

## Configure Arch

### Time

1. `ln -sf /usr/share/zoneinfo/Region/City /etc/localtime` to set the timezone
  - Example: `ln -sf /usr/share/zoneinfo/Europe/Prague /etc/localtime`
  - `ls /usr/share/zoneinfo/` to list possible Regions
  - `ls /usr/share/zoneinfo/Region/` to list possible cities
1. run `hwclock --systohc`
1. run `hwclock` to check that the time is right. [If not](https://ddg.gg/?q=how+to+set+up+time+linux)

### Localization

1. Uncomment line `en_US.UTF-8 UTF-8` (and others if you need them) in `/etc/locale.gen` **IMPORTANT**
1. run `locale-gen` to generate uncommented locales
1. run `echo "LANG=en_US.UTF-8" > /etc/locale.conf
  - replace `en_US.UTF-8` if you need to

### Network

1. `echo "hostname" > /etc/hostname`
  - sets computer hostname to "hostname"
  - replace "hostname" with name of your pc (for example "prokop-pc")
1. setup `/etc/hosts`
  - add following lines:
  127.0.0.1	localhost
  ::1	localhost
  127.0.1.1	yourhostname.localdomain
  yourhostname

### Bootloader

1. `pacman -S grub`
  - to install grub; grub is a bootloader
1. `grub-install --target=i386-pc /dev/sdX`
  - to install bootloader on `/dev/sdX`
  - possible error: "this GPT partition label contains no BIOS Boot Partition"
    - that means that the grub need to be installed on its own partition
    1. exit chroot using crtl+d
    1. run `umount /dev/sdX1` to unmount the disk
    1. `fdisk /dev/sdX1`
      1. `d` to delete a partition (you need to create space for new boot partition)
      1. `n` to create the partition
        - Partition number leave default
        - First sector leave default
        - Last sector type `+200MB`
          - this partition will have 200 MB size
        - If it asks, yes, remove signature
      1. `n` again to create main partition
        - Partition number leave default
        - First sector leave default
        - Last sector leave defual
        - If it asks, yes, remove signature
      1. `t` to change partition type
        - Partition number `1`
	- Partition type `1` (EFI System)
      1. `w` to write changes to disk
    1. `mkfs.ext4 /dev/sdX2` to make (ext4) file system on the main partition;
    1. `mkfs.vfat /dev/sdX1` to make (FAT32) file system on the boot partition
    1. `mount /dev/sdX2 /mnt`
    1. `mkdir /mnt/efi` to create mount point for the boot partition
    1. `mount /dev/sdX1 /mnt/efi`
    1. `grub-install --target=x86_64-efi --efi-directory=/mnt/efi --root-directory=/mnt
    1. now you have to install and configure the arch again :c
      - Be avare that the main partition is now /dev/sdX2 not /dev/sdX1
      - Skip bootloader section
1. exit chroot using crtl+d
1. `reboot` to reboot
1. You should be booted to Arch

## Post-installation

1. `passwd` to set root password
1. Post "I use Arch BTW" on your favourite social media!
