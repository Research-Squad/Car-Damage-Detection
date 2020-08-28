# Damage Detection on Cars using Deflectometry & Computer Vision

## Overview
A project where we detect various classes of damage on cars moving through a device constructed to photgraph slow moving cars that pass through it. This device is already deployed at several locations of Merecedes Benz dealerships in Germany. We have image data from these locations, some labeled with damage. Our goal is to create a model that can detect damage, classify it, and create a bounding box of the damage location. The device has deflectometry pattern display screens which are commonly used for solving this kind of task.

# Data

## Image Examples

<table>
  
  <tr>
    <td colspan="3">Links</td>
    <td colspan="3">Rechts</td>
  <tr>
  <tr>
    <td>Dach</td>
    <td>Seite Mitte</td>
    <td>Seite Unten</td>
    <td>Dach</td>
    <td>Seite Mitte</td>
    <td>Seite Unten</td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00190.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00130.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00110.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00170.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00070.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00050.jpg"></td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00192.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00132.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00112.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00172.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00072.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00052.jpg"></td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00194.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00134.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00114.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00174.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00074.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00054.jpg"></td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00196.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00136.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00116.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00176.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00076.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00056.jpg"></td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00198.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00138.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00118.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00178.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00078.jpg"></td>
   <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00058.jpg"></td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Links-_00200.jpg"></td>
    <td><img width="200" alt="car_img" src="/Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BMitte-_00140.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BLinks%2BUnten-_00120.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Dach/2020-07-18%2B17-21-47%2BALU4567-Dach-Rechts-_00180.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Mitte/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BMitte-_00080.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Seite/Unten/2020-07-18%2B17-21-47%2BALU4567-Seite%2BRechts%2BUnten-_00060.jpg"></td>
  </tr>
</table>

### Front
<table>
  <tr>
    <td colspan="2">Nah</td>
   <td colspan="2">Weit</td>
  </tr>
  <tr>
    <td>Links</td>
    <td>Rechts</td>
    <td>Links</td>
    <td>Rechts</td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BNah%2BLinks-_00023.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BNah%2BRechts-_00020.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BLinks-_00313.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Front/2020-07-18%2B17-21-47%2BALU4567-Front%2BWeit%2BRechts-_00310.jpg"></td>
  </tr>
</table>

### Heck
<table>
  <tr>
    <td colspan="2">Nah</td>
   <td colspan="2">Weit</td>
  </tr>
  <tr>
    <td>Links</td>
    <td>Rechts</td>
    <td>Links</td>
    <td>Rechts</td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Heck/2020-07-18%2B17-21-47%2BALU4567-Heck%2BNah%2BLinks-_00033.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Heck/2020-07-18%2B17-21-47%2BALU4567-Heck%2BNah%2BRechts-_00030.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Heck/2020-07-18%2B17-21-47%2BALU4567-Heck%2BWeit%2BLinks-_00043.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Heck/2020-07-18%2B17-21-47%2BALU4567-Heck%2BWeit%2BRechts-_00040.jpg"></td>
  </tr>
</table>

### Schweller
<table>
  <tr>
    <td>Links</td>
    <td>Rechts</td>
  </tr>
  <tr>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Schweller/2020-07-18%2B17-21-47%2BALU4567-Schweller-L-_00222.jpg"></td>
    <td><img width="200" alt="car_img" src="Data-CarPictures/Schweller/2020-07-18%2B17-21-47%2BALU4567-Schweller-R-_00243.jpg"></td>
  </tr>
</table>

### Image Variability

#### Movement
8 km/hr movement through scanner allowed
Sometimes users drive faster than that

#### Data Changes
 Varied lighting conditions
 Varied Cars Brands
 
## Remote Server

```ssh username@1.2tronic.biz -p 7722```

## Storage Share Database Folder Layout

[Storage Share Website](https://nx11096.your-storageshare.de/apps/files/?dir=/ADA&fileid=2035778)

* ADA
* * Asperg (a)
* * Ellgau (a)
* * Essen (a)
* * KI
* * * First Step Ordner
* * *  Quick Check Daten
* * Marker
* * * Bialek
* * * Eisfeld
* * * Felix
* * * * N0U101
* * * * * {date}
* * * * * * {time}
* * * * * * * face
* * * * * * * thumbnails
* * * * * * * {img-name} (96 files)
* * * * ...(5 more)
* * * Hakobyan
* * * Marker1
* * * Theodor
* * * Theodor1
* * * Victor
* * Nuernberg (a)
* * Stuttgart (a)

Folder Structure (a) - Damage Reports

* * * corrosion
* * * crack
* * * deformation
* * * dent bump
* * * dirt
* * * misc
* * * no damage
* * * reflection
* * * rim damage
* * * scratch
* * * vehicle

## Hardware

### Cameras
6 Cameras - 2-3 photos for each - 4k resolution
6 * 3 * 3840*2160 = 149,299,200 pixels per scan

### Proposed
Relectometry


# Use Case

## Customers

* Mercedes Sellers
Their customers take a weekend test drive in their Mercedes.
This device checks for scratches when the customer returns it.

* Repair Stations

* Factory Line Damage Check

* Leasing companies

* Rental car companies
